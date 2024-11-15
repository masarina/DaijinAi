using UdonSharp;
using UnityEngine;

public class QRCodeMapInitializerPlayer : UdonSharpBehaviour
{
    // メンバ変数（Pythonのインスタンス変数に相当）
    public int Version = 2; // QRコードのバージョン
    public int GridSize = 25; // QRコードのグリッドサイズ
    public float[] ModeCharNumInfoChecksumBitlist; // モード/文字数情報/チェックサムのビットリスト

    // RinaNumpyをアタッチ
    public RinaNumpy RinaNumpyInstance; // Unityエディタでアタッチすることを想定

    // 依存するプレイヤー
    public UdonSharpBehaviour ChecksumPlayer; // Unityでアタッチすることを想定

    // 自分の名前を返すメソッド
    public string ReturnMyName()
    {
        return "QRCodeMapInitializerPlayer";
    }

    // メイン処理
    public string ExecuteMain()
    {
        /*
         * UnityエディタでChecksumPlayerとRinaNumpyInstanceをアタッチすることを前提に処理を進める
         */

        // ChecksumPlayerからデータを取得
        QRCodeMapInitializerPlayer checksumPlayer = (QRCodeMapInitializerPlayer)ChecksumPlayer;
        ModeCharNumInfoChecksumBitlist = checksumPlayer.ModeCharNumInfoChecksumBitlist;

        // RinaNumpyを活用した処理例: 配列の正規化
        float mean = RinaNumpyInstance.Mean_FloatArray(ModeCharNumInfoChecksumBitlist);
        float std = RinaNumpyInstance.Std_FloatArray(ModeCharNumInfoChecksumBitlist);
        ModeCharNumInfoChecksumBitlist = RinaNumpyInstance.Subtract_FloatArray_Float(ModeCharNumInfoChecksumBitlist, mean);
        ModeCharNumInfoChecksumBitlist = RinaNumpyInstance.Divide_FloatArray_Float(ModeCharNumInfoChecksumBitlist, std);

        // 実行の確認用メッセージ
        Debug.Log($"{ReturnMyName()}が実行されました。");
        Debug.Log($"Version: {Version}, GridSize: {GridSize}");
        Debug.Log($"Normalized ModeCharNumInfoChecksumBitlist: {ModeCharNumInfoChecksumBitlist}");

        // プレイヤー自身を更新する処理
        return "Completed";
    }
}
