using UdonSharp;
using UnityEngine;

public class InitFromQrcodePlayer : SuperPlayer
{
    private int data;
    private string mode;

    private void Start()
    {
        // プレイヤーの名前を初期化
        this.myName = null;
        this.data = 0;
        this.mode = string.Empty;
    }

    public override string ReturnMyName()
    {
        return "InitFromQrcodePlayer";
    }

    public override string ExecuteMain()
    {
        Debug.Log("\n==== InitFromQrcodePlayer ExecuteMain ==============================");

        // QRコードにしたいデータの設定
        this.data = 12345;
        this.mode = "numeric";

        // デバッグ出力でデータを表示
        Debug.Log($"Data: {data}");
        Debug.Log($"Mode: {mode}");

        // 実行結果をワールドのインスタンスに反映
        if (world != null)
        {
            world.initFromQrcodePlayer = this;
        }
        else
        {
            Debug.LogError("world が null です。");
        }

        Debug.Log("\n==== InitFromQrcodePlayer ExecuteMain (END) ==============================\n");

        return "Completed";
    }
}