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
        ・QRcodeに特化。shape的に(n, 2)の2次元リストに限る
        """
        
        """ 入力 """
        list2d
        
        """ 初期化 """
        read_list = [] # 読み込まれた1次元リスト(最終的に完成品となる)
        
        """ メイン処理 """
        for pair in list2d:
            
            """ 右, 左の順に格納。負の数である場合は格納しないでパスする。 """
            # 右の要素
            if 0 > pair[1]:
                read_list.append(pair[1])
            else:
                pass
                
            # 左の要素
            if 0 > pair[0]:
                read_list.append(pair[0]):
            else:
                pass
        
        """ 出力 """
        return read_list
    

    def main(self):
        """
        このメソッド実行直前に、
        このスーパークラスのメンバ変数 one_time_world_instanceに、
        最新のworldインスタンスを代入しています。
        """
        
        """ 初期化 """
        # QRコードのマトリックスを取得
        binary_matrix = self.one_time_world_instance.qrCodeCorrectionPlayer.binary_matrix_2Dlist
        
        """ メイン処理 """
        # データを右下から読み込む
        self.data_read = self.flatten_list2d(list2d=binary_matrix)
        # 読み込んだデータを確認
        print(f"データが右下から読み込まれました: {self.data_read}")
        # 自身を更新
        self.one_time_world_instance.rightBottomReaderPlayer = self

        """ 完成したデータ """
        self.data_read


        return "Completed"
