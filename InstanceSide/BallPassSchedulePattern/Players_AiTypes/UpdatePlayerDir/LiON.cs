using UdonSharp;
using UnityEngine;

public class LiON : UdonSharpBehaviour
{
    // デフォルトパラメータ（クラス変数として設定）
    public float alpha = 0.01f; // 学習率
    public float beta = 0.9f;   // モーメント項の減衰率

    // モーメントベクトル
    private float[] v;

    // 初期化メソッド
    public void Initialize(int parameterSize)
    {
        v = new float[parameterSize]; // パラメータサイズに応じてモーメントを初期化
        for (int i = 0; i < parameterSize; i++)
        {
            v[i] = 0.0f;
        }
    }

    // 更新式: w = 更新式(w, dw)
    public float[] UpdateWeights(float[] w, float[] dw)
    {
        if (v == null || v.Length != w.Length)
        {
            Debug.LogError("LiONUpdater not initialized or parameter size mismatch.");
            return w; // 初期化されていない場合は、入力の重みをそのまま返す
        }

        // 勾配のモーメントを計算
        for (int i = 0; i < w.Length; i++)
        {
            v[i] = beta * v[i] + (1 - beta) * dw[i]; // モーメント更新
        }

        // 重みを更新
        for (int i = 0; i < w.Length; i++)
        {
            w[i] -= alpha * Mathf.Sign(v[i]); // 符号に基づいて学習率を適用
        }

        return w;
    }
}
