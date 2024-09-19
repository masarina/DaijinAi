import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeAlignmentPatternPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.qr_code_map = None  # QRコードのグリッドを格納する変数

    def return_my_name(self):
        return "QRCodeAlignmentPatternPlayer"

    def fill_alignment_pattern(self, grid):
        """
        アライメントパターンをQRコードに配置する関数（バージョン2用）
        """
        # アライメントパターンの位置はバージョン2では(20, 20)付近に配置される
        alignment_pattern_position = (20, 20)
        x_start, y_start = alignment_pattern_position

        # まず5×5で塗りつぶす
        for i in range(x_start - 2, x_start + 3):
            for j in range(y_start - 2, y_start + 3):
                grid[i][j] = -1

        # その後、中央部分を3×3で0に戻す
        for i in range(x_start - 1, x_start + 2):
            for j in range(y_start - 1, y_start + 2):
                grid[i][j] = 0

        # 最後に中央を1×1で-1に塗りつぶす
        grid[x_start][y_start] = -1

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
        
        # アライメントパターンを適用して、qr_code_mapに保存
        self.qr_code_map = self.fill_alignment_pattern(self.qr_code_map)

        print(f"{self.return_my_name()}が実行されました。")

        # 自身を更新
        self.one_time_world_instance.qRCodeAlignmentPatternPlayer = self

        return "Completed"
