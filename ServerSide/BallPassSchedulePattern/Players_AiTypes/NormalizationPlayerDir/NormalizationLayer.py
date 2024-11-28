import numpy as np

class NormalizationLayer:
    def __init__(self, initial_gamma, initial_beta):
        """
        初期化
        :param initial_gamma: スケールパラメータ (1DリストまたはNumPy配列)
        :param initial_beta: シフトパラメータ (1DリストまたはNumPy配列)
        """
        self.gamma = np.array(initial_gamma)
        self.beta = np.array(initial_beta)
        self.x_cache = None
        self.x_normalized_cache = None
        self.mean_cache = None
        self.std_cache = None
        self.dx = None
        self.dgamma = None
        self.dbeta = None

    def forward(self, x, epsilon=1e-5):
        """
        フォワード処理
        :param x: 入力データ (1DリストまたはNumPy配列)
        :param epsilon: 標準偏差の安定化のための小さい値
        :return: 出力データ (1D NumPy配列)
        """
        x = np.array(x)
        self.x_cache = x

        # 平均と標準偏差を計算
        self.mean_cache = np.mean(x)
        self.std_cache = np.std(x) + epsilon

        # 正規化
        self.x_normalized_cache = (x - self.mean_cache) / self.std_cache

        # gammaとbetaを適用
        out_data = self.gamma * self.x_normalized_cache + self.beta

        return out_data

    def backward(self, dout, epsilon=1e-5):
        """
        バックプロパゲーション処理
        :param dout: 出力側からの誤差 (1DリストまたはNumPy配列)
        :param epsilon: 標準偏差の安定化のための小さい値
        :return: dx (入力側への誤差勾配)
        """
        dout = np.array(dout)

        # dbetaの計算
        self.dbeta = np.sum(dout)

        # dgammaの計算
        self.dgamma = np.sum(dout * self.x_normalized_cache)

        # dx_normalizedの計算
        dx_normalized = dout * self.gamma

        # x - meanの計算
        x_minus_mean = self.x_cache - self.mean_cache

        # 標準偏差の逆数
        std_inv = 1.0 / self.std_cache

        # dx_normalizedによる標準偏差の勾配
        dstd = -np.sum(dx_normalized * x_minus_mean) * (std_inv ** 2)

        # 分散の勾配
        dvar = 0.5 * dstd / self.std_cache

        # 分散によるxの勾配
        dx_var_component = 2.0 * x_minus_mean * dvar / len(self.x_cache)

        # 平均の勾配
        dmean = -np.sum(dx_normalized) * std_inv + np.sum(dx_var_component) / len(self.x_cache)

        # dxの計算
        dx1 = dx_normalized * std_inv
        dx2 = np.ones_like(self.x_cache) * dmean / len(self.x_cache)
        self.dx = dx1 + dx2

        return self.dx
