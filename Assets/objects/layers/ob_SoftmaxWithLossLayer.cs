using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class SoftmaxWithLoss : UdonSharpBehaviour
{
    public SoftmaxLayer softmaxLayer; // SoftmaxLayerオブジェクトへの参照

    private float loss; // 損失
    private float[] y; // softmaxの出力
    private float[] t; // 教師データ(one-hot vector)

    public float Forward(float[] x, float[] t)
    {
        this.t = t;
        y = softmaxLayer.Forward(x); // SoftmaxLayerのForwardメソッドを使用
        loss = CrossEntropyError(y, t);
        return loss;
    }

    public float[] Backward(float dout = 1.0f)
    {
        int batch_size = 1; // バッチ処理なし
        float[] dx = new float[y.Length];

        for (int i = 0; i < dx.Length; i++)
        {
            dx[i] = (y[i] - t[i]) * dout / batch_size;
        }

        return dx;
    }

    private float CrossEntropyError(float[] y, float[] t)
    {
        float epsilon = 1e-7f;
        float sum = 0.0f;

        for (int i = 0; i < y.Length; i++)
        {
            sum += t[i] * Mathf.Log(y[i] + epsilon);
        }

        return -sum;
    }
}
