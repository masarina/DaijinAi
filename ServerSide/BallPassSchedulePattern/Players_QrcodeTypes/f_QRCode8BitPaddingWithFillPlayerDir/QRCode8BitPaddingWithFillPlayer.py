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

        Args:
            bit_chunks (list): 8ビットごとに区切られたビット列
            target_data_code_words (int): シンボルのデータコード数 (辞書から取得)

        Returns:
            list: 必要に応じて11101100と00010001が交互に追加されたビット列のリスト
        """
        fillers = ["11101100", "00010001"]
        index = 0

        while len(bit_chunks) < target_data_code_words:
            bit_chunks.append(fillers[index])
            index = (index + 1) % 2  # 交互に11101100と00010001を追加
        
        return bit_chunks

    def main(self):
        """
        メイン処理メソッド。
        ワールドからデータビット列をインポートし、8ビット単位に区切り、シンボル容量に満たない場合は11101100と00010001を交互に付加します。
        """
        # Worldからデータビット列とシンボル容量を取得する仮想的なメソッド
        bit_sequence = self.one_time_world_instance.qRCodeTerminationPlayer.data_and_last4pattern # データ + 4bitパディング
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
        padded_bit_sequence, padding_bits = self.pad_to_8bit(bit_sequence)
        
        # 8ビットごとに区切る
        bit_chunks = self.split_to_8bit_chunks(padded_bit_sequence)

        # データコード数が足りない場合、11101100と00010001を交互に追加
        bit_chunks_with_fillers = self.add_fillers(bit_chunks, target_data_code_words)
        
        """ 出力 """
        woT = self.one_time_world_instance.qRCodeTerminationPlayer
        self.data_4pad_8pad = bit_chunks_with_fillers
        self.data_bits = woT.data_bits # データのみ
        self.padding_48bits = woT.padding_bits + padding_bits
        self.mode_charaCount = wo.modeBit_and_CharacterCountBit
        
        

        # 処理後のデータをワールドに反映させる仮想的なメソッド
        self.one_time_world_instance.qRCode8BitPaddingWithFillPlayer = self  # 自身のインスタンスをワールドに登録
        self.one_time_world_instance.set_bit_chunks(bit_chunks_with_fillers)  # 8ビット区切りされたビット列を反映

        return "Completed"
