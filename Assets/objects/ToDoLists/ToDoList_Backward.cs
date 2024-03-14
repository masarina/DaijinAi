using UdonSharp;
using UnityEngine;

public class ToDoList_Backward : UdonSharpBehaviour
{
    public EmbeddingLayer ob_EmbeddingLayer;
    public LayerNormalization ob_LayerNormalization;
    public AttentionWeightLayer ob_AttentionWeightLayer;
    public WeightSumLayer ob_WeightSumLayer;
    public SwishAffineLayer ov_SwishAffineLayer;
    public SikpAddLayer ob_SkipAddLayer;
    public SoftmaxWithLossLayer ob_SoftmaxWithLossLayer;
    
    // 省略

    public void ToDoStep(int stepID)
    {
        // 実行したいstepIDが入力されるので、それに伴い各々実行する。
        if (stepID == 0)
        {
            ob_SoftmaxWithLossLayer.Backward()
        }

        else if (stepID == 1)
        {
            ob_LayerNormalization.Backward()
        }
        
        else if (stepID == 2)
        {
            ob_SwishAffineLayer.Backward()
        }
        
        else if (stepID == 3)
        {
            ob_LayerNormalization.Backward()
        }
        
        else if (stepID == 4)
        {
            ob_WeightSumLayer.Backward()
        }
        
        else if (stepID == 5
        {
            ob_AttentionWeightLayer.Backward()
        }
        
        else if (stepID == 5)
        {
            ob_SkipAddLayer.Backward()
        }
        
        else if (stepID == 6)
        {
            ob_LayerNormalization.Backward()
        }
        
        else if (stepID == 7)
        {
            ob_EmbeddingLayer.Backward()
        }
        
        else
        {
            Debug.log("BackwardのstepIDが不自然です")
        }
    }

}
