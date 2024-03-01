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
    
    private float[] xMinusMean; // 「x - mean」の計算結果を保持する変数

    // 平均を計算する関数
    private float ComputeMean(float[] x)
    {
        return RinaNumpy.Mean_FloatArray(x);
    }

    // 標準偏差を計算する関数
    private float ComputeStd(float[] x)
    {
        return RinaNumpy.Std_FloatArray(x);
    }

    // 正規化を行う関数
    private float[] Normalize(float[] x, float mean, float std)
    {
        return RinaNumpy.Divide_FloatArray_Float(RinaNumpy.Subtract(x, mean), std + epsilon);
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
        return RinaNumpy.Add_FloatArray_FloatArray(xScaled, beta);
    }

    // forward処理
    public float[] Forward(float[] x)
    {
        float mean = ComputeMean(x);
        float std = ComputeStd(x);
        xNormalized = Normalize(x, mean, std); // ここでクラス変数に保存
        xMinusMean = RinaNumpy.Subtract(x, mean); //「x - mean」の計算と保持(backwardで使用)
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
        // 入力データの勾配dxNormalizedの平均を計算
        float dmean = RinaNumpy.Mean_FloatArray(dxNormalized);
        // 平均勾配をすべてのデータポイントに適用
        // ここでstdを扱う形式にRinaNumpyメソッドを更新する。
        return RinaNumpy.Multiply(RinaNumpy.Ones(dxNormalized.Length), dmean);
    }
    
    // データの標準偏差に関する勾配を計算する関数(確実に合っています。崩すな。)
    private float[] ComputeDstd(float[] dxNormalized, float[] dout, float mean, float std)
    {
        float[] diff = RinaNumpy.Subtract(dout, mean);
        float[] grad = RinaNumpy.Multiply(dxNormalized, diff);
        float dstd = RinaNumpy.Sum_FloatArray2d_Float_axis0(grad);
        dstd = -0.5f * RinaNumpy.Power_FloatArray_Float(std + epsilon, -1.5f) * dstd;
    
        // dstdのスカラー値を元の配列のサイズに合わせた配列として返す
        float[] dstdArray = RinaNumpy.Multiply(RinaNumpy.Ones(dout.Length), dstd);
        return dstdArray;
    }

    // Dgammaの計算
    private float[] ComputeDgamma(float[] xNormalized, float[] dout)
    {
        return RinaNumpy.Mean_FloatArray(RinaNumpy.Multiply(xNormalized, dout), axis: 0);
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
        
        // dx1: 正規化されたデータの勾配と標準偏差の逆数を用いて計算
        float[] dx1 = RinaNumpy.Divide_FloatArray_Float(dxNormalized, std + epsilon);
        
        // dx2: 平均に関する勾配を全データポイントに均等に分配
        float[] dx2 = RinaNumpy.Multiply(dmean, RinaNumpy.Ones(N) / N);
        
        // dx3の計算では、x - meanによる偏差を2倍し、dstdによるスケーリングを行い、Nで割る
        float[] dx3 = RinaNumpy.Multiply(dstd, RinaNumpy.Multiply(xMinusMean, 2) / N);
    
        // 最終的な勾配dxは、dx1, dx2, dx3の和として計算される
        return RinaNumpy.Add_FloatArray_FloatArray(RinaNumpy.Add_FloatArray_FloatArray(dx1, dx2), dx3);
    }
}
