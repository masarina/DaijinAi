using UdonSharp;
using UnityEngine;

public class ReplacePatternPlayer : SuperPlayer
{
    public string PngFilePath; // 写真のパス
    public int[,] BinaryMatrix2DArray; // 置き換え前のQRコード部分(25x25の2次元配列)
    public int[,] ReplacedMatrix; // 置き換え後のQRコードマトリックス(25x25の2次元配列)

    public PatternDetectionPlayer PatternDetectionPlayer; // Unityエディタでアタッチ
    public FormatInfoCatcherPlayer FormatInfoCatcherPlayer; // Unityエディタでアタッチ
    public RinaNumpy rinaNumpy; // RinaNumpyをUnityエディタでアタッチ

    public override string ReturnMyName()
    {
        return "ReplacePatternPlayer";
    }

    private int[,] ReplacePatterns(int[,] matrix)
    {
        // matrixの大きさチェック
        if (matrix.GetLength(0) != 25 || matrix.GetLength(1) != 25)
        {
            Debug.LogError("Matrix must be 25x25.");
            return new int[0, 0];
        }

        // 入力マトリックスをコピー
        int[,] result = new int[25, 25];
        rinaNumpy.CopyIntArray(matrix, result, 25 * 25); // RinaNumpyで配列をコピー

        // 位置検出パターン
        for (int i = 0; i < 7; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                result[i, j] = -11; // 左上
                result[i, 25 - 7 + j] = -11; // 右上
                result[25 - 7 + i, j] = -11; // 左下
            }
        }

        // タイミングパターン
        for (int i = 8; i < 17; i++)
        {
            result[6, i] = -11; // 横方向
            result[i, 6] = -11; // 縦方向
        }

        // ダークモジュール
        result[8, 13] = -11;

        return result;
    }

    public override string ExecuteMain()
    {
        // PatternDetectionPlayerのデータを取得
        if (PatternDetectionPlayer != null)
        {
            PngFilePath = PatternDetectionPlayer.PngFilePath;
            BinaryMatrix2DArray = PatternDetectionPlayer.BinaryMatrix2DArray;
        }
        else
        {
            Debug.LogError("PatternDetectionPlayer is not attached.");
            return "Error";
        }

        // FormatInfoCatcherPlayerのデータを取得
        int[,] matrix = null;
        if (FormatInfoCatcherPlayer != null)
        {
            matrix = FormatInfoCatcherPlayer.Matrix;
        }
        else
        {
            Debug.LogError("FormatInfoCatcherPlayer is not attached.");
            return "Error";
        }

        // QRコードのパターンを置き換える
        ReplacedMatrix = ReplacePatterns(matrix);

        // 自身を更新
        PatternDetectionPlayer.ReplacePatternPlayer = this;

        return "Completed";
    }
}
