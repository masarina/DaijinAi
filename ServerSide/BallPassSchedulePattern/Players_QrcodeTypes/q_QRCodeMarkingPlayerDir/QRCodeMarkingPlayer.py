import os, sys
import numpy as np  # numpyをインポート
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeMarkingPlayer(SuperPlayer):  # 名前を変更
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.modified_qr_code_map = None  # 更新されたQRコードのグリッドを保存する変数
        self.marking_num = -4  # マーキングする値（今回は-4と言う数字を書き込むことにした）

    def return_my_name(self):
        return "QRCodeMarkingPlayer"  # 新しい名前を返す

    def modify_qr_code(self, qr_code_map):
        """
        QRコードの6ビット部分に指定された値を代入するメソッド。
        numpyを使用して2次元リストを扱い、スライスを適用する。
        """
        # qr_code_mapをnumpy配列に変換
        qr_code_array = np.array(qr_code_map)

        # 指定された箇所にself.marking_numを代入
        qr_code_array[0:5, 8] = self.marking_num  # 上部の6ビット部分
        qr_code_array[7, 8] = self.marking_num    # 中央の縦
        qr_code_array[8, 8] = self.marking_num    # 中央の縦
        qr_code_array[8, 0:5] = self.marking_num  # 左部の6ビット部分
        qr_code_array[8, 7] = self.marking_num    # 中央の横
        qr_code_array[-7:-1, 8] = self.marking_num  # 下部の縦
        qr_code_array[8, -8:-1] = self.marking_num  # 右部の横
        qr_code_array[-8, 8] = -1 # ダークモジュールのマーキング

        # numpy配列をリストに戻して返す
        return qr_code_array.tolist()

    def main(self):
        """
        このメソッド実行直前に、スーパークラスのメンバ変数
        one_time_world_instanceに最新のworldインスタンスが代入されている。
        """
        # 前のプレイヤーが生成したQRコードの2次元リストを取得
        qr_code_map = self.one_time_world_instance.qRCodeAlignmentPatternPlayer.qr_code_map

        # QRコードを修正
        self.modified_qr_code_map = self.modify_qr_code(qr_code_map)

        print(f"{self.return_my_name()}が実行されました。QRコードが修正されました。")

        # 自身を更新
        self.one_time_world_instance.qRCodeMarkingPlayer = self

        return "Completed"
