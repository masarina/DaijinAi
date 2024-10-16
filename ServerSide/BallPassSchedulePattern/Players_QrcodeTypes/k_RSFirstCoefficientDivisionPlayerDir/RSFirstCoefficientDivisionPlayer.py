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

    def calculate_division_polynomial(self, f_coefficients, g_polynomial, exponent_table):
        """
        f(x)の全ての項の係数をαのべき乗に変換し、g(x)に掛けた多項式を計算します。
    
        Parameters:
        f_coefficients: list - f(x)の全ての項の係数のリスト
        g_polynomial: list - 生成多項式g(x)の係数リスト
        exponent_table: list - αのべき乗を参照するテーブル
    
        Returns:
        list - g(x)にそれぞれのαのべき乗を掛けた結果の多項式
        """
        division_polynomial = []
        
        # f(x)の各項に対して処理
        for i, coef in enumerate(f_coefficients):
            # それぞれの係数をαのべき乗に変換
            alpha_exponent = exponent_table[coef]
    
            # g(x)にαのべき乗を掛けて多項式を計算
            result = [(g_coef + alpha_exponent) % 255 for g_coef in g_polynomial]
            
            division_polynomial.append(result)
        
        return division_polynomial

    def main(self):
        """
        メインの処理を行います。f(x)の最初の係数をα^5に変換し、g(x)に掛けた多項式を計算します。
        
        リード・ソロモン符号の誤り訂正では
        多項式の最初の項（最高次項）から
        順番に処理をしていくのが基本なの。
        具体的には、
        最初の項を生成多項式 g(x) で割って、
        その結果をもとに次のステップに進む
        という形で、1つずつ処理を進めていくの。
        
        このプレイヤーは、
        その一番最初の要素のみの変換をする
        プレイヤーになります。
        """
        
        # 前のプレイヤーから変数を取得
        """ 入力 """
        woP = self.one_time_world_instance.polynomialDivisionPlayer
        self.data_str = woP.data_bits # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = woP.mode_charNumInfo_data_pad4_pad8_list
        self.loop11101100and00010001pad_only_list = woP.loop11101100and00010001pad_only_list
        self.rs_blocks = woP.rs_blocks
        self.error_correction_polynomial = woP.error_correction_polynomial
        self.exponent_table = woP.exponent_table
        self.log_table = woP.log_table
        self.error_correction_polynomial = self.one_time_world_instance.errorCorrectionPolynomialPlayer.error_correction_polynomial
        
        f_x = self.one_time_world_instance.polynomialDivisionPlayer.mode_charNumInfo_data_pad4_pad8_Decimal_list  # （mode+文字数情報+データ+4bitパディング+8bitパディング のガロア基準の10進数リスト
        g_x = self.one_time_world_instance.polynomialDivisionPlayer.rs_blocks  # 生成多項式g(x)
        alpha_exp_table = self.one_time_world_instance.galoisFieldPlayer.exponent_table  # αのべき乗テーブル

        # f(x)の最初の係数を変換し、多項式を計算
        self.division_polynomial = self.calculate_division_polynomial(f_x, g_x, alpha_exp_table)

        # 結果をワールドに渡す
        self.one_time_world_instance.rSFirstCoefficientDivisionPlayer = self  # 自身のインスタンスを登録
        self.one_time_world_instance.set_division_polynomial(self.division_polynomial)  # 計算結果を登録

        return "Completed"
