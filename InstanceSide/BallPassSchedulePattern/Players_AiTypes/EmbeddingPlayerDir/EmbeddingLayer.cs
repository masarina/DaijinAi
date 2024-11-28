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
        // 入力トークンIDに対応する単語表現ベクトルを取得
        if (weights == null || tokenId < 0 || tokenId >= weights.Length)
        {
            Debug.LogError("EmbeddingLayer: Invalid tokenId or weights not initialized.");
            return null;
        }
        return weights[tokenId];
    }

    public void Backward(int tokenId, float[] gradient)
    {
        // 勾配を保持する
        if (weights == null || tokenId < 0 || tokenId >= weights.Length)
        {
            Debug.LogError("EmbeddingLayer: Invalid tokenId or weights not initialized for Backward.");
            return;
        }

        if (gradient == null || gradient.Length != weights[tokenId].Length)
        {
            Debug.LogError("EmbeddingLayer: Gradient size mismatch.");
            return;
        }

        // 勾配を蓄積
        for (int i = 0; i < gradients[tokenId].Length; i++)
        {
            gradients[tokenId][i] += gradient[i];
        }
    }

    public float[][] GetGradients()
    {
        // 勾配を取得（他のプロセスで更新するため）
        return gradients;
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
