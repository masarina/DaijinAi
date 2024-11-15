using UdonSharp;
using UnityEngine;

public class QRCodeMapInitializerPlayer : UdonSharpBehaviour
{
    // メンバ変数（Pythonのインスタンス変数に相当）
    public int Version = 2; // QRコードのバージョン
    public int GridSize = 25; // QRコードのグリッドサイズ
    public int[] ModeCharNumInfoChecksumBitlist; // モード/文字数情報/チェックサムのビットリスト

    // 依存するプレイヤー（Pythonの`self.one_time_world_instance`の置き換え）
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
         * UnityエディタでChecksumPlayerをアタッチすることを前提に処理を進める
         */
        
        // ChecksumPlayerからモード/文字数情報/チェックサムのビットリストを取得
        QRCodeMapInitializerPlayer checksumPlayer = (QRCodeMapInitializerPlayer)ChecksumPlayer;
        ModeCharNumInfoChecksumBitlist = checksumPlayer.ModeCharNumInfoChecksumBitlist;

        // 実行の確認用メッセージ
        Debug.Log($"{ReturnMyName()}が実行されました。");

        // データの出力（Unityエディタのインスペクタで確認可能）
        Debug.Log($"Version: {Version}, GridSize: {GridSize}");

        // プレイヤー自身を更新する処理
        // Unityでの設計に応じて、他のスクリプトやオブジェクトと連携させる

        return "Completed";
    }
}
