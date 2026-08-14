# Weyl特征标公式

## 介绍

Weyl特征标公式（Weyl Character Formula）是紧李群表示论中最深刻的定理之一，由赫尔曼·外尔在 20 世纪 20 年代建立。该公式给出了紧李群 $G$ 的不可约表示的特征标的一个显式表达式，用最高权、根系统和 Weyl 群来描述。Weyl特征标公式是李群表示论的顶峰，统一了李代数的表示理论、根系统理论和 Weyl 群的作用，是理解李群表示分类的关键。

## 分析

**前置依赖**：李群、李代数、根系统、Weyl 群、最高权表示、特征标理论。

**数学内涵**：

**设定**：设 $G$ 是紧连通李群，$T \subseteq G$ 是极大环面，$\mathfrak{g}$ 和 $\mathfrak{t}$ 是李代数，$\Phi \subseteq \mathfrak{t}^*$ 是根系统，$W$ 是 Weyl 群。选正根系统 $\Phi^+$，$\rho = \frac{1}{2} \sum_{\alpha \in \Phi^+} \alpha$ 是半根和。

**Weyl 特征标公式**：设 $V_\lambda$ 是最高权为 $\lambda$ 的不可约 $G$-模（$\lambda$ 是支配整权），则其特征标 $\chi_\lambda: T \to \mathbb{C}$ 为：
$$
\chi_\lambda(\exp H) = \frac{\sum_{w \in W} \varepsilon(w) e^{i \langle w(\lambda+\rho), H \rangle}}{\sum_{w \in W} \varepsilon(w) e^{i \langle w(\rho), H \rangle}}, \quad H \in \mathfrak{t}
$$
其中 $\varepsilon(w) = \det(w) = (-1)^{\ell(w)}$ 是 $w$ 的符号。

**等价形式**（Weyl 分母公式）：
$$
\sum_{w \in W} \varepsilon(w) e^{i \langle w(\rho), H \rangle} = \prod_{\alpha \in \Phi^+} 2i \sin\left(\frac{\langle \alpha, H \rangle}{2}\right)
$$

**Weyl 维数公式**：
$$
\dim V_\lambda = \prod_{\alpha \in \Phi^+} \frac{\langle \lambda + \rho, \alpha \rangle}{\langle \rho, \alpha \rangle}
$$

**数学内涵**：Weyl特征标公式给出了不可约表示特征标的闭形式表达式，是李群表示论分类理论的顶点。

**证明策略**：利用李代数上的 Casimir 算子的特征值，结合 Weyl 群的作用和 Borel-Weil 理论。

## 思考过程

Weyl特征标公式的分子是 $\lambda+\rho$ 在 Weyl 群作用下的交错和，分母是 $\rho$ 的交错和（即 Weyl 分母）。公式的优美之处在于，它将特征标这个"整体"量用根系统这个"局部"量完全表达出来。

Weyl 维数公式是特征标公式的直接推论，它给出了不可约表示维数的显式乘积公式。例如，对于 $SU(n)$ 的不可约表示，维数公式给出了一个具体的整数表达式。

Weyl特征标公式可以看作是对紧李群上的傅里叶分析（Peter-Weyl 定理）的具体化——它给出了每个不可约表示的特征标的具体表达式。

## 证明过程

### 基本设定

设 $G$ 是紧连通李群，$T \subseteq G$ 是极大环面，$\mathfrak{t}$ 是 $T$ 的李代数。$G$ 的不可约表示由最高权 $\lambda$ 分类，$\lambda$ 是支配整权。

$W$ 是 Weyl 群，在 $\mathfrak{t}^*$ 上作用。选正根 $\Phi^+$，$\rho = \frac{1}{2} \sum_{\alpha \in \Phi^+} \alpha$。

### Weyl 分母公式

**引理 1**（Weyl 分母公式）：
$$
\sum_{w \in W} \varepsilon(w) e^{i \langle w(\rho), H \rangle} = \prod_{\alpha \in \Phi^+} (e^{i\langle \alpha, H \rangle/2} - e^{-i\langle \alpha, H \rangle/2}) = \prod_{\alpha \in \Phi^+} 2i \sin\left(\frac{\langle \alpha, H \rangle}{2}\right)
$$

**证明**：通过根系统的性质，利用 Weyl 群在根上的作用，对 $\dim \mathfrak{t}$ 归纳证明。$\square$

### Weyl 特征标公式

**定理**（Weyl 特征标公式）：设 $\chi_\lambda$ 是最高权为 $\lambda$ 的不可约 $G$-模 $V_\lambda$ 的特征标（在 $T$ 上的限制）。则对 $H \in \mathfrak{t}$，
$$
\chi_\lambda(\exp H) = \frac{\sum_{w \in W} \varepsilon(w) e^{i \langle w(\lambda+\rho), H \rangle}}{\sum_{w \in W} \varepsilon(w) e^{i \langle w(\rho), H \rangle}}
$$

**证明**：

**步骤 1**：特征标 $\chi_\lambda$ 是 $T$ 上的函数，可写为权空间维数的和：
$$
\chi_\lambda(t) = \sum_{\mu} \dim V_\lambda(\mu) e^{i\langle \mu, H \rangle}, \quad t = \exp H
$$
其中 $V_\lambda(\mu)$ 是权为 $\mu$ 的权空间。

**步骤 2**：对任意 $w \in W$，$\chi_\lambda$ 是 $W$-不变的（因为特征标是类函数，Weyl 群作用对应于共轭作用），故 $\chi_\lambda(w \cdot t) = \chi_\lambda(t)$。

**步骤 3**：考虑交错和 $A_\lambda(H) = \sum_{w \in W} \varepsilon(w) e^{i \langle w(\lambda+\rho), H \rangle}$。证明 $A_\lambda$ 是 $W$-交错的（即 $A_\lambda(w \cdot H) = \varepsilon(w) A_\lambda(H)$），且 $A_\lambda$ 可被分母 $A_0(H) = \sum_{w \in W} \varepsilon(w) e^{i \langle w(\rho), H \rangle}$ 整除。

**步骤 4**：$A_\lambda / A_0$ 是 $W$-不变的，且在 $T$ 的正则元处解析。由特征标的正交性，$\chi_\lambda$ 是唯一满足以下条件的 $W$-不变函数：
- $\chi_\lambda$ 可以展开为 $e^{i\langle \mu, H \rangle}$ 的线性组合，其中 $\mu$ 是权。
- 最高权 $\lambda$ 的系数为 1。
- 对 $\mu < \lambda$（在支配序下），系数非负。

**步骤 5**：$A_\lambda/A_0$ 满足上述所有条件，因此 $\chi_\lambda = A_\lambda/A_0$。$\square$

### Weyl 维数公式

**推论 1**（Weyl 维数公式）：
$$
\dim V_\lambda = \prod_{\alpha \in \Phi^+} \frac{\langle \lambda + \rho, \alpha \rangle}{\langle \rho, \alpha \rangle}
$$

**证明**：在 Weyl 特征标公式中令 $H \to 0$，两边取极限。左边 $\chi_\lambda(1) = \dim V_\lambda$。右边利用分母公式：
$$
\lim_{H \to 0} \frac{\sum_{w \in W} \varepsilon(w) e^{i \langle w(\lambda+\rho), H \rangle}}{\prod_{\alpha \in \Phi^+} 2i \sin(\langle \alpha, H \rangle/2)}
$$
通过洛必达法则或展开为幂级数计算，得到乘积公式。$\square$

### 例子

**例 1**（$SU(2)$ 的不可约表示）：$SU(2)$ 的根系统为 $A_1$，正根 $\alpha$，$\rho = \alpha/2$。最高权 $\lambda = n\alpha/2$（$n \ge 0$）。Weyl 特征标公式给出：
$$
\chi_n(e^{i\theta}) = \frac{e^{i(n+1)\theta} - e^{-i(n+1)\theta}}{e^{i\theta} - e^{-i\theta}} = \frac{\sin((n+1)\theta)}{\sin\theta}
$$
维数公式：$\dim V_n = n+1$。

**例 2**（$SU(3)$ 的不可约表示）：$SU(3)$ 的根系统为 $A_2$，有三个正根 $\alpha, \beta, \alpha+\beta$，$\rho = \alpha + \beta$。最高权 $\lambda = m\alpha + n\beta$ 的不可约表示维数为：
$$
\dim V_{m,n} = \frac{(m+1)(n+1)(m+n+2)}{2}
$$

**应用**：Weyl特征标公式是李群表示论中最核心的公式之一，广泛应用于粒子物理（强子的分类）、代数几何（Borel-Weil-Bott 定理）和数论（模形式理论）中。$\square$