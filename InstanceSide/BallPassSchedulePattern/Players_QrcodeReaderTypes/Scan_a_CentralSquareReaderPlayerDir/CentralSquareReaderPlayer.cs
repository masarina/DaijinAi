using UdonSharp;
using UnityEngine;

public class CentralSquareReaderPlayer : SuperPlayer
{
    [Tooltip("QRコード画像が設定されたマテリアル")]
    public Material qrCodeMaterial; // QRコード画像が設定されたマテリアルをアタッチ

    public int[][] binaryMatrix2DList; // QRコードの2次元リスト
    public string pngFilePath; // 画像のパス（今回は利用しないが保持）

    [Tooltip("RinaNumpyをアタッチしてください")]
    public RinaNumpy rinaNumpy; // RinaNumpyインスタンスをアタッチ

    void Start()
    {
        ResetPlayer(); // プレイヤーの初期化
    }

    public void ResetPlayer()
    {
        myName = "CentralSquareReaderPlayer"; // プレイヤー名を設定
        binaryMatrix2DList = new int[0][]; // 初期化
        pngFilePath = ""; // 初期化
    }

    public override string ReturnMyName()
    {
        return "CentralSquareReaderPlayer";
    }

    public int[][] ExtractCentralSquare(Texture2D texture, int rP = 80)
    {
        // テクスチャの横幅と縦幅を取得
        int textureWidth = texture.width;
        int textureHeight = texture.height;

        // 短辺の長さとそのインデックスを取得 (RinaNumpyを使用)
        int smallSideIndex = rinaNumpy.SmallSideIndexCatcher(textureWidth, textureHeight);
        int smallSideSize = smallSideIndex == 0 ? textureWidth : textureHeight;

        // 中央部分のサイズを計算
        int squareSize = (smallSideSize * rP) / 100;

        // 中央座標を計算 (RinaNumpyのメソッドで置き換え)
        int[] centerCoords = new int[] { textureWidth / 2, textureHeight / 2 };

        // 正方形の左上座標を計算
        int startX = centerCoords[0] - (squareSize / 2);
        int startY = centerCoords[1] - (squareSize / 2);

        // 中央部分のデータを保持するジャグ配列を初期化
        int[][] centralSquare = new int[squareSize][];
        for (int i = 0; i < squareSize; i++)
        {
            centralSquare[i] = new int[squareSize];
        }

        // テクスチャからデータを取得して中央部分を抽出
        Color[] pixels = texture.GetPixels(startX, startY, squareSize, squareSize);

        for (int y = 0; y < squareSize; y++)
        {
            for (int x = 0; x < squareSize; x++)
            {
                // 色を二値化 (白:1, 黒:0)
                centralSquare[y][x] = rinaNumpy.Negative_FloatArray(
                    new float[] { pixels[y * squareSize + x].grayscale > 0.5f ? 1 : 0 })[0];
            }
        }

        return centralSquare;
    }

    public override string ExecuteMain()
    {
        if (qrCodeMaterial == null)
        {
            Debug.LogError("QRコードのマテリアルがアタッチされていません。");
            return "Error";
        }

        if (rinaNumpy == null)
        {
            Debug.LogError("RinaNumpyがアタッチされていません。");
            return "Error";
        }

        // マテリアルからテクスチャを取得
        Texture2D qrTexture = qrCodeMaterial.mainTexture as Texture2D;
        if (qrTexture == null)
        {
            Debug.LogError("QRコードのマテリアルに適切なテクスチャが設定されていません。");
            return "Error";
        }

        // 中央80%部分の正方形を取得
        binaryMatrix2DList = ExtractCentralSquare(qrTexture, 80);

        Debug.Log("CentralSquareReaderPlayer processing completed.");
        return "Completed";
    }
}
