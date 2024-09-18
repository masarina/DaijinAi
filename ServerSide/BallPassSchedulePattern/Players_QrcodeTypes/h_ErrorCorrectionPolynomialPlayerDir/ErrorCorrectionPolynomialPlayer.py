import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ErrorCorrectionPolynomialPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        # 誤り訂正用の生成多項式 g(x) の係数リストをメンバ変数に保持
        self.error_correction_polynomial = [43, 139, 206, 78, 43, 239, 123, 206, 214, 147, 24, 99, 150, 39, 243, 163, 136]

    def return_my_name(self):
        return "ErrorCorrectionPolynomialPlayer"

    def main(self):
        """
        メイン処理を行います。誤り訂正用の生成多項式 g(x) を設定し、次に渡す準備をします。
        """
        # self.one_time_world_instance に生成多項式を渡す
        self.one_time_world_instance.ErrorCorrectionPolynomialPlayer = self  # 自身のインスタンスを登録

        return "Completed"
