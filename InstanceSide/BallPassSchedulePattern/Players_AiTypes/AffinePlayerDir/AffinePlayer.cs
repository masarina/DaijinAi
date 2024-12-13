using UdonSharp;
using UnityEngine;

public class AffinePlayer : SuperPlayer
{
    public string myName;
    
    public AffineLayer affineLayer;
    public InitAiTypesPlayer initAiTypesPlayer;
    public AiFlagsPlayer aiFlagsPlayer;
    public SkipAddPlayer skipAddPlayer;
    
    public float[] x;
    public float[] y;
    public float[] dout;
    public float[] dx;
    
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

    public float[] Backward(float[] dout)
    {
        float[] dx = affineLayer.Backward(dout)

        return dx;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        if (aiFlagsPlayer.TravelMode == "Forward")
        {
            this.y = this.Forward(
                skipAddPlayer.y
            );
            
        }
        else if
        {
            this.dc = this.Backward(
                normalizationPlayer2.dx
            );
        }

        return "Completed";
    }
}
