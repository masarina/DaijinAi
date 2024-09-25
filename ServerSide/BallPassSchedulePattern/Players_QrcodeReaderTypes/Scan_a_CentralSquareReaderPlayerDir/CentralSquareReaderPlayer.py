class CentralSquareReaderPlayer:
    def __init__(self):
        self.my_name = None  # 初期化は必ずNone
        self.binary_matrix_2Dlist = None  # QRコードの2次元リストを保持する
        self.png_file_path = None

    def return_my_name(self):
        return "CentralSquareReaderPlayer"

    def small_sidecatcher(self, a, b):
        return (a + b - ((a - b) * 2) / 2) / 2
        
    def small_sideindex_catcher(self, a, b):
        beta = (a + b - ((a - b) * 2) / 2) / 2
        if a == beta:
            return 0
        else:
            return 1
        
    def extract_central_square(self, r_p=80):
        """
        binary_matrix_2Dlist の中央部分 (r_p%) を抽出する。
        """
        # 短い方の長さを取り、そのr_p%の値をとる
        default_rowsize = len(self.binary_matrix_2Dlist)
        default_colsize = len(self.binary_matrix_2Dlist[0])
        small_side_index = small_sideindex_catcher(default_rowsize, default_colsize)
        small_sidesize = self.binary_matrix_2Dlist[small_side_index]
        line_length = small_sidesize // 100 * r_p # r_p%の長さを算出

        # 中央座標をとる
        row_halfnum = default_rowsize / 2
        col_halfnum = default_colsize / 2
        center_rowcol = (row_halfnum, col_halfnum)
        
        # 写真全体(100%)の内、中央80%の正方形の左上の座標の算出
        line_halflength = line_length / 2 # 正方形の半径を取得
        start_col = center_rowcol[1] - line_halflength # 中央よりも、正方形の半径分、左側
        start_row = center_rowcol[0] - line_halflength # 中央よりも、正方形の半径分、上側
        leftup_rowcol = (start_row, start_col)
        
        # 空のmatrixを作成
        _row = []
        for i in range(line_length):
            _row += [None]
        new_mtr = []
        for i in range(line_length):
            new_mtr += [_row]

        # 長いので変名
        mtr = self.binary_matrix_2Dlist
        
        """ 空のマトリックスに1bitずつ書き込んでいく。 """
        for n in range(len(new_mtr)): # r_p%の行数分だけループ
            
            # 画像データ中の n行目を取得
            _row = leftup_rowcol[0] # 開始地点左上座標のrowを取得
            row_data = mtr[_row + n] # 画像データのn行目全てを取得
            
            # 画像データr_p% の列の部分 だけを抽出
            for o in range(len(new_mtr[0])): # r_p%の列数分だけループ
                _col = leftup_rowcol[1] # 開始地点左上座標のcolを取得
                
                # 画像データr_p% のn行目 o列のbitデータを取得
                bit_data = row_data[_col + o] # r_p%に当たるn行目のo番目のbitデータを取得
                
                # 新しいmatrixの方に書き込む
                new_mtr[n][o] = bit_data
                
                
        return new_mtr # 完成したr_p%部分のみのmatrixを返却
            

    def main(self):
        """
        QRコード画像を読み込み、binary_matrix_2Dlist にリサイズして保持。
        """
        # ここに画像の読み込み処理 (既存の処理)
        self.read_qr_code(self.png_file_path)

        # 中央の80%部分の正方形を取得
        self.binary_matrix_2Dlist = self.extract_central_square()

        # 結果を表示
        print("中央部分の抽出結果（ビットデータ化のみの時点）:")
        print(self.binary_matrix_2Dlist) 
        
        self.one_time_world_instance.centralSquareReaderPlayer = self

        return "Completed"
