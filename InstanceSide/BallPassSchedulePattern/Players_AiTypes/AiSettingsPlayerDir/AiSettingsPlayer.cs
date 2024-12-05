using UdonSharp;
using UnityEngine;

public class AiSettingsPlayer : SuperPlayer
{
    public string myName;
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AiSettingsPlayerReset()
    {
        myName = "AiSettingsPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "AiSettingsPlayer";
    }

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // ForwardPlayerでライブラリ的に使用するので
        // 実装今のところ不要
        return "Completed";
    }
}

