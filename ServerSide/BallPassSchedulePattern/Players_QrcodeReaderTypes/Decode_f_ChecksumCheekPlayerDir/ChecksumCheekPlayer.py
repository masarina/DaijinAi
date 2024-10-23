import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ChecksumCheekPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化

    def return_my_name(self):
        return "ChecksumCheekPlayer"

    def main(self):
        """
        このメソッド実行直前に、
        one_time_world_instanceに、最新のworldインスタンスを代入しています。
        """
        # プレイヤーのメインロジックを書く場所
        print(f"{self.return_my_name()}が実行されました。")

        # チェックサムを計算する処理を想定
        data_to_check = self.one_time_world_instance.allDataPlayer.data_to_check
        checksum = self.calculate_checksum(data_to_check)
        print(f"チェックサム: {checksum}")

        # 自身のインスタンスを更新
        self.one_time_world_instance.checksumCheekPlayer = self

        return "Completed"

    def calculate_checksum(self, data):
        """
        チェックサムを計算するメソッド。dataはリストや文字列などのデータ。
        """
        if isinstance(data, str):
            return sum(ord(char) for char in data)
        elif isinstance(data, list):
            return sum(data)
        else:
            return 0
            