import numpy as np

class LiON:
    """
    LiON (Layered Intelligent Optimization for Neural networks) オプティマイザの実装。
    重みの更新方法にスケールダウンやモーメントを用いる。
    """
    def __init__(self, alpha=0.01, beta=0.9, threshold=1.0, scaling_factor=0.9,
                 min_learning_rate=0.001, max_learning_rate=0.05, scale_factor=0.1,
                 scale_boost_beta=0.05, dropout_rate=0.2):
        """
        初期化メソッド。デフォルト値で各種ハイパーパラメータを設定。
        """
        self.alpha = alpha  # 初期学習率
        self.beta = beta  # モーメントの減衰率
        self.threshold = threshold  # スケールダウンのしきい値
        self.scaling_factor = scaling_factor  # スケールダウン係数
        self.min_learning_rate = min_learning_rate  # 最小学習率
        self.max_learning_rate = max_learning_rate  # 最大学習率
        self.scale_factor = scale_factor  # 学習率の調整係数
        self.scale_boost_beta = scale_boost_beta  # スケールダウン時の学習率増加係数
        self.dropout_rate = dropout_rate  # ドロップアウト率
        self.v = None  # モーメントベクトル
        self.layer_learning_rates = None  # 各レイヤの学習率

    def initialize(self, parameter_size):
        """
        モーメントベクトルとレイヤ学習率の初期化を行う。
        """
        self.v = np.zeros(parameter_size)  # モーメントベクトルを0で初期化
        self.layer_learning_rates = np.full(parameter_size, self.alpha)  # 各レイヤの学習率を初期化

    def generate_dropout_mask(self, size):
        """
        ドロップアウトのマスクを生成する。
        :param size: マスクのサイズ
        :return: ドロップアウトマスク (True: 使用, False: 無効)
        """
        return np.random.rand(size) >= self.dropout_rate  # ドロップアウト率に基づくマスクを生成

    def update_weights(self, weights, gradients):
        """
        重みを更新する。
        :param weights: 現在の重み
        :param gradients: 現在の勾配
        :return: 更新された重み
        """
        if self.v is None or len(self.v) != len(weights):
            raise ValueError("LiONOptimizer not initialized or parameter size mismatch.")

        dropout_mask = self.generate_dropout_mask(len(weights))  # ドロップアウトマスクの生成

        for i in range(len(weights)):
            if not dropout_mask[i]:
                continue  # ドロップアウト対象のユニットはスキップ

            # モーメントの更新
            self.v[i] = self.beta * self.v[i] + (1 - self.beta) * gradients[i]

            # モーメントのスケールダウン
            if abs(self.v[i]) > self.threshold:
                self.v[i] *= self.scaling_factor
                self.layer_learning_rates[i] += self.scale_boost_beta  # 学習率を増加

            # 学習率の調整
            avg_change = abs(gradients[i])  # 勾配の絶対値を平均変化量として利用
            self.layer_learning_rates[i] += self.scale_factor * avg_change

            # 学習率の範囲を制約
            self.layer_learning_rates[i] = np.clip(self.layer_learning_rates[i],
                                                   self.min_learning_rate,
                                                   self.max_learning_rate)

            # 重みの更新
            weights[i] -= self.layer_learning_rates[i] * np.sign(self.v[i])

            # 重みのスケールダウン
            if abs(weights[i]) > self.threshold:
                weights[i] *= self.scaling_factor
                self.layer_learning_rates[i] += self.scale_boost_beta  # 学習率を増加

        return weights

