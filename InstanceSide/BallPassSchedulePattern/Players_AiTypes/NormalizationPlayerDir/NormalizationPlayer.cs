using UdonSharp;
using UnityEngine;

public class NormalizationPlayer : SuperPlayer
{
    public string myName;
    public NormalizationLayer normalizationLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool normalizationLayerReset()
    {
        myName = "normalizationLayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "normalizationLayer";
    }

    public float[] Forward(float[] x)
    {
        float[] y = normalizationLayer.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dx)
    {
        float[] dout = normalizationLayer.Backward(dx)

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
