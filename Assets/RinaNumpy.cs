using UdonSharp;
using UnityEngine;

public class RinaNumpy : UdonSharpBehaviour
{
    public static float Mean_FloatArray(float[] x) 
    {
        float sum = 0;
        foreach (float value in x) 
        {
            sum += value;
        }
        return sum / x.Length;
    }
    
    public static float Std_FloatArray(float[] x) {
        float mean = Mean_FloatArray(x);
        float sumOfSquares = 0;
        foreach (float value in x) {
            sumOfSquares += (value - mean) * (value - mean);
        }
        return Mathf.Sqrt(sumOfSquares / x.Length);
    }
    
    public static float[] Divide_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] / y;
        }
        return result;
    }
    
    public static float[] Subtract_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] - y;
        }
        return result;
    }
    
    public static float[] Multiply_FloatArray_FloatArray(float[] x, float[] y) {
        if (x.Length != y.Length) throw new System.ArgumentException("Arrays must be of equal length.");
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] * y[i];
        }
        return result;
    }
    
    public static float[] Multiply_FloatArray_Float(float[] x, float y) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] * y;
        }
        return result;
    }
    
    public static float[] Add_FloatArray_FloatArray(float[] x, float[] y) {
        if (x.Length != y.Length) throw new System.ArgumentException("Arrays must be of equal length.");
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = x[i] + y[i];
        }
        return result;
    }
    
    public static float[] OnesLike_FloatArray(float[] x) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = 1;
        }
        return result;
    }
    
    public static float[] ZerosLike_FloatArray(float[] x) {
        return new float[x.Length]; // Default initialization to 0
    }
    
    public static float Sum_FloatArray(float[] x) {
        float sum = 0;
        foreach (float value in x) {
            sum += value;
        }
        return sum;
    }
        
    public static float[] Negative_FloatArray(float[] x) {
        float[] result = new float[x.Length];
        for (int i = 0; i < x.Length; i++) {
            result[i] = -x[i];
        }
        return result;
    }
}
