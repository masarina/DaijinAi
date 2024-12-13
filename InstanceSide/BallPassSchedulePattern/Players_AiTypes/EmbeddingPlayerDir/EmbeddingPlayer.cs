// EmbeddingLayerのみ、パラメータは自分で持たせてOK.
// Forward,Backwardの入力は、ベクトルを想定します。


using UdonSharp;
using UnityEngine;

public class EmbeddingPlayer : SuperPlayer
{
    public string myName;
    
    public InitAiTypesPlayer initAiTypesPlayer;
    public EmbeddingLayer embeddingLayer;
    public AiSettingsPlayer aiSettingsPlayer;
    public RinaNumpy rinaNumpy;
    public AiFlagsPlayer aiFlagsPlayer;

    
    public float[][] W;
    public float[][] dW;
    public int[] SampleIdVer;
    public float[][] SampleVecVer; // forwardの出力用
    public float[][] dSampleVecVer; // Backwardの時、レイヤー群が、1トークン1トークンここに微分を追加していく。
    
    // 初期化メソッド (Pythonの__init__に相当)
    public bool EmbeddingPlayerReset()
    {
        // パラメータ群の初期化
        int[] Shape = {aiSettingsPlayer.VocabSize, aiSettingsPlayer.EmbeddingSize}
        this.W = this.rinaNumpy.CreateArray2d(Shape)
        this.dW = this.rinaNumpy.CreateArray2d(Shape)
        this.SampleIdVer = this.aiSettingsPlayer.SampleIdVer
        this.SampleVecVer = this.aiSettingsPlayer.SampleVecVer

        
        myName = "EmbeddingPlayer";
        return true;
    }

    // プレイヤーの名前を返すメソッド
    public override string ReturnMyName()
    {
        return "EmbeddingPlayer";
    }

    public float[] Forward(int[] ids)
    {
        // サンプル(IDタイプ)を保持
        this.SampleIdVer = ids
        
        // 全ての語彙をID化
        for (int id = 0; id < ids.Length; id += 1)
        {
            this.SampleVecVer = RinaNumpy.AppendRow_FloatArray2D(SampleVecVer, embeddingLayer.Forward(id));
        }

        return this.SampleVecVer;
    }

    public void Backward(float[][] dSampleVecVer)
    {
        Debug.Log("単語ベクトルの順番は、しっかり、Forward時と同じ並び順ですか?(確認するまで消さないで_2024-12-12)")
        
        // Sampleの単語数分ループ
        for (int RowIndex 0; RowIndex < SampleIdVer.Length; RowIndex += 1)
        {
            dW = embeddingLayer.Backward(TokenVecs, RowIndex, dW)
        }

    }
    
    // メイン処理を行うメソッド
    public override string ExecuteMain()
    {
        if (aiFlagsPlayer.TravelMode == "Forward")
        {
            // データの準備
            SampleIdVer = aiSettingsPlayer.XDataIdVer
            
            // Forwardの実行
            this.SampleVecVer = this.Forward(SampleIdVer)
            
        }
        else if (aiFlagsPlayer.TravelMode == "Backward")
        {
         
            // Backwardの実行
            this.Backward(dSampleVecVer)
            
        }
        
        
        return "Completed";
    }
    
    
}
