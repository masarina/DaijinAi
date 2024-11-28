using UdonSharp;
using UnityEngine;

public class AttentionWeight : UdonSharpBehaviour
{
    public SoftmaxLayer softmaxLayer; // SoftmaxLayerをインスペクタからアタッチ
    public RinaNumpy rNp; // RinaNumpyをインスペクタからアタッチ

    private float[][] hs; // 入力の過去状態
    private float[] h;    // 現在の入力状態
    private float[][] cacheHs; // 過去状態のキャッシュ
    private float[] cacheHr;   // 現在状態のキャッシュ
    private float[] softmaxParams; // Softmaxのパラメータ

    public float[] Forward(float[][] hsInput, float[] hInput)
    {
        // 入力データを保持
        hs = hsInput;
        h = hInput;

        // ベクトルの長さを取得
        int T = hs.Length;   // 過去状態の数
        int H = hs[0].Length; // 特徴量の次元

        // 現在の状態をコピー
        float[] hr = rNp.Copy_FloatArray(h);

        // 過去状態との類似度を計算（スコア）
        float[] s = new float[T];
        for (int i = 0; i < T; i++)
        {
            s[i] = rNp.DotProduct_FloatArray_FloatArray(hs[i], hr);
        }

        // スコアをSoftmaxで正規化
        float[] a = softmaxLayer.Forward(s);

        // Softmaxのパラメータを取得して保持
        softmaxParams = softmaxLayer.GetParams();

        // キャッシュに保存
        cacheHs = hs;
        cacheHr = hr;

        // 重み（アテンション）を返す
        return a;
    }

    public float[][] Backward(float[] da)
    {
        // キャッシュから長さを取得
        int T = cacheHs.Length;   // 過去状態の数
        int H = cacheHs[0].Length; // 特徴量の次元

        // SoftmaxLayerにパラメータを再設定
        softmaxLayer.SetParams(softmaxParams);

        // Softmaxの逆伝播
        float[] ds = softmaxLayer.Backward(da);

        // 勾配を初期化
        float[][] dhs = new float[T][];
        float[] dh = rNp.ZerosLike_FloatArray(cacheHr);

        // 勾配を計算
        for (int i = 0; i < T; i++)
        {
            dhs[i] = rNp.Multiply_FloatArray_Float(cacheHr, ds[i]); // dhs[i] = ds[i] * cacheHr
            dh = rNp.Add_FloatArray_FloatArray(dh, rNp.Multiply_FloatArray_Float(cacheHs[i], ds[i])); // dh += ds[i] * cacheHs[i]
        }

        // 過去状態と現在状態の勾配を返す
        return new float[][] { rNp.FlattenFloatArray2D(dhs), dh };
    }
}
