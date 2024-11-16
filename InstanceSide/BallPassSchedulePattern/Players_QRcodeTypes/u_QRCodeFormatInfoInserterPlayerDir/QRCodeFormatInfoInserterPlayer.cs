using UdonSharp;
using UnityEngine;

public class QRCodeFormatInfoInserterPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy; // UnityエディタでアタッチするRinaNumpyインスタンス
    public QRCodeMaskApplicatorPlayer qRCodeMaskApplicatorPlayer; // Unityエディタでアタッチ
    public QRCodeErrorCorrectionAndMaskPlayer qRCodeErrorCorrectionAndMaskPlayer; // Unityエディタでアタッチ

    public override string ReturnMyName()
    {
        return "QRCodeFormatInfoInserterPlayer";
    }

    public void InsertFormatInfo()
    {
        /*
         * QRコードのマトリックスに形式情報を挿入する
         */
        
        // 形式情報の15bitデータを取得
        int[] formatInfo = qRCodeErrorCorrectionAndMaskPlayer.FormatBits;

        // QRコードの25x25マトリックスを取得
        int[,] matrix = qRCodeMaskApplicatorPlayer.QRMap2DArray;

        // 上部（縦方向）の挿入
        for (int i = 0; i < 6; i++)
        {
            matrix[i, 8] = formatInfo[i]; // 上部の最初の6ビット
        }
        matrix[7, 8] = formatInfo[6];  // 7行目
        matrix[8, 8] = formatInfo[7];  // 8行目（境界）

        // 左下の列方向の挿入
        for (int i = 0; i < 6; i++)
        {
            matrix[8, i] = formatInfo[8 + i]; // 下部の6ビット
        }
        matrix[8, 7] = formatInfo[13];      // 下部の6ビット目
        matrix[8, 8] = formatInfo[14];      // 境界の最後のビット

        // 配列操作をRinaNumpyを用いて行う（例: 配列の内容をコピー）
        int[] copiedFormatInfo = new int[formatInfo.Length];
        rinaNumpy.CopyIntArray(formatInfo, copiedFormatInfo, formatInfo.Length);

        // 更新されたマトリックスを戻す
        qRCodeMaskApplicatorPlayer.QRMap2DArray = matrix;
    }

    public override string ExecuteMain()
    {
        /*
         * メイン処理を実行
         */
        InsertFormatInfo();

        // 自身のインスタンスをUnity内で登録（必要に応じてアタッチ済みのインスタンスに更新）
        qRCodeMaskApplicatorPlayer.qRCodeFormatInfoInserterPlayer = this;

        return "Completed";
    }
}
