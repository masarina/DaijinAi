// 実行する度に、モードが切り替わります。

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
        if (initAiTypesPlayer.AiMode == "Train")
        {
            initAiTypesPlayer.AiMode = "Predict"
        }

        else
        {
            initAiTypesPlayer.AiMode = "Train"
        }
        
        return "Completed";
    }
}
