using UdonSharp;
using UnityEngine;

public class SwishLayer : UdonSharpBehaviour
{
    public RinaNumpy rinaNumpy; // RinaNumpyをアタッチ
    public float beta = 1.0f; // 学習可能なパラメータとしてbetaを初期化
    private float[] outArray; // forward時の出力を保持する配列
    private float[] xArray; // forward時の入力を保持する配列
    public float dbeta; // betaに関する勾配を保持する変数

    public float[] Forward(float[] x)
    {
        xArray = x; // 入力配列を保持
        float[] betaX = rinaNumpy.Multiply_FloatArray_Float(x, beta); // beta * xを計算
        float[] sigmoidBetaX = rinaNumpy.Divide_FloatArray_Float(
            rinaNumpy.OnesLike_FloatArray(betaX),
            rinaNumpy.Add_FloatArray_Float(rinaNumpy.Exp_FloatArray(rinaNumpy.Negative_FloatArray(betaX)), 1.0f)
        ); // Sigmoid(beta * x)を計算
        outArray = rinaNumpy.Multiply_FloatArray_FloatArray(x, sigmoidBetaX); // Swish(x) = x * sigmoid(beta * x)

        return outArray; // 出力を返す
    }

    public float[] Backward(float[] dout)
    {
        // 勾配配列の初期化
        float[] dx = new float[dout.Length]; // 入力に関する勾配
        dbeta = 0.0f; // betaに関する勾配をリセット

        // 各入力について計算
        for (int i = 0; i < dout.Length; i++)
        {
            float x = xArray[i];
            float e_beta_x = Mathf.Exp(-beta * x); // e^(-beta * x)
            float sigma = 1.0f / (1.0f + e_beta_x); // Sigmoid(beta * x)

            // Swish関数の導関数
            float sigma_prime = sigma + beta * x * e_beta_x / (1.0f + e_beta_x) 
                                - beta * x * x * e_beta_x / Mathf.Pow(1.0f + e_beta_x, 2);

            // dx: 出力に関する勾配(dout)とSwish導関数の積
            dx[i] = dout[i] * sigma_prime;

            // betaに関する勾配
            float f_x = x * sigma; // Swish(x)
            float df_dbeta = x * e_beta_x * (1 - sigma) / Mathf.Pow(1.0f + e_beta_x, 2);
            dbeta += dout[i] * f_x * df_dbeta;
        }

        // dbetaを平均化
        dbeta /= dout.Length;

        // dxを返す
        return dx;
    }
}
