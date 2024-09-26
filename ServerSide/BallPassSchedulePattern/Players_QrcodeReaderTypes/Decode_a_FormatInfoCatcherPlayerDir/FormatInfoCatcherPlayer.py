import os, sys
import numpy as np
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

""" ATTENTION
vec ▶︎ matrix
のコードを改造する方法で
matrix ▶︎ vec
を作成中(2024-09-26)
"""

class FormatInfoCatcherPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 初期化は必ずNone
    
    def return_my_name(self):
        return "FormatInfoCatcherPlayer"
    
    def catch_format_info(self, matrix):
        """
        25x25のQRコードマトリックスに15bitの形式情報を規格に基づいて挿入する。
        """
        # numpy配列に変換して作業する
        matrix_np = np.array(matrix)
        
        # 空の15bitベクトルを用意
        _ = []
        for in range(15):
            _ += [None]
        format_info = np.array(_)

        # 形式情報を挿入（国際規格に従う）

        # 上部（縦方向）の挿入 1列目の8ビット
        format_info[0:6] = matrix_np[0:6, 8]  # 上部の最初の6ビット
        matrix_np[0:6, 8] = -10 # 要素に全て-10を代入し、マーキングする
        format_info[6] = matrix_np[7, 8]     # 7行目
        matrix_np[7, 8] = -10
        format_info[7] = matrix_np[8, 8]      # 8行目（境界）
        matrix_np[8, 8] = -10

        # 左下の列方向の挿入
        format_info[8:13] = matrix_np[8, 0:6] # 下部の5ビット
        matrix_np[8, 0:6] = -10
        format_info[13] = matrix_np[8, 7]     # 下部の6ビット目
        matrix_np[8, 7] = -10
        format_info[14] = matrix_np[8, 8]   # 境界の最後のビット
        matrix_np[8, 8] = -10
 
        # 完成した15bitを戻値とする
        return format_info, matrix_np
    
    def main(self):
        """
        QRコードマトリックスから、15bit情報を抜き取り
        抜き取り時、抜き取った痕跡として -10 を代入
        """
        
        # QRコードのマトリックスを取得
        matrix_2Dlist = copy.deepcopy(self.one_time_world_instance.trapezoidCorrectionPlayer.binary_matrix_2Dlist)
        
        # 形式情報の15bitを取得
        data_caught_15bit_list, matrix  = self.catch_format_info(matrix_2Dlist)

        self.one_time_world_instance.formatInfoCatcherPlayer = self

        return "Completed"