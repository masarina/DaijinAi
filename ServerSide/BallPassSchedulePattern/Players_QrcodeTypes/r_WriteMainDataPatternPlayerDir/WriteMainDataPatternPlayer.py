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
        qr_map_2Dlist = self.one_time_world_instance.qRCodeMarkingPlayer.modified_qr_code_map
        
        # メインデータを取得
        maindata_2Dlist = copy.deepcopy(self.one_time_world_instance.rSXorCalculationPlayer.xor_result_polynomial)

        """ 書き込み開始 """
        now_row_col = (24,24) # 座標保持する変数(1番右下座標で初期化)
        beforetime_write_can_status = True # 前回の書き込めたか否かの情報保持(初期化は、前回書き込めたことにするためTrue)
        
        for bit_data in maindata_2Dlist:
            
            """ 書き込み処理 """
            # 今回書き込む行と列を取得
            row = now_row_col[0]
            col = now_row_col[1]
            
            # この座標は書き込んで問題ないか確認する。
            if qr_map_2Dlist[row][col] == 0: # 前回、書き込んで良い場所のみ、0で初期化しました。
                
                """ かつ、前回書き込めていない場合 """
                if beforetime_write_can_status == False:
                    # かつ、今回colが奇数の場合はpass(国際規格的に2行ずつデータを配置することにおいては、右側を優先とする為。)
                    if col%2 == 0: 
                        beforetime_write_can_status = False # 書き込めなかったらFalse
                        pass
                        
                    else: # かつ偶数である場合は書き込んでOK
                        qr_map_2Dlist[row][col] = bit_data # 書き込み
                        beforetime_write_can_status = True # 書き込めたらTrue
                        
            else: # 0ではなかったら、pass
                beforetime_write_can_status = False # 書き込めなかったらFalse
                pass
                
                
            # 次に書き込む場所を算出してnow_row_colを更新
            now_row_col = self.next_writing_rowcol_catcher(qr_map_2Dlist, written_row_col=written_row_col)
    
        # メンバ変数に保存
        self.updated_qr_map_2Dlist = maindata_2Dlist
        
        self.one_time_world_instance.writeMainDataPatternPlayer = self
        
        return "Completed"

    def next_writing_rowcol_catcher(self, qr_map_2Dlist, written_row_col=(None,None)):
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
