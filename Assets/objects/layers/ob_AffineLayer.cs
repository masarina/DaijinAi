using UdonSharp;
using UnityEngine;

public class AffineLayer : UdonSharpBehaviour
{
    public DataHolder weightsHolder; // 重みを保持するDataHolder
    public DataHolder biasHolder; // バイアスを保持するDataHolder
    private float[] outArray; // 出力を保持する配列
    private float[] xArray; // 入力を保持する配列
    
    public float[] Forward(float[] x)
    {
        // DataHolderから重みとバイアスを取得
        float[][] W = weightsHolder.ReadFloatArray2D();
        float[] b = biasHolder.ReadFloatArray();
    
        xArray = x; // 入力配列を保持
    
        // Affine変換: Wx + b をRinaNumpyを使って計算
        float[] Wx = RinaNumpy.DotProduct_FloatArray2D_FloatArray(W, x);
        outArray = RinaNumpy.Add_FloatArray_FloatArray(Wx, b);
    
        return outArray; // 計算された出力を返す
    }
    
    public void Backward(float[] dout)
    {
        // DataHolderから重みを取得
        float[][] W = weightsHolder.ReadFloatArray2D();
    
        // 重みの勾配dWを計算
        float[][] dW = new float[W.Length][];
        for (int i = 0; i < W.Length; i++)
        {
            dW[i] = new float[W[0].Length];
            for (int j = 0; j < W[0].Length; j++)
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
        float[] dx = RinaNumpy.DotProduct_FloatArray2D_FloatArray(W, dout);
    }
}
