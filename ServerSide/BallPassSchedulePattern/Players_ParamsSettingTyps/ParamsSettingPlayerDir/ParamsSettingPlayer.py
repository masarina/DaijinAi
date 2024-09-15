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
        
        """
        入力データの初期化
        """
        # 入力データのバッチ化
        
        
        xs_data_tokenType = self.one_time_world_instance.xsDataPlayer.xs_data_tokenType # 二次元トークンデータを取得
        vocabularyBuilderPlayer = self.one_time_world_instance.vocabularyBuilderPlayer # ID辞書変換機を取得
        vocabularyBuilderPlayer.mode = "vocab_to_id" # ID辞書変換器のモードを設定
        xs_data_idType = vocabularyBuilderPlayer.
        
        
        if self.model_mode == "train":
            
            
            """
            EmbeddingLayerの初期化
            """
            self.one_time_world_instance.embeddingPlayer.
            
        elif self.model_mode == "predict":
            pass
            
            
        return "Completed"
