/// <summary>
/// このプレイヤーは
/// プレイヤーとしては使用していませんが
/// ライブラリとしては使っています。
/// BitListToDecimalList だけ使用中です。
/// </summary>

using UdonSharp;
using UnityEngine;

public class PolynomialDivisionPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;  // RinaNumpyクラスを使用
    public string[] mode_charNumInfo_data_pad4_pad8_list;
    public int[] remainder;
    public int[] mode_charNumInfo_data_pad4_pad8_Decimal_list;
    public int[] error_correction_polynomial;
    public int[] data_polynomial;
    
    public GaloisFieldPlayer galoisFieldPlayer;  // ガロア体プレイヤー
    public ErrorCorrectionPolynomialPlayer errorCorrectionPolynomialPlayer; // エラー訂正多項式プレイヤー
    
    public override string ReturnMyName()
    {
        return "PolynomialDivisionPlayer";
    }

    public int[] BitListToDecimalList(string[] bitList)
    {
        // 8ビットごとのビット列を10進数に変換し、256になった場合は0に置き換えます。
        int[] decimalList = new int[bitList.Length];
        for (int i = 0; i < bitList.Length; i++)
        {
            int decimalValue = this.BitStringToInt(bitList[i]);  // 2進数の文字列を10進数に変換
            if (decimalValue == 256)  // ガロア体では256は0になるので置き換える
            {
                decimalValue = 0;
            }
            decimalList[i] = decimalValue;
        }
        return decimalList;
    }

    public int[] DividePolynomial(int[] dataPolynomial)
    {
        // データコード多項式 f(x) を生成多項式 g(x) で除算します。
        data_polynomial = dataPolynomial;

        // 出力データ: 剰余多項式（初期化）
        int[] remainder = new int[data_polynomial.Length];
        for (int i = 0; i < data_polynomial.Length; i++)
        {
            remainder[i] = data_polynomial[i];  // 手動で配列をコピー
        }

        // 生成多項式の長さを取得
        int gLen = error_correction_polynomial.Length;

        // 多項式除算を実行
        for (int i = 0; i < dataPolynomial.Length - gLen + 1; i++)
        {
            int coefficient = remainder[i];
            if (coefficient != 0)  // 係数が0でない場合のみ除算処理を行う
            {
                for (int j = 0; j < gLen; j++)
                {
                    // 各項を生成多項式と掛け合わせて引く (排他的論理和)
                    remainder[i + j] ^= GaloisMultiply(coefficient, error_correction_polynomial[j]);
                }
            }
        }
        
        // 出力データとして剰余多項式を返す
        int[] resultRemainder = new int[gLen];
        for (int i = 0; i < gLen; i++)
        {
            resultRemainder[i] = remainder[remainder.Length - gLen + i];  // 手動で配列の部分をコピー
        }
        return resultRemainder;
    }

    public int GaloisMultiply(int a, int b)
    {
        // ガロア体 GF(2^8) での乗算を行います。
        if (a == 0 || b == 0)
            return 0;
        
        int logA = galoisFieldPlayer.galois_field_log_table[a];
        int logB = galoisFieldPlayer.galois_field_log_table[b];
        int logResult = logA + logB;
        
        if (logResult >= 255)
            logResult -= 255;
        
        return galoisFieldPlayer.galois_field_exponent_table[logResult];
    }

    public override string ExecuteMain()
    {
        // データと設定情報の取得
        mode_charNumInfo_data_pad4_pad8_list = galoisFieldPlayer.mode_charNumInfo_data_pad4_pad8_list;
        error_correction_polynomial = errorCorrectionPolynomialPlayer.error_correction_polynomial;

        // データを10進数リストに変換
        int[] dataDecimal = BitListToDecimalList(mode_charNumInfo_data_pad4_pad8_list);

        // 多項式の除算を実行して剰余を取得
        remainder = DividePolynomial(dataDecimal);

        // 10進数バージョンも保持する。
        mode_charNumInfo_data_pad4_pad8_Decimal_list = dataDecimal;

        // worldインスタンスに自身のインスタンスを登録
        oneTimeWorldInstance.polynomialDivisionPlayer = this;

        return "Completed";
    }

}
