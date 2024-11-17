using UdonSharp;
using UnityEngine;

public class QRCodeModePlayer : SuperPlayer
{
    public SuperPlayer initFromQrcodePlayer; // アタッチ
    public string ModeStr;
    public string ModeBitStr; // モード指示子を保持する変数

    public bool QRCodeModePlayerReset()
    {
        myName = "QRCodeModePlayer";
        modeIndicator = null; // 初期化時にモード指示子をnullに設定

        return true;
    }

    public override string ReturnMyName()
    {
        return "QRCodeModePlayer";
    }

    public void SetMode(string modeType)
    {
        /*
         * モードタイプを受け取って、それに応じたモード指示子を設定する
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
        /*
         * メインの処理: QRコードのモード指示子を設定して、次のプロセスに渡す準備をする
         */

        // モード設定を行う
        this.ModeStr = initFromQrcodePlayer.mode;
        this.ModeBitStr = this.Setmode(this.ModeStr);

        return "Completed";
    }
}
