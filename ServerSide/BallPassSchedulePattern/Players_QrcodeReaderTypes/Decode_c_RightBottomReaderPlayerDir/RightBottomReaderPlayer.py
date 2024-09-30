import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class RightBottomReaderPlayer(SuperPlayer):  # 名前はりなに決めてもらってもOKよ！
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.data_read = []  # データを読み込んで保持する変数

    def return_my_name(self):
        return "RightBottomReaderPlayer"  # ここも任意の名前で変更可能よ

    def read_data_from_right_bottom(self, matrix):
        """
        QRコードのデータ部分を右下から左上に向けて読み込む。
        Args:
            matrix (list): 25x25のバイナリマトリックス。
        Returns:
            list: 読み込んだデータのリスト。
        """
        data = []

        # 右下から左上に向かってジグザグに読み取る
        size = len(matrix)
        for col in range(size-1, 0, -2):  # 2列ごとに進む（右から左）
            for row in range(size-1, -1, -1):  # 下から上に進む
                if matrix[row][col] != -1 and matrix[row][col] != -2:  # 黒と白のパターン部分以外
                    data.append(matrix[row][col])
                if col > 0 and matrix[row][col-1] != -1 and matrix[row][col-1] != -2:
                    data.append(matrix[row][col-1])

        return data

    def main(self):
        """
        このメソッド実行直前に、
        このスーパークラスのメンバ変数 one_time_world_instanceに、
        最新のworldインスタンスを代入しています。
        """
        # QRコードのマトリックスを取得
        binary_matrix = self.one_time_world_instance.qrCodeCorrectionPlayer.binary_matrix_2Dlist

        # データを右下から読み込む
        self.data_read = self.read_data_from_right_bottom(binary_matrix)

        # 読み込んだデータを確認
        print(f"データが右下から読み込まれました: {self.data_read}")

        # 自身を更新
        self.one_time_world_instance.rightBottomReaderPlayer = self

        return "Completed"
