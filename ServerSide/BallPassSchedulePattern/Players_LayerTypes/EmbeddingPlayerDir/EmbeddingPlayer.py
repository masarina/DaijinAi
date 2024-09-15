import numpy as np
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class EmbeddingPlayer(SuperPlayer):
    def __init__(self, vocab_size, word_vec_size):
        super().__init__()
        self.my_name = None
        self.input_ids = []  # 入力IDデータ
        self.output_word_vectors = []  # 出力単語ベクトル
        self.word_vec_size = word_vec_size  # 単語ベクトルのサイズ
        self.vocab_size = vocab_size  # 語彙サイズ
        self.weights = np.random.randn(vocab_size, word_vec_size)  # Embeddingの重み（ランダム初期化）

    def return_my_name(self):
        return "EmbeddingPlayer"

    def forward(self, input_ids):
        """
        Forwardパス：バッチ対応の入力IDデータから単語ベクトルを取得
        バッチサイズに対応するため、2次元の入力IDリストを想定
        """
        self.input_ids = input_ids
        # バッチ処理対応。各バッチのIDに対応するベクトルを取得
        self.output_word_vectors = np.array([self.weights[batch] for batch in input_ids])
        return self.output_word_vectors

    def backward(self, grad_output):
        """
        Backwardパス：バッチ処理対応。勾配の伝播
        バッチサイズに対応して、各バッチの勾配を計算
        """
        grad_weights = np.zeros_like(self.weights)
        for batch_idx, batch in enumerate(self.input_ids):
            for i, input_id in enumerate(batch):
                grad_weights[input_id] += grad_output[batch_idx][i]  # 各バッチ、各IDに対応する重みの勾配を計算
        return grad_weights

    def update_weights(self, grad_weights, learning_rate):
        """
        重みの更新を行う
        """
        self.weights -= learning_rate * grad_weights  # 重みの更新
