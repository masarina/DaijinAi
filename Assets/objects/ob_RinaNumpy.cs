using UdonSharp;
using UnityEngine;

public class RinaNumpy : UdonSharpBehaviour
{
    //
    public static float Sum_FloatArray(float[] x) {
        float sum = 0;
        foreach (float value in x) {
            sum += value;
        }
        return sum;
    }
    
    //
    public static float[] Divide_FloatArray_Float(float[] x, float y) {
        float epsilon = 1e-6f; // ゼロ除算を避けるための小さな値
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] / (y + epsilon); // イプシロンを追加してゼロ除算を避ける
        }
        return result;
    }
    
    //
    public static float[] Subtract_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] - y;
        }
        return result;
    }
    
    //
    public static float[] Multiply_FloatArray_FloatArray(float[] x, float[] y) {
        if (x.Length != y.Length) throw new System.ArgumentException("Arrays must be of equal length.");
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] * y[i];
        }
        return result;
    }
    
    //
    public static float[] Multiply_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] * y;
        }
        return result;
    }
    
    //
    public static float[] Add_FloatArray_FloatArray(float[] x, float[] y) {
        if (x.Length != y.Length) throw new System.ArgumentException("Arrays must be of equal length.");
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] + y[i];
        }
        return result;
    }
    
    //
    public static float[] OnesLike_FloatArray(float[] x) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = 1;
        }
        return result;
    }
    
    //
    public static float[] ZerosLike_FloatArray(float[] x) {
        return new float[x.Length]; // Default initialization to 0
    }
    

    //
    public static float[] Negative_FloatArray(float[] x) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = -x[i];
        }
        return result;
    }
    
    //
    public static float DotProduct_FloatArray_FloatArray(float[] x, float[] y)
    {
        if (x.Length != y.Length) throw new System.ArgumentException("Arrays must be of equal length for dot product.");
        
        float result = 0;
        for (int i = 0; i < x.Length; i++)
        {
            result += x[i] * y[i];
        }
        return result;
    }

    //
    public static float[] DotProduct_FloatArray2D_FloatArray(float[][] A, float[] x)
    {
        if (A[0].Length != x.Length) throw new System.ArgumentException("Matrix columns and vector size must match for dot product.");

        float[] result = new float[A.Length];
        for (int i = 0; i < A.Length; i++)
        {
            for (int j = 0; j < x.Length; j++)
            {
                result[i] += A[i][j] * x[j];
            }
        }
        return result;
    }
    
    //
    public static float Mean_FloatArray(float[] x) 
    {
        float sum = 0; // 全要素の合計値を保持する変数
        foreach (float value in x) 
        {
            sum += value; // 配列xの各要素を合計に加える
        }
        return sum / x.Length; // 合計を要素数で割って平均値を求める
    }
    
    //
    public static float Mean(float[] x)
    {
        float sum = 0f;
        foreach (float value in x)
        {
            sum += value; // 配列の各要素を合計
        }
        return sum / x.Length; // 合計を要素数で割って平均を求める
    }
    
    public static float Std_FloatArray(float[] x)
    {
        float mean = Mean(x); // まず配列xの平均値を計算
        float sumOfSquares = 0f; // 差の二乗の合計を初期化
        foreach (float value in x)
        {
            sumOfSquares += Mathf.Pow(value - mean, 2); // 各値と平均との差の二乗を加算
        }
        float variance = sumOfSquares / x.Length; // 分散は差の二乗の合計を要素数で割ったもの
        return Mathf.Sqrt(variance); // 分散の平方根が標準偏差
    }
    
    public static float[] Power_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = Mathf.Pow(x[i], y);
        }
        return result;
    }
    
    public static float[] Sum_FloatArray2d_Float_axis0(float[][] x)
    {
        float[] sum = new float[x[0].Length];
        for (int i = 0; i < x.Length; i++)
        {
            for (int j = 0; j < x[i].Length; j++)
            {
                sum[j] += x[i][j];
            }
        }
        return sum;
    }
    
    public static float[] Sum_FloatArray2d_FloatArray2d_axis1(float[][] x)
    {
        float[] sum = new float[x.Length];
        for (int i = 0; i < x.Length; i++)
        {
            for (int j = 0; j < x[i].Length; j++)
            {
                sum[i] += x[i][j];
            }
        }
        return sum;
    }
    
    public static float[] Sum_FloatArray2d_Float_axis0(float[][] x)
    {
        if (x.Length == 0 || x[0].Length == 0) return new float[0]; // 空の配列の場合は空の配列を返す
    
        float[] sum = new float[x[0].Length]; // 列の数だけ要素を持つ配列を初期化
        for (int i = 0; i < x.Length; i++) // 行のループ
        {
            for (int j = 0; j < x[i].Length; j++) // 列のループ
            {
                sum[j] += x[i][j]; // 各列の要素を足し合わせる
            }
        }
        return sum;
    }
    
    // 分散を計算するためのヘルパーメソッド
    public float Var_FloatArray(float[] x, float mean)
    {
        float sumOfSquares = 0f;
        foreach (float value in x)
        {
            sumOfSquares += Mathf.Pow(value - mean, 2);
        }
        return sumOfSquares / x.Length;
    }
    
    public static float Std_FloatArray(float[] x) {
        float mean = Mean_FloatArray(x); // 平均値の計算
        float sumOfSquares = 0f;
        for (int i = 0; i < x.Length; i++) {
            sumOfSquares += Mathf.Pow(x[i] - mean, 2); // 各要素から平均を引いて、二乗
        }
        return Mathf.Sqrt(sumOfSquares / x.Length); // その平均の平方根を取る
    }
            
}
