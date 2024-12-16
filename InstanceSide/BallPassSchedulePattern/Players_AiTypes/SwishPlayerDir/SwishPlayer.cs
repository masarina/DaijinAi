using UdonSharp;
using UnityEngine;

public class SwishPlayer : SuperPlayer
{
    public string myName;
    public SwishLayer swishLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    public AiFlagsPlayer aiFlagsPlayer;
    public NormalizationPlayer2 normalizationPlayer2;
    public NormalizationPlayer3 normalizationPlayer3;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool SwishPlayerReset()
    {
        myName = "SwishPlayer";
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

    public float[] Backward(float[] dout)
    {
        float[] dx = swishLayer.Backward(dout)

        return dx;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        if (this.aiFlagsPlayer == "Forward")
        {
            // 一つ前のレイヤのyをxとする。
            this.x = normalizationPlayer2.y
            
            this.y = this.Forward(this.x)
        }
        else if (this.aiFlagsPlayer == "Backward")
        {
            // ひとつ先のプレイヤーからdxをとってくる
            this.dout = normalizationPlayer3.dx
            
            // Backward
            this.dx = this.Backward(dout)
        }
        
        return "Completed";
    }
}
