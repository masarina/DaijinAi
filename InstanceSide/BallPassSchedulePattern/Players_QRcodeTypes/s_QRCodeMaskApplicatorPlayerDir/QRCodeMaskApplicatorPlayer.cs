using UdonSharp;
using UnityEngine;

public class QRCodeMaskApplicatorPlayer : SuperPlayer
{
    [SerializeField] private int[][] qrMap2DList;  // QRコードの2Dリスト
    [SerializeField] private int[][] updatedQrMap2DList;  // 更新済みのQRコードマップ
    [SerializeField] private RinaNumpy rinaNumpy;  // RinaNumpyをアタッチ

    public override string ReturnMyName()
    {
        return "QRCodeMaskApplicatorPlayer";  // クラス名を返す
    }

    public int[][] ApplyMask(int[][] matrix, string maskBit, int i, int j)
    {
        // 指定された maskBit に基づき (i, j) のビットを反転する
        if (rinaNumpy == null)
        {
            Debug.LogError("RinaNumpy is not assigned.");
            return matrix;  // rinaNumpyが設定されていない場合は変更しない
        }

        float[] maskValues = rinaNumpy.ConvertToFloatArrayFromBitString(maskBit);

        // 各mask_bit条件を評価し、ビットを反転
        if (maskValues[0] == 0 && (i + j) % 2 == 0)
        {
            matrix[i][j] = 1 - matrix[i][j];
        }
        else if (maskValues[1] == 0 && i % 2 == 0)
        {
            matrix[i][j] = 1 - matrix[i][j];
        }
        else if (maskValues[2] == 0 && j % 3 == 0)
        {
            matrix[i][j] = 1 - matrix[i][j];
        }
        // 他の条件もrinaNumpyと統合可能
        return matrix;
    }

    public override void ExecuteMain()
    {
        if (rinaNumpy == null)
        {
            Debug.LogError("RinaNumpy is not assigned. Please attach it in the inspector.");
            return;
        }

        // Unityエディタで設定された2Dリストを取得
        int[][] matrix = updatedQrMap2DList;

        // マスクビットを「000」に固定
        string maskBit = "000";

        // マトリックスにマスクを適用
        for (int i = 0; i < matrix.Length; i++)
        {
            for (int j = 0; j < matrix[i].Length; j++)
            {
                matrix = ApplyMask(matrix, maskBit, i, j);
            }
        }

        // RinaNumpyで行列を操作する例
        float meanValue = rinaNumpy.Mean_FloatArray(rinaNumpy.ConvertToFloatArray(matrix));

        Debug.Log($"Mean value of QR matrix: {meanValue}");

        // 結果を更新
        qrMap2DList = matrix;
    }
}
