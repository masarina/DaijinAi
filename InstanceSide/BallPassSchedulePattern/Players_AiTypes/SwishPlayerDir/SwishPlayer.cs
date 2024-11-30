using UdonSharp;
using UnityEngine;

public class SwishPlayer : SuperPlayer
{
    public string myName;
    public SwishLayer swishLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool SwishPlayerReset()
    {
        myName = "Swishplayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "SwishPlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = swishLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = swishLayer.Backward(dx)

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
