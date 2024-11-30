using UdonSharp;
using UnityEngine;

public class InitAiTypesPlayer : SuperPlayer
{
    public string AiMode;
    public string myName;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool InitAiTypesPlayerReset()
    {
        myName = "InitAiTypesPlayer";
        AiMode = "None"
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
