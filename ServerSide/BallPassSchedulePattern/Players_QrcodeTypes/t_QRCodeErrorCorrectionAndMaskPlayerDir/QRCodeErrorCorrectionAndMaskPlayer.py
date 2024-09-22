import os, sys
import numpy as np
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeErrorCorrectionAndMaskPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 必ずNoneで初期化
        self.format_bits = None  # 15bitの形式情報を保持
        self.format_info = None # 完成15ビットデータ

    def return_my_name(self):
        return "QRCodeErrorCorrectionAndMaskPlayer"

    def generate_format_info(self, error_level_bits, mask_pattern_bits):
        """
        エラー補正レベルとマスクパターンの5bitを基に、誤り訂正ビットを追加して15bitの形式情報を生成する。
        """
        # 初期の5bitの形式情報
        initial_bits = np.array(list(error_level_bits + mask_pattern_bits), dtype=int)

        # G(x) = x10 + x8 + x5 + x4 + x2 + x + 1 に対応するビット配列
        gx_bits = np.array([1, 0, 1, 0, 0, 1, 0, 1, 1, 1], dtype=int)  # x^10 + x^8 + ... + 1

        # x^10を掛けた状態にするため、末尾に0を10個付加する
        padded_bits = np.concatenate([initial_bits, np.zeros(10, dtype=int)])

        # ステップごとに剰余を計算
        for i in range(len(initial_bits)):
            if padded_bits[i] == 1:  # 1のときのみ割り算を実行
                padded_bits[i:i+11] ^= gx_bits  # 剰余をXORで計算

        # 最後に残るのが剰余ビット（10bit）
        remainder_bits = padded_bits[-10:]

        # 形式情報は初期の5bitと剰余の10bitを結合して15bitに
        format_bits = np.concatenate([initial_bits, remainder_bits])

        # 結果を保存
        self.format_bits = format_bits
        return format_bits

    def main(self):
        """
        形式情報を生成するメイン処理。
        エラー補正レベル '10'（H）とマスクパターン '000' を使用して形式情報を作成する。
        """
        # エラー補正レベルとマスクパターンのビット列
        error_level_bits = '10'  # Hレベルのエラー訂正
        mask_pattern_bits = '000'  # マスクパターンは000

        # 形式情報の生成
        self.format_info = self.generate_format_info(error_level_bits, mask_pattern_bits)

        # 自身を更新
        self.one_time_world_instance.qrCodeErrorCorrectionAndMaskPlayer = self
        return "Completed"