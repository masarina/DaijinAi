import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeCharacterCountPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.character_count_bits = None  # 文字数ビット表記を格納する変数を初期化

    def return_my_name(self):
        return "QRCodeCharacterCountPlayer"

    def calculate_bit_count(self, char_count, mode_indicator):
        """
        指定されたモード指示子に基づいて、文字数のビット数を設定する。
        mode_indicator: str (4bitのモード指示子)
        char_count: int (格納する文字数)
        """
        if mode_indicator == "0001":  # 数字モード
            bit_count = format(char_count, '010b')  # 10bit
        elif mode_indicator == "0010":  # 英数字モード
            bit_count = format(char_count, '09b')  # 9bit
        elif mode_indicator == "0100":  # 8bitバイトモード
            bit_count = format(char_count, '08b')  # 8bit
        elif mode_indicator == "1000":  # 漢字モード
            bit_count = format(char_count, '08b')  # 8bit
        else:
            raise ValueError("Invalid mode_indicator. Ensure the mode is set correctly.")
        
        return bit_count

    def main(self, char_count):
        """
        QRコードのモード指示子に基づいて、指定された文字数をビット数で表現し、
        one_time_world_instanceに設定する。
        """
        mode_indicator = self.one_time_world_instance.QRCodeModePlayer.mode_indicator  # モード指示子を取得
        
        # 文字数をビットで表現
        self.character_count_bits = self.calculate_bit_count(char_count, mode_indicator)

        # self.one_time_world_instance に文字数ビット情報を渡す
        self.one_time_world_instance.QRCodeCharacterCountPlayer = self  # 自身のインスタンスをworldに登録

        return f"Completed: {mode_indicator} {self.character_count_bits}"