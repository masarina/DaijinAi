import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class PolynomialDivisionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        # 生成多項式g(x)の係数リスト
        self.error_correction_polynomial = self.one_time_world_instance.errorCorrectionPolynomialPlayer.error_correction_polynomial
        # データコード多項式f(x)を保持するための変数
        self.data_polynomial = []

    def return_my_name(self):
        return "PolynomialDivisionPlayer"

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
        # 入力データとしてデータコード多項式を取得
        data = self.one_time_world_instance.get_data_polynomial()

        # 多項式の除算を実行し、出力データとして剰余を取得
        remainder = self.divide_polynomial(data)

        # self.one_time_world_instance に剰余多項式を登録
        self.one_time_world_instance.polynomialDivisionPlayer = self  # 自身のインスタンスを登録
        self.one_time_world_instance.set_remainder(remainder)  # 剰余をワールドに渡す仮想的なメソッド

        return "Completed"
