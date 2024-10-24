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
        
    def charNumInfo_catcher(self, mode=None, str_bit=None):
        if mode == "0001": # 数字モードの場合、10bit
            firstDatas_point = 16
            binary_str = str_bit[5:firstDatas_point] 
            decimal_number = int(binary_str, 2)
            
        elif mode == "0010": # 英数字モードの場合、9bit
            firstDatas_point = 15
            binary_str = str_bit[5:firstDatas_point] 
            decimal_number = int(binary_str, 2)
            
        elif mode == "0100": # 8bitバイトモードの場合、8bit
            firstDatas_point = 16 4
            binary_str = str_bit[5:firstDatas_point] 
            decimal_number = int(binary_str, 2)
        
        elif mode == "1000": # 漢字モードの場合、8bit
            firstDatas_point = 14
            binary_str = str_bit[5:firstDatas_point] 
            decimal_number = int(binary_str, 2)
            
        else:
            print(f"モードが正しく読み込めませんでした。mode▶︎{mode}")
            exit(1)
        
        
        return decimal_number, firstDatas_point
            

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
        mode_charNumInfo_data_flattenBit = flatten_numbers_and_to_str(self.processed_data)
        
        # modeの摘出
        self.mode = mode_charNumInfo_data_flattenBit[0:5]
        
        # 文字数情報の摘出
        self.charNumInfo_decimal, firstDatas_point = charNumInfo_catcher(
                                        mode=self.mode,
                                        str_bit=mode_charNumInfo_data_flattenBit,
                                    )
                    
        # データの摘出

        # プレイヤー自身を更新
        self.one_time_world_instance.spiritBitDataPlayer = self

        return "Completed"
