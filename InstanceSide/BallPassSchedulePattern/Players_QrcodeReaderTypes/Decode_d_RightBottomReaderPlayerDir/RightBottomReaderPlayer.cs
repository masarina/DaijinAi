using UdonSharp;
using UnityEngine;

public class RightBottomReaderPlayer : SuperPlayer
{
    public int[][] replacedMatrix; // 置き換え後のマトリックス
    public string pngFilePath; // 写真のパス
    public int[][] binaryMatrix2DList; // 置き換え前のマトリックス
    public int[][] newList2D; // n*2のリストに変換したもの
    public int[] dataRead; // 右下から読み込んだデータを保持する1次元リスト

    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // プレイヤーの初期化
    }

    public void ResetPlayer()
    {
        myName = "RightBottomReaderPlayer"; // プレイヤー名を設定
        replacedMatrix = new int[0][]; // 初期化
        pngFilePath = "";
        binaryMatrix2DList = new int[0][]; // 初期化
        newList2D = new int[0][]; // 初期化
        dataRead = new int[0]; // 初期化
    }

    public override string ReturnMyName()
    {
        return "RightBottomReaderPlayer";
    }

    private int[] FlattenList2D(int[][] list2D)
    {
        // 2次元リストを1次元リストに変換する
        int[] flattenedList = new int[0]; // 最終的な結果
        int totalLength = list2D.Length * 2; // 合計の長さを計算

        int index = 0;
        int[] tempFlattenedList = new int[totalLength]; // 一時的な配列を用意

        for (int i = 0; i < list2D.Length; i++)
        {
            int[] pair = list2D[i];

            // 右からデータをチェックして格納
            if (pair[1] >= 0)
            {
                tempFlattenedList[index++] = pair[1];
            }

            // 次に左をチェックして格納
            if (pair[0] >= 0)
            {
                tempFlattenedList[index++] = pair[0];
            }
        }

        // 必要な長さに切り詰めて新しい配列を作成
        flattenedList = rinaNumpy.SubArray(tempFlattenedList, 0, index); // RinaNumpyのSubArrayを使用

        return flattenedList;
    }

    public override string ExecuteMain()
    {
        // ColumnSplitterConcatPlayerの結果を取得
        ColumnSplitterConcatPlayer woP = (ColumnSplitterConcatPlayer)oneTimeWorldInstance.GetComponent(typeof(ColumnSplitterConcatPlayer));

        if (woP == null)
        {
            Debug.LogError("ColumnSplitterConcatPlayer is not attached or initialized.");
            return "Error";
        }

        // データを取得
        replacedMatrix = woP.replacedMatrix;
        pngFilePath = woP.pngFilePath;
        binaryMatrix2DList = woP.binaryMatrix2DList;
        newList2D = woP.newList2D;

        // 右下からデータを読み取る
        dataRead = FlattenList2D(binaryMatrix2DList);

        // 読み込んだデータをログで確認
        Debug.Log("データが右下から読み込まれました: " + rinaNumpy.IntArrayToString(dataRead)); // RinaNumpyのIntArrayToStringを使用

        // 自身を更新
        oneTimeWorldInstance.rightBottomReaderPlayer = this;

        return "Completed";
    }
}
