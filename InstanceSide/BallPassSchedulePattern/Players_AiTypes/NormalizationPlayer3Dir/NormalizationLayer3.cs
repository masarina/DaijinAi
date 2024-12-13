using UdonSharp;
using UnityEngine;

public class NormalizationLayer3 : UdonSharpBehaviour
{
    public RinaNumpy rNp; // InspectorからRinaNumpyオブジェクトをアサイン

    // クラス内で保持する変数
    private float[] xCache; // 入力値のキャッシュ
    private float[] xNormalizedCache; // 正規化後の入力のキャッシュ
    private float meanCache; // 平均のキャッシュ
    private float stdCache; // 標準偏差のキャッシュ
    public float[] dx; // 入力に対する勾配
    public float dgamma; // gammaに対する勾配
    public float dbeta; // betaに対する勾配

    // 新しくクラス変数として定義
    private float[] gamma; // スケールパラメータ
    private float[] beta; // シフトパラメータ

    public float[] Forward(float[] x, float epsilon = 1e-5f)
    {
        // 入力xをキャッシュ
        xCache = x;

        // 入力xの平均を計算してキャッシュ
        meanCache = rNp.Mean_FloatArray(x);

        // 入力xの標準偏差を計算してキャッシュ
        stdCache = rNp.Std_FloatArray(x) + epsilon;

        // 入力xを正規化してキャッシュ
        xNormalizedCache = rNp.Divide_FloatArray_Float(
            rNp.Subtract_FloatArray_Float(x, meanCache), stdCache
        );

        // 正規化されたデータに対してgammaとbetaを適用
        float[] outData = rNp.Add_FloatArray_FloatArray(
            rNp.Multiply_FloatArray_FloatArray(xNormalizedCache, gamma),
            beta
        );

        // 出力を返す
        return outData;
    }

    public float[] Backward(float[] dout, float epsilon = 1e-5f)
    {
        // dbetaの計算と保持
        dbeta = rNp.Sum_FloatArray(dout);

        // dgammaの計算と保持
        dgamma = rNp.Sum_FloatArray(
            rNp.Multiply_FloatArray_FloatArray(dout, xNormalizedCache)
        );

        // dx_normalizedの計算
        float[] dxNormalized = rNp.Multiply_FloatArray_FloatArray(dout, gamma);

        // x - meanの計算
        float[] xMinusMean = rNp.Subtract_FloatArray_Float(xCache, meanCache);

        // 標準偏差の逆数
        float stdInv = 1f / stdCache;

        // dx_normalizedによる標準偏差の勾配
        float dstdInv = rNp.DotProduct_FloatArray_FloatArray(dxNormalized, xMinusMean);
        float dstd = -dstdInv / (stdCache * stdCache);

        // 分散の勾配
        float dvar = 0.5f * dstd;

        // 分散によるxの勾配
        float[] dxVarComponent = rNp.Multiply_FloatArray_Float(
            rNp.Multiply_FloatArray_Float(xMinusMean, 2f),
            dvar / xCache.Length
        );

        // 平均の勾配
        float dmean = -rNp.Sum_FloatArray(dxNormalized) * stdInv
                      + rNp.Sum_FloatArray(dxVarComponent) / xCache.Length;

        // dxの計算
        float[] dx1 = rNp.Multiply_FloatArray_Float(dxNormalized, stdInv);
        float[] dx2 = rNp.Multiply_FloatArray_Float(
            rNp.OnesLike_FloatArray(xCache),
            dmean / xCache.Length
        );
        dx = rNp.Add_FloatArray_FloatArray(dx1, dx2);

        // dxを返す
        return dx;
    }
}
