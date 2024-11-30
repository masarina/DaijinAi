using UdonSharp;
using UnityEngine;

public class EmbeddingPlayer : SuperPlayer
{
    public EmbeddingPlayer embeddingPlayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    public string myName;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool EmbeddingPlayerReset()
    {
        myName = "EmbeddingPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "EmbeddingPlayer";
    }

    public float[] Forward(float[] id)
    {
        float[] vocab_vec = embeddingPlayer.Forward(id);
        
        return vocab_vec;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = embeddingPlayer.Backward(dx)

        return dout;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // ForwardPlayerでライブラリ的に使用するので
        // 実装今のところ不要
        return "Completed";
    }
}
