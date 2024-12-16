using UdonSharp;
using UnityEngine;

public class NormalizationPlayer3 : SuperPlayer
{
    public string myName;
    
    public NormalizationLayer3 normalizationLayer3;
    public AttentionWeightPlayer attentionWeightPlayer;
    public SwishPlayer swishPlayer;
    public AiFlagsPlayer aiFlagsPlayer;
    public AiSettingsPlayer aiSettingsPlayer;
    public RinaNumpy rinaNumpy;
    
    public float[] x; // 順入力
    public float[] y; // 順出力
    public float[] dout; // 逆入力
    public float[] dx; // 逆出力

    
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool normalizationLayer3Reset()
    {
        myName = "NormalizationLayer3";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "NormalizationLayer3";
    }

    public float[] Forward(float[] x)
    {

        y = normalizationLayer3.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dout)
    {
        float[] dx = normalizationLayer3.Backward(dx)

        return dx;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {

        if (aiFlagsPlayer.TravelMode == "Forward")
        {
            // 1つ前のレイヤのyをxとする。
            this.x = swishPlayer.y
        
            // Forward処理
            this.y = normalizationLayer3.Forward(this.x)
        }
        else if (aiFlagsPlayer.TravelMode == "Backward")
        {
            // ひとつ先のLayerのdxをdoutとする。
            this.dout = attentionWeightPlayer.dx
        
            // backward
            this.dx = normalizationLayer3.Backward(this.dout)

        }
        

        return "Completed";
    }
}
