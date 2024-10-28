using UdonSharp;
using UnityEngine;

public class QRCodeModePlayer : SuperPlayer
{
    private string modeIndicator = null;  // モード指示子を保持する変数

    private void Start()
    {
        // プレイヤーの名前を初期化
        this.myName = null;
    }

    public override string ReturnMyName()
    {
        return "QRCodeModePlayer";
    }

    public void SetMode(string modeType)
    {
        /*
         * モードタイプを受け取って、それに応じたモード指示子を設定する。
         * modeType: "numeric", "alphanumeric", "byte", "kanji"
         */
        switch (modeType)
        {
            case "numeric":
                modeIndicator = "0001";
                break;
            case "alphanumeric":
                modeIndicator = "0010";
                break;
            case "byte":
                modeIndicator = "0100";
                break;
            case "kanji":
                modeIndicator = "1000";
                break;
            default:
                Debug.LogError("Invalid modeType. Choose from: numeric, alphanumeric, byte, kanji.");
                break;
        }
    }

    public override string ExecuteMain()
    {
        Debug.Log("\n==== QRCodeModePlayer ExecuteMain ==============================");

        // モードが設定されているか確認
        if (modeIndicator == null)
        {
            Debug.LogError("Mode indicator is not set. Please call SetMode before executing ExecuteMain.");
            return "Failed";
        }

        // QRCodeModePlayerのインスタンスをworldに登録
        world.qRCodeModePlayer = this;

        Debug.Log($"Mode Indicator: {modeIndicator}");
        Debug.Log("\n==== QRCodeModePlayer ExecuteMain (END) ==============================\n");

        return "Completed";
    }
}
