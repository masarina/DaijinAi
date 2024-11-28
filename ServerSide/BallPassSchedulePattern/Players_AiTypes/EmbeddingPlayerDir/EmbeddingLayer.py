import numpy as np

class EmbeddingLayer:
    def __init__(self, initial_weights):
        """
        初期化
        :param initial_weights: 単語埋め込み行列（2D配列 or NumPy配列）
        """
        self.weights = np.array(initial_weights)  # 埋め込み行列
        self.gradients = np.zeros_like(self.weights)  # 勾配行列を初期化
        self.current_token_id = None  # 現在のトークンID
        self.current_dx = None  # Backwardで計算されるdx

    def forward(self, token_id):
        """
        トークンIDに対応する埋め込みベクトルを返す
        :param token_id: int, トークンID
        :return: 単語埋め込みベクトル（1D NumPy配列）
        """
        if token_id < 0 or token_id >= self.weights.shape[0]:
            raise ValueError("Invalid token_id or weights not initialized.")
        
        self.current_token_id = token_id
        return self.weights[token_id]

    def backward(self, gradient):
        """
        勾配を更新し、dxを計算する
        :param gradient: 1D NumPy配列, トークンIDに対応する埋め込みベクトルの勾配
        :return: dx (1D NumPy配列)
        """
        if self.current_token_id is None:
            raise ValueError("No token_id has been processed in forward.")
        
        if gradient.shape != self.weights[self.current_token_id].shape:
            raise ValueError("Gradient shape mismatch.")

        # 勾配を蓄積
        self.gradients[self.current_token_id] += gradient
        self.current_dx = gradient

        return self.current_dx

    def get_gradients(self):
        """
        蓄積された勾配を返す
        :return: 勾配行列（2D NumPy配列）
        """
        return self.gradients

    def clear_gradients(self):
        """
        勾配をクリア
        """
        self.gradients.fill(0)  # NumPyの機能で全てを0にする
