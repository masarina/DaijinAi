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

    def main(self):
        """
        QRコードのモード指示子に基づいて、指定された文字数をビット数で表現し、
        one_time_world_instanceに設定する。
        
        出力例
        'Mode 0001, Count 123': '0001111011'
        'Mode 0010, Count 45': '000101101'
        'Mode 0100, Count 200': '11001000'
        'Mode 1000, Count 300': '100101100'
        """

        """ 初期化 """
        char_count = len(self.one_time_world_instance.initFromQrcodePlayer.data) # 文字数(数値であれば、数字の数)
        mode_indicator = self.one_time_world_instance.qRCodeModePlayer.mode_indicator  # モード指示子を取得
        
        # 文字数をビットで表現
        self.character_count_bits = self.calculate_bit_count(char_count, mode_indicator)

        # self.one_time_world_instance に文字数ビット情報を渡す
        self.one_time_world_instance.qRCodeCharacterCountPlayer = self  # 自身のインスタンスをworldに登録

        return f"Completed: {mode_indicator} {self.character_count_bits}"
