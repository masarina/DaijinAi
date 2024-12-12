// 今学習しているポジションの場所等を
// 保持する必要がある。
// そのような保持が必要なものを
// ここに定義することにした。

// EmbeddingLayerのみ、パラメータは自分で持たせてOK.
// Forward,Backwardの入力は、ベクトルを想定します。


using UdonSharp;
using UnityEngine;

public class AiFlagsPlayer : SuperPlayer
{
    public string myName;

    public int NowPositionIndex;

    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AiFlagsPlayerReset()
    {
        NowPositionIndex = 0;

        myName = "EmbeddingPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "AiFlagsPlayer";
    }

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        
        
        return "Completed";
    }
    
    
}