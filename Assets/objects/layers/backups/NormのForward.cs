using UdonSharp;
using UnityEngine;

public class LayerNormalizationSingle : UdonSharpBehaviour
{
    public RinaNumpy rNp; // InspectorからRinaNumpyオブジェクトをアサイン

    public float[] LayerNormalizationForward(float[] x, float[] gamma, float[] beta, float epsilon = 1e-5f)
    {
        // 入力xの平均を計算します (入力:(D, ), 出力:スカラー)
        float mean = rNp.Mean_FloatArray(x);
        
        // 入力xの分散を計算します (入力:(D, ), 出力:スカラー)
        float var = rNp.Var_FloatArray(x, mean);
        
        // 入力xの標準偏差を計算します (入力:(D, ), 出力:スカラー)
        float std = Mathf.Sqrt(var + epsilon);
        
        // 入力xを正規化します (入力:(D, ), 出力:(D, )の形状を持つベクトル)
        float[] x_normalized = rNp.Divide_FloatArray_Float(rNp.Subtract_FloatArray_Float(x, mean), std);
        
        // 正規化されたデータに対してgammaとbetaを適用します (入力:(D, ), 出力:(D, )の形状を持つベクトル)
        float[] out = rNp.Add_FloatArray_FloatArray(rNp.Multiply_FloatArray_FloatArray(x_normalized, gamma), beta);
        
        // 出力と、backward passで使用するために値を保存 (キャッシュはUnityのGameObjectなどを使って外部に保存するか、必要に応じて設計する)
        // この例では、キャッシュをどう扱うかは示されていません。実際のアプリケーションに応じて、必要な情報を保存しましょう。

        // コメントアウトでキャッシュの内容を示す
        /*
        cache = {
            'x_normalized': x_normalized,
            'gamma': gamma,
            'x': x,
            'mean': mean,
            'std': std
        };
        */

        return out; // 出力データを返します
    }

    void Start()
    {
    }
}
