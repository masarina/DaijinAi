import numpy as np

class SoftmaxLayer:
    def __init__(self):
        """
        初期化メソッド
        """
        self.cache_exp_x = None  # Softmax計算の中間値 (指数の値)
        self.cache_sum = None    # 指数の合計
        self.last_output = None  # Softmaxの出力 (Forwardの結果をキャッシュ)

    def forward(self, x):
        """
        Forward計算: Softmaxを適用
        :param x: 入力データ (1D NumPy配列)
        :return: Softmaxの出力 (1D NumPy配列)
        """
        # オーバーフロー対策のため、入力の最大値を取得して引く
        max_val = np.max(x)

        # 指数を計算
        self.cache_exp_x = np.exp(x - max_val)  # オーバーフロー防止
        self.cache_sum = np.sum(self.cache_exp_x)  # 指数の合計

        # Softmax出力を計算
        y = self.cache_exp_x / self.cache_sum

        # 結果をキャッシュ
        self.last_output = y

        return y

    def backward(self, dout):
        """
        Backward計算: Softmaxの勾配
        :param dout: 出力側からの勾配 (1D NumPy配列)
        :return: 入力に対する勾配 (1D NumPy配列)
        """
        # doutの合計を計算
        dout_sum = np.sum(dout)

        # 入力に対する勾配を計算
        dx = self.cache_exp_x * (dout - dout_sum / self.cache_sum)

        return dx

    def get_params(self):
        """
        キャッシュされたSoftmaxの出力を返す
        :return: Softmaxの出力 (1D NumPy配列)
        """
        return self.last_output

    def set_params(self, parameters):
        """
        キャッシュにパラメータを設定
        :param parameters: 設定するパラメータ (1D NumPy配列)
        """
        self.last_output = np.array(parameters)
