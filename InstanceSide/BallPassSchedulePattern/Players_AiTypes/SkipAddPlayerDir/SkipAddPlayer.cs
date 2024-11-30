using UdonSharp;
using UnityEngine;

public class SkipAddPlayer : SuperPlayer
{
    public string myName;
    public SkipAddLayer skipAddLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool SkipAddPlayerReset()
    {
        myName = "SkipAddPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "SkipAddPlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = SkipAddPlayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = SkipAddPlayer.Backward(dx)

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
