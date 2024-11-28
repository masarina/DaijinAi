using UdonSharp;
using UnityEngine;

public class SoftmaxWithLoss : UdonSharpBehaviour
{
    public SoftmaxLayer softmaxLayer; // SoftmaxLayerオブジェクトへの参照

    private float loss; // 損失
    private float[] y; // softmaxの出力
    private float[] t; // 教師データ(one-hot vector)
    private object softmaxParams; // SoftmaxLayerから受け取るパラメータ

    public float Forward(float[] x, float[] t)
    {
        this.t = t;

        // SoftmaxLayerのForwardメソッドを呼び出し、結果を取得
        y = softmaxLayer.Forward(x);

        // SoftmaxLayerから現在のパラメータを取得
        softmaxParams = softmaxLayer.GetParams();

        // 損失を計算
        loss = CrossEntropyError(y, t);

        return loss;
    }

    public float[] Backward(float dout = 1.0f)
    {
        // SoftmaxLayerに取得したパラメータを適用
        softmaxLayer.SetParams(softmaxParams);

        int batch_size = 1; // バッチ処理なし
        float[] dx = new float[y.Length];

        // 逆伝播の計算
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
