using UdonSharp;
using UnityEngine;

public class ChangeAiModePlayer : SuperPlayer
{
    public string myName;
    public InitAiTypesPlayer initAiTypesPlayer;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool ChangeAiModePlayerReset()
    {
        myName = "ChangeAiModePlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "ChangeAiModePlayer";
    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        return "Completed";
    }
}
