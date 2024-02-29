using UdonSharp;
using UnityEngine;
using RinaNumpy; // これは想定されたRinaNumpyクラスを使用するためのもの

public class LayerNormalizationSingle : UdonSharpBehaviour
{
    [SerializeField]
    private float epsilon = 1e-6f; // ゼロ除算エラーを避けるための小さな値
    private float[] gamma; // スケールパラメータ、後で学習
    private float[] beta; // シフトパラメータ、後で学習
    private float[] xNormalized; // backwardで使用するため、保持。

    // 平均を計算する関数
    private float ComputeMean(float[] x)
    {
        return RinaNumpy.Mean(x);
    }

    // 標準偏差を計算する関数
    private float ComputeStd(float[] x)
    {
        return RinaNumpy.Std(x);
    }

    // 正規化を行う関数
    private float[] Normalize(float[] x, float mean, float std)
    {
        return RinaNumpy.Divide(RinaNumpy.Subtract(x, mean), std + epsilon);
    }

    // ハダマード積算を行う関数(スケーリング)
    private float[] Scale(float[] xNormalized)
    {
        if (gamma == null)
        {
            gamma = RinaNumpy.OnesLike(xNormalized); // gammaを1で初期化
        }
        return RinaNumpy.Multiply(gamma, xNormalized);
    }

    // beta加算(シフト)を行う関数
    private float[] Shift(float[] xScaled)
    {
        if (beta == null)
        {
            beta = RinaNumpy.ZerosLike(xScaled); // betaを0で初期化
        }
        return RinaNumpy.Add(xScaled, beta);
    }

    // forward処理
    public float[] Forward(float[] x)
    {
        float mean = ComputeMean(x);
        float std = ComputeStd(x);
        xNormalized = Normalize(x, mean, std); // ここでクラス変数に保存
        float[] xScaled = Scale(xNormalized);
        return Shift(xScaled);
    }
    
    // backward処理
    public float[] Backward(float[] dout)
    {
        float mean = ComputeMean(dout);
        
        float std = ComputeStd(dout);
        
        float[] dxNormalized = ComputeDxNormalized(dout, gamma);
        
        float[] dmean = ComputeDmean(dxNormalized, std);
        
        float[] dstd = ComputeDstd(dxNormalized, dout, mean, std);
        
        float[] Dgamma = ComputeDgamma(xNormalized,dout);
        
        float[] Dbeta = ComputeDbeta(dout);
        
        return ComputeDx(dout, dxNormalized, dmean, dstd, mean, std);
    }

    // 正規化されたデータの勾配を計算する関数
    private float[] ComputeDxNormalized(float[] dout, float[] gamma)
    {
        return RinaNumpy.Multiply(dout, gamma);
    }

    // データの平均に関する勾配を計算する関数
    private float[] ComputeDmean(float[] dxNormalized, float std)
    {
        float[] dmean = RinaNumpy.Sum(dxNormalized, axis: 0);
        return RinaNumpy.Negative(RinaNumpy.Divide(dmean, std + epsilon));
    }

    // データの標準偏差に関する勾配を計算する関数
    private float[] ComputeDstd(float[] dxNormalized, float[] dout, float mean, float std)
    {
        float[] dstd = RinaNumpy.Sum(RinaNumpy.Multiply(dxNormalized, RinaNumpy.Subtract(dout, mean)), axis: 0);
        dstd = RinaNumpy.Negative(RinaNumpy.Divide(dstd, (std + epsilon) * (std + epsilon)));
        return RinaNumpy.Multiply(dstd, std);
    }

    // Dgammaの計算
    private float[] ComputeDgamma(float[] xNormalized, float[] dout)
    {
        return RinaNumpy.Mean(RinaNumpy.Multiply(xNormalized, dout), axis: 0);
    }
    
    // Dbetaの計算
    private float[] ComputeDbeta(float[] dout)
    {
        return RinaNumpy.Sum(dout, axis: 0);
    }

    // 入力データに関する勾配を計算する関数
    private float[] ComputeDx(float[] dout, float[] dxNormalized, float[] dmean, float[] dstd, float mean, float std)
    {
        int N = dout.Length;
        float[] dx1 = RinaNumpy.Divide(dxNormalized, std + epsilon);
        float[] dx2 = RinaNumpy.Multiply(dmean, RinaNumpy.Ones(N) / N);
        float[] dx3 = RinaNumpy.Multiply(dstd, RinaNumpy.Multiply(RinaNumpy.Subtract(dout, mean), 2) / N);
        return RinaNumpy.Add(RinaNumpy.Add(dx1, dx2), dx3);
    }
}
