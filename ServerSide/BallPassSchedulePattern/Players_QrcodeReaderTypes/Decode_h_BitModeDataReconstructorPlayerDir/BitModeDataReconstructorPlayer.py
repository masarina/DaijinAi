import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class BitModeDataReconstructorPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # イニシャライザでself.my_nameをNoneで初期化する

    def return_my_name(self):
        return "BitModeDataReconstructorPlayer"

    def main(self):
        """ 
        modeに応じたデータ復元を行う
        """

        # 8bitデータをフラットなビット文字列に変換
        mode_charNumInfo_data_flattenBit = flatten_numbers_and_to_str(self.processed_data)
        
        # モードを摘出
        self.mode = mode_charNumInfo_data_flattenBit[0:5]

        # 文字数情報の摘出とデータの最初のインデックス取得
        self.charNumInfo_decimal, firstDatas_point = charNumInfo_catcher(
            mode=self.mode,
            str_bit=mode_charNumInfo_data_flattenBit,
        )

        # データの復元処理 (具体的な復元処理をここに実装)
        self.reconstructed_data = reconstruct_data(
            mode=self.mode,
            data=mode_charNumInfo_data_flattenBit[firstDatas_point:],
            char_count=self.charNumInfo_decimal
        )
        
        # 自身のプレイヤー情報を更新
        self.one_time_world_instance.bitModeDataReconstructorPlayer = self
        
        return "Completed"
