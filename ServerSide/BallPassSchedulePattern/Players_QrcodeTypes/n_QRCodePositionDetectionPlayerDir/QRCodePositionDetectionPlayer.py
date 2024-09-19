import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

多分、余分にマイナス2してるかも、周りのヤツの処理


class QRCodePositionDetectionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.grid_size = 25  # QRコードのグリッドサイズ
        self.qr_code_map = None  # 位置検出パターンを格納するための変数

    def return_my_name(self):
        return "QRCodePositionDetectionPlayer"

    def fill_position_detection_patterns(self):
        """位置検出パターンの作成"""
        # 25×25の2次元リストを初期化 (全て0で埋める)
        grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # 位置検出パターンの座標範囲 (7×7) の塗りつぶし
        position_patterns = [
            (0, 0),      # 左上
            (0, self.grid_size - 7),  # 右上
            (self.grid_size - 7, 0)  # 左下
        ]

        # 各位置検出パターンの領域を-1で塗りつぶし (7×7)
        for (x_start, y_start) in position_patterns:
            for i in range(x_start, x_start + 7):
                for j in range(y_start, y_start + 7):
                    grid[i][j] = -1

        # 中央を5×5で-2に戻す (5×5)
        for (x_start, y_start) in position_patterns:
            for i in range(x_start + 1, x_start + 6):  # 中央部分を5×5で-2に戻す
                for j in range(y_start + 1, y_start + 6):
                    grid[i][j] = -2

        # さらに中央の3×3を-1で塗りつぶす (3×3)
        for (x_start, y_start) in position_patterns:
            for i in range(x_start + 2, x_start + 5):  # 中央部分を3×3で-1に戻す
                for j in range(y_start + 2, y_start + 5):
                    grid[i][j] = -1

        # 位置検出パターンの周囲1マスを-2で塗りつぶす
        for (x_start, y_start) in position_patterns:
            for i in range(x_start - 1, x_start + 8):  # 周り1マス分を-2で埋める
                for j in range(y_start - 1, y_start + 8):
                    if 0 <= i < self.grid_size and 0 <= j < self.grid_size and (i < x_start or i >= x_start + 7 or j < y_start or j >= y_start + 7):
                        grid[i][j] = -2

        return grid

    def main(self):
        """
        このメソッド実行直前に、
        このスーパークラスのメンバ変数
        one_time_world_instanceに、
        最新のworldインスタンスを代入しています。
        
        このメソッド終了後、
        メインで使用しているworld_instanceを
        このスーパークラスのメンバ変数
        one_time_world_instanceで上書きし、
        更新しています。
        """
        
        # 位置検出パターンを適用して、qr_code_mapに保存
        self.qr_code_map = self.fill_position_detection_patterns()

        print(f"{self.return_my_name()}が実行されました。")

        # 自身を更新
        self.one_time_world_instance.qRCodePositionDetectionPlayer = self

        return "Completed"
