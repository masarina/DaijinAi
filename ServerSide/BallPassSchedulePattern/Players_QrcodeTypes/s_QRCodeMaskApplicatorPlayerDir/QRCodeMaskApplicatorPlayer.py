import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeMaskApplicatorPlayer(SuperPlayer):  # 新しい名前！
    def __init__(self):
        super().__init__()
        self.my_name = None  # 初期化は必ずNone
        self.qr_map_2Dlist = None  # QRコードの2Dリストを保持

    def return_my_name(self):
        return "QRCodeMaskApplicatorPlayer"  # 新しい名前！

    def apply_mask(self, matrix, mask_bit, i, j):
        """
        2次元リスト matrix に対して、指定された mask_bit に基づいて (i, j) のビットを反転させる。
        """
        if mask_bit == "000":
            if (i + j) % 2 == 0:
                matrix[i][j] = 1 - matrix[i][j]  # ビットを反転
        elif mask_bit == "001":
            if i % 2 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "010":
            if j % 3 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "011":
            if (i + j) % 3 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "100":
            if ((i // 2) + (j // 3)) % 2 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "101":
            if (i * j) % 2 + (i * j) % 3 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "110":
            if ((i * j) % 2 + (i * j) % 3) % 2 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        elif mask_bit == "111":
            if ((i * j) % 3 + (i + j) % 2) % 2 == 0:
                matrix[i][j] = 1 - matrix[i][j]
        return matrix

    def main(self, matrix, mask_bit):
        """
        2次元リスト matrix (25x25) に対して、mask_bitに基づき全座標のビットを反転させて変換後のリストを返す。
        """
        for i in range(len(matrix)):   # 行の数
            for j in range(len(matrix[i])):  # 列の数
                matrix = self.apply_mask(matrix, mask_bit, i, j)  # 各座標ごとにマスク適用

        self.qr_map_2Dlist = matrix
        self.one_time_world_instance.qrCodeMaskApplicatorPlayer = self  # 結果を保持
        return matrix
