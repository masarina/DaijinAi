using UdonSharp;
using UnityEngine;

public class ChecksumPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;  // RinaNumpyクラスのインスタンス
    public QRCodeBitConversionPlayer qRCodeBitConversionPlayer;
    public PolynomialDivisionPlayer polynomialDivisionPlayer;
    
    public string[] modeCharNumInfoChecksumBitlist;
    public string dataStr;
    public string modeCharNumInfoBitlist;

    public override string ReturnMyName()
    {
        return "ChecksumPlayer";
    }

    public int CalculateChecksum(int[] dataList)
    {
        // データリストからChecksumを計算し、256で割った余りを返す
        int sum = 0;
        for (int i = 0; i < dataList.Length; i++)
        {
            sum += dataList[i];
        }
        return sum % 256;
    }

    public int[] AppendChecksum(int[] dataList, int checksum)
    {
        // データリストにChecksumを追加
        int[] dataListWithChecksum = new int[dataList.Length + 1];
        for (int i = 0; i < dataList.Length; i++)
        {
            dataListWithChecksum[i] = dataList[i];
        }
        dataListWithChecksum[dataList.Length] = checksum;
        return dataListWithChecksum;
    }

    private string ArrayToString(int[] array)
    {
        // 配列を文字列に変換
        string result = "";
        for (int i = 0; i < array.Length; i++)
        {
            result += array[i].ToString();
            if (i < array.Length - 1)
            {
                result += ", ";
            }
        }
        return result;
    }

    public void PrintData(int[] dataList, int checksum, int[] dataListWithChecksum)
    {
        // データリスト、Checksum、Checksum付きデータリストをログ出力
        Debug.Log("元のデータリスト: " + ArrayToString(dataList));
        Debug.Log("Checksum: " + checksum);
        Debug.Log("Checksum付きデータリスト: " + ArrayToString(dataListWithChecksum));
    }

    public override string ExecuteMain()
    {
        // QRCodeBitConversionPlayerからビットデータを取得
        this.dataStr = qRCodeBitConversionPlayer.dataBits;
        this.modeCharNumInfoBitlist = qRCodeBitConversionPlayer.modeAndCountInfoBit + this.dataStr;

        // PolynomialDivisionPlayerからビット列を10進数リストに変換
        int[] modeCharNumInfoDecimalList = polynomialDivisionPlayer.BitListToDecimalList(this.modeCharNumInfoBitlist);

        // Checksumの計算
        int checksum = CalculateChecksum(modeCharNumInfoDecimalList);

        // Checksumをデータリストに追加
        int[] modeCharNumInfoChecksumBitlist = AppendChecksum(modeCharNumInfoDecimalList, checksum);
        this.modeCharNumInfoChecksumBitlist = new string[modeCharNumInfoChecksumBitlist.Length];
        
        // 配列の内容を文字列形式で保存
        for (int i = 0; i < modeCharNumInfoChecksumBitlist.Length; i++)
        {
            this.modeCharNumInfoChecksumBitlist[i] = modeCharNumInfoChecksumBitlist[i].ToString();
        }

        // 自身のインスタンスをone_time_world_instanceに登録
        oneTimeWorldInstance.checksumPlayer = this;

        return "Completed";
    }
}
