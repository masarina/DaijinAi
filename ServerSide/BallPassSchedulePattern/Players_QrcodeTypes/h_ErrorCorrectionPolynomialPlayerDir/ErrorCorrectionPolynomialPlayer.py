import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ErrorCorrectionPolynomialPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.data = None
        self.data_4pad_8pad = None
        self.padding_48bits = None
        self.mode_charaCount = None
        self.rs_blocks = None
        self.error_correction_polynomial = None
        
    def get_error_correction_polynomial(self):
        # 誤り訂正用の生成多項式 g(x) の係数リストを返します。(バージョン2,エラー訂正レベルH専用)
        # リストにある数字は生成多項式の係数を表しています
        # QRコードのリード・ソロモン符号で、14符号語分（14 * 8 = 112ビット）のエラー訂正が行われます
        output = [1, 25, 81, 228, 225, 202, 217, 141, 188, 180, 192, 181, 209, 246]
        # ここでは、QRコードのバージョン2-H型の誤り訂正符号用に、14符号語を使います(この14要素は、国際規格から)

        return output

    def return_my_name(self):
        # プレイヤーの名前を返すメソッド。これで、このプレイヤーがどの処理を行うかを識別できる。
        return "ErrorCorrectionPolynomialPlayer"

    def main(self):
        """
        メイン処理を行います。誤り訂正用の生成多項式 g(x) を設定し、次に渡す準備をします。
        
        1符号語 = 8ビットであることに注意してください。
        QRコードのリード・ソロモン符号は、データが破損しても復元できるようにエラー訂正符号を追加します。
        ここでは、生成多項式 g(x) を次のプレイヤーに渡していきます。
        """
        """ 初期化 """
        woB = self.one_time_world_instance.rSBlockAndPolynomialPlayer
        self.data = wo8B.data_bits
        self.data_4pad_8pad = woB.data_4pad_8pad
        self.padding_48bits = woB.padding_48bits
        self.mode_charaCount = woB.mode_charaCount
        self.rs_blocks = woB.self.rs_blocks
        
        self.error_correction_polynomial = self.get_error_correction_polynomial()
        # self.one_time_world_instance に生成多項式を渡す
        # QRコードのリード・ソロモン符号の誤り訂正符号語の生成に使われる多項式を持たせています。
        self.one_time_world_instance.ErrorCorrectionPolynomialPlayer = self  # 自身のインスタンスを登録


        # 処理が完了したら "Completed" を返します
        return "Completed"
