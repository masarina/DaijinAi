""" MEMO
・読み込む前に25＊25のマトリックスを
  n*2のマトリックスに変換します
・もちろん、データが同じ方向を向くようにします。

"""

import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer
import pandas as pd

class ColumnSplitterConcatPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 必ずNoneで初期化
        self.new_list2d = []
        self.replaced_matrix = None # 置き換え後のmatrix
        self.png_file_path = None # 写真のパス
        self.binary_matrix_2Dlist = None # 置き換え前のmatrix
        

    def return_my_name(self):
        return "ColumnSplitterConcatPlayer"
        
    def add_column_with_negative_13_to_the_left(self, matrix):
        # 新しい2次元リストを作成するためのリストを準備する
        new_matrix = []
    
        # 元の行に-13を左側に追加する処理を行う
        for row in matrix:
            new_row = [-13] + row  # 行の左側に-13を追加
            new_matrix.append(new_row)  # 新しいリストに追加
    
        return new_matrix
        
    def list2d_to_reverseRow(self, list2d):
        """ 2次元リストの行を逆順にするメソッド
        [[a],
        [b],
        [c]]
        であれば、
        [[c],
        [b],
        [a]]
        と変換します
        
        """
        
        """ 初期化 """
        reversed_list2d = []
        line_point = -1 # データを取得する行のインデックス
        
        """ メイン処理 """
        for _ in range(len(list2d)): # 行数分ループ
            # 1番後ろの行をとる
            line = list2d[line_point]
            
            # 新しいモノとする。
            reversed_list2d += [line]
    

    def main(self):
        """
        このメソッド実行直前に、スーパークラスのメンバ変数
        one_time_world_instanceに、最新のworldインスタンスを代入しています。
        
        引数：2次元リスト
        処理：2次元リストを
            右から2列ごとに分割させ、
            縦に連結させたものを、
            新しい2次元リストとする
        出力：新しい2次元リスト
        """
        """ 入力 """
        woP = self.one_time_world_instance.replacePatternPlayer
        self.replaced_matrix = woP.replaced_matrix # 置き換え後のmatrix
        self.png_file_path = woP.png_file_path # 写真のパス
        self.binary_matrix_2Dlist = woP.binary_matrix_2Dlist # 置き換え前のmatrix
        
        """ 初期化 """
        # 読み込んだqr配列(読み込み禁止箇所マーキング済み)を取得
        matrix = self.replaced_matrix.tolist()
        self.new_list2d # 最終的に完成品となるもの
        col_point = -1

        # 列数が奇数の場合
        is_last_col_bool = 1 == (len(list2d[0]) % 2) # マトリックスの列数が奇数だった場合True
        if is_last_col_bool:
          # 列数が奇数の場合、1番左の行の処理ができないので、1番左に列をひとつ追加
          matrix = self.add_column_with_negative_13_to_the_left(matrix) # 追加する列の各セルには-13を入れておく。
          
        loop_point = len(matrix[0] // 2) # 処理回数を計算。今回はマトリックスの右側2列ごとに処理するため、(全体の行数 * 1/2)回とする
        
        """ メイン処理 """
        
        # 列数の半分の回数、ループ処理
        for j in range(loop_point): # 列数の半分の数だけループ
          # 列を算出する
          
          
          row_num = len(matrix) # 行数
          # 後ろ2列を取得
          onetime_list2d =[] # 一時的リスト
          
          """ 2列を次のようにする。
          [...[2,3],...[5,6],...[8,9]]
          ↓
          [[8,9],[5,6],[2,3]] (▶︎ onetime_list2d)
          """
          for i in range(row_num): # 行数分ループ
            # インデックスを算出
            row_index = row_num - i
          
            # 1行をとる
            line = list2d[row_index] # 下から順に…
            
            # 2列部分にあたる箇所を取得
            pair = [line[col_point - 1], line[col_point]]
            
            # 一時的リストに追加
            onetime_list2d += [pair] # [[0, 1]] (appendと異なり、ひとつカッコが消滅するので…)
          
      
        
          # col_point を進める
          col_point += -2 # 後ろから2列ずつずらして読み込むので。
          
          # 2回に1回、行を反転させる
          if 0 == (col_point % 2): # 偶数で反転
            onetime_list2d = self.list2d_to_reverseRow(copy.deepcopy(onetime_list2d))
            
          # new_list2d の先頭に追加
          self.new_list2d = onetime_list2d + self.new_list2d
        
        
        """ 出力 """
        self.replaced_matrix # 置き換え後のmatrix
        self.png_file_path # 写真のパス
        self.binary_matrix_2Dlist # 置き換え前のmatrix
        self.new_list2d = new_list2d # データ部分をn*2のリストに変換したもの

        # 自身のプレイヤーの更新
        self.one_time_world_instance.columnSplitterConcatPlayer = self
        return "Completed"
