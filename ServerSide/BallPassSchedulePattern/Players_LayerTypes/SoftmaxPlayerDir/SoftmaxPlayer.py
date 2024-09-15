import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class SoftmaxPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_data = None  # 入力データ
        self.output_data = None  # 出力データ（Softmax適用後）
        self.grad_output = None  # 出力に対する勾配
        self.grad_input = None  # 入力に対する勾配
        self.mode = "forward"  # 'forward'か'backward'を設定

    def return_my_name(self):
        return "SoftmaxPlayer"

    def main(self):
        """
        モードに応じてフォワードまたはバックワードを実行
        """
        if self.mode == "forward":
            self.output_data = self.forward(self.input_data)
            print(f"Forward Result: {self.output_data}")
        elif self.mode == "backward":
            self.grad_input = self.backward(self.grad_output)
            print(f"Backward Result: {self.grad_input}")

        return "Completed"

    def forward(self, input_data):
        """
        Forwardパス：Softmaxをバッチ処理で適用
        """
        self.input_data = input_data
        # 入力データの最大値を引いてオーバーフローを防ぐ
        input_shifted = input_data - np.max(input_data, axis=-1, keepdims=True)
        # Softmaxの計算：指数関数を計算し、各行で正規化
        exp_data = np.exp(input_shifted)
        softmax_output = exp_data / np.sum(exp_data, axis=-1, keepdims=True)
        return softmax_output

    def backward(self, grad_output):
        """
        Backwardパス：Softmaxの勾配をバッチ処理で計算
        """
        self.grad_output = grad_output
        # Softmaxの勾配を計算する（ここでは簡略化して、ダイレクトな方法で実装）
        grad_input = self.output_data * (grad_output - np.sum(grad_output * self.output_data, axis=-1, keepdims=True))
        return grad_input
