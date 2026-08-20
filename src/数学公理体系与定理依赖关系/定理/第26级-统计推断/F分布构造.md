# F分布构造

> **一句话大白话**：把两个独立卡方变量各自除以自由度再相除，得到的商服从 F 分布 $F=\frac{V_1/\nu_1}{V_2/\nu_2}\sim F(\nu_1,\nu_2)$，适合比较两组的"伸缩程度"（方差）。
>
> **小例子**：比较两个正态总体方差 $H_0:\sigma_1^2=\sigma_2^2$，用 $F=\frac{S_1^2}{S_2^2}\sim F(n_1-1,n_2-1)$ 作为检验统计量，$F$ 偏大或偏小就拒绝原假设。

## 介绍

F 分布（Fisher-Snedecor F-distribution）是数理统计中用于方差比较的重要分布，由 Ronald Fisher 和 George Snedecor 提出。F 分布的构造基于两个独立卡方变量的比值：若 $V_1 \sim \chi^2_{\nu_1}$ 与 $V_2 \sim \chi^2_{\nu_2}$ 独立，则 $F = \frac{V_1/\nu_1}{V_2/\nu_2}$ 服从自由度为 $(\nu_1, \nu_2)$ 的 F 分布，记为 $F \sim F(\nu_1, \nu_2)$。F 分布是方差分析（ANOVA）、回归分析中整体显著性检验和两正态总体方差比推断的基础。其概率密度函数为 $f(x) = \frac{\Gamma((\nu_1+\nu_2)/2)}{\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}\right)^{\nu_1/2} x^{\nu_1/2-1} \left(1 + \frac{\nu_1}{\nu_2}x\right)^{-(\nu_1+\nu_2)/2}$。

## 分析

**前置依赖**：正态分布、卡方分布、t 分布、Gamma 函数、随机变量的变换。

**数学内涵**：
- 构造：$F = \frac{V_1/\nu_1}{V_2/\nu_2}$，其中 $V_1 \sim \chi^2_{\nu_1}$，$V_2 \sim \chi^2_{\nu_2}$，$V_1$ 与 $V_2$ 独立。
- 概率密度函数：$f_F(x) = \frac{\Gamma((\nu_1+\nu_2)/2)}{\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}\right)^{\nu_1/2} x^{\nu_1/2-1} \left(1 + \frac{\nu_1}{\nu_2}x\right)^{-(\nu_1+\nu_2)/2}$，$x > 0$。
- 性质：右偏分布，取值非负。
- 与 t 分布的关系：若 $T \sim t_\nu$，则 $T^2 \sim F(1, \nu)$。
- 矩：$E[F] = \frac{\nu_2}{\nu_2-2}$（$\nu_2 > 2$），$\text{Var}(F) = \frac{2\nu_2^2(\nu_1+\nu_2-2)}{\nu_1(\nu_2-2)^2(\nu_2-4)}$（$\nu_2 > 4$）。

**结构**：
1. 构造定义。
2. 概率密度函数的推导。
3. 基本性质。
4. 与 t 分布的关系。

## 思考过程

F 分布的构造源于方差比较的实际需求。在比较两个正态总体的方差 $\sigma_1^2$ 和 $\sigma_2^2$ 时，自然考虑样本方差比 $S_1^2/S_2^2$。由正态总体抽样分布定理，$(n_i-1)S_i^2/\sigma_i^2 \sim \chi^2_{n_i-1}$，且两样本独立时，这两个卡方变量也独立。

因此，在 $H_0: \sigma_1^2 = \sigma_2^2$ 下：
$$\frac{S_1^2}{S_2^2} = \frac{[(n_1-1)S_1^2/\sigma^2]/(n_1-1)}{[(n_2-1)S_2^2/\sigma^2]/(n_2-1)} \sim F(n_1-1, n_2-1)$$

F 分布的密度函数可以通过联合分布和变量变换法推导，类似于 t 分布的推导过程，但涉及两个卡方变量的比值，需要二维到二维的变换。

## 证明过程

**定理**（F 分布的构造与密度）：设 $V_1 \sim \chi^2_{\nu_1}$，$V_2 \sim \chi^2_{\nu_2}$，且 $V_1$ 与 $V_2$ 独立。定义 $F = \frac{V_1/\nu_1}{V_2/\nu_2} = \frac{\nu_2 V_1}{\nu_1 V_2}$，则 $F$ 的概率密度函数为
$$f_F(x) = \frac{\Gamma((\nu_1+\nu_2)/2)}{\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}\right)^{\nu_1/2} x^{\nu_1/2-1} \left(1 + \frac{\nu_1}{\nu_2}x\right)^{-(\nu_1+\nu_2)/2}, \quad x > 0$$

**证明**：

### 1. 联合分布

$V_1$ 和 $V_2$ 的联合概率密度函数为：
$$f_{V_1,V_2}(v_1, v_2) = \frac{1}{2^{(\nu_1+\nu_2)/2}\Gamma(\nu_1/2)\Gamma(\nu_2/2)} v_1^{\nu_1/2-1} v_2^{\nu_2/2-1} e^{-(v_1+v_2)/2}, \quad v_1, v_2 > 0$$

### 2. 变量变换

令
$$F = \frac{\nu_2 V_1}{\nu_1 V_2}, \quad U = V_2$$

则逆变换为：
$$V_1 = \frac{\nu_1}{\nu_2} F U, \quad V_2 = U$$

变换的雅可比行列式为：
$$J = \det\begin{pmatrix} \frac{\partial v_1}{\partial f} & \frac{\partial v_1}{\partial u} \\ \frac{\partial v_2}{\partial f} & \frac{\partial v_2}{\partial u} \end{pmatrix} = \det\begin{pmatrix} \frac{\nu_1}{\nu_2}u & \frac{\nu_1}{\nu_2}f \\ 0 & 1 \end{pmatrix} = \frac{\nu_1}{\nu_2}u$$

### 3. 联合密度变换

$(F, U)$ 的联合密度为：
$$f_{F,U}(f, u) = f_{V_1,V_2}\left(\frac{\nu_1}{\nu_2}fu, u\right) \cdot \left|\frac{\nu_1}{\nu_2}u\right|$$

代入得：
$$f_{F,U}(f, u) = \frac{1}{2^{(\nu_1+\nu_2)/2}\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}fu\right)^{\nu_1/2-1} u^{\nu_2/2-1} e^{-\frac{1}{2}\left(\frac{\nu_1}{\nu_2}fu + u\right)} \cdot \frac{\nu_1}{\nu_2}u$$

整理：
$$f_{F,U}(f, u) = \frac{1}{2^{(\nu_1+\nu_2)/2}\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}\right)^{\nu_1/2} f^{\nu_1/2-1} u^{(\nu_1+\nu_2)/2-1} e^{-\frac{u}{2}\left(1 + \frac{\nu_1}{\nu_2}f\right)}$$

### 4. 边缘密度

对 $u$ 积分得到 $F$ 的边缘密度：
$$f_F(f) = \int_0^\infty f_{F,U}(f, u) du = \frac{(\nu_1/\nu_2)^{\nu_1/2} f^{\nu_1/2-1}}{2^{(\nu_1+\nu_2)/2}\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \int_0^\infty u^{(\nu_1+\nu_2)/2-1} e^{-\frac{u}{2}\left(1 + \frac{\nu_1}{\nu_2}f\right)} du$$

令 $s = \frac{u}{2}\left(1 + \frac{\nu_1}{\nu_2}f\right)$，则：
$$\int_0^\infty u^{(\nu_1+\nu_2)/2-1} e^{-\frac{u}{2}\left(1 + \frac{\nu_1}{\nu_2}f\right)} du = \left(\frac{2}{1 + \frac{\nu_1}{\nu_2}f}\right)^{(\nu_1+\nu_2)/2} \Gamma\left(\frac{\nu_1+\nu_2}{2}\right)$$

代入得：
$$f_F(f) = \frac{\Gamma((\nu_1+\nu_2)/2)}{\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left(\frac{\nu_1}{\nu_2}\right)^{\nu_1/2} f^{\nu_1/2-1} \left(1 + \frac{\nu_1}{\nu_2}f\right)^{-(\nu_1+\nu_2)/2}$$

$\square$

**性质**：

1. **与 t 分布的关系**：若 $T \sim t_\nu$，则 $T^2 \sim F(1, \nu)$。这是因为 $T = Z/\sqrt{V/\nu}$，则 $T^2 = Z^2/(V/\nu) = \frac{\chi^2_1/1}{\chi^2_\nu/\nu} \sim F(1, \nu)$。

2. **倒数性质**：若 $F \sim F(\nu_1, \nu_2)$，则 $1/F \sim F(\nu_2, \nu_1)$。这反映了 F 分布中分子分母自由度交换的对称性。

3. **收敛性**：当 $\nu_2 \to \infty$ 时，$\nu_1 F \xrightarrow{d} \chi^2_{\nu_1}$，即分母的方差估计趋于确定。

4. **矩**：
   - $E[F] = \frac{\nu_2}{\nu_2 - 2}$（$\nu_2 > 2$）
   - $\text{Var}(F) = \frac{2\nu_2^2(\nu_1 + \nu_2 - 2)}{\nu_1(\nu_2 - 2)^2(\nu_2 - 4)}$（$\nu_2 > 4$）

**注**：F 分布在方差分析（ANOVA）中用于检验多个组均值是否相等，在回归分析中用于检验模型的整体显著性，在线性模型中扮演着核心角色。F 检验与 t 检验在单变量线性回归中相互呼应：对于单个回归系数的显著性检验，$t^2 = F$。