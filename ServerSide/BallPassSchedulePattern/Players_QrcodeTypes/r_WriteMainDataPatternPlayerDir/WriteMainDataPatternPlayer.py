import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer


class WriteMainDataPatternPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None  # 必ずNoneで初期化

    def return_my_name(self):
        return "WriteMainDataPatternPlayer"
        
    def main(self):
        # マップを取得
        qr_map_2Dlist = 
        
        maindata_2Dlist = self.one_time_world_instance.rSXorCalculationPlayer.xor_result_polynomial

        for 
        
        self.one_time_world_instance.writeMainDataPatternPlayer = self
        
        return "Completed"

    def one_bit_writer(self, qr_map_2Dlist, written_row_col=(None,None)):
        """
        25x25の2次元リスト (qr_map_2Dlist) と
        前回書き込んだ座標 (row, col) を処理するメインメソッド。
        """
        # 初期化とチェック
        assert len(qr_map_2Dlist) == 25 and len(qr_map_2Dlist[0]) == 25, "リストのサイズが不正です。25x25を想定しています。"
        
        # colを使用するのでコピー
        row = written_row_col[0]
        col = written_row_col[1]
        cache = written_row_col[1]
        
        # colが奇数の場合
        if col % 2 == 1:
            cache += 1
            if cache % 4 == 0:
                # 4で割り切れる場合、右上に移動 (row -= 1, col += 1)
                row -= 1
                col += 1
                
                # map座標をはみ出た場合の処理
                if row < 0: # 上にはみ出た
                    row += 1 # rowのみ戻して
                    col -= 2 # 左に2つ移動
                
                    # さらにcolが左にはみ出た場合
                    if col < 0:
                        col = "overflow"
                
            else:
                # 割り切れない場合、右下に移動 (row += 1, col += 1)
                row += 1
                col += 1
                
                # はみ出た場合の処理
                if row > 24: # 下にはみ出た
                    row -= 1 # 1行戻す
                    col -= 2 # 左に2列移動
                    
                    # さらにcolが左にはみ出た場合
                    if col < 0:
                        col = "overflow"
                    
        
        # colが偶数の場合
        else:
            # 左に移動(row += 0, col -= 1)
            col -= 1
            
            # colが左にはみ出た場合
            if col < 0:
                col = "overflow"

        
        # 更新した座標を返す
        return qr_map_2Dlist, (row, col)
