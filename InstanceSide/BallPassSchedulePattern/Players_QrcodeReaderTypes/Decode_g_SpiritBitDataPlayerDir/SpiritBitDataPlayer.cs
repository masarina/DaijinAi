using UdonSharp;
using UnityEngine;

public class SpiritBitDataPlayer : SuperPlayer
{
    // Unityエディタでアタッチするプロパティ
    [HideInInspector]
    public string pngFilePath; // 写真のパス
    [HideInInspector]
    public int[] processedData; // 8bit毎にスプリットしたデータ
    [HideInInspector]
    public string mode; // モード情報
    [HideInInspector]
    public string data; // データ部分
    [HideInInspector]
    public int charNumInfoDecimal; // 文字数情報

    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    public override string ReturnMyName()
    {
        return "SpiritBitDataPlayer";
    }

    public override string ExecuteMain()
    {
        if (oneTimeWorldInstance == null || rinaNumpy == null)
        {
            Debug.LogError("oneTimeWorldInstance or RinaNumpy is not set.");
            return "Error";
        }

        // 入力データを取得
        ChecksumCheekPlayer woP = oneTimeWorldInstance.checksumCheekPlayer;
        pngFilePath = woP.pngFilePath; // 写真のパス
        processedData = woP.processedData; // 8bit毎にスプリットしたデータ

        // メイン処理
        string modeCharNumInfoDataFlattenBit = rinaNumpy.IntArrayToString(processedData); // FlattenNumbersAndToStrを置き換え

        // モードの抽出
        mode = modeCharNumInfoDataFlattenBit.Substring(0, 5);

        // 文字数情報の抽出
        int firstDatasPoint;
        charNumInfoDecimal = CharNumInfoCatcherWithRinaNumpy(mode, modeCharNumInfoDataFlattenBit, out firstDatasPoint);

        // データ部分の抽出
        data = modeCharNumInfoDataFlattenBit.Substring(firstDatasPoint);

        // 自身を更新
        oneTimeWorldInstance.spiritBitDataPlayer = this;

        Debug.Log("SpiritBitDataPlayer execution completed with RinaNumpy.");
        return "Completed";
    }

    private int CharNumInfoCatcherWithRinaNumpy(string mode, string strBit, out int firstDatasPoint)
    {
        /**
         * RinaNumpyを利用してモードとビット文字列から文字数情報を取得する。
         */
        int decimalNumber = 0;
        firstDatasPoint = 0; // 初期化

        switch (mode)
        {
            case "0001": // 数字モード（10bit）
                firstDatasPoint = 16;
                decimalNumber = rinaNumpy.BitStringToInt(strBit.Substring(5, 10));
                break;
            case "0010": // 英数字モード（9bit）
                firstDatasPoint = 15;
                decimalNumber = rinaNumpy.BitStringToInt(strBit.Substring(5, 9));
                break;
            case "0100": // 8bitバイトモード（8bit）
                firstDatasPoint = 16;
                decimalNumber = rinaNumpy.BitStringToInt(strBit.Substring(5, 8));
                break;
            case "1000": // 漢字モード（13bit）
                firstDatasPoint = 14;
                decimalNumber = rinaNumpy.BitStringToInt(strBit.Substring(5, 13));
                break;
            default:
                Debug.LogError($"Invalid mode: {mode}");
                break;
        }
        return decimalNumber;
    }
}
