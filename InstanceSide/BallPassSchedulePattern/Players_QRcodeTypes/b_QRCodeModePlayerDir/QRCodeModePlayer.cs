using UdonSharp;
using UnityEngine;

public class QRCodeModePlayer : SuperPlayer
{
    private string modeIndicator;

    // 初期化メソッド
    public bool QRCodeModePlayerReset()
    {
        myName = "QRCodeModePlayer";
        modeIndicator = null;  // モード指示子を初期化
        return true;
    }

    public override string ReturnMyName()
    {
        return "QRCodeModePlayer";
    }

    public void SetMode(string modeType)
    {
        /*
         * モードタイプを受け取って、それに応じたモード指示子を設定する。
         * modeType: "numeric", "alphanumeric", "byte", "kanji"
         */
        if (modeType == "numeric")
        {
            modeIndicator = "0001";
        }
        else if (modeType == "alphanumeric")
        {
            modeIndicator = "0010";
        }
        else if (modeType == "byte")
        {
            modeIndicator = "0100";
        }
        else if (modeType == "kanji")
        {
            modeIndicator = "1000";
        }
        else
        {
            Debug.LogError("Invalid modeType. Choose from: numeric, alphanumeric, byte, kanji.");
        }
    }

    public override string ExecuteMain()
    {
        // 初期化された `modeIndicator` をチェックし、セットされていなければエラーを出力
        if (string.IsNullOrEmpty(modeIndicator))
        {
            Debug.LogError("Mode indicator is not set. Please call SetMode before executing main.");
            return "Error";
        }

        Debug.Log($"{ReturnMyName()}が実行されました。モード指示子: {modeIndicator}");

        return "Completed";
    }
}