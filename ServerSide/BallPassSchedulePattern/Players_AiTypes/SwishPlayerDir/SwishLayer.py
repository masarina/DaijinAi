import numpy as np

class SwishLayer:
    def __init__(self, beta=1.0):
        """
        SwishLayerの初期化
        :param beta: 学習可能なパラメータ (初期値は1.0)
        """
        self.beta = beta  # 学習可能なパラメータ
        self.x_array = None  # forward時の入力
        self.out_array = None  # forward時の出力
        self.dbeta = 0.0  # betaに関する勾配

    def forward(self, x):
        """
        Forward処理
        :param x: 入力 (NumPy配列)
        :return: 出力 (Swishの計算結果)
        """
        self.x_array = x
        beta_x = self.beta * x
        sigmoid_beta_x = 1 / (1 + np.exp(-beta_x))  # Sigmoid(beta * x)
        self.out_array = x * sigmoid_beta_x  # Swish(x) = x * sigmoid(beta * x)
        return self.out_array

    def backward(self, dout):
        """
        Backward処理
        :param dout: 出力に対する勾配 (NumPy配列)
        :return: dx: 入力に対する勾配
        """
        dx = np.zeros_like(dout)  # 入力に関する勾配
        dbeta = 0.0  # betaに関する勾配をリセット

        for i in range(len(dout)):
            x = self.x_array[i]
            e_beta_x = np.exp(-self.beta * x)  # e^(-beta * x)
            sigma = 1 / (1 + e_beta_x)  # Sigmoid(beta * x)

            # Swish関数の導関数
            sigma_prime = sigma + self.beta * x * sigma * (1 - sigma)  # sigma' = sigma + beta * x * sigma * (1 - sigma)

            # dx: 出力に関する勾配(dout)とSwish導関数の積
            dx[i] = dout[i] * sigma_prime

            # betaに関する勾配
            f_x = x * sigma  # Swish(x)
            df_dbeta = x * sigma * (1 - sigma)  # x * sigma' = x * sigma * (1 - sigma)
            dbeta += dout[i] * f_x * df_dbeta

        # dbetaを平均化
        self.dbeta = dbeta / len(dout)

        return dx
