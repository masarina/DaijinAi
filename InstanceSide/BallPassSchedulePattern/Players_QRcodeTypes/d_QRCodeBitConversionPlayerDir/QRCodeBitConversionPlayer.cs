using UdonSharp;
using UnityEngine;

public class QRCodeBitConversionPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;  // RinaNumpyクラスを使用
    public string modeIndicator;
    public string dataBits;
    public string modeAndCountInfoBit;

    public override string ReturnMyName()
    {
        return "QRCodeBitConversionPlayer";
    }

    public string NumericModeBitConversion(string data)
    {
        // 数字モードのビット変換ロジック
        string bits = "";
        int chunkLength = 3;

        for (int i = 0; i < data.Length; i += chunkLength)
        {
            string chunk = data.Substring(i, Mathf.Min(chunkLength, data.Length - i));
            int value = int.Parse(chunk);
            if (chunk.Length == 3)
            {
                bits += rinaNumpy.ConvertToBinary(value, 10);  // 3桁 -> 10bit
            }
            else if (chunk.Length == 2)
            {
                bits += rinaNumpy.ConvertToBinary(value, 7);   // 2桁 -> 7bit
            }
            else if (chunk.Length == 1)
            {
                bits += rinaNumpy.ConvertToBinary(value, 4);   // 1桁 -> 4bit
            }
        }
        return bits;
    }

    public string AlphanumericModeBitConversion(string data)
    {
        // 英数字モードのビット変換ロジック
        string bits = "";
        int[] alphanumericTable = new int[45];
        alphanumericTable['0'] = 0; alphanumericTable['1'] = 1; // 以降45文字分初期化を続ける

        for (int i = 0; i < data.Length; i += 2)
        {
            int combinedValue;
            if (i + 1 < data.Length)
            {
                combinedValue = alphanumericTable[data[i]] * 45 + alphanumericTable[data[i + 1]];
                bits += rinaNumpy.ConvertToBinary(combinedValue, 11);  // 2文字 -> 11bit
            }
            else
            {
                combinedValue = alphanumericTable[data[i]];
                bits += rinaNumpy.ConvertToBinary(combinedValue, 6);  // 1文字 -> 6bit
            }
        }
        return bits;
    }

    public string ByteModeBitConversion(string data)
    {
        // バイトモードのビット変換ロジック
        string bits = "";
        for (int i = 0; i < data.Length; i++)
        {
            int asciiValue = (int)data[i];
            bits += rinaNumpy.ConvertToBinary(asciiValue, 8);  // ASCII文字を8bitで表現
        }
        return bits;
    }

    public override string ExecuteMain()
    {
        // データとモードの取得
        string data = oneTimeWorldInstance.initFromQrcodePlayer.data;
        string mode = oneTimeWorldInstance.initFromQrcodePlayer.mode;

        // モードに応じたビット変換
        if (mode == "numeric")
        {
            dataBits = NumericModeBitConversion(data);
        }
        else if (mode == "alphanumeric")
        {
            dataBits = AlphanumericModeBitConversion(data);
        }
        else if (mode == "byte")
        {
            dataBits = ByteModeBitConversion(data);
        }
        else
        {
            Debug.LogError("Invalid mode. Choose from: numeric, alphanumeric, byte.");
            return "Failed";
        }

        // モードと文字数情報のビットを設定
        modeAndCountInfoBit = oneTimeWorldInstance.qRCodeCharacterCountPlayer.output_bits;

        // ワールドに自身のインスタンスを反映
        oneTimeWorldInstance.qRCodeBitConversionPlayer = this;

        return "Completed";
    }
}