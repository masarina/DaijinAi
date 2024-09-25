import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class TrapezoidCorrectionPlayer(SuperPlayer):
    def __init__(self):
        """
        プレイヤーの初期化メソッド。
        QRコードの台形行列やプレイヤー名をNoneで初期化する。
        """
        super().__init__()
        self.my_name = None  # プレイヤー名は初期化時にNoneに設定
        self.binary_matrix_2Dlist = None  # QRコードの台形2次元リストを保持

    def return_my_name(self):
        """
        プレイヤー名を返す。
        """
        return "TrapezoidCorrectionPlayer"

    def find_left_right_edges(self, row):
        """
        行中の最初と最後のビット1の位置を見つけ、左端と右端を返す。

        Args:
            row (list): QRコード行のビットデータ。

        Returns:
            tuple: 左端と右端のビット1のインデックス。
        """
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

        # エラーハンドリング
        if left_edge is None or right_edge is None:
            raise ValueError("行内にビット1が見つかりませんでした。")

        return left_edge, right_edge

    def find_top_bottom_edges(self, matrix):
        """
        行列全体から最上部と最下部のビット1の行を見つける。

        Args:
            matrix (list): QRコードのビット行列。

        Returns:
            tuple: 上端と下端の行インデックス。
        """
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

        # エラーハンドリング
        if top_edge is None or bottom_edge is None:
            raise ValueError("行列内にビット1が見つかりませんでした。")

        return top_edge, bottom_edge

    def get_trapezoid_corners(self, matrix):
        """
        台形の4つの頂点座標を取得する。

        Args:
            matrix (list): QRコードのビット行列。

        Returns:
            tuple: 左上、右上、左下、右下の各頂点座標。
        """
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
            delta_left = left_down[0] - left_up[0]
            if delta_left != 0:
                ratio_left = (i - left_up[0]) / delta_left
            else:
                ratio_left = 0
            left_x = int(left_up[1] + (left_down[1] - left_up[1]) * ratio_left)

            # 右エッジのx座標を計算
            delta_right = right_down[0] - right_up[0]
            if delta_right != 0:
                ratio_right = (i - right_up[0]) / delta_right
            else:
                ratio_right = 0
            right_x = int(right_up[1] + (right_down[1] - right_up[1]) * ratio_right)

            # x座標の範囲チェック
            left_x = max(0, min(left_x, matrix_width - 1))
            right_x = max(0, min(right_x, matrix_width - 1))

            if left_x > right_x:
                left_x, right_x = right_x, left_x

            # 行を生成
            row = [0] * matrix_width
            for j in range(left_x, right_x + 1):
                row[j] = 1
            corrected_matrix.append(row)

        return corrected_matrix

    def correct_trapezoid_to_square(self, matrix):
        """
        台形の行列を補完し、正方形に近づける処理。

        Args:
            matrix (list): 台形のビット行列。

        Returns:
            list: 正方形に補完された行列データ。
        """
        # 台形の4つの頂点を取得
        left_up, right_up, left_down, right_down = self.get_trapezoid_corners(matrix)

        # 行列のサイズを取得
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])

        # エッジを補間して正方形の行列を生成
        corrected_matrix = self.interpolate_edges(
            left_up, right_up, left_down, right_down, matrix_height, matrix_width
        )

        return corrected_matrix

    def main(self):
        """
        QRコードの台形行列を正方形に補正し、結果を出力する。

        Returns:
            str: 処理完了のメッセージ。
        """
        # VR空間から取得したQRコードの台形行列を使用
        trapezoid_image = self.one_time_world_instance.ball.all_data_dict.

        # 入力データの検証
        if trapezoid_image is None or not trapezoid_image:
            raise ValueError("QRコードの台形行列が取得できませんでした。")

        # 台形の行列を正方形に補正
        self.binary_matrix_2Dlist = self.correct_trapezoid_to_square(trapezoid_image)

        # 補正結果を表示（デバッグ用）
        print("Corrected Matrix (正方形に近い形に補正された行列):")
        for row in self.binary_matrix_2Dlist:
            print(row)

        # 自身を更新
        self.one_time_world_instance.trapezoidCorrectionPlayer = self

        return "Completed"
