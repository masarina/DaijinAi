using UdonSharp;
using UnityEngine;

public class LayerNormalizationSingle : UdonSharpBehaviour
{
    public RinaNumpy rNp; // InspectorからRinaNumpyオブジェクトをアサイン

    public float[] Backward(float[] dout, float[] x_normalized, float[] gamma, float[] x, float mean, float std)
    {
        float epsilon = 1e-6f;
        
        // dbetaの勾配計算
        float dbeta = rNp.Sum_FloatArray(dout);
        
        // dgammaの勾配計算
        float[] dout_x_normalized = rNp.Multiply_FloatArray_FloatArray(dout, x_normalized);
        float dgamma = rNp.Sum_FloatArray(dout_x_normalized);
        
        // dx_normalizedに関する勾配計算
        float[] dx_normalized = rNp.Multiply_FloatArray_FloatArray(dout, gamma);

        // x - mean
        float[] x_minus_mean = rNp.Subtract_FloatArray_Float(x, mean);

        // 標準偏差の逆数
        float std_inv = 1f / (std + epsilon);

        // dx_normalizedによる分母の逆数の勾配
        float dstd_inv = rNp.Sum_FloatArray(rNp.Multiply_FloatArray_FloatArray(dx_normalized, x_minus_mean));

        // 分母の勾配
        float dstd = -dstd_inv / (std * std + epsilon);
        
        // 分散(var)の逆数
        float var_inv = 1f / (std * std + epsilon);

        // 分散の勾配
        float dvar = 0.5f * dstd * var_inv;

        // x_minus_meanの2倍
        float[] x_minus_mean_doubled = rNp.Multiply_FloatArray_Float(x_minus_mean, 2f);

        // 分散による平均の勾配
        float dmean_var_component = dvar * rNp.Sum_FloatArray(x_minus_mean_doubled) / x.Length;

        // 平均の勾配
        float dmean = -rNp.Sum_FloatArray(dx_normalized) * std_inv + dmean_var_component;

        // xに関する勾配
        float[] dx1 = rNp.Multiply_FloatArray_Float(dx_normalized, std_inv);
        float[] dx2 = rNp.OnesLike_FloatArray(x); // 全ての要素が1の配列を作成
        dx2 = rNp.Multiply_FloatArray_Float(dx2, dmean_var_component / x.Length);
        float[] dx3 = rNp.OnesLike_FloatArray(x); // 全ての要素が1の配列を作成
        dx3 = rNp.Multiply_FloatArray_Float(dx3, dmean / x.Length);

        // 最終的なdx
        float[] dx = rNp.Add_FloatArray_FloatArray(dx1, dx2);
        dx = rNp.Add_FloatArray_FloatArray(dx, dx3);

        // 出力と、キャッシュについては、最後にまとめてコメントアウトで
        // dx: 入力層への勾配
        // dgamma: gammaパラメータへの勾配
        // dbeta: betaパラメータへの勾配

        return dx; // この例ではdxのみを返す。dgammaとdbetaも必要に応じて返すように調整すること。
    }
}
