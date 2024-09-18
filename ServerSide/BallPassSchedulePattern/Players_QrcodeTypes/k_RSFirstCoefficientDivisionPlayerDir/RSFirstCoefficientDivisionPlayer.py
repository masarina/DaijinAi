import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class RSFirstCoefficientDivisionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.first_coefficient = None  # f(x)の最初の項の係数
        self.alpha_exponent_first = None  # 最初の係数をαのべき乗に変換
        self.division_polynomial = []  # g(x)にα^5を掛けた多項式を格納するリスト。次のプレイヤーに渡すデータ。

    def return_my_name(self):
        return "RSFirstCoefficientDivisionPlayer"

    def calculate_division_polynomial(self, first_coefficient, g_polynomial, exponent_table):
        """
        f(x)の最初の項の係数をαのべき乗に変換し、g(x)に掛けた多項式を計算します。

        Parameters:
        first_coefficient: int - f(x)の最初の項の係数（例: 32）
        g_polynomial: list - 生成多項式g(x)の係数リスト（例: [43, 139, 206, ...]）
        exponent_table: list - αのべき乗を参照するテーブル

        Returns:
        list - g(x)にαのべき乗を掛けた結果の多項式
        """
        # f(x)の最初の係数をαのべき乗に変換（exponent_tableを使用）
        self.alpha_exponent_first = exponent_table[first_coefficient]

        # g(x)にαのべき乗を掛けて多項式を計算
        self.division_polynomial = [(coef + self.alpha_exponent_first) % 255 for coef in g_polynomial]
        
        return self.division_polynomial

    def main(self):
        """
        メインの処理を行います。f(x)の最初の係数をα^5に変換し、g(x)に掛けた多項式を計算します。
        """
        # ワールドからデータを取得（仮想メソッドとして想定）
        f_x_first = self.one_time_world_instance.get_first_coefficient()  # f(x)の最初の項
        g_x_polynomial = self.one_time_world_instance.get_g_polynomial()  # 生成多項式g(x)
        alpha_exp_table = self.one_time_world_instance.get_alpha_exponent_table()  # αのべき乗テーブル

        # f(x)の最初の係数を変換し、多項式を計算
        self.calculate_division_polynomial(f_x_first, g_x_polynomial, alpha_exp_table)

        # 結果をワールドに渡す
        self.one_time_world_instance.RSFirstCoefficientDivisionPlayer = self  # 自身のインスタンスを登録
        self.one_time_world_instance.set_division_polynomial(self.division_polynomial)  # 計算結果を登録

        return "Completed"
