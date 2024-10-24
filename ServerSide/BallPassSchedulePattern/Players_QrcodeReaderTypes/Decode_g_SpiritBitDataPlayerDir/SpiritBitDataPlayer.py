import os
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class SpiritBitDataPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化

    def return_my_name(self):
        return "SpiritBitDataPlayer"

    def main(self):
        """
        このメソッド実行直前に、最新のworldインスタンスを
        one_time_world_instanceに代入しています。
        
        このプレイヤーはSpiritBitに関連するデータを操作する予定です。
        """
        # データ操作の処理を書く場所
        print(f"{self.return_my_name()}が実行されました。")

        # プレイヤー自身を更新
        self.one_time_world_instance.spiritBitDataPlayer = self

        return "Completed"
