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

    def main(self):
        """
        このメソッド実行直前に、スーパークラスのメンバ変数
        one_time_world_instanceに、最新のworldインスタンスを代入しています。
        """

        # 結果を保存
        self.one_time_world_instance.processed_dataframe = concatenated_df

        # 自身のプレイヤーの更新
        self.one_time_world_instance.columnSplitterConcatPlayer = self
        return "Completed"
