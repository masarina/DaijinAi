import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class BitDataProcessorPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 必ずNoneで初期化

    def return_my_name(self):
        return "BitDataProcessorPlayer"

    def process_bit_data(self, bit_data):
        """
        1次元リストで受け取ったビットデータを8ビットごとに区切って、
        新しいリストとして返すメソッド。
        
        入力: [0001011010111101010110] のようなビットデータ
        出力: 8ビットごとに区切ったリスト ['00010110', '10111101', ...]
        """
        # 8ビットごとにスライスして新しいリストに格納
        return [bit_data[i:i+8] for i in range(0, len(bit_data), 8)]

    def main(self):
        """
        リストデータを取得して、それを8ビットごとに
        分割し、戻り値として返す。
        """
        """ 入力 """
        woP = self.one_time_world_instance.rightBottomReaderPlayer
        self.replaced_matrix = woP.replaced_matrix # 置き換え後のmatrix
        self.png_file_path = woP.png_file_path # 写真のパス
        self.new_list2d = woP.new_list2d # データ部分をn*2のリストに変換したもの
        self.data_read = woP.data_read # データ部分を1次元リスト化したもの。

        
        # 仮のビットデータを用意
        bit_data = "0001011010111101010110"  # 22ビットのデータ
        
        # ビットデータを8ビットごとに変換
        processed_data = self.process_bit_data(bit_data)
        
        # 結果を表示
        print(processed_data)

        # 自身を更新して、return "Completed"を返す
        self.one_time_world_instance.bitDataProcessorPlayer = self
        return "Completed"