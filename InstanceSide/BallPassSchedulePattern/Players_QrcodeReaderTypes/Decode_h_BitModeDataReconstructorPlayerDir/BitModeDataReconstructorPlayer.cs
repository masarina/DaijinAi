using UdonSharp;
using UnityEngine;

public class BitModeDataReconstructorPlayer : SuperPlayer
{
    public string mode; // モード (例: "0001")
    public int charNumInfoDecimal; // 文字数情報（10進数）
    public string data; // 元データ
    public string reconstructedData; // 復元されたデータ

    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // 初期化処理
    }

    public void ResetPlayer()
    {
        // プレイヤーの初期化
        myName = "BitModeDataReconstructorPlayer";
        mode = "";
        charNumInfoDecimal = 0;
        data = "";
        reconstructedData = "";
    }

    public override string ReturnMyName()
    {
        return "BitModeDataReconstructorPlayer";
    }

    private string ReconstructData(string data, string mode)
    {
        // データ復元処理
        string bitString = "";

        if (mode == "0001") // 数字モード
        {
            // 3桁ずつ分割してビットに変換
            for (int i = 0; i < data.Length; i += 3)
            {
                string chunk = data.Substring(i, Mathf.Min(3, data.Length - i)); // 最大3桁まで取得
                if (chunk.Length == 3)
                {
                    bitString += rinaNumpy.ConvertToBinary(int.Parse(chunk), 10); // RinaNumpyのメソッドを利用
                }
                else if (chunk.Length == 2)
                {
                    bitString += rinaNumpy.ConvertToBinary(int.Parse(chunk), 7); // RinaNumpyのメソッドを利用
                }
                else if (chunk.Length == 1)
                {
                    bitString += rinaNumpy.ConvertToBinary(int.Parse(chunk), 4); // RinaNumpyのメソッドを利用
                }
            }
        }
        else
        {
            Debug.LogWarning("Unsupported mode: " + mode);
        }

        return bitString;
    }

    public override string ExecuteMain()
    {
        // 必要なデータを取得
        var spiritBitDataPlayer = oneTimeWorldInstance.spiritBitDataPlayer;
        if (spiritBitDataPlayer == null)
        {
            Debug.LogError("SpiritBitDataPlayer is not attached.");
            return "Error";
        }

        mode = spiritBitDataPlayer.mode;
        charNumInfoDecimal = spiritBitDataPlayer.charNumInfoDecimal;
        data = spiritBitDataPlayer.data;

        // データ復元
        reconstructedData = ReconstructData(data, mode);

        // 文字数情報と復元データの長さを確認
        if (charNumInfoDecimal != reconstructedData.Length)
        {
            Debug.LogError("Character count mismatch. Reconstruction failed.");
            // 必要に応じてエラー処理を追加
        }

        // 自身のプレイヤー情報を更新
        oneTimeWorldInstance.bitModeDataReconstructorPlayer = this;

        Debug.Log("BitModeDataReconstructorPlayer completed successfully.");
        return "Completed";
    }
}
