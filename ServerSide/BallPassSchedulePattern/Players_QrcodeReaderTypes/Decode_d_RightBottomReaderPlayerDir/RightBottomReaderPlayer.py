import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class RightBottomReaderPlayer(SuperPlayer):  # 名前はりなに決めてもらってもOKよ！
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.data_read = []  # データを読み込んで保持する変数
        self.replaced_matrix = None # 置き換え後のmatrix
        self.png_file_path = None # 写真のパス
        self.binary_matrix_2Dlist = None # 置き換え前のmatrix
        self.new_list2d = None # データ部分をn*2のリストに変換したもの


    def return_my_name(self):
        return "RightBottomReaderPlayer"  # ここも任意の名前で変更可能よ
    
    def flatten_list2d(self, list2d=None):
        """ 2次元リストを1次元リストにするメソッド
        ・shape的に(n, 2)の2次元リストに限る
        """
        
        """ 入力 """
        list2d
        
        """ 初期化 """
        read_list = [] # 読み込まれた1次元リスト(最終的に完成品となる)
        
        """ メイン処理 """
        # 全体を回す。
        for pair in list2d: # 1行取る
            
            """ 右, 左の順に格納。負の数である場合は格納しないでパスする。 """
            # 右から見る。
            if 0 <= pair[1]: # 0以上であれば
                read_list.append(pair[1]) # 登録
            else:
                pass
                
            # 次に左を見る。
            if 0 <= pair[0]: # 0以上であれば
                read_list.append(pair[0]) # 登録
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
        
        """ 入力 """
        woP = self.one_time_world_instance.columnSplitterConcatPlayer
        self.replaced_matrix = woP.replaced_matrix # 置き換え後のmatrix
        self.png_file_path = woP.png_file_path # 写真のパス
        self.binary_matrix_2Dlist = woP.binary_matrix_2Dlist # 置き換え前のmatrix
        self.new_list2d = woP.new_list2d # データ部分をn*2のリストに変換したもの

        
        
        # n行2列のマトリックスを取得
        binary_matrix = self.binary_matrix_2Dlist
        
        """ メイン処理 """
        # データを右下から読み込む
        self.data_read = self.flatten_list2d(list2d=binary_matrix)
        # 読み込んだデータを確認
        print(f"データが右下から読み込まれました: {self.data_read}")

        """ 出力 """
        self.replaced_matrix # 置き換え後のmatrix
        self.png_file_path # 写真のパス
        self.new_list2d # データ部分をn*2のリストに変換したもの
        self.data_read # データ部分を1次元リスト化したもの。

        # 自身を更新
        self.one_time_world_instance.rightBottomReaderPlayer = self

        return "Completed"
