using UdonSharp;
using UnityEngine;

public class ParamsPlayer : SuperPlayer
{
    public float[][] AllParams;

    public RinaNumpy rinaNumpy;
    public string myName;
    public AiSettingsPlayer aiSettingsPlayer;
    public int XSize;
    public int NumberOfAllLayers; // 全てのレイヤーの数

    // 初期化メソッド (Pythonの__init__に相当)
    public bool ParamsPlayerReset()
    {
        myName = "ParamsPlayer";
        
        // aiSettingsPlayerからXSizeを取得
        XSize = aiSettingsPlayer.XSize;
        
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "ParamsPlayer";
    }

    public int[] ResultIndexOfParamsSave(
        int x, 
        int LayerIndex // EmbeddingLayerから数えて自分が何層目のLayerなのか。
    )
    // 引数：処理中のposition数
    // 戻値：このポジションが保存すべきParamsのIndexs
    {
        // 結果を格納するリストを初期化
        int[] y = new int[0]; // Pythonで言う「y = []」に同じ。

        // 保存インデックスを作成
        int[] bs = new int[]
        {
            0 + LayerIndex,
            1 + LayerIndex,
            2 + LayerIndex
        };

        // 傾き (1Layerに3つの空パラメータ付与) * (Embedding以降の全Layerの数)
        int a = aiSettingsPlayer.LayerParamsSize * aiSettingsPlayer.LayerSize;

        // 保存インデックスを計算して格納
        for (int bi = 0; bi < bs.Length; bi++)
        {
            y = rinaNumpy.Append_IntArray(y, a * x + bs[bi]); // 型に合わせてメソッドを変更
        }

        return y;
    }

    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // 必要な処理を記述する
        return "Completed";
    }
}
