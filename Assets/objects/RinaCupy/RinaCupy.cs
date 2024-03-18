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
        sumArrayComputeShader.Dispatch(kernelHandle, 1, 1, 1);

        // 結果の取得
        float[] result = new float[1];
        resultBuffer.GetData(result);
        resultBuffer.Release(); // リソースの解放

        // Texture2Dのリソースも解放
        Destroy(inputTexture);

        return result[0];
    }
}
