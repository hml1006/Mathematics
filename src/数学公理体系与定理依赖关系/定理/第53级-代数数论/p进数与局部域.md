# p-进数与局部域

## 一、定理介绍

$p$-进数（$p$-adic numbers）是数论中最基本的局部域（local field），由 Hensel 于 1897 年引入。$p$-进数域 $\mathbb{Q}_p$ 是有理数域 $\mathbb{Q}$ 关于 $p$-进绝对值 $|\cdot|_p$ 的完备化，它与实数域 $\mathbb{R}$（$\mathbb{Q}$ 关于通常绝对值的完备化）一起，构成了 $\mathbb{Q}$ 的所有**位置**（places）对应的局部域。

$p$-进数的核心思想是：用素数 $p$ 的幂次来度量数的"大小"。两个有理数在 $p$-进意义下"接近"，当且仅当它们的差被 $p$ 的高次幂整除。这种度量方式与通常的绝对值度量截然不同，它捕捉了数的**算术性质**（整除性、同余），而非几何性质。

局部域理论是代数数论的支柱之一。Hasse-Minkowski 定理、局部类域论、$p$-进 Hodge 理论等深刻结果都建立在 $p$-进数的基础之上。现代数论的许多前沿研究——如 $p$-进 Galois 表示、$p$-进 L-函数、perfectoid 空间——都以 $p$-进数为出发点。

## 二、原理思路

### $p$-进绝对值

对每个素数 $p$，定义 $\mathbb{Q}$ 上的 **$p$-进绝对值** $|\cdot|_p$：对非零有理数 $x = p^v \cdot \frac{a}{b}$（$p \nmid a, p \nmid b$），
$$|x|_p = p^{-v}, \quad |0|_p = 0.$$

$p$-进绝对值满足：
- **非 Archimedean 性（强三角不等式）：** $|x + y|_p \leq \max(|x|_p, |y|_p)$。
- **乘性：** $|xy|_p = |x|_p |y|_p$。

这与通常绝对值 $|\cdot|_\infty$ 形成对比：通常绝对值满足 Archimedean 性质（对任意 $x$，存在 $n$ 使得 $|nx| > 1$），而 $p$-进绝对值是非 Archimedean 的。

### Ostrowski 定理

**Ostrowski 定理**断言：$\mathbb{Q}$ 上的每个非平凡绝对值都等价于某个 $|\cdot|_p$（$p$ 为素数）或 $|\cdot|_\infty$（通常绝对值）。这意味着 $\mathbb{Q}$ 的"完备化方式"恰好有：可数多个 $p$-进完备化 $\mathbb{Q}_p$，和一个 Archimedean 完备化 $\mathbb{R}$。

### $\mathbb{Q}_p$ 的结构

$\mathbb{Q}_p$ 中的每个元素都可以唯一地写成**$p$-进级数**：
$$x = \sum_{i=v}^{\infty} a_i p^i, \quad a_i \in \{0, 1, \ldots, p-1\},$$
其中 $v \in \mathbb{Z}$。这类似于十进制小数展开，但是以 $p$ 为底，向"左"无限延伸（而非向右）。

$\mathbb{Q}_p$ 的**整数环**为 $\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \leq 1\}$，它是 $\mathbb{Z}$ 在 $\mathbb{Q}_p$ 中的闭包。$\mathbb{Z}_p$ 的唯一极大理想为 $p\mathbb{Z}_p$，剩余域为 $\mathbb{Z}_p/p\mathbb{Z}_p \cong \mathbb{F}_p$。

### Hensel 引理

**Hensel 引理**是 $p$-进分析的核心工具，它是 Newton 迭代法在 $p$-进整数环上的类比：

设 $f(x) \in \mathbb{Z}_p[x]$，$a \in \mathbb{Z}_p$ 满足 $f(a) \equiv 0 \pmod{p}$ 且 $f'(a) \not\equiv 0 \pmod{p}$。则存在唯一的 $\alpha \in \mathbb{Z}_p$ 使得 $f(\alpha) = 0$ 且 $\alpha \equiv a \pmod{p}$。

Hensel 引理使得我们可以从模 $p$ 的信息（有限域上的解）"提升"到 $p$-进整数上的精确解，这是局部域理论最强大的工具之一。

## 三、定理的严格表述

**定理（$p$-进数域的基本性质）：**

设 $p$ 为素数。

**(1) 构造：** $\mathbb{Q}_p$ 是 $\mathbb{Q}$ 关于 $p$-进绝对值 $|\cdot|_p$ 的度量完备化。$\mathbb{Q}_p$ 是特征为 0 的局部紧拓扑域，具有非 Archimedean 绝对值 $|\cdot|_p$。

**(2) 代数结构：** $\mathbb{Q}_p$ 的每个非零元素可以唯一地写成
$$x = p^v \sum_{i=0}^{\infty} a_i p^i, \quad v \in \mathbb{Z}, \quad a_i \in \{0, 1, \ldots, p-1\}, \quad a_0 \neq 0.$$
$\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \leq 1\}$ 是 $\mathbb{Q}_p$ 的赋值环，是离散赋值环（DVR），极大理想为 $p\mathbb{Z}_p$，剩余域为 $\mathbb{F}_p$。

**(3) 局部紧性：** $\mathbb{Z}_p$ 是紧致的（同胚于 Cantor 集），$\mathbb{Q}_p$ 是局部紧的。$\mathbb{Q}_p$ 是完全不连通的拓扑空间。

**(4) Hensel 引理：** 设 $f(x) \in \mathbb{Z}_p[x]$，$a_0 \in \mathbb{Z}_p$ 满足 $v_p(f(a_0)) > 2v_p(f'(a_0))$。则存在 $\alpha \in \mathbb{Z}_p$ 使得 $f(\alpha) = 0$ 且 $v_p(\alpha - a_0) \geq v_p(f(a_0)) - v_p(f'(a_0))$。

**(5) 有限扩张的分类：** $\mathbb{Q}_p$ 的每个有限扩张 $K/\mathbb{Q}_p$ 也是局部域。$K$ 有唯一的扩展赋值 $|\cdot|_K$，其整数环 $\mathcal{O}_K$ 是 DVR，剩余域是 $\mathbb{F}_q$（$q = p^f$）。$K$ 称为**完全 ramified**若 $e = [K:\mathbb{Q}_p]$，**非 ramified**若 $f = [K:\mathbb{Q}_p]$。

**定理（Ostrowski）：** $\mathbb{Q}$ 上的每个非平凡绝对值等价于某个 $|\cdot|_p$（$p$ 为素数）或 $|\cdot|_\infty$。

## 四、证明过程

### 第一步：$\mathbb{Q}_p$ 的构造

定义 $\mathbb{Q}_p$ 为 $\mathbb{Q}$ 关于 $|\cdot|_p$ 的 Cauchy 序列的等价类。具体地：
- 一个序列 $(x_n)$ 是 Cauchy 的，若对任意 $\epsilon > 0$，存在 $N$ 使得 $m, n > N$ 时 $|x_m - x_n|_p < \epsilon$。
- 两个 Cauchy 序列等价，若它们的差趋于 0。

$\mathbb{Q}_p$ 继承了一个完备的非 Archimedean 绝对值。

等价地，$\mathbb{Q}_p$ 可以定义为 $\mathbb{Z}_p$ 的分式域，其中 $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n\mathbb{Z}$ 是**$p$-进整数环**（逆极限）。

### 第二步：$p$-进展开

设 $x \in \mathbb{Q}_p$，$|x|_p = p^{-v}$。则 $p^v x \in \mathbb{Z}_p$，$|p^v x|_p = 1$。

写 $p^v x = a_0 + p \cdot x_1$，$a_0 \in \{1, \ldots, p-1\}$，$x_1 \in \mathbb{Z}_p$。递归地 $x_1 = a_1 + p \cdot x_2$，等等。得到
$$x = p^v(a_0 + a_1 p + a_2 p^2 + \cdots) = \sum_{i=v}^{\infty} a_i p^i.$$

唯一性由构造过程保证。

### 第三步：Hensel 引理的证明

设 $f(x) \in \mathbb{Z}_p[x]$，$a_0 \in \mathbb{Z}_p$ 满足 $|f(a_0)|_p < |f'(a_0)|_p^2$。

**Newton 迭代：** 定义 $a_{n+1} = a_n - \frac{f(a_n)}{f'(a_n)}$。

由 Taylor 展开：
$$f(a_{n+1}) = f(a_n) - f(a_n) + \frac{f(a_n)^2}{2} \cdot \frac{f''(a_n)}{f'(a_n)^2} + \cdots$$

精确估计得 $|f(a_{n+1})|_p \leq |f(a_n)|_p^2 / |f'(a_0)|_p^2$（在适当的非 Archimedean 估计下）。

因此 $|f(a_n)|_p \to 0$，且 $(a_n)$ 是 Cauchy 序列。设 $\alpha = \lim a_n$，则 $f(\alpha) = 0$。

唯一性由强三角不等式和 $f'$ 在 $\alpha$ 附近的非零性保证。

### 第四步：Ostrowski 定理的证明

设 $|\cdot|$ 是 $\mathbb{Q}$ 上的非平凡绝对值。

**情形 1（Archimedean）：** 若存在 $n \in \mathbb{N}$ 使得 $|n| > 1$，则 $|\cdot|$ 是 Archimedean 的。可以证明 $|\cdot|$ 等价于 $|\cdot|_\infty$（通过 $|n| = n^\alpha$ 对某个 $\alpha > 0$，然后延拓到 $\mathbb{Q}$）。

**情形 2（非 Archimedean）：** 若对所有 $n \in \mathbb{N}$，$|n| \leq 1$，则 $|\cdot|$ 是非 Archimedean 的。设 $\mathfrak{p} = \{n \in \mathbb{Z} : |n| < 1\}$。$\mathfrak{p}$ 是 $\mathbb{Z}$ 的素理想（由非 Archimedean 性），$\mathfrak{p} = p\mathbb{Z}$ 对某个素数 $p$。

对任意 $x = p^v \cdot \frac{a}{b} \in \mathbb{Q}$（$p \nmid a, p \nmid b$），$|x| = |p|^v \cdot |a|/|b| = |p|^v$（因为 $|a| = |b| = 1$）。设 $|p| = p^{-\alpha}$（$\alpha > 0$），则 $|x| = p^{-\alpha v} = |x|_p^\alpha$。

因此 $|\cdot|$ 等价于 $|\cdot|_p$。$\blacksquare$

## 五、应用与意义

### 1. 局部整体原理

$p$-进数与实数一起构成了 $\mathbb{Q}$ 的所有局部完备化。Hasse-Minkowski 定理等局部整体原理的核心思想是：整体问题（在 $\mathbb{Q}$ 上）可以通过研究所有局部问题（在 $\mathbb{R}$ 和所有 $\mathbb{Q}_p$ 上）来解决。

### 2. 局部类域论

局部域 $K$（有限扩张 of $\mathbb{Q}_p$ 或 $\mathbb{F}_q((t))$）的 Abel 扩张由**局部类域论**完全描述。局部 Artin 映射给出了 $K^\times$ 的完备化到 $\text{Gal}(K^{ab}/K)$ 的同构。局部类域论比全局类域论简单得多，是理解全局类域论的基础。

### 3. $p$-进分析与应用

- **$p$-进 L-函数：** Kubota-Leopoldt $p$-进 L-函数是经典 Dirichlet L-函数的 $p$-进插值，在 Iwasawa 理论中起核心作用。
- **$p$-进 Galois 表示：** Galois 群 $\text{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p)$ 的表示是现代数论的核心对象，与模形式、椭圆曲线密切相关。
- **$p$-进 Hodge 理论：** Fontaine 发展的 $p$-进 Hodge 理论（de Rham 表示、crystalline 表示等）是证明 Fermat 大定理的关键工具。

### 4. 数论中的 lifting

Hensel 引理使得我们可以从有限域上的信息"提升"到 $p$-进整数上的精确解。这一思想在代数几何（形式形变理论）、表示论（模 $p$ 表示提升到特征 0 表示）中有广泛应用。

### 5. Adele 与 Idele

$p$-进数是构建 **adele 环** $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times' \prod_p \mathbb{Q}_p$（受限直积）的基本组件。Adele 和 idele 为全局类域论提供了最自然的框架。

### 6. 算术几何

$p$-进数在算术几何中无处不在：
- **刚性几何（Rigid Geometry）：** Tate 发展的 $p$-进解析几何。
- **Perfectoid 空间：** Scholze 引入的 perfectoid 空间以 $p$-进数为基本对象，在 Langlands 纲领和局部 Langlands 对应中有突破性应用。
- **$p$-进 Uniformization：** 代数簇的 $p$-进统一化理论。
