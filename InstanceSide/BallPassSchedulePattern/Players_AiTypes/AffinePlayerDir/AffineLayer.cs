using UdonSharp;
using UnityEngine;

public class AffineLayer : UdonSharpBehaviour
{
    // RinaNumpyのアタッチ
    public RinaNumpy rNp;

    // クラス内で保持する変数
    private float[][] weights; // 重み
    private float[] bias; // バイアス
    private float[] xArray; // 入力
    private float[] yArray; // 出力

    // 初期化メソッド
    public void Initialize(float[][] initialWeights, float[] initialBias)
    {
        // 重みとバイアスを初期化
        weights = initialWeights;
        bias = initialBias;
    }

    public float[] Forward(float[] input)
    {
        // 入力を保持
        xArray = input;

        // Affine変換: Wx + b をRinaNumpyを使って計算
        float[] Wx = rNp.DotProduct_FloatArray2D_FloatArray(weights, xArray);
        yArray = rNp.Add_FloatArray_FloatArray(Wx, bias);

        // 出力を返す
        return yArray;
    }

    public float[] Backward(float[] dout)
    {
        // 重みの勾配dWを計算
        float[][] dW = new float[weights.Length][];
        for (int i = 0; i < weights.Length; i++)
        {
            dW[i] = new float[weights[0].Length];
            for (int j = 0; j < weights[0].Length; j++)
            {
                dW[i][j] = dout[i] * xArray[j];
            }
        }

        // バイアスの勾配dbを計算
        float[] db = new float[dout.Length];
        for (int i = 0; i < dout.Length; i++)
        {
            db[i] = dout[i]; // バイアスの勾配は出力の誤差そのもの
        }

        // 入力に対する誤差dxを計算
        float[] dx = rNp.DotProduct_FloatArray2D_FloatArray(TransposeMatrix(weights), dout);

        // 必要であれば、ここでdWとdbを別の処理に渡す
        // 例: 学習用のOptimizerに渡して更新する

        // 計算されたdxを返す
        return dx;
    }

    // 行列を転置するメソッド
    private float[][] TransposeMatrix(float[][] matrix)
    {
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        float[][] transposed = new float[cols][];
        for (int i = 0; i < cols; i++)
        {
            transposed[i] = new float[rows];
            for (int j = 0; j < rows; j++)
            {
                transposed[i][j] = matrix[j][i];
            }
        }

        return transposed;
    }
}
