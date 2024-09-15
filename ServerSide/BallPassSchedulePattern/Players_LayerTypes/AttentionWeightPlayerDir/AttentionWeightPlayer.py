import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class AttentionWeightPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_query = None  # クエリ入力
        self.input_key = None  # キー入力
        self.input_value = None  # バリュー入力
        self.output_attention_weights = None  # アテンション重み
        self.output_result = None  # アテンション出力
        self.mode = "forward"  # 'forward' か 'backward' を設定
        self.grad_output = None  # 出力に対する勾配（backwardで使用）
        self.grad_query = None  # クエリに対する勾配
        self.grad_key = None  # キーに対する勾配
        self.grad_value = None  # バリューに対する勾配

    def return_my_name(self):
        return "AttentionWeightPlayer"

    def main(self):
        """
        メイン処理：モードに応じてフォワードまたはバックワードを実行
        """
        if self.mode == "forward":
            # forwardを実行し、アテンションの重みと出力を得る
            self.output_attention_weights, self.output_result = self.forward(self.input_query, self.input_key, self.input_value)
            print(f"Forward Result: {self.output_result}")
        elif self.mode == "backward":
            # backwardを実行し、勾配計算を行う
            self.backward()

        return "Completed"

    def forward(self, query, key, value):
        """
        Forwardパス：バッチ対応のクエリ、キー、バリューからアテンション重みと出力を計算する流れ。
        """
        # 1. クエリとキーの内積を計算してアテンションスコアを得る
        #    バッチ処理対応で、クエリ(query)とキー(key)を掛け算してスコアを計算。transposeでキーの次元を調整している。
        attention_scores = np.matmul(query, key.transpose(0, 2, 1))

        # 2. スコアにソフトマックスを適用して正規化（確率化）し、アテンション重みを得る
        attention_weights = self.softmax(attention_scores)

        # 3. 得られたアテンション重みをバリュー(value)に掛け算して、アテンション出力を計算
        attention_output = np.matmul(attention_weights, value)
        return attention_weights, attention_output

    def backward(self):
        """
        Backwardパス：アテンションの勾配を計算する流れ。
        """
        # 1. 出力の勾配を使って、バリューに関する勾配を計算
        #    アテンション重みの転置行列と勾配を掛けて、バリューに対する勾配を求める
        self.grad_value = np.matmul(self.output_attention_weights.transpose(0, 2, 1), self.grad_output)

        # 2. アテンション重みに関する勾配を計算
        #    勾配とバリューの転置を掛け算して、アテンション重みの勾配を求める
        grad_attention_weights = np.matmul(self.grad_output, self.input_value.transpose(0, 2, 1))

        # 3. アテンションスコアに関する勾配を計算
        #    アテンション重みの勾配を元に、ソフトマックスの微分を考慮してスコアの勾配を求める
        grad_attention_scores = grad_attention_weights * self.output_attention_weights * (1 - self.output_attention_weights)

        # 4. クエリに関する勾配を計算
        #    スコアの勾配とキーを掛け算して、クエリに対する勾配を求める
        self.grad_query = np.matmul(grad_attention_scores, self.input_key)

        # 5. キーに関する勾配を計算
        #    スコアの勾配の転置とクエリを掛け算して、キーに対する勾配を求める
        self.grad_key = np.matmul(grad_attention_scores.transpose(0, 2, 1), self.input_query)

        print(f"Backward pass completed. Grad Query: {self.grad_query}, Grad Key: {self.grad_key}, Grad Value: {self.grad_value}")

    def softmax(self, x):
        """
        ソフトマックス関数：バッチ対応の入力スコアを正規化して確率に変換する。
        スコアが大きすぎないように最大値を引いてから、eの指数を取って正規化。
        """
        e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return e_x / e_x.sum(axis=-1, keepdims=True)
