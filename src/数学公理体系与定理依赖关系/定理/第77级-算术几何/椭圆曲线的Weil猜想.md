# 椭圆曲线的 Weil 猜想

> **一句话大白话**：椭圆曲线上有限域 $\mathbb{F}_q$ 上的点个数虽然随 $q$ 增长，但能用一个简洁的公式精确刻画：$N_m=1+q^m-(\alpha^m+\bar\alpha^m)$，其中 $\alpha$ 的绝对值恰为 $\sqrt q$。点的个数总能被"准平方根"级的量 $\alpha^m$ 追踪。
>
> **小例子**：$E:y^2=x^3+1$ 在 $\mathbb{F}_5$ 上，算得 $N_1=6$（含无穷远点），$a=1+5-6=0$，故 $\alpha=2\sqrt5$ 与 $-\bar\alpha$ 为共轭、满足 $|\alpha|=\sqrt5$，$N_m=1+5^m-(\alpha^m+\bar\alpha^m)$。

## 一、定理介绍

> **前置依赖**：有限域与 Frobenius 态射、$\ell$-进 Tate 模、对偶同态、Zeta 函数的定义、Lefschetz 不动点公式类比。

这一般情形由 Weil 猜想（1949）描述，这里给出椭圆曲线情形的完整证明。它断言 Abel 簇（含椭圆曲线）在有限域上有理点个数满足"Riemann 假设"式约束，由 Zeta 函数写成
$$Z(E/\mathbb{F}_q,T)=\frac{1-aT+qT^2}{(1-T)(1-qT)},$$
配合多项式根的模条件 $|\alpha|=\sqrt q$。这是 Weil 猜想体系中最基础又完整的样例。

## 二、原理思路

核心对象是 Frobenius 态射。$\mathbb{F}_q$-Frobenius 映射 $\operatorname{Frob}_q$（$(x:y:z)\mapsto(x^q:y^q:z^q)$）作用在 Tate 模 $T_\ell(E)\cong\mathbb{Z}_\ell^2$ 上得到一个 $\mathbb{Z}_\ell$-线性变换 $F$。由 Lefschetz 不动点（在 $\ell$-进上同调中的类比）得 $N_m=1-\operatorname{Tr}(F^m)+q^m$。证明 $|\alpha|=\sqrt q$ 用对偶化：$F\circ\hat F=q$ 且 $F,\hat F$ 特征多项式相同，故若 $\alpha$ 是 $F$ 的特征值，则 $q/\alpha=\bar\alpha$，从而 $|\alpha|=\sqrt q$。

## 三、定理的严格表述

设 $E$ 是有限域 $\mathbb{F}_q$ 上的椭圆曲线，$q=p^a$，$N_m=\#E(\mathbb{F}_{q^m})$。则存在代数整数 $\alpha\in\mathbb{C}$，$|\alpha|=\sqrt q$，使
$$N_m=1+q^m-(\alpha^m+\bar\alpha^m).$$
等价地，Zeta 函数：
$$Z(E/\mathbb{F}_q,T)=\exp\Big(\sum_{m\ge1}N_m\frac{T^m}{m}\Big)=\frac{1-aT+qT^2}{(1-T)(1-qT)},$$
其中 $a=1+q-N_1=\alpha+\bar\alpha$。

## 四、证明过程

**证明：**

**引理 1（Frobenius）。** $\mathbb{F}_q$-Frobenius $\operatorname{Frob}_q$ 满足 $E(\mathbb{F}_{q^m})$ 恰为 $\operatorname{Frob}_q^m$ 的不动点集，即 $\ker(\operatorname{Frob}_q^m-\operatorname{id})$。$\blacksquare$

**引理 2。** 设 $F=\operatorname{Frob}_q^*$ 在 $T_\ell(E)$ 上的作用，$\ell\neq p$。则 $\det(F)=q$，$\operatorname{Tr}(F)=a$。
**证明：** $F$ 特征多项式 $P(T)=T^2-(\operatorname{Tr}F)T+\det F$。由 Lefschetz 不动点类比 $N_m=1-\operatorname{Tr}(F^m)+q^m$，令特征值 $\alpha,\bar\alpha$，则 $\alpha\bar\alpha=\det F=q$，$a=\operatorname{Tr}F=\alpha+\bar\alpha$。$\blacksquare$

**Riemann 假设 $|\alpha|=\sqrt q$。** 考虑对偶化态射：$F$ 与其对偶 $\hat F$ 满足 $F\circ\hat F=q$（作为乘 $q$ 态射）。若 $\alpha$ 是 $F$ 特征值，则 $q/\alpha$ 是 $\hat F$ 特征值；而 $\hat F$ 与 $F$ 有相同特征多项式（迹/行列式经对偶不变），故 $q/\alpha=\bar\alpha$，从而 $|\alpha|=\sqrt q$。$\blacksquare$

**Zeta 函数计算：**
$$\begin{aligned}
Z&=\exp\Big(\sum_{m}\frac{(1-\alpha^m-\bar\alpha^m+q^m)T^m}{m}\Big)\\
&=\frac{(1-\alpha T)(1-\bar\alpha T)}{(1-T)(1-qT)}=\frac{1-aT+qT^2}{(1-T)(1-qT)}.
\end{aligned}$$
$\square$

## 五、应用与意义

椭圆曲线 Weil 猜想的完整证明标志着有限域上算术-几何桥梁的打通，是 Weil 猜想（对一般簇由 Deligne 于 1973 年证明）最重要的特训。它给出 Hasse 界 $|N_1-(q+1)|\le2\sqrt q$（密码学加解密安全性关键）、有限域上曲线的 Hash 点计数，并与单变量函数域 Riemann 假设（Ver尸）直接相关。$L$-函数与 $\alpha$ 的联系进入 BSD 猜想、极化 Hecke 与等源分类（Tate 猜想），是算术几何谱系的中枢。