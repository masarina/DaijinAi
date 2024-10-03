import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeTerminationPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤー名をNoneで初期化
        self.data_bits_with_termination

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


    def check_data_size(self, data_bits, symbol_capacity):  # ← 追加部分
        """
        エラー訂正レベルHに基づき、データビット列がシンボル容量の70%以下であることを確認します。
        """
        # 4bitの倍数にした時の0の数を算出
        pad_size = max_data_bits % 4
        
        # データ容量の最大値はシンボル容量の70%
        max_data_bits = symbol_capacity * 0.7  # データビット列がシンボル容量の70%を超えないことが条件

        if (len(data_bits) + pad_size) > max_data_bits:
            raise ValueError("データビット列がエラー訂正レベルHの制限を超えています。")  # ← 追加部分


    def main(self):
        """
        データビット列の終端に4ビットの終端パターンを付加する処理。
        シンボル容量を満たしている場合は何も追加しません。
        
        QRコードのバージョン2（モデル2）のシンボル容量は、国際規格 ISO/IEC 18004 に基づき
        25 × 25 のシンボルサイズから計算した。
    
        - 25 × 25 = 625 モジュール（全体のシンボル数）
        - 文字の種類情報 bit
        - 
        - 位置検出パターン（7 × 7 × 3 = 147 モジュール）
        - アライメントパターン（5 × 5 = 25 モジュール）
        - 読み取り禁止ゾーン（45 モジュール）
        - タイミングパターン（10 モジュール）
        - 左下のダークモジュール（1 モジュール）
        - フォーマット情報（15 モジュール）
    
        これらの合計243ビットを差し引いた、有効なデータ領域は
        625 - 243 = 382ビットです。
    
        したがって、シンボル容量は 382 ビットとしています。
        """
        
        """ 初期化 """
        character_count_bits = self.one_time_world_instance.qRCodeCharacterCountPlayer.character_count_bits # 文字の種類情報、の次に追加する、文字数情報
        data_bits = self.one_time_world_instance.qRCodeBitConversionPlayer.converted_bits  # 仮想的にQRデータビット列を取得
        
        symbol_capacity = 382
        
        # データサイズの確認(エラー訂正コード部分に入り組んでいたら、ダメなので。)
        self.check_data_size(data_bits, symbol_capacity)  

        # 終端パターンを追加
        self.data_bits_with_termination = self.add_termination_pattern(data_bits, symbol_capacity)

        # 結果をワールドに反映
        self.one_time_world_instance.QRCodeTerminationPlayer = self  # 自身のインスタンスを登録
        self.one_time_world_instance.set_converted_bits(data_bits_with_termination)  # 変換結果をWorldに反映する仮想的なメソッド

        return "Completed"
