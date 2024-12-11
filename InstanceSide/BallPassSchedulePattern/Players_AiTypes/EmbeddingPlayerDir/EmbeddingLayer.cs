using UdonSharp;
using UnityEngine;


public class EmbeddingLayer : UdonSharpBehaviour
{
    // クラス内で保持する変数
    public RinaNumpy rinaNumpy;

    private float[][] weights; // 単語表現ベクトル（埋め込み行列）
    private float[][] gradients; // 勾配を保持する配列
    private int currentTokenId; // Forwardで保持する現在のトークンID
    private float[] currentDx; // Backwardで保持する現在のトークンのdx


    public float[] Forward(int tokenId, float[][] W)
    {
        // 重みのアタッチ
        weights = W

        // 入力トークンIDを保持
        currentTokenId = tokenId;

        return weights[tokenId];
    }

    public float[] Backward(float[] gradient, int TokenId, float[][] dW)
    {
        // パラメータの参照
        gradients　= dW

        // 勾配を蓄積
        for (int i = 0; i < gradients[TokenId].Length; i++)
        {
            gradients[TokenId][i] += gradient[i];
        }

        // dxを保持
        currentDx = gradient;

        // dxを返す
        return currentDx;
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
