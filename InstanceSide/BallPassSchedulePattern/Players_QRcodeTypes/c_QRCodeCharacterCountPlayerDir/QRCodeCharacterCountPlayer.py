using UdonSharp;
using UnityEngine;

public class QRCodeCharacterCountPlayer : SuperPlayer
{
    private string characterCountBits; // 文字数ビット表記を格納する変数

    // 初期化メソッド
    public bool QRCodeCharacterCountPlayerReset()
    {
        myName = "QRCodeCharacterCountPlayer";
        characterCountBits = null; // 初期化
        return true;
    }

    public override string ReturnMyName()
    {
        return "QRCodeCharacterCountPlayer";
    }

    public string CalculateBitCount(int charCount, string modeIndicator)
    {
        string bitCount = "";

        // モードに基づいてビット数を計算
        if (modeIndicator == "0001") // 数字モード
        {
            bitCount = Convert.ToString(charCount, 2).PadLeft(10, '0'); // 10bit
        }
        else if (modeIndicator == "0010") // 英数字モード
        {
            bitCount = Convert.ToString(charCount, 2).PadLeft(9, '0'); // 9bit
        }
        else if (modeIndicator == "0100" || modeIndicator == "1000") // 8bitバイトモードと漢字モード
        {
            bitCount = Convert.ToString(charCount, 2).PadLeft(8, '0'); // 8bit
        }
        else
        {
            Debug.LogError("Invalid mode_indicator. Ensure the mode is set correctly.");
        }

        return bitCount;
    }

    public override string ExecuteMain()
    {
        string modeIndicator = worldInstance.qRCodeModePlayer.modeIndicator; // モード指示子を取得
        int charCount = worldInstance.initFromQrcodePlayer.data.Length; // データの長さから文字数を取得

        // モード指示子と文字数ビットを組み合わせた出力
        characterCountBits = modeIndicator + CalculateBitCount(charCount, modeIndicator);

        // 実行結果を表示
        Debug.Log($"Completed: {modeIndicator} {characterCountBits}");

        return "Completed";
    }
}
