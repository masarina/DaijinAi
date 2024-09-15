import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class CrossEntropyErrorPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_predictions = None  # 予測データ（Softmaxの出力）
        self.input_labels = None  # 正解ラベル（ターゲットID）
        self.output_loss = None  # クロスエントロピー誤差
        self.grad_input = None  # 入力に対する勾配

    def return_my_name(self):
        return "CrossEntropyErrorPlayer"

    def main(self):
        """
        モードに応じてフォワードまたはバックワードを実行
        """
        if self.mode == "forward":
            self.output_loss = self.forward(self.input_predictions, self.input_labels)
            print(f"Loss: {self.output_loss}")
        elif self.mode == "backward":
            self.grad_input = self.backward(self.input_predictions, self.input_labels)
            print(f"Backward Grad: {self.grad_input}")

        return "Completed"

    def forward(self, predictions, labels):
        """
        Forwardパス：クロスエントロピー誤差を計算（バッチ処理対応）
        
        - predictions: モデルがSoftmaxを通じて出力した語彙全体の確率分布
        - labels: 正解の単語のID（インデックス）
        
        Transformerにおける正解ラベルは、モデルが予測すべき単語のID（語彙のインデックス）です。
        これをSoftmaxの出力と比較して、正解単語に対応する位置の誤差を計算します。
        Embedding層の単語ベクトルそのものではなく、ターゲットとなる単語のIDが用いられます。
        """
        self.input_predictions = predictions
        self.input_labels = labels
        # 予測の対数を取る（log(0)を防ぐために微小な値を追加）
        log_predictions = np.log(predictions + 1e-7)
        # 正解ラベルとのクロスエントロピー誤差を計算
        # ラベルはone-hotエンコーディングされていると想定
        cross_entropy_loss = -np.sum(labels * log_predictions, axis=-1)
        # バッチの平均を取る
        return np.mean(cross_entropy_loss)

    def backward(self, predictions, labels):
        """
        Backwardパス：クロスエントロピー誤差の勾配を計算（バッチ処理対応）
        
        - predictions: モデルのSoftmax出力（予測確率分布）
        - labels: 正解の単語のID（one-hot表現）
        
        Backwardでは、予測とラベルの差を使って、Softmaxの出力に対する勾配を計算します。
        勾配は、正解単語に関しては予測が高くなるよう、間違った単語に対しては予測が低くなるように調整されます。
        """
        self.input_predictions = predictions
        self.input_labels = labels
        # 勾配計算：予測からラベルを引いたもの
        grad_input = (predictions - labels) / predictions.shape[0]
        return grad_input
