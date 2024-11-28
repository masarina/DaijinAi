using UdonSharp;
using UnityEngine;

public class SoftmaxLayer : UdonSharpBehaviour
{
    public RinaNumpy rinaNumpy; // 最新のRinaNumpyをアタッチ

    private float[] cacheExpX; // Softmax計算の中間値 (指数の値)
    private float cacheSum; // 指数の合計
    private float[] lastOutput; // Softmaxの出力 (Forwardの結果をキャッシュ)

    public float[] Forward(float[] x)
    {
        // 最大値を取得してオーバーフローを防ぐ
        float max = rinaNumpy.Max_FloatArray(x); // 最大値をRinaNumpyで取得

        // Softmax計算
        cacheExpX = new float[x.Length];
        cacheSum = 0.0f;

        for (int i = 0; i < x.Length; i++)
        {
            cacheExpX[i] = Mathf.Exp(x[i] - max); // オーバーフロー対策
        }

        cacheSum = rinaNumpy.Sum_FloatArray(cacheExpX); // 合計値をRinaNumpyで計算

        float[] y = new float[x.Length];
        for (int i = 0; i < x.Length; i++)
        {
            y[i] = cacheExpX[i] / cacheSum;
        }

        // 結果をキャッシュ
        lastOutput = y;

        return y;
    }

    public float[] Backward(float[] dout)
    {
        // doutの合計を計算
        float doutSum = rinaNumpy.Sum_FloatArray(dout);

        // 入力に対する勾配を計算
        float[] dx = new float[dout.Length];
        for (int i = 0; i < dout.Length; i++)
        {
            dx[i] = cacheExpX[i] * (dout[i] - doutSum / cacheSum);
        }

        return dx;
    }

    public object GetParams()
    {
        // キャッシュされたSoftmaxの出力を返す
        return lastOutput;
    }

    public void SetParams(object parameters)
    {
        // キャッシュにパラメータを設定
        lastOutput = (float[])parameters;
    }
}
