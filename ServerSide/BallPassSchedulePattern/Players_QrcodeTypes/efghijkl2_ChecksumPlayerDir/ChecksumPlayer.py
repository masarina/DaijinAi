import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ChecksumPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化
        self.mode_charNumInfo_checksum_bitlist = None
        self.loop11101100and00010001pad_only_list = None

    def return_my_name(self):
        return "ChecksumPlayer"

    def calculate_checksum(self, data_list):
        """
        データリストからChecksumを計算する
        :param data_list: 数値のリスト
        :return: Checksum値
        """
        return sum(data_list) % 256

    def append_checksum(self, data_list, checksum):
        """
        データリストにChecksumを追加する
        :param data_list: 数値のリスト
        :param checksum: 計算されたChecksum
        :return: Checksum付きのデータリスト
        """
        return data_list + [checksum]

    def print_data(self, data_list, checksum, data_list_with_checksum):
        """
        データリスト、Checksum、Checksum付きデータリストを出力する
        """
        print("元のデータリスト:", data_list)
        print("Checksum:", checksum)
        print("Checksum付きデータリスト:", data_list_with_checksum)

    def main(self):
        """
        mainメソッドで全てのメソッドを実行します。
        このメソッドの流れ:
        
        1. `QRCodeBitConversionPlayer`から、データビットとモード・文字数のビット情報を取得。
        2. 取得したビット列情報を10進数のリストに変換(`polynomialDivisionPlayer`のメソッドを使用)。
        3. 変換された10進数リストを用いて、Checksumを計算。
        4. 計算したChecksumを元のデータリストに追加し、最終的なデータリストとして保持。
        5. 自身のインスタンスを`one_time_world_instance`に登録。
        
        これにより、データリストにChecksumを追加し、他のプレイヤーがアクセスできるように設定。
        """
        
        """ 入力 """
        woP = self.one_time_world_instance.qRCodeBitConversionPlayer
        self.data_str = woP.data_bits # データのみ
        self.mode_charNumInfo_bitlist = woP.mode_and_countinfo_bit + self.data_str
        to_decimal = self.one_time_world_instance.polynomialDivisionPlayer.bit_list_to_decimal_list # to10bitメソッド
        
        """ メイン """
        # 任意のデータリスト
        mode_charNumInfo_decimallist = to_decimal(self.self.mode_charNumInfo_bitlist)
        
        # Checksumの計算
        checksum = self.calculate_checksum(mode_charNumInfo_decimallist)
        
        # Checksumをデータに追加
        self.mode_charNumInfo_checksum_bitlist  = self.append_checksum(self.mode_charNumInfo_bitlist , checksum)
        
        """ 出力 """
        self.mode_charNumInfo_checksum_bitlist
        
        """ プレイヤー自身を更新 """
        self.one_time_world_instance.checksumPlayer = self
        
        return "Completed"
