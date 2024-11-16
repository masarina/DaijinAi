using UdonSharp;
using UnityEngine;

public class QRCodeAlignmentPatternPlayer : SuperPlayer
{
    // Unityエディタでアタッチ
    public QRCodeTimingPatternPlayer timingPatternPlayer;
    public RinaNumpy rinaNumpy; // RinaNumpyのインスタンスをアタッチ
    public int gridSize; // グリッドサイズ
    public int version; // バージョン
    public int[,] qrCodeMap; // QRコードのグリッドマップ

    public override string ReturnMyName()
    {
        return "QRCodeAlignmentPatternPlayer";
    }

    public bool QRCodeAlignmentPatternPlayerReset()
    {
        return true;
    }

    public int[,] FillAlignmentPattern(int[,] grid)
    {
        /*
         * アライメントパターンをQRコードに配置する関数（バージョン2用）
         * RinaNumpyを活用して計算や操作を効率化
         */
        int alignmentX = 20; // アライメントパターンの位置X
        int alignmentY = 20; // アライメントパターンの位置Y

        // グリッドに適用するためにローカル変数を初期化
        int[,] result = new int[grid.GetLength(0), grid.GetLength(1)];
        for (int i = 0; i < grid.GetLength(0); i++)
        {
            for (int j = 0; j < grid.GetLength(1); j++)
            {
                result[i, j] = grid[i, j];
            }
        }

        // 5x5のエリアを塗りつぶす
        for (int i = alignmentX - 2; i <= alignmentX + 2; i++)
        {
            for (int j = alignmentY - 2; j <= alignmentY + 2; j++)
            {
                result[i, j] = -1;
            }
        }

        // 中央部分をRinaNumpyで0に戻す
        float[] zeroArray = rinaNumpy.ZerosLike_FloatArray(new float[3]); // 長さ3の0配列
        for (int i = alignmentX - 1; i <= alignmentX + 1; i++)
        {
            for (int j = alignmentY - 1; j <= alignmentY + 1; j++)
            {
                result[i, j] = (int)zeroArray[j - (alignmentY - 1)];
            }
        }

        // 最後に中央を1x1で-1に塗りつぶす
        result[alignmentX, alignmentY] = -1;

        return result;
    }

    public override string ExecuteMain()
    {
        /*
         * このメソッドはUnityエディタで設定された他のプレイヤーや
         * グリッドマップの情報を利用して、アライメントパターンを適用する。
         */

        // 入力の取得
        gridSize = timingPatternPlayer.gridSize;
        version = timingPatternPlayer.version;
        qrCodeMap = timingPatternPlayer.qrCodeMap;

        // アライメントパターンの適用
        qrCodeMap = FillAlignmentPattern(qrCodeMap);

        Debug.Log($"{ReturnMyName()}が実行されました。");

        // 自身を更新（Unityエディタで設定される必要がある）
        timingPatternPlayer.qrCodeMap = qrCodeMap;

        return "Completed";
    }
}

