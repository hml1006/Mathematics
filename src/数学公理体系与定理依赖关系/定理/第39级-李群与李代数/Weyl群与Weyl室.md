# Weyl 群与 Weyl 室

## 介绍

Weyl 群与 Weyl 室是根系统理论中的核心概念，由 Hermann Weyl 在其对半单李群表示论的研究中引入。Weyl 群是由根系统生成的反射群，它反映了根系统的对称性；Weyl 室则是 Weyl 群在 Cartan 子代数对偶空间中的基本区域。这两个概念在半单李代数分类、表示论和特征标理论中扮演着关键角色，也是理解 Weyl 特征标公式的基础。

## 分析

**前置依赖**：根系统、Cartan 子代数、Killing 型、反射变换、半单李代数。

**定理内容**：设 $\Phi$ 是欧几里得空间 $E$ 中的根系统。

**Weyl 群的定义**：Weyl 群 $W$ 是由所有反射 $s_\alpha$（$\alpha \in \Phi$）生成的群，其中
$$s_\alpha(v) = v - 2\frac{(v,\alpha)}{(\alpha,\alpha)}\alpha,\quad v \in E$$
$W$ 是 $O(E)$ 的有限子群。

**Weyl 室的定义**：固定一组单根 $\Delta = \{\alpha_1,\dots,\alpha_n\} \subset \Phi$，定义主 Weyl 室为
$$C = \{v \in E \mid (v,\alpha_i) > 0,\ \forall \alpha_i \in \Delta\}$$
Weyl 室是 $E$ 中由超平面 $P_\alpha = \{v \in E \mid (v,\alpha) = 0\}$（$\alpha \in \Phi$）分割而成的开区域。Weyl 群 $W$ 作用在 Weyl 室的集合上，且该作用是可迁的。

**Weyl 群的性质**：
1. $W$ 是有限 Coxeter 群，由 $s_{\alpha_i}$（$\alpha_i \in \Delta$）生成。
2. $W$ 在根系统 $\Phi$ 上的作用保持 $\Phi$ 不变。
3. $W$ 在 Weyl 室集合上的作用是简单可迁的。
4. $W$ 的阶等于 $|W| = \prod_{i=1}^n \frac{(\alpha_i^\vee, \rho) + 1}{(\alpha_i^\vee, \rho)}$，其中 $\rho$ 是半正根和的一半。

**数学内涵**：Weyl 群编码了半单李代数的全部对称性，它在李代数表示论中起着关键作用——Weyl 特征标公式、Weyl 维数公式等核心结果都依赖于 Weyl 群。Weyl 室则提供了根系统的一个"基本区域"，使得在 Weyl 群作用下每个轨道有唯一的代表元。

**证明策略**：Weyl 群是有限群的证明依赖于根系统是有限集这一事实，以及 $W$ 忠实作用在 $\Phi$ 上。Weyl 室的性质通过分析反射超平面的分割来证明，核心是证明 $W$ 在 Weyl 室上的作用简单可迁。

## 思考过程

Weyl 群的概念源于对根系统对称性的研究。每个根 $\alpha$ 定义了一个反射 $s_\alpha$，它将 $\alpha$ 映射到 $-\alpha$，同时保持根系统 $\Phi$ 不变。这些反射生成的群 $W$ 就是 Weyl 群。

Weyl 室是理解 Weyl 群作用的关键几何对象。在 $E$ 中，所有反射超平面 $P_\alpha$ 将 $E$ 分割成若干个开锥形区域，每个区域就是一个 Weyl 室。Weyl 群 $W$ 将 Weyl 室映射到 Weyl 室，且该作用是可迁的——这意味着 $W$ 的阶等于 Weyl 室的个数。

在表示论中，Weyl 群的一个重要应用是 Weyl 特征标公式：
$$\chi_\lambda = \frac{\sum_{w \in W} \varepsilon(w) e^{w(\lambda+\rho)}}{\prod_{\alpha > 0} (e^{\alpha/2} - e^{-\alpha/2})}$$
这个公式将不可约表示的特征标表示为 Weyl 群作用下的交错和。

## 证明过程

**定理**（Weyl 群与 Weyl 室）：设 $\Phi \subset E$ 是根系统，$W$ 是 Weyl 群。

**(1) $W$ 是有限群**：反射 $s_\alpha$ 将 $\Phi$ 映射到 $\Phi$，故 $W$ 作用在 $\Phi$ 上。若 $w \in W$ 在 $\Phi$ 上的作用是平凡的，则 $w$ 固定所有 $\alpha \in \Phi$，从而固定张成 $E$ 的 $\Phi$ 的基，故 $w = 1$。因此 $W$ 同构于 $\operatorname{Sym}(\Phi)$ 的子群，而 $\Phi$ 是有限集，故 $W$ 有限。

**(2) 反射超平面与 Weyl 室**：对每个 $\alpha \in \Phi$，定义超平面 $P_\alpha = \{v \in E \mid (v,\alpha) = 0\}$。这些超平面将 $E$ 分割为有限个连通开区域，每个区域称为一个 Weyl 室。

固定一组单根 $\Delta = \{\alpha_1,\dots,\alpha_n\}$，主 Weyl 室为
$$C = \{v \in E \mid (v,\alpha_i) > 0,\ \forall \alpha_i \in \Delta\}$$
对每个 $\alpha \in \Phi^+$（正根），$(v,\alpha) > 0$ 对 $v \in C$ 成立（因为正根是单根的正线性组合）。

**(3) $W$ 在 Weyl 室上的作用可迁**：对任意 Weyl 室 $C'$，取 $v \in C'$。存在 $w \in W$ 使得 $w(v)$ 属于主 Weyl 室 $C$ 的闭包。实际上，可以取 $w$ 使得 $(w(v),\rho)$ 最大，其中 $\rho$ 是正根和的一半，则 $w(v) \in \overline{C}$。若 $w(v) \notin C$，则存在 $\alpha_i$ 使得 $(w(v),\alpha_i) = 0$，从而 $s_{\alpha_i}w(v) = w(v)$，通过调整可得 $w(v) \in \overline{C}$ 且 $(w(v),\rho)$ 更大，矛盾。故 $w(v) \in C$，即 $w(C') = C$。

**(4) $W$ 在 Weyl 室上的作用简单可迁**：若 $w(C) = C$，则 $w$ 保持所有单根的正性，即 $(w(v),\alpha_i) > 0$ 对 $v \in C$ 成立。这意味着 $w(\alpha_i)$ 是正根。同理 $w^{-1}(\alpha_i)$ 也是正根，故 $w(\alpha_i) = \alpha_i$ 对所有 $\alpha_i \in \Delta$ 成立，从而 $w = 1$。

**(5) $W$ 由关于单根的反射生成**：对任意 $\alpha \in \Phi$，将 $\alpha$ 写成单根的正/负线性组合。可以证明存在 $w \in W' = \langle s_{\alpha_i} \mid \alpha_i \in \Delta \rangle$ 使得 $w(\alpha) \in \Delta$。因此 $s_\alpha = w^{-1}s_{w(\alpha)}w \in W'$，故 $W = W'$。$\square$

**推论**（Weyl 维数公式）：设 $\mathfrak{g}$ 是半单李代数，$\lambda$ 是支配整权，则不可约表示 $V(\lambda)$ 的维数为
$$\dim V(\lambda) = \prod_{\alpha > 0} \frac{(\lambda + \rho, \alpha)}{(\rho, \alpha)}$$
其中 $\rho = \frac{1}{2}\sum_{\alpha > 0} \alpha$。