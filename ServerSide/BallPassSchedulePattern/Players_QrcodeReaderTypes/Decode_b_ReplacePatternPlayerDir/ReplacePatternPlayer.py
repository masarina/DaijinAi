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
        # 左上
        matrix_np[0:7, 0:7] = -11
        # 右上
        matrix_np[0:7, 18:25] = -11
        # 左下
        matrix_np[18:25, 0:7] = -11

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
        
        """ 初期化 """
        # FormatInfoCatcherPlayerで取得したmatrixを取得
        matrix_2Dlist = copy.deepcopy(self.one_time_world_instance.formatInfoCatcherPlayer.matrix)
        
        """ matrixの特定部分を-11に置き換え """
        self.replaced_matrix = self.replace_patterns(matrix_2Dlist)
        
        # 自信を更新
        self.one_time_world_instance.replacePatternPlayer = self
        
        """ 結果 """
        # 置き換え後のmatrixを準備
        self.replaced_matrix

        return "Completed"
