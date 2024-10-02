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
        # DataFrameの右から列を分割して縦に結合する処理を行う
        df = self.one_time_world_instance.some_dataframe  # 任意のDataFrameを取得
        num_columns_to_split = 2  # 例えば右から2列を分割する
        split_df = df.iloc[:, -num_columns_to_split:]  # 右から列を取得
        remaining_df = df.iloc[:, :-num_columns_to_split]  # 残りの列
        concatenated_df = pd.concat([remaining_df, split_df], axis=0)  # 縦に結合

        # 結果を保存
        self.one_time_world_instance.processed_dataframe = concatenated_df

        # 自身のプレイヤーの更新
        self.one_time_world_instance.columnSplitterConcatPlayer = self
        return "Completed"
