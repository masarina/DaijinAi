using UdonSharp;
using UnityEngine;

public class SkipAddLayer : UdonSharpBehaviour
{
    // SkipAddLayerは、2つの入力配列を受け取って、それらを要素ごとに加算するシンプルなレイヤです。
    public float[] Forward(float[] x1, float[] x2)
    {
        if (x1.Length != x2.Length) throw new System.ArgumentException("Input arrays must be of equal length.");

        float[] outArray = new float[x1.Length];
        for (int i = 0; i < x1.Length; i++)
        {
            outArray[i] = x1[i] + x2[i];
        }
        return outArray;
    }

    // Backwardメソッドでは、加算レイヤなので、受け取った勾配をそのまま前の層に伝えます。
    public float[][] Backward(float[] dout)
    {
        // doutは外部から受け取った勾配
        // SkipAddLayerは加算を行うだけなので、勾配をそのまま前の層に伝える
        return new float[][] { dout, dout };
    }
}
