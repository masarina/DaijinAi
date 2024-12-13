// 逆伝播時、純伝播時にパラメータを抽出した側のLayerには、
// doutを"加算"してください。
// これは、2023年論文により
// 加算が良いとされているためです。

using UdonSharp;
using UnityEngine;

public class SkipAddLayer : UdonSharpBehaviour
{
    // SkipAddLayerは、2つの入力配列を受け取って、それらを要素ごとに加算するシンプルなレイヤです。
    public float[] Forward(float[] x)
    {
        return x; // 先のLayerで参照して、自身でaddさせる。
    }

    // Backwardメソッドでは、加算レイヤなので、受け取った勾配をそのまま前の層に伝えます。
    public float[] Backward(float[] dout, float[] dout2)
    {
        rinaNumpy.Add_FloatArray_FloatArray(dout, dout2)

        return new float[][] { dout, dout };
    }
}
