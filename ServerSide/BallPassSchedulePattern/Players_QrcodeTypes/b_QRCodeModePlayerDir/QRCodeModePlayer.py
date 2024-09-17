import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeModePlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.mode_indicator = None  # モード指示子を保持する変数を初期化
    
    def return_my_name(self):
        return "QRCodeModePlayer"

    def set_mode(self, mode_type):
        """
        モードタイプを受け取って、それに応じたモード指示子を設定する。
        mode_type: str ( "numeric", "alphanumeric", "byte", "kanji" )
        """
        if mode_type == "numeric":
            self.mode_indicator = "0001"
        elif mode_type == "alphanumeric":
            self.mode_indicator = "0010"
        elif mode_type == "byte":
            self.mode_indicator = "0100"
        elif mode_type == "kanji":
            self.mode_indicator = "1000"
        else:
            raise ValueError("Invalid mode_type. Choose from: numeric, alphanumeric, byte, kanji.")
    
    def main(self):
        """
        メインの処理をここで行う。QRコードのモード指示子を設定して、次に渡す準備をする。
        """
        if self.mode_indicator is None:
            raise ValueError("Mode indicator is not set. Please call set_mode before executing main.")
        
        # self.one_time_world_instance にモード情報を渡す
        self.one_time_world_instance.QRCodeModePlayer = self  # 自身のインスタンスをworldに登録

        return "Completed"
