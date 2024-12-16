using UdonSharp;
using UnityEngine;

public class ParamsPlayer : SuperPlayer
{
    public float[][] AllParams;

    public RinaNumpy rinaNumpy;
    public string myName;
    public AiSettingsPlayer aiSettingsPlayer;
    int XSize;
    int NumberOfAllLayers; // 全てのレイヤーの数
    int LayersSettingsParamsSize; // 重み、バイアス、ベータ値であれば、3とかかな。


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

    public int[] ResultIndexOfParamsSave(int x)
    // 引数：処理中のposition数
    // 戻値：このポジションが保存すべきParamsのIndexs
    {
        // 結果を格納する配列を初期化
        int[] y = new int[3];
        int[] b = { 0, 1, 2 };

        // bの各要素に3 * xを加算してyに格納
        for (int i = 0; i < b.Length; i++)
        {
            y[i] = b[i] + 3 * x;
        }

        return y;
    }

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {


        return "Completed";
    }
}
