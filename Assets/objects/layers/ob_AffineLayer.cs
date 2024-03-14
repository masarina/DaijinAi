using UdonSharp;
using UnityEngine;

public class AffineLayer : UdonSharpBehaviour
{
    // RinaNumpyのアタッチ。
    public RinaNumpy rNp;
    
    // DataHolderオブジェクトを用意
    public DataHolder weightsHolder; // 重みを保持するDataHolder
    public DataHolder biasHolder; // バイアスを保持するDataHolder
    public DataHolder xHolder; // 入力を保持するDataHolder
    public DataHolder yHolder; // 出力を保持するDataHolder

    // プライベート変数の定義と、代入させるパラメータ設定。
    private float[] outArray; // 出力を保持する配列
    private float[] xArray; // 入力を保持する配列
    xArray = xHolder.ReadFloatArray(); // サンプルデータの読み込み。
    
    public float[] Forward()
    {
        // DataHolderから重みとバイアスを取得
        float[][] W = this.weightsHolder.ReadFloatArray2D();
        float[] b = this.biasHolder.ReadFloatArray();
    
        // Affine変換: Wx + b をRinaNumpyを使って計算
        float[] Wx = rNp.DotProduct_FloatArray2D_FloatArray(W, x);
        outArray = rNp.Add_FloatArray_FloatArray(Wx, b);
    
        this.yHolder.WriteFloatArray(outArray) // 計算された出力をyに書き込む
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
