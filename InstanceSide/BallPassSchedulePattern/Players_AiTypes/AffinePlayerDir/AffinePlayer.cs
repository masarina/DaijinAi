using UdonSharp;
using UnityEngine;

public class AffinePlayer : SuperPlayer
{
    public string myName;
    public AffineLayer affineLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AffinePlayerReset()
    {
        myName = "AffinePlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "AffinePlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = affineLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = affineLayer.Backward(dx)

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
