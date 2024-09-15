import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ParamsSettingPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None

    def return_my_name(self):
        return "ParamsSettingPlayer"

    def main(self):
        """
        モードに応じてエンコードまたはデコードを実行し、結果をメンバ変数に保持
        """
        if self.model_mode == "train":
            pass
        elif self.model_mode == "predict":
            pass
            
            
        return "Completed"

