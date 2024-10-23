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
        """ 入力 """
        woP = self.one_time_world_instance.bitDataProcessorPlayer
        self.png_file_path = woP.png_file_path # 写真のパス
        self.processed_data = woP.processed_data # 8bit毎にスプリットしたデータ
        self.encode_time_check_code = self.processed_data.pop() # encode時のチェックサムを取り除く。
        woC = self.one_time_world_instance.checksumPlayer
        
        
        """ メイン """
        # 任意のデータリスト
        mode_charNumInfo_decimallist = woC.to_decimal(self.processed_data)     
          
        # Checksumの計算
        decode_time_checksum = woC.calculate_checksum(mode_charNumInfo_decimallist)
        
        # チェックサムが正しいか確認
        if encode_time_checksum != decode_time_checksum:
            # もしチェックサムが正しくない場合、commonプレイヤー以外の実行を拒むフラグを立てる。
            # ↪︎ KBprojectの方で実装したので、その方法をここでも使用しよう。

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
            