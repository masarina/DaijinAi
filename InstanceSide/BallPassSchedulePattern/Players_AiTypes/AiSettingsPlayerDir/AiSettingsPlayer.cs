using UdonSharp;
using UnityEngine;

public class AiSettingsPlayer : SuperPlayer
{
    public string myName;
    public string[] Data;
    public string[] XData;
    public string[] TData;
    public int PositionSize;
    public int XSize;
    public int EmbeddingSize;
    public int NumberOfAllLayers; //全てのレイヤーの数
    public int LayersSettingsParamsSize; // 重み、バイアス、ベータ値であれば、3とかかな。
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AiSettingsPlayerReset()
    {    
        # デザインパターン用
        myName = "AiSettingsPlayer";
        
        # 本プログラム用
        XData = "半角 で 区切 った 文章";
        XData = Data.data.Substring(0, data.Length - 1); // 0から-1までをとる
        TData = Data.Substring(1); // インデックス1以降の文字列を取得
        PositionSize = XData.Length;
        XSize = PositionSize;
        NumberOfAllLayers = 1; // 100とかになると思う。最後に改良すべき。
        
        
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "AiSettingsPlayer";
    }

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        // ForwardPlayerでライブラリ的に使用するので
        // 実装今のところ不要
        return "Completed";
    }
}
