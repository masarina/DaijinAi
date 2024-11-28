using UdonSharp;
using UnityEngine;

public class EmbeddingLayer : UdonSharpBehaviour
{
    // クラス内で保持する変数
    private float[][] weights; // 単語表現ベクトル（埋め込み行列）
    private float[][] gradients; // 勾配を保持する配列

    // 初期化メソッド
    public void Initialize(float[][] initialWeights)
    {
        // 単語表現ベクトルを初期化
        weights = initialWeights;

        // 勾配の初期化（weightsと同じサイズ）
        gradients = new float[weights.Length][];
        for (int i = 0; i < weights.Length; i++)
        {
            gradients[i] = new float[weights[i].Length];
        }
    }

    public float[] Forward(int tokenId)
    {
        // トークンIDに対応する単語表現ベクトルを取得
        if (weights == null || tokenId < 0 || tokenId >= weights.Length)
        {
            Debug.LogError("EmbeddingLayer: Invalid tokenId or weights not initialized.");
            return null;
        }
        return weights[tokenId];
    }

    public float[] Backward(int tokenId, float[] gradient)
    {
        // 勾配を保持する
        if (weights == null || tokenId < 0 || tokenId >= weights.Length)
        {
            Debug.LogError("EmbeddingLayer: Invalid tokenId or weights not initialized for Backward.");
            return null;
        }

        if (gradient == null || gradient.Length != weights[tokenId].Length)
        {
            Debug.LogError("EmbeddingLayer: Gradient size mismatch.");
            return null;
        }

        // 勾配を蓄積
        for (int i = 0; i < gradients[tokenId].Length; i++)
        {
            gradients[tokenId][i] += gradient[i];
        }

        // 勾配をそのまま返す（次のレイヤー用）
        return gradient;
    }

    public void Update(System.Action<float[][], float[][], float> updateFunc, float learningRate)
    {
        // Update関数を実行
        updateFunc(weights, gradients, learningRate);
    }

    public void ClearGradients()
    {
        // 勾配をクリア（次の更新に備える）
        for (int i = 0; i < gradients.Length; i++)
        {
            for (int j = 0; j < gradients[i].Length; j++)
            {
                gradients[i][j] = 0f;
            }
        }
    }
}
