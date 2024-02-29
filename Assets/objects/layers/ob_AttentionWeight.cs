using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class AttentionWeight : UdonSharpBehaviour
{
    public SoftmaxLayer softmaxLayer; // この部分は、インスペクタからSoftmaxLayerをアタッチする
    private float[][] hs;
    private float[] h;
    private float[][] cacheHs;
    private float[] cacheHr;

    public float[] Forward(float[][] hsInput, float[] hInput)
    {
        hs = hsInput;
        h = hInput;
        int T = hs.Length;
        int H = hs[0].Length;
        float[] hr = new float[H];
        h.CopyTo(hr, 0);
        float[] s = new float[T];
        for (int i = 0; i < T; i++)
        {
            for (int j = 0; j < H; j++)
            {
                s[i] += hs[i][j] * hr[j];
            }
        }
        float[] a = softmaxLayer.Forward(s);
        cacheHs = hs;
        cacheHr = hr;
        return a;
    }

    public float[][] Backward(float[] da)
    {
        int T = cacheHs.Length;
        int H = cacheHs[0].Length;
        float[] ds = softmaxLayer.Backward(da);
        float[][] dhs = new float[T][];
        float[] dh = new float[H];
        for (int i = 0; i < T; i++)
        {
            dhs[i] = new float[H];
            for (int j = 0; j < H; j++)
            {
                dhs[i][j] += ds[i] * cacheHr[j];
                dh[j] += ds[i] * cacheHs[i][j];
            }
        }
        return new float[][] { dhs, dh };
    }
}
