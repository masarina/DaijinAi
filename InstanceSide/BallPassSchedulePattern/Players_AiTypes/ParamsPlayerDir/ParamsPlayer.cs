FANZusing UdonSharp;
using UnityEngine;

public class ParamsPlayer : SuperPlayer
{
    public float[][] AllParams;

    public RinaNumpy rinaNumpy;
    public string myName;
    public AiSettingsPlayer aiSettingsPlayer;
    public int XSize;
    public int NumberOfAllLayers; // 全てのレイヤーの数


    // 初期化メソッド (Pythonの__init__に相当)
    public bool ParamsPlayerReset()
    {
        myName = "ParamsPlayer";
        
        XSize = aiSettingsPlayer.XSize
        
        
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "ParamsPlayer";
    }

    public int[] ResultIndexOfParamsSave(
                                int x, 
                                int[] LayerIndex // EmbeddingLayerから数えて自分が何層目のLayerなのか。
                )
    // 引数：処理中のposition数
    // 戻値：このポジションが保存すべきParamsのIndexs
    {
        // 結果を格納する配列を初期化
        int[] y = new int[3];
        bs = { 0 + LayerIndex, 
                1 + LayerIndex, 
                2 + LayerIndex
            };

        // 傾きは、
        // (1Layerに3つ(今回)の空パラメータ付与) * (Embedding以降の全Layerの数)
        int[] a = aiSettingsPlayer.LayerParamsSize * aiSettingsPlayer.LayerSize

        for (int bi = 0; bi < bs.Length;bi++)
        {
            y = rinaNumpy.Append_FloatArray(y, a * x + bs[bi]);
        }

        return y;
    }
    

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {


        return "Completed";
    }
}
