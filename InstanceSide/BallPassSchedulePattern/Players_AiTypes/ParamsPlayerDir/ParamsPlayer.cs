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

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {


        return "Completed";
    }
}
