using UdonSharp;
using UnityEngine;

public class SkipAddPlayer : SuperPlayer
{
    public string myName;
    
    public AiSettingsPlayer aiSettingsPlayer;
    public SkipAddLayer skipAddLayer;
    public AiFlagsPlayer aiFlagsPlayer;
    public NormalizationPlayer normalizationPlayer;
    public AffinPlayer affinePlayer;
    public AffinPlayer2 affinePlayer2;
    
    public float[] x;
    public float[] y;
    public float[] y2;
    public float[] dout;
    public float[] dout2;
    public float[] dx;
    
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
        this.y, this.y2 = SkipAddPlayer.Forward(x);
        
        return this.y, this.y2;
    }

    public float[] Backward(float[] dout)
    {
        this.dx = SkipAddPlayer.Backward(dout, dout2)

        return this.dout;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        if (aiFlagsPlayer.TravelMode == "Forward")
        {
            // Forward
            this.y, this.y2 = this.Forward(
                normalizationPlayer.y
                )
        }
        else if (aiFlagsPlayer.TravelMode == "Backward");
        {
            // Backward
            this.dx this.Backward(
                affinePlayer.dx,
                affinePlayer2.dx
                );
        }
        
        return "Completed";
    }
}
