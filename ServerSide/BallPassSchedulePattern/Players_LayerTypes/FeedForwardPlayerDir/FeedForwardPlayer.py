import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class FeedForwardPlayer(SuperPlayer):
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        super().__init__()
        self.my_name = None
        self.input_data = None  # 入力データ
        self.output_data = None  # 出力データ
        self.hidden_data = None  # 中間層データ
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)  # 入力層→中間層の重み
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)  # 中間層→出力層の重み
        self.bias_hidden = np.zeros(hidden_size)  # 中間層のバイアス
        self.bias_output = np.zeros(output_size)  # 出力層のバイアス
        self.learning_rate = learning_rate  # 学習率

    def return_my_name(self):
        return "FeedForwardPlayer"

    def forward(self, input_data):
        """
        Forwardパス：データを前方に伝播させる
        """
        self.input_data = input_data
        # 中間層計算（入力データ x 重み + バイアス）
        self.hidden_data = np.dot(self.input_data, self.weights_input_hidden) + self.bias_hidden
        # 活性化関数（ReLU）を適用
        self.hidden_data = np.maximum(0, self.hidden_data)
        print(f"Hidden Layer Output: {self.hidden_data}")
        
        # 出力層計算（中間層データ x 重み + バイアス）
        self.output_data = np.dot(self.hidden_data, self.weights_hidden_output) + self.bias_output
        print(f"Output Layer Output: {self.output_data}")

        return self.output_data

    def backward(self, grad_output):
        """
        Backwardパス：勾配を伝播させる
        """
        # 出力層→中間層の勾配
        grad_weights_hidden_output = np.dot(self.hidden_data.T, grad_output)
        grad_bias_output = np.sum(grad_output, axis=0)
        grad_hidden = np.dot(grad_output, self.weights_hidden_output.T)

        # ReLUの勾配計算
        grad_hidden[self.hidden_data <= 0] = 0

        # 中間層→入力層の勾配
        grad_weights_input_hidden = np.dot(self.input_data.T, grad_hidden)
        grad_bias_hidden = np.sum(grad_hidden, axis=0)

        # 重みとバイアスの更新
        self.weights_hidden_output -= self.learning_rate * grad_weights_hidden_output
        self.bias_output -= self.learning_rate * grad_bias_output
        self.weights_input_hidden -= self.learning_rate * grad_weights_input_hidden
        self.bias_hidden -= self.learning_rate * grad_bias_hidden

        print(f"Grad Weights Hidden-Output: {grad_weights_hidden_output}")
        print(f"Grad Bias Output: {grad_bias_output}")
        print(f"Grad Weights Input-Hidden: {grad_weights_input_hidden}")
        print(f"Grad Bias Hidden: {grad_bias_hidden}")

        return grad_hidden
