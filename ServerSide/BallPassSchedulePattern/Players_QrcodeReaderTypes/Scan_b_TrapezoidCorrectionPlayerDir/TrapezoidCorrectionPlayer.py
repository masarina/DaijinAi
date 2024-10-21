import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class TrapezoidCorrectionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # プレイヤー名は初期化時にNoneに設定
        self.binary_matrix_2Dlist = None  # QRコードの台形2次元リストを保持
        self.png_file_path = None
        self.mode_charNumInfo_checksum_bitlist = None
        self.version = None
        self.grid_size = None
        self.qr_code_map = None
        self.modified_qr_code_map = None

        

    def return_my_name(self):
        return "TrapezoidCorrectionPlayer"

    def find_left_right_edges(self, row):
        left_edge = None
        right_edge = None

        # 左端のビット1を探すループ
        for i, bit in enumerate(row):
            if bit == 1:
                left_edge = i
                break

        # 右端のビット1を探すループ（逆順で検索）
        for i, bit in enumerate(reversed(row)):
            if bit == 1:
                right_edge = len(row) - 1 - i
                break

        # ビット1がない場合、行全体が0なので両端を設定
        if left_edge is None or right_edge is None:
            left_edge = 0
            right_edge = len(row) - 1

        return left_edge, right_edge

    def find_top_bottom_edges(self, matrix):
        top_edge = None
        bottom_edge = None

        # 上端のビット1を探すループ
        for i, row in enumerate(matrix):
            if any(bit == 1 for bit in row):
                top_edge = i
                break

        # 下端のビット1を探すループ（逆順で検索）
        for i, row in enumerate(reversed(matrix)):
            if any(bit == 1 for bit in row):
                bottom_edge = len(matrix) - 1 - i
                break

        # ビット1がない場合、行列全体が0なので両端を設定
        if top_edge is None or bottom_edge is None:
            top_edge = 0
            bottom_edge = len(matrix) - 1

        return top_edge, bottom_edge

    def get_trapezoid_corners(self, matrix):
        top_edge, bottom_edge = self.find_top_bottom_edges(matrix)
        left_up = None
        right_up = None
        left_down = None
        right_down = None

        if top_edge is not None:
            row = matrix[top_edge]
            left_up_col, right_up_col = self.find_left_right_edges(row)
            left_up = (top_edge, left_up_col)
            right_up = (top_edge, right_up_col)

        if bottom_edge is not None:
            row = matrix[bottom_edge]
            left_down_col, right_down_col = self.find_left_right_edges(row)
            left_down = (bottom_edge, left_down_col)
            right_down = (bottom_edge, right_down_col)

        # エラーハンドリング
        if None in [left_up, right_up, left_down, right_down]:
            raise ValueError("台形の頂点を正しく取得できませんでした。")

        return left_up, right_up, left_down, right_down

    def interpolate_edges(self, left_up, right_up, left_down, right_down, matrix_height, matrix_width):
        corrected_matrix = []

        for i in range(matrix_height):
            # 左エッジのx座標を計算
            total_rows_left = left_down[0] - left_up[0]
            if total_rows_left != 0:
                ratio_left = (i - left_up[0]) / total_rows_left
            else:
                ratio_left = 0
            left_x = left_up[1] + (left_down[1] - left_up[1]) * ratio_left

            # 右エッジのx座標を計算
            total_rows_right = right_down[0] - right_up[0]
            if total_rows_right != 0:
                ratio_right = (i - right_up[0]) / total_rows_right
            else:
                ratio_right = 0
            right_x = right_up[1] + (right_down[1] - right_up[1]) * ratio_right

            # x座標の範囲チェックと整数化
            left_x = int(round(max(0, min(left_x, matrix_width - 1))))
            right_x = int(round(max(0, min(right_x, matrix_width - 1))))

            if left_x > right_x:
                left_x, right_x = right_x, left_x

            # 行を生成
            row = [0] * matrix_width
            for j in range(left_x, right_x + 1):
                row[j] = 1
            corrected_matrix.append(row)

        return corrected_matrix

    def correct_trapezoid_to_square(self, matrix):
        left_up, right_up, left_down, right_down = self.get_trapezoid_corners(matrix)
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])

        corrected_matrix = self.interpolate_edges(
            left_up, right_up, left_down, right_down, matrix_height, matrix_width
        )

        return corrected_matrix

    def resize_matrix_to_25x25(self, matrix):
        original_height = len(matrix)
        original_width = len(matrix[0])

        new_height = 25
        new_width = 25

        resized_matrix = []

        for i in range(new_height):
            row = []
            for j in range(new_width):
                # マッピング元のインデックスを計算
                orig_i = int(i * original_height / new_height)
                orig_j = int(j * original_width / new_width)

                # インデックスの範囲チェック
                orig_i = min(orig_i, original_height - 1)
                orig_j = min(orig_j, original_width - 1)

                row.append(matrix[orig_i][orig_j])
            resized_matrix.append(row)

        return resized_matrix

    def main(self):
        """ 入力 """
        woP.one_time_world_instance.centralSquareReaderPlayer
        self.binary_matrix_2Dlist = woP.binary_matrix_2Dlist
        self.png_file_path = png_file_path
        self.mode_charNumInfo_checksum_bitlist = woP.mode_charNumInfo_checksum_bitlist
        self.version = woP.version
        self.grid_size = woP.grid_size
        self.qr_code_map = woP.qr_code_map
        self.modified_qr_code_map = woP.modified_qr_code_map

        
        
        trapezoid_image = self.one_time_world_instance.centralSquareReaderPlayer.binary_matrix_2Dlist

        # 入力データの検証
        if trapezoid_image is None or not trapezoid_image:
            raise ValueError("QRコードの台形行列が取得できませんでした。")

        # 台形の行列を正方形に補正
        corrected_matrix = self.correct_trapezoid_to_square(trapezoid_image)

        # 補正された行列を25x25にリサイズ
        self.binary_matrix_2Dlist = self.resize_matrix_to_25x25(corrected_matrix)

            
        """ 出力 """
        self.binary_matrix_2Dlist
        self.png_file_path
        self.mode_charNumInfo_checksum_bitlist
        self.version
        self.grid_size
        self.qr_code_map
        self.modified_qr_code_map


        # 自身を更新
        self.one_time_world_instance.trapezoidCorrectionPlayer = self

        return "Completed"
