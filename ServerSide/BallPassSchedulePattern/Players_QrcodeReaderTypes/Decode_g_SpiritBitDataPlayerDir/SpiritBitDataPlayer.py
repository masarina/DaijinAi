import os
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class SpiritBitDataPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化
        self.png_file_path # 写真のパス
        self.processed_data # 8bit毎にスプリットしたデータ
        self.mode = None
        self.charNum_info = None
        self.data = None

    def return_my_name(self):
        return "SpiritBitDataPlayer"

    def main(self):
        """
        このメソッド実行直前に、最新のworldインスタンスを
        one_time_world_instanceに代入しています。
        
        このプレイヤーはSpiritBitに関連するデータを操作する予定です。
        """
        """ 入力 """
        woP = self.one_time_world_instance.checksumCheekPlayer
        self.png_file_path = woP.png_file_path # 写真のパス
        self.processed_data = woP.processed_data # 8bit毎にスプリットしたデータ
        
        """ メイン """
        # modeの摘出
        
        # 文字数情報の摘出
        
        # データの摘出

        # プレイヤー自身を更新
        self.one_time_world_instance.spiritBitDataPlayer = self

        return "Completed"
