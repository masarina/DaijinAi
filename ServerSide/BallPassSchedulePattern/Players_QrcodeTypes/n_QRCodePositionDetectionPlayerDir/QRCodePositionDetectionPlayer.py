import os, sys
import numpy as np  # numpyをインポート
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer


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
        grid = np.zeros((self.grid_size, self.grid_size), dtype=int)

        # 位置検出パターンの座標
        # 左上のパターン (7×7)
        grid[0:6, 0:6] = -1  # 7×7の領域を-1で塗りつぶす
        grid[1:5, 1:5] = -2  # 中央を5×5で-2に戻す
        grid[2:4, 2:4] = -1  # 中央の3×3を-1で塗りつぶす
        grid[0:7, 7] = -2  # 右辺1マスを-2で塗りつぶす
        grid[7, 0:7] = -2  # 下辺1マスを-2で塗りつぶす
    
        # 右上のパターン (7×7)
        grid[0:7, -7:] = -1  # 7×7の領域を-1で塗りつぶす
        grid[1:6, -6:-1] = -2  # 中央を5×5で-2に戻す
        grid[2:5, -5:-2] = -1  # 中央の3×3を-1で塗りつぶす
        grid[0:8, -8] = -2  # 左辺1マスを-2で塗りつぶす
        grid[7, -8:] = -2  # 下辺1マスを-2で塗りつぶす
    
        # 左下のパターン (7×7)
        grid[-7:, 0:7] = -1  # 7×7の領域を-1で塗りつぶす
        grid[-6:-1, 1:6] = -2  # 中央を5×5で-2に戻す
        grid[-5:-2, 2:5] = -1  # 中央の3×3を-1で塗りつぶす
        grid[-8:, 7] = -2  # 右辺1マスを-2で塗りつぶす
        grid[-8, 0:8] = -2  # 上辺1マスを-2で塗りつぶす


        # numpy配列をリストに戻して返す
        return grid.tolist()

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

        print(f"{self.return_my_name()}が実行されました。QRコードの位置検出パターンが適用されました。")

        # 自身を更新
        self.one_time_world_instance.qRCodePositionDetectionPlayer = self

        return "Completed"
