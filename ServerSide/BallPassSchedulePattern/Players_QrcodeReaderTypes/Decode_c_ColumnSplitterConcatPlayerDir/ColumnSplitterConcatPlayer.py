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
        for _ in range(len(list2d): # 行数分ループ
            # 1番後ろの行をとる
            line = list2d[line_point]
            
            # 新しいモノとする。
            reversed_list2d += [line]
    

    def main(self):
        """
        このメソッド実行直前に、スーパークラスのメンバ変数
        one_time_world_instanceに、最新のworldインスタンスを代入しています。
        """
        # 読み込んだqr配列(読み込み禁止箇所マーキング済み)を取得
        matrix = self.one_time_world_instance.replacePatternPlayer.replaced_matrix

        # 結果を保存
        self.one_time_world_instance.processed_dataframe = concatenated_df

        # 自身のプレイヤーの更新
        self.one_time_world_instance.columnSplitterConcatPlayer = self
        return "Completed"
