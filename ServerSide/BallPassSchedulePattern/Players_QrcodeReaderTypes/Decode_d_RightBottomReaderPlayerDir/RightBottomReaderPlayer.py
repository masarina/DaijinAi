import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer
""" ATTENTION
ただのテンプレートです！
"""
class RightBottomReaderPlayer(SuperPlayer):  # 名前はりなに決めてもらってもOKよ！
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.data_read = []  # データを読み込んで保持する変数

    def return_my_name(self):
        return "RightBottomReaderPlayer"  # ここも任意の名前で変更可能よ
    
    def flatten_list2d(self, list2d=None):
        """ 2次元リストを1次元リストにするメソッド
        ・shape的に(n, 2)の2次元リストに限る
        """
        
        """ 初期化 """
        read_list = [] # 読み込まれた1次元リスト(最終的に完成品となる)
        
        """ メイン処理 """
        for pair in list2d:
            # 右, 左の順に格納。負の数である場合は格納しないでパスする。
            if 0 > pair[1]:
                read
    

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
