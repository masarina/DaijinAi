using UdonSharp;
using UnityEngine;

public class QRCodeMarkingPlayer : SuperPlayer
{
    // Unityエディタでアタッチするオブジェクト
    public SuperPlayer QRCodeAlignmentPatternPlayer;
    public RinaNumpy rinaNumpy;

    // 必要な変数を宣言
    public string ModeCharNumInfoChecksumBitlist;
    public int Version;
    public int GridSize;
    public int[,] QRCodeMap; // 二次元配列として定義
    public int[,] ModifiedQRCodeMap; // 修正後のQRコード

    public int MarkingNum = -4; // マーキング値

    public override string ReturnMyName()
    {
        return "QRCodeMarkingPlayer";
    }

    public int[,] ModifyQRCode(int[,] qrCodeMap)
    {
        /*
         * RinaNumpyを利用してQRコードの特定箇所を修正。
         * 必要な箇所を直接上書きする。
         */
        int rows = qrCodeMap.GetLength(0);
        int cols = qrCodeMap.GetLength(1);

        // 修正後の配列を生成
        int[,] result = new int[rows, cols];
        rinaNumpy.CopyIntArray2D(qrCodeMap, result, rows, cols);

        // 上部の6ビット部分
        for (int i = 0; i < 5; i++)
        {
            result[i, 8] = MarkingNum;
        }

        // 中央の縦
        result[7, 8] = MarkingNum;
        result[8, 8] = MarkingNum;

        // 左部の6ビット部分
        for (int j = 0; j < 5; j++)
        {
            result[8, j] = MarkingNum;
        }

        // 中央の横
        result[8, 7] = MarkingNum;

        // 下部の縦
        for (int i = rows - 7; i < rows - 1; i++)
        {
            result[i, 8] = MarkingNum;
        }

        // 右部の横
        for (int j = cols - 8; j < cols - 1; j++)
        {
            result[8, j] = MarkingNum;
        }

        // ダークモジュール
        result[rows - 8, 8] = -1;

        return result;
    }

    public override string ExecuteMain()
    {
        /*
         * QRコードを修正するメイン処理。
         * UnityエディタでアタッチされたプレイヤーとRinaNumpyのデータを利用。
         */
        
        if (QRCodeAlignmentPatternPlayer == null)
        {
            Debug.LogError("QRCodeAlignmentPatternPlayer is not attached.");
            return "Failed";
        }
        if (rinaNumpy == null)
        {
            Debug.LogError("RinaNumpy is not attached.");
            return "Failed";
        }

        // 前のプレイヤーからデータを取得
        ModeCharNumInfoChecksumBitlist = QRCodeAlignmentPatternPlayer.ModeCharNumInfoChecksumBitlist;
        Version = QRCodeAlignmentPatternPlayer.Version;
        GridSize = QRCodeAlignmentPatternPlayer.GridSize;
        QRCodeMap = QRCodeAlignmentPatternPlayer.QRCodeMap;

        // QRコードを修正
        ModifiedQRCodeMap = ModifyQRCode(QRCodeMap);

        Debug.Log($"{ReturnMyName()} has executed successfully. QR Code has been modified.");

        // 自身のインスタンスをworldに登録
        this.OneTimeWorldInstance.QRCodeMarkingPlayer = this;

        return "Completed";
    }
}
