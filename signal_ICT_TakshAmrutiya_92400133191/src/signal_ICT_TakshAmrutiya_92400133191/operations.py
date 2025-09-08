import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    t = signal[:, 0] + k  
    x = signal[:, 1]       
    result = np.column_stack((t, x))
    plt.plot(t, x,)
    plt.title(f"Time Shift by {k}")
    plt.show()
    return result

def time_scale(signal, k):
    t = signal[:, 0] * k
    x = signal[:, 1]
    result = np.column_stack((t, x))
    plt.plot(t, x,)
    plt.title(f"Time Scaling by {k}")
    plt.show()
    return result


def signal_addition(sig1, sig2):
    t1, x1 = sig1[:, 0], sig1[:, 1]
    t2, x2 = sig2[:, 0], sig2[:, 1]

    t_common = np.union1d(t1, t2)

    x1_interp = np.interp(t_common, t1, x1)
    x2_interp = np.interp(t_common, t2, x2)

    s = x1_interp + x2_interp
    result = np.column_stack((t_common, s))

    plt.plot(t_common, s)
    plt.title("Signal Addition")
    plt.show()
    return result

def signal_multiplication(sig1, sig2):
    t1, x1 = sig1[:, 0], sig1[:, 1]
    t2, x2 = sig2[:, 0], sig2[:, 1]

    t_common = np.union1d(t1, t2)

    x1_interp = np.interp(t_common, t1, x1)
    x2_interp = np.interp(t_common, t2, x2)

    s = x1_interp * x2_interp
    result = np.column_stack((t_common, s))

    plt.plot(t_common, s)
    plt.title("Signal Multiplication")
    plt.show()
    return result