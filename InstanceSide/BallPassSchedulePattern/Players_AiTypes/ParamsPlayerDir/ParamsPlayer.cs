using UdonSharp;
using UnityEngine;

public class ParamsPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;
    public string myName;
    public InitAiTypesPlayer initAiTypesPlayer;
    public float[][][][] = rinaNumpy.
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool AffinePlayerReset()
    {
        myName = "AffinePlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "ParamsPlayer";
    }

    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {


        return "Completed";
    }
}
