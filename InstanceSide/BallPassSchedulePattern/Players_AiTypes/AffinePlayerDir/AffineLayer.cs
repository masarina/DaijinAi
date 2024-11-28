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
        yArray = rNp.Add_FloatArray_FloatArray(
            rNp.DotProduct_FloatArray2D_FloatArray(weights, xArray),
            bias
        );

        // 出力を返す
        return yArray;
    }

    public float[] Backward(float[] dout)
    {
        // 重みの勾配dWを計算
        float[][] dW = new float[weights.Length][];
        for (int i = 0; i < weights.Length; i++)
        {
            // RinaNumpyを活用して、dout[i]とxArrayを掛け算
            dW[i] = rNp.Multiply_FloatArray_Float(xArray, dout[i]);
        }

        // バイアスの勾配dbを計算
        float[] db = rNp.Copy_FloatArray(dout); // doutをそのままコピー

        // 入力に対する誤差dxを計算
        float[] dx = rNp.DotProduct_FloatArray2D_FloatArray(
            rNp.TransposeMatrix(weights),
            dout
        );

        // 必要であれば、ここでdWとdbを別の処理に渡す
        // 例: 学習用のOptimizerに渡して更新する

        // 計算されたdxを返す
        return dx;
    }
}
