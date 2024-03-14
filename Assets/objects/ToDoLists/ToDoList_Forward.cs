using UdonSharp;
using UnityEngine;

public class ToDoList_Forward : UdonSharpBehaviour
{
    public EmbeddingLayer ob_EmbeddingLayer;
    public LayerNormalization ob_LayerNormalization;
    // 省略

    public void ToDoStep(int stepID)
    {
        // 実行したいstepIDが入力されるので、それに伴い各々実行する。
        if (stepID == 0)
        {
            ob_EmbeddingLayer.Forward()
        }

        else if (stepID == 1)
        {
            ob_LayerNormalization.Forward()
        }
        // 省略
    }

}