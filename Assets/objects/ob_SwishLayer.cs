using UdonSharp;
using UnityEngine;

public class SwishLayerTrainableBeta : UdonSharpBehaviour
{
    public float beta = 1.0f; // 学習可能なパラメータとしてbetaを初期化します。これはSwish関数の形状を調整する役割があります。
    private float[] outArray; // forward時の出力を保持する配列です。
    private float[] xArray; // forward時の入力を保持する配列です。

    public float[] Forward(float[] x)
    {
        xArray = x; // 入力配列を保持します。
        outArray = new float[x.Length]; // 入力と同じ長さの配列を出力用に準備します。
        for (int i = 0; i < x.Length; i++)
        {
            // Swish関数を適用します。Swish(x) = x * sigmoid(beta * x)です。
            outArray[i] = x[i] * (1.0f / (1.0f + Mathf.Exp(-beta * x[i])));
        }
        return outArray;
    }

    public (float[], float) Backward(float[] dout)
    {
        float[] dx = new float[dout.Length]; // 入力に関する勾配を保持する配列です。
        float dbeta = 0.0f; // betaパラメータに関する勾配を保持します。
        for (int i = 0; i < dout.Length; i++)
        {
            // e^(-beta*x)を計算します。これはSwish関数の導関数の計算に使用されます。
            float e_beta_x = Mathf.Exp(-beta * xArray[i]);
            // Swish関数のsigmoid部分を計算します。
            float sigma = 1.0f / (1.0f + e_beta_x);
            // Swish関数の導関数を計算します。
            float sigma_prime = sigma + (beta * xArray[i] * e_beta_x) / (1.0f + e_beta_x) - (beta * xArray[i] * xArray[i] * e_beta_x) / Mathf.Pow((1.0f + e_beta_x), 2);
    
            // xに関する勾配を計算します。これは、出力に関する勾配(dout)とSwish関数の導関数(sigma_prime)の積です。
            dx[i] = dout[i] * sigma_prime;
    
            // betaに関する勾配を計算します。これは、Swish関数のxとbetaに依存する部分を含む導関数から計算されます。
            // f(x) * sigmaはSwish関数の出力です。df/dbetaはbetaに対するSwish関数の出力の変化率です。
            float f_x = xArray[i] * sigma;
            float df_dbeta = xArray[i] * e_beta_x * (1 - sigma) / Mathf.Pow(1 + e_beta_x, 2);
            dbeta += dout[i] * f_x * df_dbeta;
        }
    
        // dbetaをdoutの長さで割って平均を取ります。これは、全ての入力データにわたるbetaの勾配の平均を求めるためです。
        dbeta /= dout.Length;
    
        return (dx, dbeta);
    }
}
