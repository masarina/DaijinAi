
import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class RSXorCalculationPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.xor_result_polynomial = []  # 排他的論理和の結果を保持するリスト

    def return_my_name(self):
        return "RSXorCalculationPlayer"

    def calculate_xor_polynomial(self, f_polynomial, g_polynomial):
        """
        f(x) と g(x) の積を排他的論理和（XOR）で処理し、新しい f(x)' を生成します。

        Parameters:
        f_polynomial: list - データ多項式 f(x) の係数リスト
        g_polynomial: list - 生成多項式 g(x) に α のべき乗を掛けた結果の係数リスト

        Returns:
        list - f(x)' の係数リスト（XOR 計算結果）
        """
        # f(x) と g(x) の共通部分の長さまで XOR を計算
        length = len(g_polynomial)
        self.xor_result_polynomial = [
            f_polynomial[i] ^ g_polynomial[i] for i in range(length)
        ]
        
        # f(x) が g(x) より長い場合、残りの項をそのまま結果に追加
        if len(f_polynomial) > len(g_polynomial):
            self.xor_result_polynomial += f_polynomial[length:]
        
        return self.xor_result_polynomial

    def main(self):
        """
        メインの処理を行います。f(x) と g(x) の積を XOR で処理し、新しい f(x)' を計算します。
        """
        # ワールドからデータを取得（仮想メソッドとして想定）
        f_x_polynomial = self.one_time_world_instance.rSFirstCoefficientDivisionPlayer  # データ多項式 f(x)
        g_x_polynomial = self.one_time_world_instance.rSFirstCoefficientDivisionPlayer  # g(x)にαを掛けた結果の多項式

        # 排他的論理和の計算を行う
        self.calculate_xor_polynomial(f_x_polynomial, g_x_polynomial)

        # 結果をワールドに渡す
        self.one_time_world_instance.rSXorCalculationPlayer = self  # 自身のインスタンスを登録
        

        return "Completed"
