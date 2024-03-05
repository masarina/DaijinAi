def layer_normalization_forward(x, gamma, beta, epsilon=1e-5):
    """
    Layer Normalizationのforward passを実装します。

    入力:
    - x: 入力データ (D, )の形状を持つベクトル
    - gamma: スケールパラメータ (D, )の形状を持つベクトル
    - beta: シフトパラメータ (D, )の形状を持つベクトル
    - epsilon: 数値安定性のための小さな値

    出力:
    - out: 出力データ (D, )の形状を持つベクトル
    - cache: backward passで使用するために値を保存
    """
    # 入力xの平均を計算します (入力:(D, ), 出力:スカラー)
    mean = np.mean(x)
    
    # 入力xの分散を計算します (入力:(D, ), 出力:スカラー)
    var = np.var(x)
    
    # 入力xの標準偏差を計算します (入力:(D, ), 出力:スカラー)
    std = np.sqrt(var + epsilon)
    
    # 入力xを正規化します (入力:(D, ), 出力:(D, )の形状を持つベクトル)
    x_normalized = (x - mean) / std
    
    # 正規化されたデータに対してgammaとbetaを適用します (入力:(D, ), 出力:(D, )の形状を持つベクトル)
    out = gamma * x_normalized + beta
    
    # backward passで使用する値をcacheに保存します
    cache = {
        'x_normalized': x_normalized,
        'gamma': gamma,
        'x': x,
        'mean': mean,
        'std': std
    }
    
    return out, cache
