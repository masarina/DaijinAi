""" このプレイヤーは使用しません """

import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

"""ここで定義したふたつのリストは次のように使います。
# 掛け算の場合

# 仮のデータとテーブル
values = [15, 22, 7]  # 掛け算したいデータ
exponent_table = [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90, 180]  # 簡略化したべき乗テーブル
log_table = [0, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75, 4, 100]  # 簡略化したログテーブル

# 3つの値の掛け算を行う
for i in range(2):  # 2回掛け算を繰り返してみる
    a = values[i]
    b = values[i + 1]

    # ガロア体の掛け算
    log_a = log_table[a]
    log_b = log_table[b]
    log_result = (log_a + log_b) % 255  # ログ同士の足し算と255での剰余

    result = exponent_table[log_result]  # べき乗テーブルで戻す

    print(f"掛け算結果: {a} * {b} = {result}")

"""



class GaloisFieldPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        # ガロア体の指数テーブルと逆数テーブル（ログテーブル）を定義
        self.galois_field_exponent_table = None
        self.galois_field_log_table = None

    def return_my_name(self):
        return "GaloisFieldPlayer"

    def generate_exponent_table(self):
        """
        ガロア体 GF(2^8) のαのべき乗テーブルを生成します。
        """
        # 表4のαのべき乗テーブルを作成
        exponent_table = [
            1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90,
            180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78, 156, 37, 74, 148,
            53, 106, 212, 181, 119, 238, 193, 159, 35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186,
            105, 210, 185, 111, 222, 161, 95, 190, 97, 194, 153, 47, 94, 188, 101, 202, 137, 15,
            30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182,
            113, 226, 217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206,
            129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23,
            46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77, 154, 41, 82,
            164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115, 230, 209, 191, 99, 198, 145, 63,
            126, 252, 229, 215, 179, 123, 246, 241, 255
        ]
        return exponent_table

    def generate_log_table(self):
        """
        ガロア体 GF(2^8) のαの逆数テーブル（ログテーブル）を生成します。
        """
        # 表4の整数に対するαのべき乗を作成
        log_table = [
            0, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75, 4, 100, 224, 14, 52,
            141, 239, 129, 28, 193, 105, 248, 200, 8, 76, 113, 5, 138, 101, 47, 225, 36, 15, 33,
            53, 147, 142, 218, 240, 18, 130, 69, 29, 181, 194, 125, 106, 39, 249, 185, 201, 154,
            9, 120, 77, 228, 114, 166, 6, 191, 139, 98, 102, 221, 48, 253, 226, 152, 37, 179, 16,
            145, 34, 136, 54, 208, 148, 206, 143, 150, 219, 189, 241, 210, 19, 92, 131, 56, 70,
            64, 30, 66, 182, 163, 195, 72, 126, 107, 58, 40, 84, 250, 133, 186, 61, 202, 94, 155,
            159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87, 7, 112, 192, 247, 140,
            128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24, 227, 165, 153, 119, 38, 184, 180,
            124, 17, 68, 146, 217, 35, 32, 137, 46, 55, 63, 209, 149, 188, 207, 205, 144, 135,
            151, 178, 220, 252, 190, 97, 242, 86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71,
            109, 65, 162, 31, 45, 67, 216, 183, 123, 164, 118, 196, 23, 73, 236, 127, 12, 108, 85,
            59, 82, 41, 157, 151, 46, 131, 151, 34, 21, 156
        ]
        return log_table

    def main(self):
        woP = self.one_time_world_instance.ErrorCorrectionPolynomialPlayer
        self.data_str = woP.data_bits # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = woP.mode_charNumInfo_data_pad4_pad8_list
        self.loop11101100and00010001pad_only_list = woP.loop11101100and00010001pad_only_list
        self.rs_blocks = woP.rs_blocks
        self.error_correction_polynomial = woP.self.error_correction_polynomial
        
        """
        ガロア体 GF(2^8) の演算で使用する
        べき乗テーブルと
        ログテーブルを
        設定します。
        """
        self.exponent_table = self.generate_exponent_table()
        self.log_table = self.generate_log_table()
        
        # self.one_time_world_instance にテーブルを渡す
        self.one_time_world_instance.galoisFieldPlayer = self  # 自身のインスタンスを登録

        return "Completed"
