using UdonSharp;
using UnityEngine;

public class ParamsPlayer : SuperPlayer
{
    public RinaNumpy rinaNumpy;
    public string myName;
    public InitAiTypesPlayer initAiTypesPlayer;
    int XSize = initAiTypesPlayer.XSize; //仮
    int LayerSize = initAiTypesPlayer.LayerSize; //仮
    int ParamsSize = initAiTypesPlayer.ParamsSize; // 重み、バイアス、ベータ値であれば、3とかかな。
    int[] Shape = {XSize, LayerSize, ParamsSize}
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
