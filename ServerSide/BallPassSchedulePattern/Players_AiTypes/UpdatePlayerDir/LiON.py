import numpy as np

class LiON:
    def __init__(self):
        # パラメータ
        self.alpha = 0.01  # 初期学習率
        self.beta = 0.9  # モーメント項の減衰率
        self.threshold = 1.0  # スケールダウンのしきい値
        self.scaling_factor = 0.9  # スケールダウン係数
        self.min_learning_rate = 0.001  # 最小学習率
        self.max_learning_rate = 0.05  # 最大学習率
        self.scale_factor = 0.1  # 学習率の調整係数
        self.scale_boost_beta = 0.05  # スケールダウン時の学習率増加係数
        self.dropout_rate = 0.2  # ドロップアウト率（20%のユニットを無効化）

        # 内部状態
        self.v = None  # モーメントベクトル
        self.layer_learning_rates = None  # レイヤごとの学習率

    # 初期化メソッド
    def initialize(self, parameter_size):
        """ パラメータサイズに応じた初期化 """
        self.v = np.zeros(parameter_size)  # モーメントベクトルをゼロ初期化
        self.layer_learning_rates = np.full(parameter_size, self.alpha)  # 各レイヤの初期学習率を設定

    # ドロップアウトマスク生成
    def generate_dropout_mask(self, size):
        """ ドロップアウトマスクを生成 """
        return np.random.rand(size) >= self.dropout_rate

    # モーメント更新ロジック
    def update_momentum(self, current_momentum, gradient):
        """ モーメントを更新 """
        return self.beta * current_momentum + (1 - self.beta) * gradient

    # 学習率調整ロジック
    def adjust_learning_rate(self, current_rate, gradient):
        """ 学習率を調整 """
        avg_change = abs(gradient)
        adjusted_rate = current_rate + self.scale_factor * avg_change
        return np.clip(adjusted_rate, self.min_learning_rate, self.max_learning_rate)

    # 重み更新メソッド
    def update_weights(self, weights, gradients):
        """
        重みと勾配を受け取り、更新後の重みを返す
        weights: 重み配列
        gradients: 勾配配列
        """
        if self.v is None or len(self.v) != len(weights):
            raise ValueError("LiONが初期化されていない、またはパラメータサイズが一致しません。")

        # ドロップアウトマスク生成
        dropout_mask = self.generate_dropout_mask(len(weights))

        # 重み更新処理
        for i in range(len(weights)):
            if not dropout_mask[i]:
                continue  # ドロップアウト対象のユニットはスキップ

            # 1. モーメント更新
            self.v[i] = self.update_momentum(self.v[i], gradients[i])

            # 2. スケールダウン（必要に応じて学習率調整）
            if abs(self.v[i]) > self.threshold:
                self.v[i] *= self.scaling_factor
                self.layer_learning_rates[i] += self.scale_boost_beta

            # 3. 学習率調整
            self.layer_learning_rates[i] = self.adjust_learning_rate(self.layer_learning_rates[i], gradients[i])

            # 4. 重みの更新
            weights[i] -= self.layer_learning_rates[i] * np.sign(self.v[i])

            # 5. 重みスケールダウン
            if abs(weights[i]) > self.threshold:
                weights[i] *= self.scaling_factor
                self.layer_learning_rates[i] += self.scale_boost_beta

        return weights
