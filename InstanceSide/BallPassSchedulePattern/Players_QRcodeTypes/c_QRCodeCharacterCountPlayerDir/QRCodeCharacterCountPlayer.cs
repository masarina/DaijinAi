using UdonSharp;
using UnityEngine;

public class QRCodeCharacterCountPlayer : SuperPlayer
{
    public string modeIndicator; // モード指示子を保持
    public int charCount; // 文字数を保持する変数
    public string outputBits; // ビット列の出力を保持する変数
    public QRCodeModePlayer qRCodeModePlayer; // アタッチ
    public InitFromQrcodePlayer initFromQrcodePlayer // アタッチ
    public RinaNumpy rinaNumpy;

    // 初期化メソッド (Pythonの__init__に相当)
    public bool QRCodeCharacterCountPlayerReset()
    {
        myName = "QRCodeCharacterCountPlayer";
        modeIndicator = null;
        outputBits = null;
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "QRCodeCharacterCountPlayer";
    }

    // 指定された文字数のビット数を計算するメソッド
    public string CalculateBitCount(int charCount, string modeIndicator)
    {
        // modeIndicatorに基づいてビット数を設定
        switch (modeIndicator)
        {
            case "0001": // 数字モード
                return Convert.ToString(charCount, 2).PadLeft(10, '0'); // 10bit
            case "0010": // 英数字モード
                return Convert.ToString(charCount, 2).PadLeft(9, '0'); // 9bit
            case "0100": // 8bitバイトモード
                return Convert.ToString(charCount, 2).PadLeft(8, '0'); // 8bit
            case "1000": // 漢字モード
                return Convert.ToString(charCount, 2).PadLeft(8, '0'); // 8bit
            default:
                Debug.LogError("Invalid modeIndicator. Ensure the mode is set correctly.");
                return null;
        }
    }

    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // モード指示子と文字数を取得
        this.modeIndicator = rinaNumpy.IntToStr(this.qRCodeModePlayer.ModeBitStr);
        this.charCount = this.initFromQrcodePlayer.data.Length; // 文字数を取得

        // モード指示子 + 文字数ビット情報を出力に設定
        this.outputBits = this.modeIndicator + this.CalculateBitCount(this.charCount, this.modeIndicator);

        return "Completed";
    }
}
