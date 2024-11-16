using UdonSharp;
using UnityEngine;

public class QRCodePositionDetectionPlayer : SuperPlayer
{
    public QRCodeMapInitializerPlayer qRCodeMapInitializerPlayer; // 前のプレイヤーからデータを取得
    public RinaNumpy rinaNumpy; // RinaNumpyをアタッチして活用
    public int gridSize = 25; // QRコードのグリッドサイズ
    public int[][] qrCodeMap; // 位置検出パターンを格納する配列

    public override string ReturnMyName()
    {
        return "QRCodePositionDetectionPlayer";
    }

    public bool QRCodePositionDetectionPlayerReset()
    {
        return true;
    }

    public void FillPositionDetectionPatterns()
    {
        // 25x25の2次元配列を初期化（すべて0）
        qrCodeMap = new int[gridSize][];
        for (int i = 0; i < gridSize; i++)
        {
            qrCodeMap[i] = new int[gridSize];
        }

        // RinaNumpyの`ZerosLike_FloatArray`を利用（Unityでは型変換が必要）
        float[] zerosRow = rinaNumpy.ZerosLike_FloatArray(new float[gridSize]);
        for (int i = 0; i < gridSize; i++)
        {
            qrCodeMap[i] = new int[zerosRow.Length];
        }

        // **位置検出パターン生成を簡略化**
        // 左上のパターン (7x7)
        ApplyDetectionPattern(0, 0);
        // 右上のパターン (7x7)
        ApplyDetectionPattern(0, gridSize - 7);
        // 左下のパターン (7x7)
        ApplyDetectionPattern(gridSize - 7, 0);
    }

    private void ApplyDetectionPattern(int startRow, int startCol)
    {
        // 7x7の領域を-1で埋める
        for (int i = 0; i < 7; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                qrCodeMap[startRow + i][startCol + j] = -1;
            }
        }

        // 5x5の内部を-2に
        for (int i = 1; i < 6; i++)
        {
            for (int j = 1; j < 6; j++)
            {
                qrCodeMap[startRow + i][startCol + j] = -2;
            }
        }

        // 3x3の中央を-1に戻す
        for (int i = 2; i < 5; i++)
        {
            for (int j = 2; j < 5; j++)
            {
                qrCodeMap[startRow + i][startCol + j] = -1;
            }
        }
    }

    public override string ExecuteMain()
    {
        /*
         * メインの処理:
         * 前のプレイヤーからデータを取得し、位置検出パターンを生成する
         */

        if (qRCodeMapInitializerPlayer == null || rinaNumpy == null)
        {
            Debug.LogError("QRCodeMapInitializerPlayer or RinaNumpy is not assigned.");
            return "Error";
        }

        // 前のプレイヤーからデータを取得
        gridSize = qRCodeMapInitializerPlayer.gridSize;

        // 位置検出パターンを生成
        FillPositionDetectionPatterns();

        Debug.Log($"{ReturnMyName()} executed. QR Code position detection pattern applied.");

        // 次のプレイヤーに自分を渡す
        qRCodeMapInitializerPlayer.qRCodePositionDetectionPlayer = this;

        return "Completed";
    }
}

