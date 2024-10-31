using UdonSharp;
using UnityEngine;

public class InitFromQrcodePlayer : SuperPlayer
{
    private int data;
    private string mode;

    // 初期化メソッド
    public bool InitFromQrcodePlayerReset()
    {
        myName = "InitFromQrcodePlayer";
        data = 12345;
        mode = "numeric";

        return true;
    }

    public override string ReturnMyName()
    {
        return "InitFromQrcodePlayer";
    }

    public override string ExecuteMain()
    {
        Debug.Log($"{ReturnMyName()}が実行されました。");

        return "Completed";
    }
}
