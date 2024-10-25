import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class BitModeDataReconstructorPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # イニシャライザでself.my_nameをNoneで初期化する

    def return_my_name(self):
        return "BitModeDataReconstructorPlayer"
        
    def reconstruct_data(self, data=None,mode=None):
        # ひとまず数字だけコーディング中(2024-10-26)
        if mode == "0001": # 数字の場合
            """
            数字モードのデータをビット列に変換するメソッド
            - data: 数字の文字列
            """
            bit_string = ""
            # 3桁ずつ分割してビットに変換
            for i in range(0, len(data), 3):
                chunk = data[i:i + 3]
                # 桁数ごとに異なるビット数でエンコード
                if len(chunk) == 3:
                    bit_string += f"{int(chunk):010b}"  # 3桁→10ビット
                elif len(chunk) == 2:
                    bit_string += f"{int(chunk):07b}"   # 2桁→7ビット
                elif len(chunk) == 1:
                    bit_string += f"{int(chunk):04b}"   # 1桁→4ビット
        
        
        return bit_string
        

    def main(self):
        """ 
        modeに応じたデータ復元を行う
        """
        """ 入力 """
        woP = self.one_time_world_instance.spiritBitDataPlayer
        self.mode = woP.mode
        self.charNumInfo_decimal = woP.charNumInfo_decimal
        self.data = woP.data

        """メイン  """
        # データの復元処理 (具体的な復元処理をここに実装)
        self.reconstructed_data = reconstruct_data(
            mode=self.mode,
            data=self.data,
        )
        
        # 文字数情報と、文字数の確認
        if self.charNumInfo_decimal != len(self.reconstructed_data):
            # 一致しなかった場合、以降commonプレイヤー以外実行しなくするフラグを立てる
        
        """ 出力 """
        
        # 自身のプレイヤー情報を更新
        self.one_time_world_instance.bitModeDataReconstructorPlayer = self
        
        return "Completed"
