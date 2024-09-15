import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ParamsSettingPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.model_mode = None

    def return_my_name(self):
        return "ParamsSettingPlayer"

    def main(self):
        """
        各プレイヤーの初期化。
        """
        """ データの準備 """
        xs_data_tokenType = self.one_time_world_instance.xsDataPlayer.xs_data_tokenType # 二次元トークンデータを取得
        
        """ 基本設定 """
        self.model_mode = "train" # モデルのモード設定
        batch_size = 3

        if self.model_mode == "train":
            """ 学習モード設定 """
        
            """ 入力データのバッチ化 """
            # バッチサイズ計算機にバッチサイズを設定
            self.one_time_world_instance.tokenBatcherPlayer.batch_size = batch_size 
            
            
            vocabularyBuilderPlayer = self.one_time_world_instance.vocabularyBuilderPlayer # ID辞書変換機を取得
            vocabularyBuilderPlayer.mode = "vocab_to_id" # ID辞書変換器のモードを設定
            xs_data_idType = vocabularyBuilderPlayer.
            
            
            
            """
            EmbeddingLayerの初期化
            """
            self.one_time_world_instance.embeddingPlayer.
            
        elif self.model_mode == "predict":
            pass
            
            
        return "Completed"
