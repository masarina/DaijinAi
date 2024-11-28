import numpy as np

class AffineLayer:
    def __init__(self, initial_weights, initial_bias):
        """
        初期化
        :param initial_weights: 重み (2DリストまたはNumPy配列)
        :param initial_bias: バイアス (1DリストまたはNumPy配列)
        """
        self.weights = np.array(initial_weights)  # 重み
        self.bias = np.array(initial_bias)  # バイアス
        self.x_array = None  # 入力
        self.y_array = None  # 出力

    def forward(self, input_data):
        """
        Forward処理: Wx + b を計算
        :param input_data: 入力 (1DリストまたはNumPy配列)
        :return: 出力 (1D NumPy配列)
        """
        self.x_array = np.array(input_data)
        self.y_array = np.dot(self.weights, self.x_array) + self.bias
        return self.y_array

    def backward(self, dout):
        """
        Backward処理: 勾配の計算
        :param dout: 出力側からの誤差勾配 (1DリストまたはNumPy配列)
        :return: dx (入力側への誤差勾配)
        """
        dout = np.array(dout)
        
        # 重みの勾配 (dW)
        dW = np.outer(dout, self.x_array)  # 各doutに対してxArrayを掛ける

        # バイアスの勾配 (db)
        db = np.copy(dout)  # doutそのままコピー

        # 入力に対する誤差 (dx)
        dx = np.dot(self.weights.T, dout)  # 重み行列の転置を使用

        # 必要に応じてdW, dbを外部で利用可能
        self.dW = dW
        self.db = db

        return dx
