using UdonSharp;
using UnityEngine;

public class TrapezoidCorrectionPlayer : SuperPlayer
{
    public int[][] binaryMatrix2DList; // QRコードの台形2次元リスト
    public Texture2D inputTexture; // アタッチされた画像データ
    public int[][] correctedMatrix2D; // 補正後のマトリックス
    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // プレイヤーを初期化
    }

    public void ResetPlayer()
    {
        myName = "TrapezoidCorrectionPlayer"; // プレイヤー名を設定
        binaryMatrix2DList = new int[0][]; // 初期化
        correctedMatrix2D = new int[0][]; // 初期化
    }

    public override string ReturnMyName()
    {
        return "TrapezoidCorrectionPlayer";
    }

    private int[] FindLeftRightEdges(int[] row)
    {
        int[] result = new int[2];
        result[0] = -1; // 左端
        result[1] = -1; // 右端

        // 左端のビット1を探す
        for (int i = 0; i < row.Length; i++)
        {
            if (row[i] == 1)
            {
                result[0] = i;
                break;
            }
        }

        // 右端のビット1を探す
        for (int i = row.Length - 1; i >= 0; i--)
        {
            if (row[i] == 1)
            {
                result[1] = i;
                break;
            }
        }

        // ビットが見つからない場合のデフォルト値
        if (result[0] == -1 || result[1] == -1)
        {
            result[0] = 0;
            result[1] = row.Length - 1;
        }

        return result;
    }

    private int[] FindTopBottomEdges(int[][] matrix)
    {
        int topEdge = -1;
        int bottomEdge = -1;

        // 上端のビット1を探す
        for (int i = 0; i < matrix.Length; i++)
        {
            if (rinaNumpy.Sum_FloatArray2d_Float_axis0(rinaNumpy.IntArrayToFloatArray(matrix[i])) > 0)
            {
                topEdge = i;
                break;
            }
        }

        // 下端のビット1を探す
        for (int i = matrix.Length - 1; i >= 0; i--)
        {
            if (rinaNumpy.Sum_FloatArray2d_Float_axis0(rinaNumpy.IntArrayToFloatArray(matrix[i])) > 0)
            {
                bottomEdge = i;
                break;
            }
        }

        // エッジが見つからなかった場合
        if (topEdge == -1 || bottomEdge == -1)
        {
            topEdge = 0;
            bottomEdge = matrix.Length - 1;
        }

        return new int[] { topEdge, bottomEdge };
    }

    private int[][] ResizeMatrixTo25x25(int[][] matrix)
    {
        return rinaNumpy.Resize_Matrix_25_25(matrix); // RinaNumpyのメソッドを利用してリサイズ
    }

    public override string ExecuteMain()
    {
        // テクスチャが正しくアタッチされているか確認
        if (inputTexture == null)
        {
            Debug.LogError("Input texture is not assigned.");
            return "Error";
        }

        // 台形行列の補正処理
        int[][] tempMatrix = rinaNumpy.Correct_Trapezoid_Matrix(binaryMatrix2DList); // RinaNumpyの補正メソッドを使用
        correctedMatrix2D = ResizeMatrixTo25x25(tempMatrix); // リサイズもRinaNumpyを使用

        Debug.Log("Trapezoid correction completed with RinaNumpy.");
        return "Completed";
    }
}
