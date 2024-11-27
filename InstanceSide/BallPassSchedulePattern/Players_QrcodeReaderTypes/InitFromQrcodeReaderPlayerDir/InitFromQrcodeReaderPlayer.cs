using UdonSharp;
using UnityEngine;

public class InitFromQrcodeReaderPlayer : SuperPlayer
{
    [Header("Players (Attach in Unity Editor)")]
    public ColumnSplitterConcatPlayer columnSplitterConcatPlayer; // Unityエディタでアタッチ
    public InitFromQrcodeReaderPlayer initFromQrcodeReaderPlayer; // 自分自身を保持（Unityエディタで設定）

    void Start()
    {
        ResetPlayer(); // 初期化処理
    }

    public void ResetPlayer()
    {
        myName = "InitFromQrcodeReaderPlayer"; // プレイヤー名を設定
    }

    public override string ReturnMyName()
    {
        return "InitFromQrcodeReaderPlayer";
    }

    public override string ExecuteMain()
    {
        /*
         * このメソッド実行直前に、SuperPlayerのメンバ変数
         * one_time_world_instanceに最新のworldインスタンスが代入されていることを想定
         */

        // 初期化メッセージを表示
        Debug.Log($"{ReturnMyName()} が実行されました。");

        if (columnSplitterConcatPlayer == null)
        {
            Debug.LogError("ColumnSplitterConcatPlayer がアタッチされていません。Unityエディタで設定してください。");
            return "Error";
        }

        // ColumnSplitterConcatPlayer からデータを取得
        int[][] list2d = columnSplitterConcatPlayer.newList2D;

        if (list2d == null || list2d.Length == 0)
        {
            Debug.LogWarning("ColumnSplitterConcatPlayer の newList2D が初期化されていません。");
        }
        else
        {
            Debug.Log($"取得したデータの行数: {list2d.Length}");
        }

        // 自身を保持する
        initFromQrcodeReaderPlayer = this;

        Debug.Log("InitFromQrcodeReaderPlayer の処理が完了しました。");
        return "Completed";
    }
}
