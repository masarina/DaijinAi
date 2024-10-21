import os, sys
import numpy as np
import copy
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ReplacePatternPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 初期化は必ずNone
        self.replaced_matrix = None
        self.png_file_path = None # 写真のパス
        self.binary_matrix_2Dlist = None # コード部分25＊25
    
    def return_my_name(self):
        return "ReplacePatternPlayer"
    
    def replace_patterns(self, matrix):
        """
        QRコードの位置検出パターン、タイミングパターン、ダークモジュールを-11に置き換える。
        25x25のQRコードのマトリックスを前提として処理する。
        """
        # numpy配列に変換して作業する
        matrix_np = np.array(matrix)
        
        # 位置検出パターン（左上、右上、左下の位置）
        matrix_np[0:7, 0:7] = -11  # 7×7の領域(と、内側の方1分)を-11で塗りつぶす
        matrix_np[0:7, -7:] = -11  
        matrix_np[-7:, 0:7] = -11  

        # タイミングパターン（縦横方向の特定の行列）
        matrix_np[6, 8:17] = -11  # 横方向
        matrix_np[8:17, 6] = -11  # 縦方向

        # ダークモジュール（特定の座標）
        matrix_np[8, 13] = -11

        # 完成した置き換え後のマトリックスを戻り値とする
        return matrix_np
    
    def main(self):
        """
        抽出後のmatrixを取得し、位置検出パターン、タイミングパターン、ダークモジュールを
        -11に置き換える。
        """
        """ 入力 """
        woP = self.one_time_world_instance.patternDetectionPlayer
        self.png_file_path = woP.png_file_path # 写真のパス
        self.binary_matrix_2Dlist = woP.binary_matrix_2Dlist # コード部分25＊25
        
        """ 初期化 """
        # FormatInfoCatcherPlayerで取得したmatrixを取得
        matrix_2Dlist = copy.deepcopy(self.one_time_world_instance.formatInfoCatcherPlayer.matrix)
        
        """ matrixの特定部分を-11に置き換え """
        self.replaced_matrix = self.replace_patterns(matrix_2Dlist)
        
        # 自身を更新
        self.one_time_world_instance.replacePatternPlayer = self
        
        """ 出力 """
        self.replaced_matrix # 置き換え後のmatrix
        self.png_file_path # 写真のパス
        self.binary_matrix_2Dlist # 置き換え前のmatrix

        return "Completed"
