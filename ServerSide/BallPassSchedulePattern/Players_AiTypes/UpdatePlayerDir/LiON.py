import numpy as np

class LiON:
    def __init__(self, alpha=0.01, beta=0.9):
        """
        LiONアップデートの初期化
        :param alpha: 学習率 (デフォルト: 0.01)
        :param beta: モーメント項の減衰率 (デフォルト: 0.9)
        """
        self.alpha = alpha  # 学習率
        self.beta = beta    # モーメント係数
        self.v = None       # モーメントベクトル

    def initialize(self, parameter_size):
        """
        モーメントベクトルを初期化
        :param parameter_size: 更新するパラメータの数
        """
        self.v = np.zeros(parameter_size)

    def update_weights(self, w, dw):
        """
        LiONによる重み更新
        :param w: 現在の重み (NumPy配列)
        :param dw: 重みに対する勾配 (NumPy配列)
        :return: 更新された重み (NumPy配列)
        """
        if self.v is None or len(self.v) != len(w):
            raise ValueError("LiONUpdater not initialized or parameter size mismatch.")

        # モーメントの更新
        self.v = self.beta * self.v + (1 - self.beta) * dw

        # 重みの更新
        w -= self.alpha * np.sign(self.v)

        return w
