using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class WeightSum : UdonSharpBehaviour
{
    private float[][] hs;
    private float[] a;
    private float[][] cacheHs;
    private float[] cacheA;

    public float[] Forward(float[][] hsInput, float[] aInput)
    {
        hs = hsInput;
        a = aInput;
        int T = hs.Length;
        int H = hs[0].Length;
        float[] c = new float[H];
        for (int i = 0; i < T; i++)
        {
            for (int j = 0; j < H; j++)
            {
                c[j] += hs[i][j] * a[i];
            }
        }
        cacheHs = hs;
        cacheA = a;
        return c;
    }

    public float[][] Backward(float[] dc)
    {
        int T = cacheHs.Length;
        int H = cacheHs[0].Length;
        float[][] dhs = new float[T][];
        for (int i = 0; i < T; i++)
        {
            dhs[i] = new float[H];
            for (int j = 0; j < H; j++)
            {
                dhs[i][j] = dc[j] * cacheA[i];
            }
        }
        float[] da = new float[T];
        for (int i = 0; i < T; i++)
        {
            for (int j = 0; j < H; j++)
            {
                da[i] += dc[j] * cacheHs[i][j];
            }
        }
        return new float[][] { dhs, da };
    }
}
