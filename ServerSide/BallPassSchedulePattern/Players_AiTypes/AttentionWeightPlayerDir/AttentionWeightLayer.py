import numpy as np

class AttentionWeight:
    def __init__(self, softmax_layer):
        """
        初期化
        :param softmax_layer: Softmaxの処理を行うクラスのインスタンス
        """
        self.softmax_layer = softmax_layer
        self.hs = None  # 過去状態
        self.h = None   # 現在の入力状態
        self.cache_hs = None  # キャッシュされた過去状態
        self.cache_hr = None  # キャッシュされた現在の状態
        self.softmax_params = None  # Softmaxのパラメータ

    def forward(self, hs_input, h_input):
        """
        フォワード処理
        :param hs_input: 過去状態 (2D配列: T × H)
        :param h_input: 現在の状態 (1D配列: H)
        :return: アテンションの重み (1D配列: T)
        """
        self.hs = np.array(hs_input)
        self.h = np.array(h_input)

        # 現在の状態をコピー
        hr = np.copy(self.h)

        # 過去状態とのスコアを計算
        s = np.dot(self.hs, hr)

        # スコアをSoftmaxで正規化
        a = self.softmax_layer.forward(s)

        # Softmaxのパラメータを保存
        self.softmax_params = self.softmax_layer.get_params()

        # キャッシュに保存
        self.cache_hs = self.hs
        self.cache_hr = hr

        return a

    def backward(self, da):
        """
        バックワード処理
        :param da: アテンションの重みに対する勾配 (1D配列: T)
        :return: 過去状態と現在状態の勾配 (2D配列: [dhs, dh])
        """
        # SoftmaxLayerにパラメータを再設定
        self.softmax_layer.set_params(self.softmax_params)

        # Softmaxの逆伝播
        ds = self.softmax_layer.backward(da)

        # 勾配を初期化
        T, H = self.cache_hs.shape
        dhs = np.zeros_like(self.cache_hs)
        dh = np.zeros_like(self.cache_hr)

        # 勾配を計算
        for i in range(T):
            dhs[i] = ds[i] * self.cache_hr  # dhs[i] = ds[i] * cache_hr
            dh += ds[i] * self.cache_hs[i]  # dh += ds[i] * cache_hs[i]

        return dhs, dh
