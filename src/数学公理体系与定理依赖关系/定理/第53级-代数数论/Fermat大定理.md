# Fermat 大定理（Wiles 证明）

## 一、定理介绍

Fermat 大定理（Fermat's Last Theorem, FLT）是数学史上最著名的定理之一。它断言：对整数 $n \geq 3$，方程
$$x^n + y^n = z^n$$
没有正整数解 $(x, y, z)$。

这一定理由 Pierre de Fermat 于 1637 年左右提出，他在阅读 Diophantus 的《算术》时在页边写道："我有一个与此命题真正美妙的证明，但页边太窄写不下。"此后三百五十多年间，这一命题成为数学中最著名的未解决问题。

1995 年，Andrew Wiles（在 Richard Taylor 的协助下）最终证明了 Fermat 大定理。Wiles 的证明是现代数论的巅峰之作，它建立了一条从椭圆曲线到模形式的惊人桥梁（模性定理），并综合运用了代数数论、代数几何、表示论、Galois 表示等深刻的数学工具。

证明的核心思路并非直接攻击 Fermat 方程，而是通过以下间接路线：
1. **Frey (1984)：** 若 FLT 不成立，则可以构造一条奇特的椭圆曲线（Frey 曲线）。
2. **Serre (1985)：** 提出关于 Galois 表示的精确猜想（$\epsilon$-猜想），暗示 Frey 曲线不可能存在。
3. **Ribet (1986)：** 证明了 Serre 猜想的关键一步（$\epsilon$-猜想的水平降低），将 Frey 曲线与模形式联系起来。
4. **Wiles-Taylor (1995)：** 证明了半稳定椭圆曲线的模性定理（Taniyama-Shimura-Weil 猜想的一部分），从而推出 Frey 曲线必须是模的，与 Ribet 的结论矛盾，因此 FLT 成立。

## 二、原理思路

### 从 Fermat 方程到椭圆曲线

设 $p \geq 5$ 是素数，假设存在非零互素整数 $a, b, c$ 使得 $a^p + b^p = c^p$。

**Frey 曲线：** 定义椭圆曲线
$$E: y^2 = x(x - a^p)(x + b^p).$$

这条曲线具有极为特殊的性质：
- 它的**判别式** $\Delta_E = (abc)^{2p} / 2^8$（在适当的归一化下），被 $p$ 的高次幂整除。
- 它的**导子** $N_E$ 非常小：$N_E = \prod_{\ell | abc} \ell$（只被 $abc$ 的素因子整除，且每个素因子只出现一次——即 $E$ 是**半稳定**的，在 $2$ 以外无加性约化）。

Frey 注意到：这样一条"判别式被高次幂整除但导子很小"的椭圆曲线，按常理不应该存在。

### Serre 的模性猜想

Serre 关于 $\text{GL}_2(\mathbb{F}_p)$ 的模表示提出了精确的猜想：每个奇不可约 $\rho: \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \text{GL}_2(\mathbb{F}_p)$ 都来自某个权为 $k$、水平为 $N$ 的模形式，其中 $k$ 和 $N$ 由 $\rho$ 的局部性质（在 $p$ 和其他素数处的行为）精确确定。

对 Frey 曲线 $E$ 的 $p$-扭转 $E[p]$，对应的 Galois 表示 $\bar{\rho}_{E,p}: \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \text{GL}_2(\mathbb{F}_p)$ 具有以下性质：
- **不可约**（由 Mazur 的定理）。
- **在 $p$ 处平坦**（flat）——因为 $E$ 的判别式被 $p$ 的高次幂整除。
- **导子极小**——$N_E$ 只被 $abc$ 的素因子整除。

由 Serre 猜想，$\bar{\rho}_{E,p}$ 应该来自权为 2、水平为 $N_E$（或 $2N_E$）的模形式。

### Ribet 的水平降低定理

Ribet (1986) 证明了 Serre 猜想中的**水平降低**部分：若 $\bar{\rho}_{E,p}$ 来自权 2、水平 $N$ 的模形式，且 $\ell | N$ 但 $\bar{\rho}_{E,p}$ 在 $\ell$ 处非分歧，则 $\bar{\rho}_{E,p}$ 也来自权 2、水平 $N/\ell$ 的模形式。

反复应用水平降低，可以将 Frey 曲线的导子降低到 $N = 2$。但权 2、水平 2 的模形式空间 $S_2(\Gamma_0(2))$ 是 0 维的！这意味着 $\bar{\rho}_{E,p}$ 不可能来自任何模形式，矛盾。

### Wiles 的模性定理

为了完成证明，Wiles 需要证明：Frey 曲线 $E$ 确实是模的（即来自模形式）。

**Taniyama-Shimura-Weil 猜想（特殊情形）：** 每条（半稳定）椭圆曲线 $E/\mathbb{Q}$ 都是模的，即存在权 2、水平 $N_E$ 的正规化新形式 $f$ 使得 $L(E, s) = L(f, s)$。

Wiles 的证明策略：
1. 研究 $E$ 的 $p$-进 Galois 表示 $\rho_{E,p}: \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \text{GL}_2(\mathbb{Z}_p)$。
2. 证明 $\rho_{E,p}$ 是模的（即来自模形式的 $p$-进 Galois 表示）。
3. 使用**形变理论**（deformation theory）：证明 $\rho_{E,p}$ 的形变环 $R$ 与 Hecke 代数 $\mathbb{T}$ 同构（$R = \mathbb{T}$ 定理）。

$R = \mathbb{T}$ 定理的证明是 Wiles 论文最技术性的部分，涉及：
- **Euler 系统**（Kolyvagin-Flach 方法）：用于控制 Selmer 群的大小。
- **Iwasawa 理论：** 用于处理 $p$-进形变。
- **交换代数：** Hecke 代数的 Cohen-Macaulay 性质和完全交叉性质。

最终 Wiles 和 Taylor 合作解决了剩余的技术困难，完成了半稳定椭圆曲线模性定理的证明。

## 三、定理的严格表述

**定理（Fermat 大定理）：**

对整数 $n \geq 3$，方程
$$x^n + y^n = z^n$$
没有正整数解 $(x, y, z) \in \mathbb{Z}_{>0}^3$。

等价地（通过约化到素指数）：

**定理（Fermat 大定理，素指数形式）：**

对每个奇素数 $p \geq 3$，方程 $x^p + y^p = z^p$ 没有正整数解。

**定理（Wiles 模性定理）：**

每条半稳定椭圆曲线 $E/\mathbb{Q}$ 都是模的。即存在权为 2、水平为 $N_E$（$E$ 的导子）的 Hecke 特征形式 $f \in S_2(\Gamma_0(N_E))$，使得对所有素数 $\ell$，
$$a_\ell(f) = \ell + 1 - \#E(\mathbb{F}_\ell),$$
其中 $a_\ell(f)$ 是 $f$ 的第 $\ell$ 个 Fourier 系数。

**推论（Fermat 大定理）：** 由 Frey 曲线 + Ribet 定理 + Wiles 模性定理，Fermat 大定理成立。

## 四、证明过程

### 第一步：约化到素指数

若 $n \geq 3$ 有解 $(x, y, z)$，设 $p | n$ 为 $n$ 的素因子。则 $(x^{n/p})^p + (y^{n/p})^p = (z^{n/p})^p$，所以只需对素指数 $p \geq 5$（$p=3$ 由 Euler 证明）证明无解。

进一步可以假设 $x, y, z$ 两两互素（否则约去公因子）。

### 第二步：Frey 曲线

假设 $a^p + b^p = c^p$，$a \equiv -1 \pmod{4}$，$b$ 为偶数（通过调整符号和排列总可以做到）。

定义 **Frey 曲线**：
$$E_{a,b,c}: y^2 = x(x - a^p)(x + b^p).$$

$E_{a,b,c}$ 的性质：
- 判别式 $\Delta = 2^4 (abc)^{2p}$（在最小 Weierstrass 模型下）。
- 导子 $N = \prod_{\ell | abc, \ell \neq 2} \ell$（或乘以 $2$ 的某次幂）。
- $E$ 是半稳定的：在 $\ell | abc$（$\ell \neq 2$）处有乘性约化，在 $\ell \nmid 2abc$ 处有好约化。

### 第三步：Galois 表示

对 $E = E_{a,b,c}$，考虑 $p$-进 Tate 模 $T_p(E)$ 和 $p$-扭转 $E[p]$。

$\rho_{E,p}: G_\mathbb{Q} = \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \text{Aut}(T_p(E)) \cong \text{GL}_2(\mathbb{Z}_p)$

$\bar{\rho}_{E,p}: G_\mathbb{Q} \to \text{Aut}(E[p]) \cong \text{GL}_2(\mathbb{F}_p)$

由 Mazur 定理，$\bar{\rho}_{E,p}$ 是不可约的（因为 $p \geq 5$ 且 $E$ 是半稳定的）。

### 第四步：Ribet 定理

**Ribet 定理 (1986)：** $\bar{\rho}_{E,p}$ 是模的，且来自权 2、水平 $N = 2$ 的模形式空间。

但 $S_2(\Gamma_0(2)) = 0$（水平 2 的权 2 尖点形式空间是零维的）。矛盾！

因此 Frey 曲线 $E_{a,b,c}$ 不存在，即 $a^p + b^p = c^p$ 无解。

**但** Ribet 定理的前提是 $\bar{\rho}_{E,p}$ 是模的，即 $E$ 本身是模的。这正是 Wiles 需要证明的。

### 第五步：Wiles 的模性定理证明

Wiles 证明：每条半稳定椭圆曲线 $E/\mathbb{Q}$ 是模的。

**策略：** 使用形变理论。设 $\bar{\rho} = \bar{\rho}_{E,p}$。

**(a) 形变环 $R$：** 定义 $\bar{\rho}$ 的形变函子，证明其可表，表示对象为局部完全交叉环 $R$（universal deformation ring）。

**(b) Hecke 代数 $\mathbb{T}$：** 定义与 $\bar{\rho}$ 相关的 Hecke 代数 $\mathbb{T}$（参数化模形式的 Fourier 系数）。

**(c) 自然映射 $R \to \mathbb{T}$：** 由模形式的 Galois 表示构造自然同态 $R \to \mathbb{T}$。

**(d) $R = \mathbb{T}$ 定理：** Wiles 证明 $R \to \mathbb{T}$ 是同构。证明的关键是：
- 计算 Selmer群 $H^1_\Sigma(G_\mathbb{Q}, \text{Ad}(\rho))$ 的上界（使用 Euler 系统方法）。
- 证明 Hecke 代数 $\mathbb{T}$ 的某些不变量（如 $\#\mathbb{T}/\mathfrak{p}$）与 Selmer 群的大小匹配。
- 利用交换代数中的判据（Wiles 的数值判据）：若 $\#\mathbb{T}/I \geq \#R/I$ 且某个不变量等式成立，则 $R \cong \mathbb{T}$。

Wiles 最初的证明在 Euler 系统部分有一个缺口。在 Taylor 的协助下，他们发展了一种新的方法（Wiles-Taylor 方法），利用完全交叉环的性质和两个素数的比较来弥补缺口。

### 第六步：完成证明

由 Wiles 模性定理，Frey 曲线 $E_{a,b,c}$ 是模的。由 Ribet 定理，$\bar{\rho}_{E,p}$ 来自水平 2 的模形式。但 $S_2(\Gamma_0(2)) = 0$，矛盾。

因此假设 $a^p + b^p = c^p$ 有解是错误的。Fermat 大定理成立。$\blacksquare$

## 五、应用与意义

### 1. 模性定理的完全证明

Wiles 的工作开创了证明椭圆曲线模性定理的新纪元。在 Wiles 证明半稳定情形后：
- **Breuil-Conrad_Diamond_Taylor (2001)：** 证明了所有椭圆曲线 $E/\mathbb{Q}$ 都是模的（完全 Taniyama-Shimura-Weil 猜想）。
- 模性定理使得椭圆曲线的 $L$-函数可以用模形式的 $L$-函数来研究，极大地丰富了椭圆曲线的算术理论。

### 2. Langlands 纲领的验证

椭圆曲线的模性定理是 **Langlands 纲领**在 $\text{GL}_2/\mathbb{Q}$ 上的重要实例。Langlands 纲领断言：Galois 表示与自守表示之间存在深刻的对应关系。Wiles 的工作为 Langlands 纲领提供了最壮观的验证。

### 3. 形变方法的深远影响

Wiles 的 $R = \mathbb{T}$ 方法（形变理论 + Hecke 代数）已成为现代数论的标准工具：
- **完全交叉性与模性提升：** 用于证明更多 Galois 表示的模性。
- **算术几何中的模性提升：** 将模性从 residual 表示提升到 $p$-进表示。
- **Fontaine-Mazur 猜想：** 关于 $p$-进 Galois 表示的几何性的猜想，部分通过形变方法证明。

### 4. 对 Diophantine 方程的影响

Fermat 大定理的证明展示了模形式和 Galois 表示在解决 Diophantine 方程中的强大威力。这一方法被推广到：
- **广义 Fermat 方程：** $x^p + y^q = z^r$（$1/p + 1/q + 1/r < 1$）。
- **Fermat-Catalan 猜想。**
- **其他 Diophantine 问题：** 通过构造类似的" Frey 对象"（如 Frey 抽象曲面、Frey 表示）并证明其模性来排除解的存在。

### 5. 计算与验证

在 Wiles 的证明之前，Fermat 大定理已对大量素指数 $p$ 进行了计算机验证。Wiles 的证明给出了对所有 $p$ 的统一证明，结束了这一长达三百多年的努力。

### 6. 数学的统一

Fermat 大定理的证明体现了现代数学惊人的统一性：
- **数论：** 代数数论（理想类群、类域论）、解析数论（L-函数）。
- **代数几何：** 椭圆曲线、模空间、算术曲面。
- **表示论：** Galois 表示、自守表示。
- **交换代数：** 形变环、Hecke 代数。

Wiles 的证明不仅是 Fermat 大定理的证明，更是整个现代数论的一次壮丽展示。它揭示了看似不相关的数学领域之间的深刻联系，为未来的研究开辟了广阔的方向。
