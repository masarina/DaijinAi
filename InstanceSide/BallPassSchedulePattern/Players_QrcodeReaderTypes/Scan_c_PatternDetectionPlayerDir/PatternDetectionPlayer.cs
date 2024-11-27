using UdonSharp;
using UnityEngine;

public class PatternDetectionPlayer : SuperPlayer
{
    // Unityエディタでアタッチするオブジェクト
    public GameObject textureSource; // 画像を持つオブジェクト（マテリアルからテクスチャを取得）
    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    public string pngFilePath; // 写真のパス
    public int[][] binaryMatrix2DList; // バイナリマトリックス (25x25)
    public bool patternsDetected; // パターン検出結果

    public override string ReturnMyName()
    {
        return "PatternDetectionPlayer";
    }

    public override string ExecuteMain()
    {
        // 入力データの取得
        Texture2D texture = GetTextureFromGameObject(textureSource);

        if (texture == null)
        {
            Debug.LogError("Texture could not be retrieved from the provided GameObject.");
            return "Error";
        }

        // マトリックスデータの仮の取得（具体的には外部プロセスで生成される想定）
        binaryMatrix2DList = GetBinaryMatrixFromTexture(texture);

        if (binaryMatrix2DList == null || binaryMatrix2DList.Length != 25 || binaryMatrix2DList[0].Length != 25)
        {
            Debug.LogError("Binary matrix is invalid or not properly formatted.");
            return "Error";
        }

        // パターン検出処理
        bool positionDetected = DetectPositionPatterns(binaryMatrix2DList);
        bool timingDetected = DetectTimingPatterns(binaryMatrix2DList);
        bool darkModuleDetected = DetectDarkModule(binaryMatrix2DList);

        // 結果の確認
        patternsDetected = positionDetected && timingDetected && darkModuleDetected;

        if (patternsDetected)
        {
            Debug.Log("All patterns successfully detected.");
        }
        else
        {
            if (!positionDetected)
                Debug.LogError("Failed to detect position patterns.");
            if (!timingDetected)
                Debug.LogError("Failed to detect timing patterns.");
            if (!darkModuleDetected)
                Debug.LogError("Failed to detect dark module.");
        }

        return "Completed";
    }

    private Texture2D GetTextureFromGameObject(GameObject obj)
    {
        if (obj == null)
            return null;

        Renderer renderer = obj.GetComponent<Renderer>();
        if (renderer != null && renderer.material != null)
        {
            return renderer.material.mainTexture as Texture2D;
        }
        return null;
    }

    private int[][] GetBinaryMatrixFromTexture(Texture2D texture)
    {
        // 仮の実装: テクスチャを解析してバイナリマトリックスを生成する
        int size = 25; // 固定サイズ
        int[][] matrix = new int[size][];
        for (int i = 0; i < size; i++)
        {
            matrix[i] = new int[size];
            for (int j = 0; j < size; j++)
            {
                // テクスチャのピクセルから値を取得する処理（適宜調整）
                Color pixelColor = texture.GetPixel(i, j);
                matrix[i][j] = pixelColor.grayscale > 0.5f ? 1 : 0; // 仮の閾値
            }
        }
        return matrix;
    }

    private bool DetectPositionPatterns(int[][] matrix)
    {
        // 位置検出パターンの座標
        int[][] positions = {
            new int[] {0, 0}, // 左上
            new int[] {0, matrix.Length - 7}, // 右上
            new int[] {matrix.Length - 7, 0} // 左下
        };

        foreach (int[] position in positions)
        {
            if (!CheckPositionDetectionPattern(matrix, position[0], position[1]))
            {
                return false;
            }
        }
        return true;
    }

    private bool CheckPositionDetectionPattern(int[][] matrix, int rowStart, int colStart)
    {
        int patternSize = 7;
        int[][] expectedPattern = {
            new int[] {1, 1, 1, 1, 1, 1, 1},
            new int[] {1, 0, 0, 0, 0, 0, 1},
            new int[] {1, 0, 1, 1, 1, 0, 1},
            new int[] {1, 0, 1, 1, 1, 0, 1},
            new int[] {1, 0, 1, 1, 1, 0, 1},
            new int[] {1, 0, 0, 0, 0, 0, 1},
            new int[] {1, 1, 1, 1, 1, 1, 1}
        };

        for (int i = 0; i < patternSize; i++)
        {
            // RinaNumpyを使って簡略化
            if (!rinaNumpy.CompareIntArrays(matrix[rowStart + i], expectedPattern[i], patternSize))
            {
                return false;
            }
        }
        return true;
    }

    private bool DetectTimingPatterns(int[][] matrix)
    {
        int size = matrix.Length;

        // 行方向のタイミングパターン
        for (int col = 8; col < size - 8; col++)
        {
            int expectedBit = col % 2;
            if (matrix[6][col] != expectedBit)
            {
                return false;
            }
        }

        // 列方向のタイミングパターン
        for (int row = 8; row < size - 8; row++)
        {
            int expectedBit = row % 2;
            if (matrix[row][6] != expectedBit)
            {
                return false;
            }
        }

        return true;
    }

    private bool DetectDarkModule(int[][] matrix)
    {
        // ダークモジュールの位置は (8, 13)
        return matrix[8][13] == 1;
    }
}
