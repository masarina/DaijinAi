import numpy as np

def backward(dout, cache):
    """
    Layer Normalizationのbackward passを実装します。
    
    入力:
    - dout: 上流(出力層)からの勾配
    - cache: forward passから保存された値(x_normalized, gamma, x, mean, std)
    
    出力:
    - dx: 入力層への勾配 (D, )
    - dgamma: gammaパラメータへの勾配 (D, )
    - dbeta: betaパラメータへの勾配 (D, )
    """
    
    # cacheから値を取り出す
    x_normalized = cache['x_normalized']  # 形状は(D,)のベクトル
    gamma = cache['gamma']  # 形状は(D,)のベクトル
    x = cache['x']  # 形状は(D,)のベクトル
    mean = cache['mean']  # スカラー
    std = cache['std']  # スカラー
    
    # dbetaの勾配計算
    # dout: 上流(出力層)からの勾配、バッチ処理がないので形状は(D,)のベクトル
    # dbeta: betaパラメータへの勾配、形状は(D,)のベクトル。ただし、
    #        バッチ処理がない場合、全特徴量にわたる勾配を累積してスカラーとして扱われることもある
    dbeta = np.sum(dout, axis=0)

    # dgammaの勾配計算
    # dout: 上流(出力層)からの勾配、形状は(D,)のベクトル
    # x_normalized: 正規化された入力データ、形状は(D,)のベクトル
    # dgamma: gammaパラメータへの勾配、全特徴量にわたる勾配を累積したスカラー
    dgamma = np.sum(dout * x_normalized, axis=0)
    
    # dx_normalizedに関する勾配計算
    dx_normalized = dout * gamma

    # x - mean
    x_minus_mean = x - mean

    # 標準偏差の微分(ニュートン法を使用)
    epsilon=1e-6
    a = std**2 + epsilon
    x_n = 0.5  # 初期値
    for _ in range(5):  # 5回の反復で十分な精度が得られることが多い
        x_n = x_n * (1.5 - 0.5 * a * x_n**2)
    std_inv = x_n

    # dx_normalizedによる分母の逆数の勾配
    dstd_inv = np.sum(dx_normalized * x_minus_mean, axis=0)

    # 分母の勾配
    dstd = -dstd_inv / (std**2 + 1e-6)
    
    # 分散(var)の逆数をニュートン法で計算する
    epsilon = 1e-6
    a = std**2 + epsilon  # この場合、aは分散(std**2)にepsilonを加えたもの
    x_n = 0.5  # 初期値
    for _ in range(5):  # 5回の反復で十分な精度が得られることが多い
        x_n = x_n * (2 - a * x_n)
    var_inv = x_n  # var_invは分散の逆数の近似値
    
    # 分散の勾配を求めるために、分散の逆数の計算結果を用いる
    dvar = 0.5 * dstd * var_inv  # dstdは分散に対する勾配

    # x_minus_meanの2倍
    x_minus_mean_doubled = 2. * x_minus_mean

    # 分散による平均の勾配
    dmean_var_component = dvar * np.sum(x_minus_mean_doubled, axis=0) / x.shape[0]

    # 平均の勾配
    dmean = -np.sum(dx_normalized * std_inv, axis=0) + dmean_var_component

    # xに関する勾配
    dx1 = dx_normalized * std_inv
    dx2 = dmean_var_component / x.shape[0]
    dx3 = dmean / x.shape[0]

    # 最終的なdx
    dx = dx1 + dx2 + dx3

    return dx, dgamma, dbeta
