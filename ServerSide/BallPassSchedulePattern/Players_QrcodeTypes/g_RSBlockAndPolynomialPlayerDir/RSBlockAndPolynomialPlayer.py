import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class RSBlockAndPolynomialPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.rs_blocks = []  # RSブロックを保持するリスト
        self.galois_field_polynomial = 0b100011101  # ガロア体GF(2⁸)の原始多項式

    def return_my_name(self):
        return "RSBlockAndPolynomialPlayer"

    def divide_into_rs_blocks(self, data):
        """
        データをRSブロックに分割します。
        1-H型ではブロック数が1なので分割は不要。データをそのまま格納します。
        """
        # 1-H型の場合、ブロック数は1のため、そのままデータを一つのブロックとして格納
        self.rs_blocks = [data]
        return self.rs_blocks

    def main(self):
        """
        メイン処理を行います。データをRSブロックに分割し、多項式を設定します。
        """
        # ワールドからデータを取得（仮想的なメソッドとして想定）
        data = self.one_time_world_instance.qRCode8BitPaddingWithFillPlayer.data_bits

        # データをRSブロックに分割
        self.divide_into_rs_blocks(data)

        # self.one_time_world_instance にRSブロックと多項式を登録
        self.one_time_world_instance.rSBlockAndPolynomialPlayer = self  # 自身のインスタンスを登録

        return "Completed"
