# リーマン予想と素数密度構造の対応検証コード

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero

# 臨界線上のゼロのプロット
def plot_riemann_zeros(n=50):
    zeros = [zetazero(i) for i in range(1, n + 1)]
    re_parts = [z.real for z in zeros]
    im_parts = [z.imag for z in zeros]

    plt.figure(figsize=(6, 6))
    plt.scatter(re_parts, im_parts, alpha=0.7)
    plt.axvline(0.5, color='r', linestyle='--', label='Re(s) = 1/2')
    plt.title("Non-trivial Zeros of ζ(s)")
    plt.xlabel("Re(s)")
    plt.ylabel("Im(s)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_riemann_zeros()
