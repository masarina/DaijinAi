using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class EmbeddingLayer : UdonSharpBehaviour
{
    public DataHolder dataHolder; // DataHolderオブジェクトへの参照

    public void Start()
    {
        // DataHolderから重みデータ(ベクトル)を読み込む処理が必要かもしれない。
        // 例えば、dataHolder.ReadFloatArray2D()を使って重みを取得するなど。
    }

    public float[] Forward(int tokenId)
    {
        // DataHolderから対応するベクトルを取得
        float[][] weights = dataHolder.ReadFloatArray2D();
        if (weights == null || tokenId < 0 || tokenId >= weights.Length)
        {
            Debug.LogError("EmbeddingLayer: Invalid tokenId or weights not initialized.");
            return null;
        }
        return weights[tokenId];
    }
}
