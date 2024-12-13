using UdonSharp;
using UnityEngine;

public class InitAiTypesPlayer : SuperPlayer
{
    public string myName;
    public AiSettingsPlayer aiSettingsPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool InitAiTypesPlayerReset()
    {
        myName = "InitAiTypesPlayer";
        aiSettingsPlayer.AiMode = "None"; // TrainかPredictか。
        aiSettingsPlayer.TravelMode = "None"; // ForwardかBackwardか。
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "InitAiTypesPlayer";
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        return "Completed";
    }
}
