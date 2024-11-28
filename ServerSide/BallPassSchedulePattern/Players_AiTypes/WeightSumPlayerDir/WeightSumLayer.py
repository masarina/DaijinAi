using UdonSharp;
using UnityEngine;

public class WeightSum : UdonSharpBehaviour
{
    // RinaNumpyをアタッチ
    public RinaNumpy rNp;

    // クラス内で保持する変数
    private float[][] cacheHs; // hsのキャッシュ
    private float[] cacheA; // aのキャッシュ

    public float[] Forward(float[][] hsInput, float[] aInput)
    {
        cacheHs = hsInput; // 入力をキャッシュ
        cacheA = aInput;

        // hsをaで加重平均する: 各行 hs[i] に a[i] を掛ける
        float[][] weightedHs = new float[hsInput.Length][];
        for (int i = 0; i < hsInput.Length; i++)
        {
            weightedHs[i] = rNp.Multiply_FloatArray_Float(hsInput[i], aInput[i]);
        }

        // 各列を合計して結果を返す
        return rNp.Sum_FloatArray2d_Float_axis0(weightedHs);
    }

    public float[][] Backward(float[] dc)
    {
        int T = cacheHs.Length;
        int H = cacheHs[0].Length;

        // dhsの計算: 各列に cacheA[i] を掛ける
        float[][] dhs = new float[T][];
        for (int i = 0; i < T; i++)
        {
            dhs[i] = rNp.Multiply_FloatArray_Float(dc, cacheA[i]);
        }

        // daの計算: 各行 hs[i] と dc のドット積
        float[] da = new float[T];
        for (int i = 0; i < T; i++)
        {
            da[i] = rNp.DotProduct_FloatArray_FloatArray(dc, cacheHs[i]);
        }

        return new float[][] { rNp.FlattenMatrix(dhs), da };
    }
}
