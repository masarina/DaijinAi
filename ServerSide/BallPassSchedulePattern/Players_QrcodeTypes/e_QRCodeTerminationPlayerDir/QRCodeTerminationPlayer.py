import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeTerminationPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化

    def return_my_name(self):
        return "QRCodeTerminationPlayer"

    def add_termination_pattern(self, data_bits, symbol_capacity):
        """
        終端パターンとして0000を付加します。
        データビット列がシンボル容量を満たしている場合は終端パターンは不要です。
        - data_bits: QRコードのデータビット列 (文字列としての2進数)
        - symbol_capacity: QRコードのシンボル容量 (許容される最大ビット数)
        
        国際規格に基づき、データビット列がシンボル容量未満の場合、4ビットの終端パターンを追加します。
        """
        # 現在のデータビット数を取得
        current_length = len(data_bits)

        # データビット列がシンボル容量を満たしていない場合のみ終端パターンを付加
        if current_length < symbol_capacity:
            remaining_bits = symbol_capacity - current_length
            # 最低4ビットの終端パターンを追加
            termination_bits = "0000"
            # 必要な分だけ付加するが、最大でも4ビット
            data_bits += termination_bits[:min(remaining_bits, 4)]

        return data_bits

    def main(self):
        """
        データビット列の終端に4ビットの終端パターンを付加する処理。
        シンボル容量を満たしている場合は何も追加しません。
        """
        data_bits = self.one_time_world_instance.get_converted_bits()  # 仮想的にQRデータビット列を取得
        symbol_capacity = self.one_time_world_instance.get_symbol_capacity()  # 仮想的にシンボル容量を取得

        # 終端パターンを追加
        data_bits_with_termination = self.add_termination_pattern(data_bits, symbol_capacity)

        # 結果をワールドに反映
        self.one_time_world_instance.QRCodeTerminationPlayer = self  # 自身のインスタンスを登録
        self.one_time_world_instance.set_converted_bits(data_bits_with_termination)  # 変換結果をWorldに反映する仮想的なメソッド

        return "Completed"