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
        2-H型ではブロック数が1なので分割は不要。データをそのまま格納します。
        """
        # 2-H型の場合、ブロック数は1のため、そのままデータを一つのブロックとして格納
        """ ここで言うデータとは
        使用する部分: モード情報（4ビット）や文字数ビット、その後の本データ（文字データ）、4ビットの0パディング、8ビット単位の0パディングを含んだ部分を使用します。
        ただし、最後の残りのパディング（11101100や00010001の繰り返しパターン）とエラー訂正コードは含めません。エラー訂正コードはこれから生成するからです。
        """
        output = [data]
        
        return output

    def main(self):
        """
        メイン処理を行います。データをRSブロックに分割し、多項式を設定します。
        """
        # ワールドからデータを取得
        wo8 = self.one_time_world_instance.qRCode8BitPaddingWithFillPlayer
        self.data_str = woT.data_bits # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = mode_charNumInfo_data_pad4_pad8_list
        self.loop11101100and00010001pad_only_list = loop11101100and00010001pad_only_list
        
        
        
        self.data = wo8.data_bits
        self.data_4pad_8pad = wo8.data_4pad_8pad
        self.padding_48bits = wo8.padding_48bits
        self.mode_charaCount = wo8.mode_charaCount

        # データをRSブロックに分割
        self.rs_blocks = self.divide_into_rs_blocks(self.data)

        # self.one_time_world_instance にRSブロックと多項式を登録
        self.one_time_world_instance.rSBlockAndPolynomialPlayer = self  # 自身のインスタンスを登録

        return "Completed"
