using UdonSharp;
using UnityEngine;

public class WeightSumPlayer : SuperPlayer
{
    public string myName;
    public WeightSumLayer weightSumLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool WeightSumPlayerReset()
    {
        myName = "WeightSumPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "WeightSumPlayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = weightSumLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = weightSumLayer.Backward(dx)

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
