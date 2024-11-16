using UdonSharp;
using UnityEngine;

public class WriteMainDataPatternPlayer : SuperPlayer
{
    // 必要なフィールドをUnityエディタでアタッチ
    public QRCodeMarkingPlayer qRCodeMarkingPlayer;
    public RSXorCalculationPlayer rSXorCalculationPlayer;
    public RinaNumpy rinaNumpy; // RinaNumpyを追加

    // フィールド
    public string[] modeCharNumInfoChecksumBitlist;
    public int version;
    public int gridSize;
    public int[,] qrCodeMap;
    public int[,] modifiedQrCodeMap;
    public int[,] updatedQrMap2DList;

    // 書き込み中の状態保持
    private int[] currentRowCol = new int[2] { 24, 24 }; // 初期座標（右下）
    private bool previousWriteStatus = true; // 初期状態は「書き込めた」

    public override string ExecuteMain()
    {
        // データの取得
        modeCharNumInfoChecksumBitlist = qRCodeMarkingPlayer.modeCharNumInfoChecksumBitlist;
        version = qRCodeMarkingPlayer.version;
        gridSize = qRCodeMarkingPlayer.gridSize;
        qrCodeMap = qRCodeMarkingPlayer.qrCodeMap;
        modifiedQrCodeMap = qRCodeMarkingPlayer.modifiedQrCodeMap;

        // メインデータを取得
        int[,] maindata2DList = rinaNumpy.CopyInt2DArray(rSXorCalculationPlayer.xorResultPolynomial);

        // 書き込み開始
        for (int i = 0; i < maindata2DList.GetLength(0); i++)
        {
            for (int j = 0; j < maindata2DList.GetLength(1); j++)
            {
                int bitData = maindata2DList[i, j];

                int row = currentRowCol[0];
                int col = currentRowCol[1];

                // 書き込み可能な場所を確認
                if (qrCodeMap[row, col] == 0)
                {
                    if (!previousWriteStatus && col % 2 == 0)
                    {
                        previousWriteStatus = false; // 書き込めなかった場合の状態保持
                        continue;
                    }
                    else
                    {
                        modifiedQrCodeMap[row, col] = bitData;
                        previousWriteStatus = true; // 書き込み成功
                    }
                }
                else
                {
                    previousWriteStatus = false; // 書き込み失敗
                }

                // 次の書き込み位置を計算
                currentRowCol = NextWritingRowCol(modifiedQrCodeMap, currentRowCol);
                if (currentRowCol[1] == -1)
                {
                    Debug.LogError("書き込み範囲を超えました。");
                    return "Error";
                }
            }
        }

        // メンバ変数に保存
        updatedQrMap2DList = modifiedQrCodeMap;

        // 自身のインスタンスをworldに登録
        this.oneTimeWorldInstance.writeMainDataPatternPlayer = this;

        return "Completed";
    }

    private int[] NextWritingRowCol(int[,] qrMap2DList, int[] writtenRowCol)
    {
        int row = writtenRowCol[0];
        int col = writtenRowCol[1];

        // colが奇数の場合
        if (col % 2 == 1)
        {
            col++;
            if (col % 4 == 0)
            {
                row--;
                col++;
                if (row < 0)
                {
                    row++;
                    col -= 2;
                    if (col < 0)
                    {
                        col = -1; // overflowを表す
                    }
                }
            }
            else
            {
                row++;
                col++;
                if (row > 24)
                {
                    row--;
                    col -= 2;
                    if (col < 0)
                    {
                        col = -1; // overflowを表す
                    }
                }
            }
        }
        else
        {
            col--;
            if (col < 0)
            {
                col = -1; // overflowを表す
            }
        }

        return new int[2] { row, col };
    }
}
