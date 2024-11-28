using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class SoftmaxLayer : UdonSharpBehaviour
{
    private float[] cacheExpX;
    private float cacheSum;

    public float[] Forward(float[] x)
    {
        float max = x[0];
        for (int i = 1; i < x.Length; i++)
        {
            if (x[i] > max)
            {
                max = x[i];
            }
        }
        
        cacheExpX = new float[x.Length];
        cacheSum = 0.0f;
        for (int i = 0; i < x.Length; i++)
        {
            cacheExpX[i] = Mathf.Exp(x[i] - max); // オーバーフロー対策
            cacheSum += cacheExpX[i];
        }

        float[] y = new float[x.Length];
        for (int i = 0; i < x.Length; i++)
        {
            y[i] = cacheExpX[i] / cacheSum;
        }

        return y;
    }

    public float[] Backward(float[] dout)
    {
        float doutSum = RinaNumpy.Sum(dout); // RinaNumpy.Sumを使ってdoutの合計を計算
        float[] dx = new float[dout.Length];
    
        for (int i = 0; i < dout.Length; i++)
        {
            dx[i] = cacheExpX[i] * (dout[i] - doutSum / cacheSum);
        }
        return dx;
    }
}
