import numpy as np

class SkipAddLayer:
    def forward(self, x1, x2):
        """
        順伝播: 2つの入力配列を要素ごとに加算します。
        :param x1: 入力1 (NumPy配列)
        :param x2: 入力2 (NumPy配列)
        :return: 加算結果 (NumPy配列)
        """
        if x1.shape != x2.shape:
            raise ValueError("Input arrays must have the same shape.")
        
        return x1 + x2  # NumPyの要素ごとの加算

    def backward(self, dout):
        """
        逆伝播: 加算レイヤの勾配はそのまま伝播されます。
        :param dout: 外部から受け取った勾配 (NumPy配列)
        :return: 勾配のリスト [dout, dout]
        """
        # 加算レイヤでは、入力それぞれに同じ勾配を伝播
        return [dout, dout]
