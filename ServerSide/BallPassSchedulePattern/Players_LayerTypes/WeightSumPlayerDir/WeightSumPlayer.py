import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class WeightSumPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_attention_weights = None  # アテンション重み（注意の重み付け）
        self.input_values = None  # 値（バリュー、処理対象のデータ）
        self.output_weighted_sum = None  # 重み付けされた出力結果
        self.mode = "forward"  # 'forward'か'backward'を設定
        self.grad_output = None  # 出力に対する勾配（backwardで使用）
        self.grad_attention_weights = None  # アテンション重みに対する勾配
        self.grad_values = None  # バリューに対する勾配

    def return_my_name(self):
        return "WeightSumPlayer"

    def main(self):
        """
        メイン処理：モードに応じてフォワードまたはバックワードを実行
        """
        if self.mode == "forward":
            # Forward処理を呼び出し、アテンション重みとバリューから重み付き和を計算
            self.output_weighted_sum = self.forward(self.input_attention_weights, self.input_values)
            print(f"Forward Result: {self.output_weighted_sum}")
        elif self.mode == "backward":
            # Backward処理を呼び出して勾配を計算
            self.backward()

        return "Completed"

    def forward(self, attention_weights, values):
        """
        Forwardパス：アテンション重みとバリューを用いて重み付きの和を計算
        """
        # バッチ処理対応。attention_weights（バッチサイズ×シーケンス長×シーケンス長）と
        # values（バッチサイズ×シーケンス長×ベクトルサイズ）の行列積を計算
        # 各重み付けされたバリューを加算してweighted_sumを得る
        weighted_sum = np.matmul(attention_weights, values)
        return weighted_sum

    def backward(self):
        """
        Backwardパス：バリューとアテンション重みに関する勾配計算
        """
        # grad_output（出力の勾配）を用いて、バリューの勾配を計算
        # attention_weightsの転置を掛けることで、valuesに関する勾配を求める
        self.grad_values = np.matmul(self.input_attention_weights.transpose(0, 2, 1), self.grad_output)

        # grad_outputを用いて、アテンション重みに対する勾配を計算
        # valuesの転置を掛けることで、attention_weightsに関する勾配を求める
        self.grad_attention_weights = np.matmul(self.grad_output, self.input_values.transpose(0, 2, 1))

        print(f"Backward pass completed. Grad Attention Weights: {self.grad_attention_weights}, Grad Values: {self.grad_values}")
