/// Created by Masarina(Twitter_@Masarina002)

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
        RinaNumpy.CopyIntArray(dataList, dataListWithChecksum, dataList.Length); // RinaNumpyで配列をコピー
        dataListWithChecksum[dataList.Length] = checksum;
        return dataListWithChecksum;
    }

    private string ArrayToString(int[] array)
    {
        // 配列を文字列に変換
        int[] tempArray = new int[array.Length]; // コピー用の一時配列
        RinaNumpy.CopyIntArray(array, tempArray, array.Length); // 配列をコピー
        string result = "";

        for (int i = 0; i < tempArray.Length; i++)
        {
            result += tempArray[i].ToString(); // 各要素を文字列化して結合
            if (i < tempArray.Length - 1)
            {
                result += ", "; // 区切り文字を追加
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

        return "Completed";
    }
}
