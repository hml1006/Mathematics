# FFT与卷积定理

> **一句话大白话**：把两个信号"卷在一起"揉成一个新信号，若直接硬算很慢；绕到频率世界（傅里叶变换）里一乘再转回来就快多了——"乘在频域等于卷在时域"这条定理，配合快速算法（FFT）让海量数据的卷积唰一下就算完。
>
> **小例子**：$\mathcal{F}(f*g)=\mathcal{F}(f)\cdot\mathcal{F}(g)$，即卷积的傅里叶等于各自傅里叶的乘积；于是先 FFT、"点乘"、再 IFFT 三步，就能 $O(N\log N)$ 完成原本 $O(N^2)$ 的卷积。

## 介绍

快速傅里叶变换（Fast Fourier Transform, FFT）是计算离散傅里叶变换（DFT）的快速算法，由 James Cooley 和 John Tukey 在1965年提出，但其核心思想可追溯到 Gauss。FFT 将 DFT 的计算复杂度从 $O(N^2)$ 降低到 $O(N \log N)$，是20世纪最重要的数值算法之一。卷积定理（Convolution Theorem）则建立了傅里叶变换与卷积运算之间的深刻联系：时域中的卷积等价于频域中的逐点乘积。FFT 与卷积定理的结合使得大规模卷积运算变得可行，广泛应用于信号处理、图像处理、偏微分方程数值解和机器学习等领域。

## 分析

**定理的精确表述**（离散傅里叶变换 DFT）：设 $x = (x_0, x_1, \ldots, x_{N-1})$ 是长度为 $N$ 的复序列，其 DFT 定义为

$$
X_k = \sum_{n=0}^{N-1} x_n \omega_N^{-nk}, \quad k = 0, 1, \ldots, N-1,
$$

其中 $\omega_N = e^{2\pi i/N}$ 是 $N$ 次单位根。

**FFT 算法（Cooley-Tukey）**：当 $N = 2^m$ 时，DFT 可以分解为：

$$
X_k = \sum_{n=0}^{N/2-1} x_{2n} \omega_{N/2}^{-nk} + \omega_N^{-k} \sum_{n=0}^{N/2-1} x_{2n+1} \omega_{N/2}^{-nk}.
$$

**卷积定理**：对序列 $x, y$，其循环卷积 $z = x * y$ 定义为 $z_n = \sum_{m=0}^{N-1} x_m y_{n-m \bmod N}$。则

$$
\widehat{z}_k = \widehat{x}_k \cdot \widehat{y}_k,
$$

其中 $\widehat{\cdot}$ 表示 DFT。

**依赖的概念**：傅里叶变换、单位根、分治算法、循环卷积、线性卷积。

**证明策略**：通过直接验证 DFT 的定义和卷积的定义，利用求和交换和单位根的性质。

## 思考过程

FFT 的核心思想是分治策略：将 $N$ 点的 DFT 分解为两个 $N/2$ 点的 DFT（分别对应偶数索引和奇数索引），然后通过组合得到完整结果。这个分解可以递归进行，总计算量为 $O(N \log N)$。

卷积定理的证明是直接的代数验证，它揭示了傅里叶变换的一个基本性质：它将卷积运算对角化。在频域中，卷积变为逐点乘法，这大大简化了计算。

FFT 计算卷积的步骤：
1. 计算 $x$ 和 $y$ 的 FFT：$\widehat{x} = \mathrm{FFT}(x)$，$\widehat{y} = \mathrm{FFT}(y)$。
2. 逐点相乘：$\widehat{z}_k = \widehat{x}_k \cdot \widehat{y}_k$。
3. 逆 FFT：$z = \mathrm{IFFT}(\widehat{z})$。

## 证明过程

**定理**（FFT 算法正确性）：设 $N = 2^m$，$X = \mathrm{DFT}(x)$。则 FFT 算法正确计算 $X$，计算复杂度为 $O(N \log N)$。

**证明**：

**步骤 1：分解 DFT。**

将 $X_k = \sum_{n=0}^{N-1} x_n \omega_N^{-nk}$ 按 $n$ 的奇偶性分解：

$$
X_k = \sum_{j=0}^{N/2-1} x_{2j} \omega_N^{-2jk} + \sum_{j=0}^{N/2-1} x_{2j+1} \omega_N^{-(2j+1)k}
= \sum_{j=0}^{N/2-1} x_{2j} \omega_{N/2}^{-jk} + \omega_N^{-k} \sum_{j=0}^{N/2-1} x_{2j+1} \omega_{N/2}^{-jk}.
$$

**步骤 2：递归计算。**

设 $E_k = \sum_{j=0}^{N/2-1} x_{2j} \omega_{N/2}^{-jk}$ 是偶数序列的 $N/2$ 点 DFT，$O_k = \sum_{j=0}^{N/2-1} x_{2j+1} \omega_{N/2}^{-jk}$ 是奇数序列的 $N/2$ 点 DFT。则

$$
X_k = E_k + \omega_N^{-k} O_k, \quad k = 0, \ldots, N/2-1,
$$
$$
X_{k+N/2} = E_k - \omega_N^{-k} O_k, \quad k = 0, \ldots, N/2-1.
$$

其中利用了 $\omega_N^{-(k+N/2)} = -\omega_N^{-k}$。

**步骤 3：复杂度分析。**

设 $T(N)$ 是计算 $N$ 点 DFT 的时间。则 $T(N) = 2T(N/2) + O(N)$，解为 $T(N) = O(N \log N)$。$\square$

**定理**（卷积定理）：设 $x, y \in \mathbb{C}^N$，$z = x * y$ 是循环卷积。则 $\widehat{z}_k = \widehat{x}_k \cdot \widehat{y}_k$ 对所有 $k = 0, \ldots, N-1$。

**证明**：

由定义，

$$
\widehat{z}_k = \sum_{n=0}^{N-1} z_n \omega_N^{-nk} = \sum_{n=0}^{N-1} \sum_{m=0}^{N-1} x_m y_{n-m} \omega_N^{-nk}.
$$

交换求和顺序，令 $p = n-m$（模 $N$），得

$$
\widehat{z}_k = \sum_{m=0}^{N-1} x_m \left( \sum_{p=0}^{N-1} y_p \omega_N^{-(m+p)k} \right) = \sum_{m=0}^{N-1} x_m \omega_N^{-mk} \cdot \sum_{p=0}^{N-1} y_p \omega_N^{-pk} = \widehat{x}_k \cdot \widehat{y}_k.
$$

$\square$

**推论**（线性卷积的 FFT 计算）：对长度为 $M$ 和 $N$ 的序列，其线性卷积可以通过补零至 $L \ge M+N-1$，计算 FFT，逐点相乘，再 IFFT 得到，复杂度为 $O(L \log L)$。