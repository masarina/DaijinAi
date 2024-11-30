using UdonSharp;
using UnityEngine;

public class SoftmaxWithLossPlayer : SuperPlayer
{
    public string myName;
    public SoftmaxWithLossLayer softmaxWithLossLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool SoftmaxWithLossPlayerReset()
    {
        myName = "SoftmaxWithLossPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "SoftmaxWithLossPlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = softmaxWithLossLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = softmaxWithLossLayer.Backward(dx)

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
