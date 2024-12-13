using UdonSharp;
using UnityEngine;

public class NormalizationPlayer2 : SuperPlayer
{
    public string myName;
    
    public NormalizationLayer2 normalizationLayer2;
    public SkipAddPlayer skipAddPlayer;
    public AiFlagsPlayer aiFlagsPlayer;
   
    public AiSettingsPlayer aiSettingsPlayer;
    public RinaNumpy rinaNumpy;
    
    public float[] x; // 順入力
    public float[] y; // 順出力
    public float[] dout; // 逆入力
    public float[] dx; // 逆出力

    
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool normalizationLayer2Reset()
    {
        myName = "NormalizationLayer2";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "NormalizationLayer2";
    }

    public float[] Forward(float[] x)
    {
        y = normalizationLayer2.Forward(x);
        
        return y;
    }

    public float[] Backward(float[] dout)
    {
        float[] dx = normalizationLayer2.Backward(dx)

        return dx;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {

        if (aiFlagsPlayer. TravelMode == "Forward")
        {
            // 1つ前のレイヤから、xを取ってくる
            this.x = embeddingPlayer.SampleVecVer[aiFlagsPlayer.NowPositionIndex]
        
            // Forward処理
            this.y = normalizationLayer2.Forward(this.x)
        }
        else if (aiFlagsPlayer.TravelMode == "Backward")
        {
            // ひとつ先のLayerから、doutを取ってくる
            this.dout = skipAddPlayer.dx
        
            // backward
            this.dx = normalizationLayer2.Backward(this.dout)
            
            // このポジション終了したので+=1
            aiFlagsPlayer.NowPositionIndex += 1;
        }
        

        return "Completed";
    }
}
