using UdonSharp;
using UnityEngine;

public class RinaCupy : UdonSharpBehaviour
{
    public ComputeShader sumArrayComputeShader; // Sum_FloatArray計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float Sum_FloatArray_GPU(float[] x) {
        // Texture2Dの作成
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        // データをTextureに設定
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = sumArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(1, sizeof(float), ComputeBufferType.Default);
        sumArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        sumArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        
                
        // Compute Shaderの実行
        int dataCount = x.Length; // xは入力データの配列
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)dataCount / threadsPerGroup); // 必要なグループ数を計算
        
        sumArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し
                
                
        // 結果の取得
        float[] result = new float[1];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture);

        return result[0];
    }
    

    public ComputeShader divideArrayComputeShader; // Divide_FloatArray_Float計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float[] Divide_FloatArray_GPU(float[] x, float divisor) {
        // Texture2Dの作成とデータの設定
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply();

        // Compute Shaderのセットアップ
        int kernelHandle = divideArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer outputBuffer = new ComputeBuffer(x.Length, sizeof(float), ComputeBufferType.Default);
        divideArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        divideArrayComputeShader.SetBuffer(kernelHandle, "OutputArray", outputBuffer);
        divideArrayComputeShader.SetFloat("Divisor", divisor);
        
        // Compute Shaderの実行
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        divideArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);
        
        // 結果の取得
        float[] result = new float[x.Length];
        outputBuffer.GetData(result);
        outputBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture);

        return result;
    }
    
    public ComputeShader subtractArrayComputeShader; // 上で作成したComputeShader

    public float[] Subtract_FloatArray_Float_GPU(float[] x, float subtractValue) 
    {
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply();

        int kernelHandle = subtractArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(x.Length, sizeof(float));
        subtractArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        subtractArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        subtractArrayComputeShader.SetFloat("SubtractValue", subtractValue);

        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        subtractArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);

        float[] result = new float[x.Length];
        resultBuffer.GetData(result);
        resultBuffer.Release();

        Destroy(inputTexture);

        return result;
    }
    
    public ComputeShader multiplyArrayComputeShader; // Compute Shaderをアタッチ。

    public float[] Multiply_FloatArray_FloatArray_GPU(float[] x, float[] y) {
        // Texture2Dの作成
        Texture2D inputTexture1 = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        Texture2D inputTexture2 = new Texture2D(y.Length, 1, TextureFormat.RFloat, false);
        // データをTextureに設定
        for (int i = 0; i < x.Length; i++) {
            inputTexture1.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
            inputTexture2.SetPixel(i, 0, new Color(y[i], 0, 0, 0));
        }
        inputTexture1.Apply(); // データのアップロードを確定
        inputTexture2.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = multiplyArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(x.Length, sizeof(float), ComputeBufferType.Default);
        multiplyArrayComputeShader.SetTexture(kernelHandle, "InputArray1", inputTexture1);
        multiplyArrayComputeShader.SetTexture(kernelHandle, "InputArray2", inputTexture2);
        multiplyArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
                
        // Compute Shaderの実行
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        multiplyArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);
                
        // 結果の取得
        float[] result = new float[x.Length];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture1);
        Destroy(inputTexture2);

        return result;
    }
    
    
    public ComputeShader multiplyArrayComputeShader; // Multiply_FloatArray_Float計算がHLSLで書かれたCompute Shaderをアタッチ。
    
    public float[] Multiply_FloatArray_Float_GPU(float[] x, float multiplyValue) {
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply();
    
        int kernelHandle = multiplyArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(x.Length, sizeof(float));
        multiplyArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        multiplyArrayComputeShader.SetFloat("MultiplyValue", multiplyValue);
        multiplyArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
    
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        multiplyArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);
    
        float[] result = new float[x.Length];
        resultBuffer.GetData(result);
        resultBuffer.Release();
    
        Destroy(inputTexture);
    
        return result;
    }
    
    public ComputeShader addArrayComputeShader; // Add_FloatArray_FloatArray計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float[] Add_FloatArray_FloatArray_GPU(float[] x, float[] y) {
        // Texture2Dの作成
        Texture2D inputTexture1 = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        Texture2D inputTexture2 = new Texture2D(y.Length, 1, TextureFormat.RFloat, false);

        // データをTextureに設定
        for (int i = 0; i < x.Length; i++) {
            inputTexture1.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture1.Apply(); // データのアップロードを確定

        for (int i = 0; i < y.Length; i++) {
            inputTexture2.SetPixel(i, 0, new Color(y[i], 0, 0, 0));
        }
        inputTexture2.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = addArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(x.Length, sizeof(float), ComputeBufferType.Default);
        addArrayComputeShader.SetTexture(kernelHandle, "InputArray1", inputTexture1);
        addArrayComputeShader.SetTexture(kernelHandle, "InputArray2", inputTexture2);
        addArrayComputeShader.SetBuffer(kernelHandle, "ResultArray", resultBuffer);

        // Compute Shaderの実行
        int dataCount = x.Length; // xは入力データの配列
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)dataCount / threadsPerGroup); // 必要なグループ数を計算

        addArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し

        // 結果の取得
        float[] result = new float[dataCount];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture1);
        Destroy(inputTexture2);

        return result;
    }
    
    public ComputeShader onesLikeArrayComputeShader; // OnesLike_FloatArray計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float[] OnesLike_FloatArray_GPU(int arrayLength) {
        // Compute Shaderのセットアップ
        int kernelHandle = onesLikeArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(arrayLength, sizeof(float), ComputeBufferType.Default);
        onesLikeArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        
        // Compute Shaderの実行
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)arrayLength / threadsPerGroup); // 必要なグループ数を計算
        
        onesLikeArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し
                
        // 結果の取得
        float[] result = new float[arrayLength];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        return result;
    }
    
    public float[] ZerosLike_FloatArray_GPU(int length) {
        // Compute Shaderのセットアップ
        int kernelHandle = sumArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(length, sizeof(float), ComputeBufferType.Default); // 長さがlengthのバッファを作成
        sumArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        
        // Compute Shaderの実行
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)length / threadsPerGroup); // 必要なグループ数を計算
        
        sumArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し
        
        // 結果の取得
        float[] result = new float[length];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放
    
        return result;
    }
        

    public ComputeShader negativeArrayComputeShader; // Negative_FloatArray用のCompute Shaderをアタッチ。

    public float[] Negative_FloatArray_GPU(float[] x) {
        // Texture2Dの作成
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        // データをTextureに設定
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = negativeArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(x.Length, sizeof(float), ComputeBufferType.Default);
        negativeArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        negativeArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);

        // Compute Shaderの実行
        int dataCount = x.Length;
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)dataCount / threadsPerGroup);
        negativeArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);

        // 結果の取得
        float[] result = new float[x.Length];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture);

        return result;
    }
    
    public ComputeShader sumArrayComputeShader; // Sum_FloatArray用のCompute Shader
    public ComputeShader dotProductComputeShader; // DotProduct_FloatArray_FloatArray用のCompute Shader

    public float DotProduct_FloatArray_FloatArray_GPU(float[] x, float[] y) {
        // Texture2Dの作成と設定
        Texture2D inputTextureA = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        Texture2D inputTextureB = new Texture2D(y.Length, 1, TextureFormat.RFloat, false);
        
        for (int i = 0; i < x.Length; i++) {
            inputTextureA.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
            inputTextureB.SetPixel(i, 0, new Color(y[i], 0, 0, 0));
        }
        inputTextureA.Apply(); // データのアップロードを確定
        inputTextureB.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = dotProductComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(1, sizeof(float), ComputeBufferType.Default);
        dotProductComputeShader.SetTexture(kernelHandle, "InputArrayA", inputTextureA);
        dotProductComputeShader.SetTexture(kernelHandle, "InputArrayB", inputTextureB);
        dotProductComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);

        // Compute Shaderの実行
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup); // 必要なグループ数を計算
        dotProductComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し

        // 結果の取得
        float[] result = new float[1];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTextureA);
        Destroy(inputTextureB);

        return result[0];
    }
    
    
    public ComputeShader dotProductComputeShader; // DotProduct_FloatArray2D_FloatArray計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float[] DotProduct_FloatArray2D_FloatArray_GPU(float[][] matrix, float[] vector) {
        // 行列とベクトルのTexture2Dを作成
        int matrixWidth = matrix[0].Length;
        int matrixHeight = matrix.Length;
        Texture2D inputMatrixTexture = new Texture2D(matrixWidth, matrixHeight, TextureFormat.RFloat, false);
        Texture2D inputVectorTexture = new Texture2D(vector.Length, 1, TextureFormat.RFloat, false);
        
        // データをTextureに設定
        for (int i = 0; i < matrixHeight; i++) {
            for (int j = 0; j < matrixWidth; j++) {
                inputMatrixTexture.SetPixel(j, i, new Color(matrix[i][j], 0, 0, 0));
            }
        }
        inputMatrixTexture.Apply(); // データのアップロードを確定

        for (int i = 0; i < vector.Length; i++) {
            inputVectorTexture.SetPixel(i, 0, new Color(vector[i], 0, 0, 0));
        }
        inputVectorTexture.Apply(); // データのアップロードを確定

        // Compute Shaderのセットアップ
        int kernelHandle = dotProductComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(matrixHeight, sizeof(float), ComputeBufferType.Default);
        dotProductComputeShader.SetTexture(kernelHandle, "InputMatrix", inputMatrixTexture);
        dotProductComputeShader.SetTexture(kernelHandle, "InputVector", inputVectorTexture);
        dotProductComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);

        // Compute Shaderの実行
        int threadsPerGroup = 1024; // Compute Shaderで設定した[numthreads(1024, 1, 1)]のX値
        int groupCount = Mathf.CeilToInt((float)matrixHeight / threadsPerGroup); // 必要なグループ数を計算
        dotProductComputeShader.Dispatch(kernelHandle, groupCount, 1, 1); // 必要なグループ数でDispatchを呼び出し

        // 結果の取得
        float[] result = new float[matrixHeight];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputMatrixTexture);
        Destroy(inputVectorTexture);

        return result;
    }
    
    public ComputeShader meanArrayComputeShader; // Mean_FloatArray計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float Mean_FloatArray_GPU(float[] x) {
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply();

        int kernelHandle = meanArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(1, sizeof(float), ComputeBufferType.Default);
        meanArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        meanArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        
        meanArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);
                
        float[] result = new float[1];
        resultBuffer.GetData(result);
        resultBuffer.Release();

        Destroy(inputTexture);

        return result[0];
    }
    
    public ComputeShader meanArrayComputeShader; // Mean計算がHLSLで書かれたCompute Shaderをアタッチ。

    public float Mean_GPU(float[] x) {
        Texture2D inputTexture = new Texture2D(x.Length, 1, TextureFormat.RFloat, false);
        for (int i = 0; i < x.Length; i++) {
            inputTexture.SetPixel(i, 0, new Color(x[i], 0, 0, 0));
        }
        inputTexture.Apply();

        int kernelHandle = meanArrayComputeShader.FindKernel("CSMain");
        ComputeBuffer resultBuffer = new ComputeBuffer(1, sizeof(float), ComputeBufferType.Default);
        meanArrayComputeShader.SetTexture(kernelHandle, "InputArray", inputTexture);
        meanArrayComputeShader.SetBuffer(kernelHandle, "Result", resultBuffer);
        
        int threadsPerGroup = 1024;
        int groupCount = Mathf.CeilToInt((float)x.Length / threadsPerGroup);
        
        meanArrayComputeShader.Dispatch(kernelHandle, groupCount, 1, 1);
                
        float[] result = new float[1];
        resultBuffer.GetData(result);
        resultBuffer.Release();

        Destroy(inputTexture);

        return result[0];
    }
    
    
}
