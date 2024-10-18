""" このプレイヤーは使用しない """

import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCode8BitPaddingWithFillPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.data_4pad_8pad = None
        self.data_bits = None
        self.padding_48bits = None
        self.mode_charaCount = None
        
        self.data_str = None # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = None
        self.loop11101100and00010001pad_only_list = None
        
    
    def return_my_name(self):
        return "QRCode8BitPaddingWithFillPlayer"

    def pad_to_8bit(self, bit_sequence):
        """
        ビット列を8ビット単位に区切り、最後のビット列が8ビット未満の場合は0で埋めます。
        
        Args:
            bit_sequence (str): QRコードデータのビット列
    
        Returns:
            tuple: パディング後のビット列と、追加されたパディング部分
        """
        bit_length = len(bit_sequence)
        padding_needed = 8 - (bit_length % 8) if bit_length % 8 != 0 else 0
        padding_bits = ""
    
        # パディングが必要な場合は0を追加
        if padding_needed > 0:
            padding_bits = '0' * padding_needed
            bit_sequence += padding_bits
    
        # パディング後のビット列と、パディング部分を返す
        return bit_sequence, padding_bits


    def split_to_8bit_chunks(self, bit_sequence):
        """
        ビット列を8ビットごとに区切ります。
        
        Args:
            bit_sequence (str): QRコードデータのビット列

        Returns:
            list: 8ビットごとに区切られたビット列のリスト
        """
        return [bit_sequence[i:i+8] for i in range(0, len(bit_sequence), 8)]

    def add_fillers(self, bit_chunks, target_data_code_words):
        """
        シンボルのデータコード数に満たない場合、11101100と00010001を交互に付加します。
        
        QRコードの規格において、シンボルのバージョンと誤り訂正レベルに応じて、必要なデータコード数が定義されています。
        ここではバージョン2、誤り訂正レベルHのQRコードを例にして説明します。
    
        Args:
            bit_chunks (list): 8ビットごとに区切られたビット列。
                - 各ビット列は、1バイト (8ビット) のデータを表します。
                - QRコードのデータは8ビットごとに分けられ、この配列に保存されます。
            
            target_data_code_words (int): シンボルのデータコード数 (辞書から取得)。
                - バージョン2のQRコードで、誤り訂正レベルHを使用する場合、データコード数は28個です。
                - ISO/IEC 18004によれば、バージョン2・誤り訂正レベルHでは、最大で28のコードワード（データコード）を収める必要があります。
                - ここでいう「コードワード」とは、8ビット（1バイト）のデータ単位を指します。
                - データが28個のコードワードに満たない場合、この関数で規定のパディングバイトを追加します。
    
        Returns:
            list: 必要に応じて11101100と00010001が交互に追加されたビット列のリスト。
                - 追加されるビット列（11101100, 00010001）は、ISO/IEC 18004で規定されているパディングバイトです。
                - バージョン2・誤り訂正レベルHでは、データが不足した場合、これらのパターンでデータを埋めます。
                - 例: もしデータが20コードワードしかなければ、8コードワード分を11101100と00010001で埋めます。
        """
        fillers = ["11101100", "00010001"]
        index = 0
        target_data_code_words # ここでは28が代入されているはず。
        loop_pad = [] # fillersのループパディングのみの二次元リスト(今作るやつね)
        data_bits_list2d = copy.deepcopy(bit_chunks)
    
        # データコード数が28に満たない場合、パディングバイトを交互に追加
        while len(data_bits_list2d) < target_data_code_words:
            data_bits_list2d.append(fillers[index]) # カウント用
            loop_pad.append(fillers[index])
            
            # バージョン2、誤り訂正レベルHでは、コードワード数が28個必要
            # 11101100 (十六進数で0xEC)と00010001 (0x11)を交互に追加
            index = (index + 1) % 2  # 交互に11101100と00010001を追加
        
        return loop_pad

    def main(self):
        """
        メイン処理メソッド。
        ワールドからデータビット列をインポートし、8ビット単位に区切り、シンボル容量に満たない場合は11101100と00010001を交互に付加します。
        """
        woT = self.one_time_world_instance.qRCodeTerminationPlayer
        
        # Worldからデータビット列とシンボル容量を取得する仮想的なメソッド
        
        mode_charNumInfo_data_pad4_str = woT.modeBit_and_CharacterCountBit + woT.data_and_last4pattern # 指示子 + 文字数情報 + データ + 4bitパディング
        error_correction_level = "H"  # 固定します
        
        # Version 2のデータコード数を辞書から取得
        version_2_data = {
            'L': 34,
            'M': 28,
            'Q': 22,
            'H': 16 # データコード数は16。(8＊16ビットが最大。これ以下であれば、11101100と00010001を交互にパディング。つまりそれ以降は空。)
        }
        target_data_code_words = version_2_data[error_correction_level]

        # 8ビットに整える
        mode_charNumInfo_data_pad4_pad8_str, _ = self.pad_to_8bit(mode_charNumInfo_data_pad4_str)
        
        # 8ビットごとに区切る
        mode_charNumInfo_data_pad4_pad8_list = self.split_to_8bit_chunks(mode_charNumInfo_data_pad4_pad8_str)

        # データコード数が足りない場合、11101100と00010001を交互に追加
        loop11101100and00010001pad_only_list = self.add_fillers(mode_charNumInfo_data_pad4_pad8_list, target_data_code_words)
        
        """ 出力 """
        
        self.data_str = woT.data_bits # データのみ
        self.mode_charNumInfo_data_pad4_pad8_list = mode_charNumInfo_data_pad4_pad8_list
        self.loop11101100and00010001pad_only_list = loop11101100and00010001pad_only_list
        
        

        # 処理後のデータをワールドに反映させる仮想的なメソッド
        self.one_time_world_instance.qRCode8BitPaddingWithFillPlayer = self  # 自身のインスタンスをワールドに登録
        self.one_time_world_instance.set_bit_chunks(bit_chunks_with_fillers)  # 8ビット区切りされたビット列を反映

        return "Completed"
