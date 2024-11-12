using UdonSharp;
using UnityEngine;

public class ChecksumPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;  // RinaNumpyクラスを使用
    public string[] modeCharNumInfoChecksumBitList;
    public QRCodeBitConversionPlayer qRCodeBitConversionPlayer;
    public PolynomialDivisionPlayer polynomialDivisionPlayer;

    public override string ReturnMyName()
    {
        return "ChecksumPlayer";
    }

    public int CalculateChecksum(int[] dataList)
    {
        // データリストからチェックサムを計算するメソッド
        int sum = 0;
        foreach (int value in dataList)
        {
            sum += value;
        }
        return sum % 256;  // チェックサムを256で割った余り
    }

    public int[] AppendChecksum(int[] dataList, int checksum)
    {
        // データリストにチェックサムを追加
        int[] result = new int[dataList.Length + 1];
        dataList.CopyTo(result, 0);
        result[dataList.Length] = checksum;
        return result;
    }

    public override string ExecuteMain()
    {
        // ワールドインスタンスからデータを取得
        string dataStr = this.qRCodeBitConversionPlayer.dataBits;
        string modeAndCountInfoBitStr = this.qRCodeBitConversionPlayer.modeAndCountInfoBit;
        
        // モードと文字数情報ビットリストを結合
        string modeCharNumInfoBitList = modeAndCountInfoBitStr + dataStr;

        // ビットリストを10進数リストに変換
        int[] modeCharNumInfoDecimalList = polynomialDivisionPlayer.BitListToDecimalList(modeCharNumInfoBitList);

        // チェックサムの計算
        int checksum = CalculateChecksum(modeCharNumInfoDecimalList);

        // チェックサムをデータに追加
        modeCharNumInfoChecksumBitList = AppendChecksum(modeCharNumInfoDecimalList, checksum);

        // 自身のインスタンスをワールドに反映
        oneTimeWorldInstance.checksumPlayer = this;

        return "Completed";
    }
}
