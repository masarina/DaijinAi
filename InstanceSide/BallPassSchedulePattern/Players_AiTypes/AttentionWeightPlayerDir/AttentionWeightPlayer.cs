using UdonSharp;
using UnityEngine;

public class AttentionWeightPlayer : SuperPlayer
{
    public string myName;
    
    public AttentionWeightPlayer attentionWeightPlayer;
    public InitAiTypesPlayer initAiTypesPlayer;

    public NormalizationPlayer3 normalizationPlayer3;
    public NormalizationPlayer4 normalizationPlayer4;
    public AiFlagsPlayer aiFlagsPlayer;
    public float[] x;
    public float[] y;
    public float[] dx;
    public float[] dout;

    public float[][] hs; // RinaNumpy使って、Resetメソッド内で初期化するのがいいかも。
    public int MyPositionNum; // メイン処理(？未定)でのforループで取得可能になるはず。
    public int MyLayerNum; // 自身がEmbeddingから数えて何番目のLayerなのか。

    
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
        hs = 
        float[] a = attentionWeightLayer.Forward(x, );
        
        return a;
    }

    public float[] Backward(float[] da)
    {
        float[] dout = attentionWeightLayer.Backward(da)

        return dout;
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        if (aiFlagsPlayer.TravelMode == "Forward")
        {
            // 1つ前のyをxとする。
            this.x = normalizationPlayer3.y;

            // Forward
            this.y = this.Forward(this.x);
        }
        else if (aiFlagsPlayer.TravelMode == "Backward")
        {
            // ひとつ先のdxをdoutとする。
            this.dout = normalizationPlayer4.dx;

            // Backward
            this.dx = this.Backward(this.dout);
        }

        return "Completed";
    }
}
