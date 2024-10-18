import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ChecksumPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化

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
        mainメソッドで全てのメソッドを実行
        """
        # 任意のデータリスト
        data_list = [100, 200, 50, 75, 25]
        
        # Checksumの計算
        checksum = self.calculate_checksum(data_list)
        
        # Checksumをデータに追加
        data_list_with_checksum = self.append_checksum(data_list, checksum)
        
        # データリストとChecksumの出力
        self.print_data(data_list, checksum, data_list_with_checksum)
        
        # プレイヤー自身を更新
        self.one_time_world_instance.checksumPlayer = self
        
        return "Completed"
