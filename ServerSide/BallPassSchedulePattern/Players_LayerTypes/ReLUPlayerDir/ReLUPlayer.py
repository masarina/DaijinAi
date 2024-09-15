import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class ReLUPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_data = None  # 入力データ
        self.output_data = None  # 出力データ（ReLU適用後）
        self.grad_output = None  # 出力に対する勾配
        self.grad_input = None  # 入力に対する勾配
        self.mode = "forward"  # 'forward' か 'backward' を設定

    def return_my_name(self):
        return "ReLUPlayer"

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
        Forwardパス：ReLUをバッチ対応で適用
        """
        self.input_data = input_data
        # ReLU関数：バッチ対応で0以下の値を0に、それ以外はそのまま返す
        return np.maximum(0, input_data)

    def backward(self, grad_output):
        """
        Backwardパス：ReLUの勾配をバッチ対応で計算
        """
        self.grad_output = grad_output
        # ReLUの勾配：入力が0より大きいバッチに対して、勾配をそのまま通し、0以下なら勾配も0にする
        grad_input = grad_output * (self.input_data > 0).astype(float)
        return grad_input
