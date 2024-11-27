using UdonSharp;
using UnityEngine;

public class ChecksumCheekPlayer : SuperPlayer
{
    [HideInInspector] public string pngFilePath; // 写真のパス
    [HideInInspector] public int[] processedData; // 8bit毎にスプリットしたデータ
    [HideInInspector] public int encodeTimeCheckCode; // encode時のチェックサム

    public BitDataProcessorPlayer bitDataProcessorPlayer; // Unityエディタでアタッチ
    public ChecksumPlayer checksumPlayer; // Unityエディタでアタッチ
    public RinaNumpy rinaNumpy; // RinaNumpyをUnityエディタでアタッチ

    void Start()
    {
        ResetPlayer(); // 初期化メソッドの呼び出し
    }

    public void ResetPlayer()
    {
        myName = "ChecksumCheekPlayer";
        pngFilePath = string.Empty;
        processedData = new int[0];
        encodeTimeCheckCode = 0;
    }

    public override string ReturnMyName()
    {
        return "ChecksumCheekPlayer";
    }

    public override string ExecuteMain()
    {
        // 入力部分
        if (bitDataProcessorPlayer == null || checksumPlayer == null || rinaNumpy == null)
        {
            Debug.LogError("Required components are not attached.");
            return "Error";
        }

        // BitDataProcessorPlayerからデータを取得
        pngFilePath = bitDataProcessorPlayer.pngFilePath;
        processedData = (int[])rinaNumpy.CopyArray(bitDataProcessorPlayer.processedData); // RinaNumpyで配列コピー
        encodeTimeCheckCode = processedData[processedData.Length - 1]; // 最後の要素をチェックサムとして取得

        // 配列からチェックサム部分を除去
        int[] dataWithoutChecksum = rinaNumpy.SubArray(processedData, 0, processedData.Length - 1); // RinaNumpyで部分配列取得

        // ChecksumPlayerを使ったメイン処理
        int[] modeCharNumInfoDecimalList = checksumPlayer.ToDecimal(dataWithoutChecksum);
        int decodeTimeChecksum = checksumPlayer.CalculateChecksum(modeCharNumInfoDecimalList);

        // チェックサムが正しいか確認
        if (encodeTimeCheckCode != decodeTimeChecksum)
        {
            Debug.LogError("Checksum mismatch detected.");
            // 必要に応じてフラグを立てる（共通フラグの実装は別箇所で行う）
            return "ChecksumMismatch";
        }

        // 出力部分
        Debug.Log("Checksum validated successfully.");

        // 自身のインスタンスを更新
        this.oneTimeWorldInstance.checksumCheekPlayer = this;

        return "Completed";
    }
}
