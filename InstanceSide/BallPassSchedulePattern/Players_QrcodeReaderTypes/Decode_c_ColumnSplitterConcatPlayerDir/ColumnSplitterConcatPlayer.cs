using UdonSharp;
using UnityEngine;

public class ColumnSplitterConcatPlayer : SuperPlayer
{
    public int[][] replacedMatrix; // 置き換え後のマトリックス
    public string pngFilePath; // 写真のパス
    public int[][] binaryMatrix2DList; // 置き換え前のマトリックス
    public int[][] newList2D; // 処理結果の新しいジャグ配列

    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // プレイヤーを初期化
    }

    public void ResetPlayer()
    {
        myName = "ColumnSplitterConcatPlayer"; // プレイヤー名を設定
        replacedMatrix = new int[0][]; // 初期化
        pngFilePath = "";
        binaryMatrix2DList = new int[0][]; // 初期化
        newList2D = new int[0][]; // 初期化
    }

    public override string ReturnMyName()
    {
        return "ColumnSplitterConcatPlayer";
    }

    private int[][] AddColumnWithNegative13ToTheLeft(int[][] matrix)
    {
        // 左に-13を追加した新しいジャグ配列を作成
        int[][] newMatrix = new int[matrix.Length][];
        for (int i = 0; i < matrix.Length; i++)
        {
            int[] newRow = new int[matrix[i].Length + 1];
            newRow[0] = -13; // 左端に-13を追加
            for (int j = 0; j < matrix[i].Length; j++) // コピー処理
            {
                newRow[j + 1] = matrix[i][j];
            }
            newMatrix[i] = newRow;
        }
        return newMatrix;
    }

    private int[][] ReverseRows(int[][] matrix)
    {
        // 行を逆順にする
        int[][] reversedMatrix = new int[matrix.Length][];
        for (int i = 0; i < matrix.Length; i++)
        {
            reversedMatrix[i] = matrix[matrix.Length - 1 - i];
        }
        return reversedMatrix;
    }

    public override string ExecuteMain()
    {
        if (replacedMatrix == null || replacedMatrix.Length == 0)
        {
            Debug.LogError("Replaced Matrix is not initialized.");
            return "Error";
        }

        // マトリックスを処理
        int[][] matrix = CopyJaggedArray(replacedMatrix);

        // 列数が奇数なら列を追加
        if (matrix[0].Length % 2 != 0)
        {
            matrix = AddColumnWithNegative13ToTheLeft(matrix);
        }

        int loopPoint = matrix[0].Length / 2; // 処理回数
        int colPoint = -1; // 初期の列インデックス

        int[][] tempNewList2D = new int[0][];

        // 右から2列ずつ処理
        for (int j = 0; j < loopPoint; j++)
        {
            int[][] oneTimeList2D = new int[matrix.Length][];

            // 各行の該当列を取得
            for (int i = 0; i < matrix.Length; i++)
            {
                int rowIndex = matrix.Length - 1 - i; // 下から順に行を取得
                int[] row = matrix[rowIndex];
                oneTimeList2D[i] = new int[] { row[colPoint - 1], row[colPoint] }; // 2列分追加
            }

            colPoint -= 2; // 次の列へ

            // 偶数回目で行を反転
            if (j % 2 == 0)
            {
                oneTimeList2D = ReverseRows(oneTimeList2D);
            }

            // 新しいジャグ配列を作成してマージ
            tempNewList2D = MergeJaggedArrays(oneTimeList2D, tempNewList2D);
        }

        // 処理結果を保持
        newList2D = tempNewList2D;

        Debug.Log("ColumnSplitterConcatPlayer processing completed.");
        return "Completed";
    }

    private int[][] CopyJaggedArray(int[][] source)
    {
        // ジャグ配列の深いコピーを作成
        int[][] copy = new int[source.Length][];
        for (int i = 0; i < source.Length; i++)
        {
            copy[i] = new int[source[i].Length];
            for (int j = 0; j < source[i].Length; j++)
            {
                copy[i][j] = source[i][j];
            }
        }
        return copy;
    }

    private int[][] MergeJaggedArrays(int[][] array1, int[][] array2)
    {
        // ジャグ配列をマージ
        int[][] mergedArray = new int[array1.Length + array2.Length][];
        int index = 0;
        for (int i = 0; i < array1.Length; i++)
        {
            mergedArray[index++] = array1[i];
        }
        for (int i = 0; i < array2.Length; i++)
        {
            mergedArray[index++] = array2[i];
        }
        return mergedArray;
    }
}
