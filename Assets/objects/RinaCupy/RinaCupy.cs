    public ComputeShader subtractArrayComputeShader; // 上で作成したComputeShader

    public float[] Subtract_FloatArray_Float_GPU(float[] x, float subtractValue) {
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
