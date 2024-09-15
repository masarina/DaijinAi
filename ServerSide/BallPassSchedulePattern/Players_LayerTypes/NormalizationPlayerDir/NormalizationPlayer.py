import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class NormalizationPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_data = None  # 入力データを保持
        self.output_data = None  # 出力データを保持
        self.mean = None  # 平均値
        self.variance = None  # 分散
        self.epsilon = 1e-8  # 安定化のための小さな値

    def return_my_name(self):
        return "NormalizationPlayer"

    def forward(self, input_data):
        """
        Forwardパス：正規化処理を順番に計算する
        """
        self.input_data = input_data
        
        # Step 1: 平均を計算
        self.mean = np.mean(self.input_data, axis=0)
        print(f"Step 1: Mean = {self.mean}")

        # Step 2: 入力データから平均を引く
        centered_data = self.input_data - self.mean
        print(f"Step 2: Centered Data = {centered_data}")

        # Step 3: 分散を計算
        self.variance = np.var(centered_data, axis=0)
        print(f"Step 3: Variance = {self.variance}")

        # Step 4: 標準偏差を計算する（公式を使う）
        stddev = (self.variance + self.epsilon) ** 0.5  # 標準偏差を公式で計算
        print(f"Step 4: Standard Deviation = {stddev}")

        # Step 5: 正規化（平均を引いて標準偏差で割る）
        self.output_data = centered_data / stddev
        print(f"Step 5: Normalized Data = {self.output_data}")

        return self.output_data

    def backward(self, grad_output):
        """
        Backwardパス：順番に勾配を計算する
        """
        N, D = self.input_data.shape

        # Step 1: 分散の勾配を計算
        centered_data = self.input_data - self.mean
        grad_variance = np.sum(grad_output * centered_data * -0.5 * (self.variance + self.epsilon)**(-1.5), axis=0)
        print(f"Step 1: Gradient of Variance = {grad_variance}")

        # Step 2: 標準偏差の勾配を計算
        grad_stddev = grad_output / (self.variance + self.epsilon) ** 0.5
        print(f"Step 2: Gradient of Standard Deviation = {grad_stddev}")

        # Step 3: 中心化データの勾配を計算
        grad_centered_data = grad_stddev
        print(f"Step 3: Gradient of Centered Data = {grad_centered_data}")

        # Step 4: 入力データの勾配を計算
        grad_input = grad_centered_data + (2.0 / N) * centered_data * grad_variance
        print(f"Step 4: Gradient of Input Data = {grad_input}")

        # Step 5: 平均の勾配を計算してから、最終的な勾配を計算
        grad_mean = np.sum(grad_centered_data * -1.0, axis=0)
        grad_input += (1.0 / N) * grad_mean
        print(f"Step 5: Gradient of Mean = {grad_mean}")
        print(f"Step 5: Final Gradient of Input Data = {grad_input}")

        return grad_input
