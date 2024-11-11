using UdonSharp;
using UnityEngine;

public class QRCodeTerminationPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;  // RinaNumpyクラスを使用
    public string modeIndicator;
    public string dataAndLast4Pattern;  // 完成したデータ + 終端パターン
    public string modeBitAndCharacterCountBit;
    public string errorMessage;
    public QRCodeCharacterCountPlayer qRCodeCharacterCountPlayer;
    public QRCodeModePlayer qRCodeModePlayer;
    public string paddingBits;  // パディングのビット部分
    
    public override string ReturnMyName()
    {
        return "QRCodeTerminationPlayer";
    }

    public string AddTerminationPattern(string dataBits, int symbolCapacity)
    {
        // 終端パターンを追加するロジック
        string terminationBits = "0000";  // 終端パターンとして4ビットの"0000"を用意
        int remainingBits = symbolCapacity - dataBits.Length;

        if (remainingBits > 0)
        {
            // 追加できるビット数を確保
            terminationBits = terminationBits.Substring(0, Mathf.Min(remainingBits, 4));
            dataBits += terminationBits;
        }

        return dataBits;
    }

    public void CheckDataSize(string dataBits, int symbolCapacity, string characterCountBits)
    {
        // シンボル容量の70%以内で収まっているかチェック
        int maxDataBits = Mathf.FloorToInt(symbolCapacity * 0.7f);
        int bitSize = dataBits.Length + characterCountBits.Length;

        if (bitSize > maxDataBits)
        {
            errorMessage = "データビット列がエラー訂正レベルHの制限を超えています。";
            Debug.LogError(errorMessage);
        }
    }

    public override string ExecuteMain()
    {
        // 必要な情報の取得
        string dataBits = qRCodeCharacterCountPlayer.dataBits;
        string modeIndicator = qRCodeModePlayer.modeIndicator;
        string characterCountBits = qRCodeCharacterCountPlayer.outputBits;

        // シンボル容量を計算（25×25 モジュールを使用）
        int symbolCapacity = 625 - 4 - 10;  // 説明に基づいて必要な減算値を適用

        // データサイズの確認
        CheckDataSize(dataBits, symbolCapacity, characterCountBits);

        // 終端パターンを追加
        dataAndLast4Pattern = AddTerminationPattern(dataBits, symbolCapacity);

        // 結果をワールドに反映


        return "Completed";
    }
}
