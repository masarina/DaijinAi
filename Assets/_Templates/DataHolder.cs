using UdonSharp;
using UnityEngine;

public class DataHolder : UdonSharpBehaviour
{
    public string strData;
    public float floatData;
    public float[][] floatArray2D;
    public float[][][] floatArray3D;
    public float[][][][] floatArray4D;
    public float[] floatArray;
    public int intData;
    public int[] intArray;
    public int[][] intArray2D;
    public int[][][] intArray3D;
    public int[][][][] intArray4D;

    // str型書き込みコード
    public void WriteStrData(string newData)
    {
        this.strData = newData;
    }
    
    // str型読み込みコード
    public string ReadStrData()
    {
        return this.strData;
    }
    
    // float型書き込みコード群
    public void WriteFloatData(float newData)
    {
        this.floatData = newData;
    }
    public void WriteFloatArray(float[] newData)
    {
        this.floatArray = newData;
    }
    public void WriteFloatArray2D(float[][] newData)
    {
        this.floatArray2D = newData;
    }
    public void WriteFloatArray3D(float[][][] newData)
    {
        this.floatArray3D = newData;
    }
    public void WriteFloatArray4D(float[][][][] newData)
    {
        this.floatArray4D = newData;
    }

    // float型読み込みコード群
    public float ReadFloatData()
    {
        return this.floatData;
    }
    public float[] ReadFloatArray()
    {
        return this.floatArray;
    }
    public float[][] ReadFloatArray2D()
    {
        return this.floatArray2D;
    }
    public float[][][] ReadFloatArray3D()
    {
        return this.floatArray3D;
    }
    public float[][][][] ReadFloatArray4D()
    {
        return this.floatArray4D;
    }
    
    // int型のデータを書き込むメソッド群
    public void WriteIntData(int newData)
    {
        this.intData = newData;
    }
    public void WriteIntArray(int[] newData)
    {
        this.intArray = newData;
    }
    public void WriteIntArray2D(int[][] newData)
    {
        this.intArray2D = newData;
    }
    public void WriteIntArray3D(int[][][] newData)
    {
        this.intArray3D = newData;
    }
    public void WriteIntArray4D(int[][][][] newData)
    {
        this.intArray4D = newData;
    }
    
    // int型のデータを読み込むメソッド群
    public int ReadIntData()
    {
        return this.intData;
    }
    public int[] ReadIntArray()
    {
        return this.intArray;
    }
    public int[][] ReadIntArray2D()
    {
        return this.intArray2D;
    }
    public int[][][] ReadIntArray3D()
    {
        return this.intArray3D;
    }
    public int[][][][] ReadIntArray4D()
    {
        return this.intArray4D;
    }
}
