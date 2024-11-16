using UdonSharp;
using UnityEngine;

public class QRCodeTimingPatternPlayer : SuperPlayer
{
    [HideInInspector] public string myName;  // プレイヤーの名前
    [HideInInspector] public int version;  // QRコードのバージョン
    [HideInInspector] public int gridSize;  // グリッドサイズ (バージョンによる)
    [HideInInspector] public int[][] qrCodeMap;  // QRコードのマップ (2次元配列)

    public QRCodePositionDetectionPlayer qRCodePositionDetectionPlayer; // Unityエディタでアタッチ
    public RinaNumpy rinaNumpy; // UnityエディタでRinaNumpyをアタッチ

    private void QRCodeTimingPatternPlayerReset()
    {
        myName = "QRCodeTimingPatternPlayer";
        version = 0;
        gridSize = 0;
        qrCodeMap = null; // 初期化
    }

    public string ReturnMyName()
    {
        return "QRCodeTimingPatternPlayer";
    }

    private int[][] AddTimingPattern(int[][] qrCodeMap)
    {
        int gridSize = qrCodeMap.Length;

        // タイミングパターンの配置 (縦と横の交互配置)
        for (int i = 8; i < gridSize - 8; i++)
        {
            // 横方向のタイミングパターン (y = 6)
            qrCodeMap[6][i] = (i % 2 == 0) ? -2 : -1; // 偶数: -2 (白), 奇数: -1 (黒)
            // 縦方向のタイミングパターン (x = 6)
            qrCodeMap[i][6] = (i % 2 == 0) ? -2 : -1;
        }

        return qrCodeMap;
    }

    public override string ExecuteMain()
    {
        /*
         * メイン処理: タイミングパターンを追加
         */

        // QRコードの位置検出プレイヤーからデータを取得
        version = qRCodePositionDetectionPlayer.version;
        gridSize = version;
        qrCodeMap = qRCodePositionDetectionPlayer.qrCodeMap;

        // RinaNumpyでグリッドサイズチェック（例: 配列長の取得など）
        if (rinaNumpy == null)
        {
            Debug.LogError("RinaNumpy is not attached. Please attach it in the Unity Editor.");
            return "Failed";
        }

        // 必要な配列操作にRinaNumpyメソッドを活用
        float[] exampleArray = new float[gridSize]; // 必要に応じて変換
        for (int i = 0; i < exampleArray.Length; i++)
        {
            exampleArray[i] = i % 2 == 0 ? -2f : -1f;
        }

        // タイミングパターンを追加
        qrCodeMap = AddTimingPattern(qrCodeMap);

        // 実行完了メッセージ
        Debug.Log($"{ReturnMyName()}が実行されました。");

        // 必要な変数を再設定
        qRCodePositionDetectionPlayer.qrCodeMap = qrCodeMap;

        return "Completed";
    }
}

