# t分布构造

## 介绍

t 分布（Student's t-distribution）是统计推断中最重要的分布之一，由 William Sealy Gosset 于 1908 年以笔名"Student"发表。t 分布的构造基于标准正态分布与卡方分布的比值：若 $Z \sim N(0, 1)$ 与 $V \sim \chi^2_\nu$ 独立，则 $T = Z/\sqrt{V/\nu}$ 服从自由度为 $\nu$ 的 t 分布，记为 $T \sim t_\nu$。t 分布是正态总体下均值推断的核心工具，在样本量较小且总体方差未知时，用于构造均值的置信区间和进行假设检验。t 分布的概率密度函数为 $f(t) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\,\Gamma(\nu/2)}\left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}$。

## 分析

**前置依赖**：正态分布、卡方分布、Gamma 函数、随机变量的变换。

**数学内涵**：
- 构造：$T = \frac{Z}{\sqrt{V/\nu}}$，其中 $Z \sim N(0, 1)$，$V \sim \chi^2_\nu$，$Z$ 与 $V$ 独立。
- 概率密度函数：$f_T(t) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\,\Gamma(\nu/2)}\left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}$。
- 性质：关于 $0$ 对称，形状类似标准正态分布但尾部更厚。
- 当 $\nu \to \infty$ 时，$t_\nu \xrightarrow{d} N(0, 1)$。
- 矩：$E[T] = 0$（$\nu > 1$），$\text{Var}(T) = \nu/(\nu-2)$（$\nu > 2$）。

**结构**：
1. 构造定义。
2. 概率密度函数的推导。
3. 基本性质。
4. 与正态分布的关系。

## 思考过程

t 分布的构造动机源于实际统计推断中的需求。在正态总体均值的推断中，当方差 $\sigma^2$ 已知时，$(\bar{X} - \mu)/(\sigma/\sqrt{n}) \sim N(0, 1)$ 可直接用于检验。但方差未知时，需要用样本方差 $S^2$ 替代 $\sigma^2$，这时统计量 $(\bar{X} - \mu)/(S/\sqrt{n})$ 的分母也是随机变量，其分布不再正态。

由正态总体抽样分布定理，$\bar{X}$ 与 $S^2$ 独立，且 $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n}) \sim N(0, 1)$，$V = (n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$。因此
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{Z}{\sqrt{V/(n-1)}} \sim t_{n-1}$$

t 分布的密度函数可以通过联合分布和变量变换法推导：先写出 $Z$ 和 $V$ 的联合密度，再作变换 $T = Z/\sqrt{V/\nu}$ 和辅助变量 $U = V$，最后积分消去 $U$。

## 证明过程

**定理**（t 分布的构造与密度）：设 $Z \sim N(0, 1)$，$V \sim \chi^2_\nu$，且 $Z$ 与 $V$ 独立。定义 $T = \frac{Z}{\sqrt{V/\nu}}$，则 $T$ 的概率密度函数为
$$f_T(t) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\,\Gamma(\nu/2)}\left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}, \quad t \in \mathbb{R}$$

**证明**：

### 1. 联合分布

$Z$ 和 $V$ 的联合概率密度函数为：
$$f_{Z,V}(z, v) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2} \cdot \frac{1}{2^{\nu/2}\Gamma(\nu/2)}v^{\nu/2-1}e^{-v/2}, \quad z \in \mathbb{R}, v > 0$$

### 2. 变量变换

令
$$T = \frac{Z}{\sqrt{V/\nu}} = \frac{Z\sqrt{\nu}}{\sqrt{V}}, \quad U = V$$

则逆变换为：
$$Z = T\sqrt{U/\nu}, \quad V = U$$

变换的雅可比行列式为：
$$J = \det\begin{pmatrix} \frac{\partial z}{\partial t} & \frac{\partial z}{\partial u} \\ \frac{\partial v}{\partial t} & \frac{\partial v}{\partial u} \end{pmatrix} = \det\begin{pmatrix} \sqrt{u/\nu} & \frac{t}{2\sqrt{\nu u}} \\ 0 & 1 \end{pmatrix} = \sqrt{\frac{u}{\nu}}$$

### 3. 联合密度变换

$(T, U)$ 的联合密度为：
$$f_{T,U}(t, u) = f_{Z,V}\left(t\sqrt{\frac{u}{\nu}}, u\right) \cdot \left|\sqrt{\frac{u}{\nu}}\right|$$

代入得：
$$f_{T,U}(t, u) = \frac{1}{\sqrt{2\pi}}e^{-t^2u/(2\nu)} \cdot \frac{1}{2^{\nu/2}\Gamma(\nu/2)}u^{\nu/2-1}e^{-u/2} \cdot \sqrt{\frac{u}{\nu}}$$

整理：
$$f_{T,U}(t, u) = \frac{1}{\sqrt{2\pi\nu}\,2^{\nu/2}\Gamma(\nu/2)} u^{(\nu-1)/2} e^{-\frac{u}{2}\left(1 + \frac{t^2}{\nu}\right)}, \quad u > 0, t \in \mathbb{R}$$

### 4. 边缘密度

对 $u$ 积分得到 $T$ 的边缘密度：
$$f_T(t) = \int_0^\infty f_{T,U}(t, u) du = \frac{1}{\sqrt{2\pi\nu}\,2^{\nu/2}\Gamma(\nu/2)} \int_0^\infty u^{(\nu-1)/2} e^{-\frac{u}{2}\left(1 + \frac{t^2}{\nu}\right)} du$$

令 $s = \frac{u}{2}\left(1 + \frac{t^2}{\nu}\right)$，则 $u = \frac{2s}{1 + t^2/\nu}$，$du = \frac{2}{1 + t^2/\nu}ds$：
$$\int_0^\infty u^{(\nu-1)/2} e^{-\frac{u}{2}\left(1 + \frac{t^2}{\nu}\right)} du = \left(\frac{2}{1 + t^2/\nu}\right)^{(\nu+1)/2} \int_0^\infty s^{(\nu-1)/2} e^{-s} ds = \left(\frac{2}{1 + t^2/\nu}\right)^{(\nu+1)/2} \Gamma\left(\frac{\nu+1}{2}\right)$$

代入得：
$$f_T(t) = \frac{1}{\sqrt{2\pi\nu}\,2^{\nu/2}\Gamma(\nu/2)} \cdot \left(\frac{2}{1 + t^2/\nu}\right)^{(\nu+1)/2} \Gamma\left(\frac{\nu+1}{2}\right)$$

化简：
$$f_T(t) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\,\Gamma(\nu/2)}\left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}$$

$\square$

**性质**：

1. **对称性**：$f_T(-t) = f_T(t)$，即 t 分布关于 $0$ 对称。
2. **尾部厚度**：t 分布的尾部比标准正态分布更厚，且 $\nu$ 越小尾部越厚。
3. **收敛性**：当 $\nu \to \infty$ 时，$t_\nu \xrightarrow{d} N(0, 1)$，因为 $\lim_{\nu\to\infty} (1 + t^2/\nu)^{-(\nu+1)/2} = e^{-t^2/2}$。
4. **矩**：$E[T] = 0$（$\nu > 1$），$\text{Var}(T) = \frac{\nu}{\nu-2}$（$\nu > 2$）。