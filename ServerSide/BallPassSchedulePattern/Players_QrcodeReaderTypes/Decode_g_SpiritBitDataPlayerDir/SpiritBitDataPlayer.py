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

    def flatten_numbers_and_to_str(self,numbers):
        """
        数字のリストをフラットにして一つの文字列にするメソッド。
        例: [222, 33, 55] -> 2223355
        """
        # 数字を文字列に変換して結合する
        flat_str = ''.join(map(str, numbers))
        return flat_str

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
        # 8bitデータを1次元的にし、さらにbit文字列に変換する。
        mode_charNumInfo_data_flattenBit = flatten_numbers_and_to_str
        
        # modeの摘出
        self.mode = mode_charNumInfo_data_flattenBit[0:5]
        
        # 文字数情報の摘出
        charNumInfo = mode_charNumInfo_data_flattenBit[5:]
        
        # データの摘出

        # プレイヤー自身を更新
        self.one_time_world_instance.spiritBitDataPlayer = self

        return "Completed"
