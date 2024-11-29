import numpy as np

class LiONWithScaling:
    def __init__(self, alpha=0.01, beta=0.9, threshold=1.0, scaling_factor=0.9):
        """
        スケールダウンを組み込んだLiONアップデート
        :param alpha: 学習率 (デフォルト: 0.01)
        :param beta: モーメント項の減衰率 (デフォルト: 0.9)
        :param threshold: スケールダウンのしきい値 (デフォルト: 1.0)
        :param scaling_factor: スケールダウン係数 (デフォルト: 0.9)
        """
        self.alpha = alpha  # 学習率
        self.beta = beta    # モーメント係数
        self.threshold = threshold  # スケールダウンのしきい値
        self.scaling_factor = scaling_factor  # スケールダウン係数
        self.v = None       # モーメントベクトル

    def initialize(self, parameter_size):
        """
        モーメントベクトルを初期化
        :param parameter_size: 更新するパラメータの数
        """
        self.v = np.zeros(parameter_size)

    def update_weights(self, w, dw):
        """
        LiONによる重み更新（スケールダウンを考慮）
        :param w: 現在の重み (NumPy配列)
        :param dw: 重みに対する勾配 (NumPy配列)
        :return: 更新された重み (NumPy配列)
        """
        if self.v is None or len(self.v) != len(w):
            raise ValueError("LiONUpdater not initialized or parameter size mismatch.")

        # モーメントの更新
        self.v = self.beta * self.v + (1 - self.beta) * dw

        # スケールダウン: モーメントがしきい値を超えた場合
        mask_v = np.abs(self.v) > self.threshold
        self.v[mask_v] *= self.scaling_factor

        # 重みを更新
        w -= self.alpha * np.sign(self.v)

        # スケールダウン: 重みがしきい値を超えた場合
        mask_w = np.abs(w) > self.threshold
        w[mask_w] *= self.scaling_factor

        return w
