import os, sys
import numpy as np
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeFormatInfoInserterPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 初期化は必ずNone
    
    def return_my_name(self):
        return "QRCodeFormatInfoInserterPlayer"
    
    def insert_format_info(self, matrix, format_info):
        """
        25x25のQRコードマトリックスに15bitの形式情報を規格に基づいて挿入する。
        """
        # numpy配列に変換して作業する
        matrix_np = np.array(matrix)

        # 形式情報を挿入（国際規格に従う）

        # 上部（縦方向）の挿入 1列目の8ビット
        matrix_np[0:6, 8] = format_info[0:6]  # 上部の最初の6ビット
        matrix_np[7, 8] = format_info[6]      # 7行目
        matrix_np[8, 8] = format_info[7]      # 8行目（境界）

        # 左下の列方向の挿入
        matrix_np[8, 0:6] = format_info[8:13]  # 下部の5ビット
        matrix_np[8, 7] = format_info[13]      # 下部の6ビット目
        matrix_np[8, 8] = format_info[14]      # 境界の最後のビット

        # 最後に2次元リストに戻す
        return matrix_np.tolist()
    
    def main(self):
        """
        形式情報をQRコードマトリックスに挿入する。
        """
        # 形式情報の15bitを取得
        data_15bit_list = self.one_time_world_instance.qRCodeErrorCorrectionAndMaskPlayer.format_bits

        # QRコードのマトリックスを取得
        matrix_2Dlist = self.one_time_world_instance.qRCodeMaskApplicatorPlayer.qr_map_2Dlist

        # 形式情報をQRコードマトリックスに挿入
        updated_matrix = self.insert_format_info(matrix_2Dlist, data_15bit_list)

        # 更新されたマトリックスを保存
        self.one_time_world_instance.qrCodeFormatInfoInserterPlayer = self
        self.one_time_world_instance.qRCodeMaskApplicatorPlayer.qr_map_2Dlist = updated_matrix

        print(f"15bit形式情報が挿入されたQRコードマトリックス: {updated_matrix}")
        return "Completed"
