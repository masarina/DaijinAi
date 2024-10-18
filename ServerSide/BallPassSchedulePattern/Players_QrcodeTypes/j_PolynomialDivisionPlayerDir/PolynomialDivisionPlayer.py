""" このプレイヤーは
プレイヤーとしては使用していませんが
ライブラリとしては使っています。 
"""

import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class PolynomialDivisionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        # 生成多項式g(x)の係数リスト
        self.error_correction_polynomial = None
        # データコード多項式f(x)を保持するための変数
        self.data_polynomial = []
        self.mode_charNumInfo_data_pad4_pad8_Decimal_list = None # データの10進数(モジュロ値256(0~255))バージョン
        self.remainder = None #このメソッドの最終出力

    def return_my_name(self):
        return "PolynomialDivisionPlayer"

    def bit_list_to_decimal_list(self, bit_list):
        """
        8ビットごとのビット列を10進数に変換し、256になった場合は0に置き換えます。
        
        Args:
            bit_list (list): 8ビットのビット列のリスト
        
        Returns:
            list: 各ビット列を10進数に変換し、256を0に置き換えたリスト
        """
        decimal_list = []
        for bit_str in bit_list:
            decimal_value = int(bit_str, 2)  # 2進数の文字列を10進数に変換
            if decimal_value == 256:  # ガロア体では256は0になるので置き換える
                decimal_value = 0
            decimal_list.append(decimal_value)
        return decimal_list

    def divide_polynomial(self, data_polynomial):
        """
        データコード多項式 f(x) を生成多項式 g(x) で除算します。
        入力データ: data_polynomial (データコード多項式のリスト)
        出力データ: 除算の結果得られる剰余
        """
        # 入力データの設定（データコード多項式 f(x) の係数リスト）
        self.data_polynomial = data_polynomial

        # 出力データ: 剰余多項式（初期化）
        remainder = self.data_polynomial[:]

        # 生成多項式の長さを取得
        g_len = len(self.error_correction_polynomial)

        # 多項式除算を実行（シンプルな形式で実装）
        for i in range(len(data_polynomial) - g_len + 1):
            # 剰余の最初の係数を使って生成多項式のスケールを計算
            coefficient = remainder[i]
            if coefficient != 0:  # 係数が0でない場合のみ除算処理を行う
                for j in range(g_len):
                    # 各項を生成多項式と掛け合わせて引く (排他的論理和)
                    remainder[i + j] ^= self.galois_multiply(coefficient, self.error_correction_polynomial[j])

        # 出力データとして剰余多項式を返す
        return remainder[-g_len:]

    def galois_multiply(self, a, b):
        """
        ガロア体 GF(2^8) での乗算を行います。
        """
        # 簡単なガロア体乗算処理 (αのべき乗テーブルとログテーブルを使った計算)
        if a == 0 or b == 0:
            return 0
        log_a = self.one_time_world_instance.galoisFieldPlayer.galois_field_log_table[a]
        log_b = self.one_time_world_instance.galoisFieldPlayer.galois_field_log_table[b]
        log_result = log_a + log_b
        if log_result >= 255:
            log_result -= 255
        return self.one_time_world_instance.galoisFieldPlayer.galois_field_exponent_table[log_result]

    def main(self):
        """
        メイン処理を行います。データコード多項式 f(x) を生成多項式 g(x) で除算し、剰余を計算します。
        """
        
        """ 入力 """
        woF = self.one_time_world_instance.galoisFieldPlayer
        self.data_str = woF.data_bits # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = woF.mode_charNumInfo_data_pad4_pad8_list
        self.loop11101100and00010001pad_only_list = woF.loop11101100and00010001pad_only_list
        self.rs_blocks = woF.rs_blocks
        self.error_correction_polynomial = woF.error_correction_polynomial
        self.exponent_table = woF.exponent_table
        self.log_table = woF.log_table
        self.error_correction_polynomial = self.one_time_world_instance.errorCorrectionPolynomialPlayer.error_correction_polynomial
        
        
        # 入力データとしてデータコード多項式を取得
        data = self.mode_charNumInfo_data_pad4_pad8_list
        data_decimal = self.bit_list_to_decimal_list(data)

        # 多項式の除算を実行し、出力データとして剰余を取得
        self.remainder = self.divide_polynomial(data_decimal)

        # 10進数バージョンも保持する。
        self.mode_charNumInfo_data_pad4_pad8_Decimal_list = data_decimal

        # self.one_time_world_instance に剰余多項式を登録
        self.one_time_world_instance.polynomialDivisionPlayer = self  # 自身のインスタンスを登録

        return "Completed"
