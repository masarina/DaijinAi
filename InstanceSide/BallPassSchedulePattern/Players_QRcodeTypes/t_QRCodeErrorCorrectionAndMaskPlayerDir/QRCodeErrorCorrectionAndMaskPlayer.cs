using UdonSharp;
using UnityEngine;

public class QRCodeErrorCorrectionAndMaskPlayer : SuperPlayer
{
    [HideInInspector] public string myName = null; // プレイヤー名を初期化
    [HideInInspector] public int[] formatBits = null; // 形式情報ビット（15bit）
    [HideInInspector] public int[] formatInfo = null; // 完成した15bit形式情報

    public RinaNumpy rinaNumpy; // RinaNumpyをUnityエディタでアタッチ

    public override string ReturnMyName()
    {
        return "QRCodeErrorCorrectionAndMaskPlayer";
    }

    public int[] GenerateFormatInfo(string errorLevelBits, string maskPatternBits)
    {
        /*
         * エラー補正レベルとマスクパターン（5bit）から
         * 15bitの形式情報を生成する
         */

        // 初期の5bit形式情報を配列に変換
        int[] initialBits = new int[5];
        for (int i = 0; i < errorLevelBits.Length; i++)
        {
            initialBits[i] = errorLevelBits[i] == '1' ? 1 : 0;
        }
        for (int i = 0; i < maskPatternBits.Length; i++)
        {
            initialBits[errorLevelBits.Length + i] = maskPatternBits[i] == '1' ? 1 : 0;
        }

        // G(x) = x^10 + x^8 + x^5 + x^4 + x^2 + x + 1
        int[] gxBits = new int[11] { 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1 };

        // x^10を掛けるため、末尾に0を10個追加
        int[] paddedBits = new int[15];
        rinaNumpy.CopyIntArray(initialBits, paddedBits, initialBits.Length); // 初期ビットをコピー

        // 剰余計算を実行
        for (int i = 0; i < initialBits.Length; i++)
        {
            if (paddedBits[i] == 1) // 1のときのみXORを実行
            {
                for (int j = 0; j < gxBits.Length; j++)
                {
                    paddedBits[i + j] ^= gxBits[j];
                }
            }
        }

        // 剰余ビット（10bit）を取得
        int[] remainderBits = new int[10];
        rinaNumpy.CopyIntArray(paddedBits, remainderBits, 10);

        // 初期5bitと剰余10bitを結合して15bit形式情報を生成
        int[] formatBits = new int[15];
        rinaNumpy.CopyIntArray(initialBits, formatBits, initialBits.Length);
        rinaNumpy.CopyIntArray(remainderBits, formatBits, remainderBits.Length);

        return formatBits;
    }

    public override string ExecuteMain()
    {
        /*
         * 形式情報を生成するメイン処理。
         * エラー補正レベル "10"（H）とマスクパターン "000" を使用。
         */

        // エラー補正レベルとマスクパターンのビット列
        string errorLevelBits = "10"; // Hレベルのエラー補正
        string maskPatternBits = "000"; // マスクパターンは000

        // 形式情報の生成
        formatInfo = GenerateFormatInfo(errorLevelBits, maskPatternBits);

        // Unityエディタでアタッチする形で自身を更新
        if (oneTimeWorldInstance != null)
        {
            oneTimeWorldInstance.qrCodeErrorCorrectionAndMaskPlayer = this;
        }

        return "Completed";
    }
}
