using UdonSharp;
using UnityEngine;

public class ToDoList_Forward : UdonSharpBehaviour
{
    public EmbeddingLayer ob_EmbeddingLayer;
    public LayerNormalization ob_LayerNormalization;
    public AttentionWeightLayer ob-AttentionWeightLayer;
    public WeightSumLayer ob_WeightSumLayer;
    public SwishAffineLayer ov_SwishAffineLayer;
    public SikpAddLayer ob_SkipAddLayer;
    public SoftmaxWithLossLayer ob_SoftmaxWithLossLayer;
    
    // 省略

    public void ToDoStep(int stepID)
    {
        // 実行したいstepIDが入力されるので、それに伴い各々実行する。
        if (stepID == 0)
        {
            ob_EmbeddingLayer.Forward()
        }

        else if (stepID == 1)
        {
            ob_LayerNormalization.Forward()
        }
        
        else if (stepID == 2)
        {
            ob_AttentionWeightLayer.Forward()
        }
        
        else if (stepID == 3)
        {
            ob_WeightSumLayer.Forward()
        }
        
        else if (stepID == 4)
        {
            ob_LayerNormalization.Forward()
        }
        
        else if (stepID == 5
        {
            ob_SwishAffineLayer.Forward()
        }
        
        else if (stepID == 5)
        {
            ob_LayerNormalization.Forward()
        }
        
        else if (stepID == 6)
        {
            ob_SkipAddLayer.Forward()
        }
        
        else if (stepID == 7)
        {
            ob_SoftmaxWithLossLayer()
        }
        
        else
        {
            Debug.log("ForwardのstepIDが不自然です")
        }
    }

}