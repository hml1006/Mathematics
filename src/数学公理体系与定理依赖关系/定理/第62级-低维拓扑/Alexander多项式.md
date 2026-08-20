# Alexander 多项式

> **一句话大白话**：给每条打了结的绳子配一个带正负次幂的整式"签名"，打不同的结签名大体不同，是最老也最经典的区分绳结的手段。
>
> **小例子**：平凡结的 Alexander 多项式为 $1$；三叶结的为 $t^{-1}-1+t$，可见正常数用 $t$ 的整式可记下三叶结构。它还可由 Seifert 矩阵 $\det(A^T-tA)$ 计算。

## 一、定理介绍

Alexander 多项式是 James W. Alexander 于 1928 年引入的经典纽结不变量，是纽结理论中最早被发现也是最有影响力的不变量之一。它通过纽结补集的第一同调覆盖或 Seifert 矩阵构造，是一个单变量 Laurent 多项式，能够区分大量纽结，并在纽结的切片性、纤维性以及三维流形手术研究中发挥关键作用。

## 二、原理思路

给定定向纽结 $K \subset S^3$，取其管状邻域 $N(K)$ 的边界 $T = \partial N(K)$。纽结补集 $M_K = S^3 \setminus \mathring{N}(K)$ 的基本群 $G_K = \pi_1(M_K)$ 具有自然的到 $\mathbb{Z}$ 的 Abeleinization 映射

$$
\varepsilon: G_K \to H_1(M_K;\mathbb{Z}) \cong \mathbb{Z},
$$

它把每个子午线映到生成元 $t$。对应于该同态的无限循环覆盖 $\widetilde{M}_K \to M_K$ 的第一同调群 $H_1(\widetilde{M}_K;\mathbb{Z})$ 成为模 $\mathbb{Z}[t,t^{-1}]$ 上的有限生成挠模。Alexander 多项式 $\Delta_K(t)$ 定义为该挠模的初等因子，在乘以 $\pm t^k$ 的意义下唯一。

另一等价构造利用 Seifert 曲面：取 $K$ 的亏格 $g$ Seifert 曲面 $F$，其上的 Seifert 配对给出 $2g \times 2g$ 的 Seifert 矩阵 $V$，则

$$
\Delta_K(t) \doteq \det(V - t V^{\mathrm{T}}),
$$

其中 $\doteq$ 表示相差 $\pm t^k$。

## 三、定理的严格表述

**定义（Alexander 模）.** 设 $K$ 为定向纽结，$G_K = \pi_1(S^3 \setminus K)$。Abeleinization 给出满同态 $\varepsilon: G_K \to \mathbb{Z}$，其核决定无限循环覆盖 $p: \widetilde{X} \to X = S^3 \setminus K$。第一同调群 $H_1(\widetilde{X};\mathbb{Z})$ 通过 deck 变换具有 $\Lambda = \mathbb{Z}[t,t^{-1}]$ 模结构，称为 Alexander 模，记为 $A(K)$。

**定理.** Alexander 模 $A(K)$ 是挠 $\Lambda$–模，且存在自由分解

$$
\Lambda^m \xrightarrow{\varphi} \Lambda^n \to A(K) \to 0.
$$

其初等理想 $E_1(A(K))$ 由某个非零 Laurent 多项式 $\Delta_K(t) \in \Lambda$ 生成。该多项式在乘以单位元 $\pm t^k$ 的意义下唯一，称为 $K$ 的 Alexander 多项式。

**定理（Seifert 矩阵公式）.** 设 $V$ 为 $K$ 的 Seifert 矩阵，则

$$
\Delta_K(t) \doteq \det(V - t V^{\mathrm{T}}).
$$

**基本性质.**

1. 对称性：$\Delta_K(t) \doteq \Delta_K(t^{-1})$。
2. 归一化：可取 $\Delta_K(1) = \pm 1$，且 $\Delta_K(t^{-1}) = t^{-\deg \Delta_K} \Delta_K(t)$。
3. 平凡纽结的 Alexander 多项式为 $1$。

## 四、证明过程

**Alexander 模为挠模的证明.**

1. 由于 $H_1(X;\mathbb{Z}) \cong \mathbb{Z}$，万有 Abel 覆盖 $\widetilde{X}$ 的 deck 变换群为 $\mathbb{Z}$，作用由 $t$ 生成。

2. 利用 $X$ 的 CW 结构提升，得到 $\Lambda$ 模的自由链复形
   $$
   C_2(\widetilde{X}) \xrightarrow{\partial_2} C_1(\widetilde{X}) \xrightarrow{\partial_1} C_0(\widetilde{X}) \to 0.
   $$
   由于 $H_0(\widetilde{X}) \cong \mathbb{Z}$（作为 $\Lambda$ 模由 $t-1$ 零化），边界映射 $\partial_1$ 在 $H_1$ 上的核给出 Alexander 模。

3. 对纽结补集，$\partial_1$ 的像由 $(t-1)$ 生成，$H_1(\widetilde{X})$ 满足 $E_1$ 理想非零，故为挠模。

**Seifert 矩阵公式证明.**

1. 取 Seifert 曲面 $F$ 的管状邻域 $N(F) \cong F \times [-1,1]$，则 $S^3 \setminus N(F)$ 是两个柄体 $H_1, H_2$ 的并。

2. 无限循环覆盖 $\widetilde{X}$ 可沿 $F$ 的提升切片。Seifert 配对 $V$ 描述的是 $H_1(F)$ 上沿正方向推离 $F$ 的环绕数。

3. Mayer–Vietoris 序列给出关系矩阵 $V - t V^{\mathrm{T}}$，其行列式即 Alexander 多项式。

**对称性证明.** 由 Alexander 模的 Blanchfield 配对或 Seifert 矩阵公式，

$$
\det(V - t V^{\mathrm{T}}) = (-t)^{2g} \det(V - t^{-1} V^{\mathrm{T}}),
$$

故 $\Delta_K(t) \doteq \Delta_K(t^{-1})$。

## 五、应用与意义

Alexander 多项式是纽结理论最经典的不变量之一。它可以有效区分大量纽结与链环，判定某些纽结是否非平凡，并用于研究纽结的切片性：Fox–Milnor 定理指出，若 $K$ 为切片纽结，则 $\Delta_K(t)$ 可分解为 $f(t)f(t^{-1})$（相差单位元）。Alexander 多项式也与纽结的纤维性密切相关：一个纽结为纤维纽结当且仅当其次级 Alexander 理想具有特定形式。此外，Alexander 多项式可推广为 Alexander–Conway 多项式、多变量 Alexander 多项式，并在代数几何（平面曲线奇点）、动力系统（辫群熵）以及低维流形手术研究中持续发挥重要作用。
