import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class BitModeDataReconstructorPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # イニシャライザでself.my_nameをNoneで初期化する

    def return_my_name(self):
        return "BitModeDataReconstructorPlayer"
        
    def reconstruct_data(self):
        if mode == "0001": # 数字の場合
            

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
            data=data,
            char_count=self.charNumInfo_decimal
        )
        
        """ 出力 """
        
        # 自身のプレイヤー情報を更新
        self.one_time_world_instance.bitModeDataReconstructorPlayer = self
        
        return "Completed"
