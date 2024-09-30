import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeTimingPatternPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # プレイヤーの名前
        self.qr_code_map = None  # QRコードのマップを保持する変数

    def return_my_name(self):
        return "QRCodeTimingPatternPlayer"

    def add_timing_pattern(self, qr_code_map):
        """
        バージョン2のQRコードにタイミングパターンを追加する関数
        入力: 2次元リスト (25x25)
        出力: タイミングパターンが追加された2次元リスト
        """
        grid_size = len(qr_code_map)
    
        # タイミングパターンは位置検出パターンの下と右にあるため、座標が(6,y)と(x,6)の位置に交互に配置
        for i in range(8, grid_size - 8):  # タイミングパターンは (6,y) と (x,6) の位置に配置
            # 横方向のタイミングパターン (y = 6)
            qr_code_map[6][i] = -2 if i % 2 == 0 else -1 # 偶数であれば-2(白色)、奇数であれば-1(黒色)とする。
            # 縦方向のタイミングパターン (x = 6)
            qr_code_map[i][6] = -2 if i % 2 == 0 else -1
    
        return qr_code_map


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
        
        # QRコードのタイミングパターンを追加
        self.qr_code_map = self.add_timing_pattern(self.one_time_world_instance.qr_code_map)

        print(f"{self.return_my_name()}が実行されました。")

        # 自身を更新
        self.one_time_world_instance.qRCodeTimingPatternPlayer = self

        return "Completed"
