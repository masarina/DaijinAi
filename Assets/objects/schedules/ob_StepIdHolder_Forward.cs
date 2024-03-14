using UdonSharp;
using UnityEngine;

public class StepIdHolder_Forward : UdonSharpBehaviour
{
    public int intData;

    public void WriteIntData(int newData)
    {
        this.intData = newData;
    }

    public void ReadIntData()
    {
        return this.intData;
    }
}