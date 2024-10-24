import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeBitConversionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.mode_indicator = None  # モード指示子を保持する変数を初期化
    
    def return_my_name(self):
        return "QRCodeBitConversionPlayer"

    def numeric_mode_bit_conversion(self, data):
        """
        数字モードでのデータを2進数に変換します。
        3桁ずつ10bitで表現し、余りの桁は4bit, 7bitで表現します。
        """
        bits = ""
        for i in range(0, len(data), 3):
            chunk = data[i:i+3]
            if len(chunk) == 3:
                bits += format(int(chunk), '010b')  # 3桁なら10bit
            elif len(chunk) == 2:
                bits += format(int(chunk), '07b')   # 2桁なら7bit
            elif len(chunk) == 1:
                bits += format(int(chunk), '04b')   # 1桁なら4bit
        return bits

    def alphanumeric_mode_bit_conversion(self, data):
        """
        英数字モードでのデータを2進数に変換します。
        2文字ごとに11bitで表現し、1文字余った場合は6bitで表現します。
        """
        alphanumeric_table = {
            '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
            'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
            'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
            '+': 40, '-': 41, '.': 42, '/': 43, ':': 44
        }
        bits = ""
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                first_char_value = alphanumeric_table[data[i]]
                second_char_value = alphanumeric_table[data[i+1]]
                combined_value = first_char_value * 45 + second_char_value
                bits += format(combined_value, '011b')  # 2文字なら11bit
            else:
                bits += format(alphanumeric_table[data[i]], '06b')  # 1文字なら6bit
        return bits

    def byte_mode_bit_conversion(self, data):
        """
        8bitバイトモードでのデータを2進数に変換します。
        各文字をASCIIコードで表現し、8bitのバイナリに変換します。
        """
        bits = ""
        for char in data:
            bits += format(ord(char), '08b')  # 各文字を8bitで表現
        return bits

    def main(self):
        """
        このメソッド内で変換モードを選択し、対応するビット変換を行います。
        データはself.one_time_world_instance内に保持されているものを使用します。
        
        出力例
        数字モード（データ："123456789"）:
        ビット列 → 000111101101110010001100010101
        英数字モード（データ："HELLO"）:
        ビット列 → 0110000101101111000110011000
        バイトモード（データ："abc123"）:
        ビット列 → 011000010110001001100011001100010011001000110011
        """
        data = self.one_time_world_instance.initFromQrcodePlayer.data  # 
        mode = self.one_time_world_instance.initFromQrcodePlayer.mode  # 

        if mode == "numeric":
            converted = self.numeric_mode_bit_conversion(data)
        elif mode == "alphanumeric":
            converted = self.alphanumeric_mode_bit_conversion(data)
        elif mode == "byte":
            converted = self.byte_mode_bit_conversion(data)
        else:
            raise ValueError("Invalid mode. Choose from: numeric, alphanumeric, byte.")
            
        """ 保存 """
        self.mode_and_countinfo_bit = self.one_time_world_instance.qRCodeCharacterCountPlayer.output_bits
        self.data_bits = converted # まだ 指示子情報と、文字数情報は分別しておきます。エラー訂正はデータのみに反映させる為です。
        
        # 変換したビット列をワールドに反映させる
        self.one_time_world_instance.qRCodeBitConversionPlayer = self  # 自身のインスタンスを登録

        return "Completed"
