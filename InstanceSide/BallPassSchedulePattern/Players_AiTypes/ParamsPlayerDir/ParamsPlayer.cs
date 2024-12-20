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
    public int LayerParamsSize; // LayerがParamsに保持してよい行数（3くらいかな）


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

    public int ResultIndexOfParamsSave(
        int PositionIndex, // 自身のポジションIndex
        int LayerIndex, // EmbeddingLayerから数えて自分が何層目のLayerなのか。
    )

    // 戻値：このポジションが保存すべきParamsのIndexsの最初の数値
    // ▶︎今回1レイヤ当たり3行の空データを提供している。その3つのインデックスの内の最初のインデックスを返す。
    {
        return (PositionIndex * (this.AllParams.Length / this.LayerParamsSize)) + (this.LayerParamsSize + LayerIndex);
    }

    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // 必要な処理を記述する
        return "Completed";
    }
}
