using UdonSharp;
using UnityEngine;

public class LiON : UdonSharpBehaviour
{
    // パラメータ（クラス変数として設定）
    public float alpha = 0.01f; // 初期学習率
    public float beta = 0.9f;   // モーメント項の減衰率
    public float threshold = 1.0f; // スケールダウンのしきい値
    public float scalingFactor = 0.9f; // スケールダウン係数
    public float minLearningRate = 0.001f; // 最小学習率
    public float maxLearningRate = 0.05f; // 最大学習率
    public float scaleFactor = 0.1f; // 学習率の調整係数
    public float scaleBoostBeta = 0.05f; // スケールダウン時の学習率増加係数
    public float dropoutRate = 0.2f; // ドロップアウト率

    // 内部状態（クラス変数として設定）
    private float[] v; // モーメントベクトル
    private float[] layerLearningRates; // 各レイヤの学習率

    // 初期化メソッド
    public void Initialize(int parameterSize)
    {
        v = new float[parameterSize];
        layerLearningRates = new float[parameterSize];

        // モーメントと学習率を初期化
        for (int i = 0; i < parameterSize; i++)
        {
            v[i] = 0.0f;
            layerLearningRates[i] = alpha; 
        }
    }

    // ドロップアウトマスク生成
    private bool[] GenerateDropoutMask(int size)
    {
        bool[] mask = new bool[size];
        for (int i = 0; i < size; i++)
        {
            mask[i] = Random.value >= dropoutRate;
        }
        return mask;
    }

    // 更新メソッド
    public float[] UpdateWeights(float[] w, float[] dw)
    {
        if (v == null || v.Length != w.Length)
        {
            Debug.LogError("LiON not initialized or parameter size mismatch.");
            return w;
        }

        // ドロップアウトマスク生成
        bool[] dropoutMask = GenerateDropoutMask(w.Length);

        // 重み更新処理
        for (int i = 0; i < w.Length; i++)
        {
            if (!dropoutMask[i]) continue;

            // 1. モーメント更新
            v[i] = UpdateMomentum(v[i], dw[i]);

            // 2. スケールダウン（必要に応じて学習率調整）
            if (Mathf.Abs(v[i]) > threshold)
            {
                v[i] *= scalingFactor;
                layerLearningRates[i] += scaleBoostBeta;
            }

            // 3. 学習率調整
            layerLearningRates[i] = AdjustLearningRate(layerLearningRates[i], dw[i]);

            // 4. 重みの更新
            w[i] -= layerLearningRates[i] * Mathf.Sign(v[i]);

            // 5. 重みスケールダウン
            if (Mathf.Abs(w[i]) > threshold)
            {
                w[i] *= scalingFactor;
                layerLearningRates[i] += scaleBoostBeta;
            }
        }

        return w;
    }

    // モーメント更新ロジック
    private float UpdateMomentum(float currentMomentum, float gradient)
    {
        return beta * currentMomentum + (1 - beta) * gradient;
    }

    // 学習率調整ロジック
    private float AdjustLearningRate(float currentRate, float gradient)
    {
        // 変化量に基づき学習率を調整
        float adjustedRate = currentRate + scaleFactor * Mathf.Abs(gradient);

        // 制約範囲にクリップ
        return Mathf.Clamp(adjustedRate, minLearningRate, maxLearningRate);
    }
}


