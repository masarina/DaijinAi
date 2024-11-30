using UdonSharp;
using UnityEngine;

public class SoftmaxPlayer : SuperPlayer
{
    public string myName;
    public SoftmaxLayer softmaxLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool SoftmaxPlayerReset()
    {
        myName = "SoftmaxPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "SoftmaxPlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = softmaxLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = softmaxLayer.Backward(dx)

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
