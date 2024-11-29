using UdonSharp;
using UnityEngine;

public class AttentionWeightPlayer : SuperPlayer
{
    public AttentionWeightPlayer attentionWeightPlayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AttentionWeightPlayerReset()
    {
        myName = "AttentionWeightPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "AttentionWeightPlayer";
    }

    public float[] Forward(float[] x)
    {
        a = attentionWeightLayer.Forward(x);
        
        return a;
    }

    public float[] Backward(float[] da)
    {
        dout = attentionWeightLayer.Backward(da)

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
