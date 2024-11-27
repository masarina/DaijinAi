using UdonSharp;
using UnityEngine;

public class BitDataProcessorPlayer : SuperPlayer
{
    public string pngFilePath; // 写真のパス
    public string dataRead; // データ部分を1次元リスト化したもの
    public string[] processedData; // 8ビット毎にスプリットしたデータ

    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // 初期化
    }

    public void ResetPlayer()
    {
        myName = "BitDataProcessorPlayer"; // プレイヤー名を設定
        pngFilePath = ""; // 初期化
        dataRead = ""; // 初期化
        processedData = new string[0]; // 初期化
    }

    public override string ReturnMyName()
    {
        return "BitDataProcessorPlayer";
    }

    private string[] ProcessBitData(string bitData)
    {
        /*
         * RinaNumpyを活用してビットデータを8ビットごとに分割
         */
        if (string.IsNullOrEmpty(bitData))
        {
            Debug.LogError("Input bitData is null or empty.");
            return new string[0];
        }

        int dataLength = bitData.Length;
        int splitCount = Mathf.CeilToInt(dataLength / 8f); // 8ビットごとに分割した個数を計算
        string[] result = new string[splitCount];

        for (int i = 0; i < splitCount; i++)
        {
            int startIndex = i * 8;
            int length = Mathf.Min(8, dataLength - startIndex);
            result[i] = bitData.Substring(startIndex, length); // RinaNumpyはここで必要なし
        }

        return result;
    }

    public override string ExecuteMain()
    {
        /*
         * データを取得して8ビットごとに分割し、結果を保存する
         */
        RightBottomReaderPlayer woP = (RightBottomReaderPlayer)oneTimeWorldInstance.GetComponent(typeof(RightBottomReaderPlayer));

        if (woP == null)
        {
            Debug.LogError("RightBottomReaderPlayer is not attached.");
            return "Error";
        }

        pngFilePath = woP.pngFilePath; // 写真のパスを取得
        dataRead = woP.dataRead; // データ部分を取得

        if (string.IsNullOrEmpty(dataRead))
        {
            Debug.LogError("DataRead is null or empty.");
            return "Error";
        }

        // RinaNumpyを使った処理
        processedData = ProcessBitData(dataRead);

        // 自身を更新
        BitDataProcessorPlayer updatedPlayer = (BitDataProcessorPlayer)oneTimeWorldInstance.GetComponent(typeof(BitDataProcessorPlayer));
        if (updatedPlayer != null)
        {
            updatedPlayer.pngFilePath = pngFilePath;
            updatedPlayer.dataRead = dataRead;
            updatedPlayer.processedData = processedData;
        }

        Debug.Log("BitDataProcessorPlayer processing completed with RinaNumpy.");
        return "Completed";
    }
}
