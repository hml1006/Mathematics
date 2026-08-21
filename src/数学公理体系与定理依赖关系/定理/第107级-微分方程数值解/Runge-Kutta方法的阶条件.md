# Runge-Kutta方法的阶条件

> **一句话大白话**：一个 s 级的 Runge-Kutta 方法到底"准不准"不是靠感觉，而是看它的系数（Butcher 表格里的 $a_{ij}, b_i, c_i$）能不能让数值解和真解的泰勒展开逐项对齐——对齐到第 $p$ 项，方法就是 $p$ 阶；这些"对齐要求"写成方程组就是阶条件。
>
> **小例子**：经典的 RK4（四阶龙格-库塔）四个系数满足 $\sum b_i=1$、$\sum b_i c_i=\tfrac12$、$\sum b_i c_i^2=\tfrac13$、$\sum b_i a_{ij}c_j=\tfrac16$ 等若干方程，所以它对 $y'=y$ 的每步误差是 $O(h^5)$，稳稳压过只满足 $\sum b_i=1$ 的向前欧拉法。

## 一、定理介绍

Runge-Kutta（RK）方法是求解常微分方程初值问题 $y'=f(t,y)$ 最广用的一类单步法。它用区间内几个"中间斜率" $k_i$ 的加权平均来推进一步。阶条件（order conditions）用 Butcher 表格的系数刻画出：方法何时能达到指定阶 $p$——即局部截断误差为 $O(h^{p+1})$。高阶条件是研究自适应步长、构造高效 RK 方法（如 Dormand-Prince）的基础。

## 二、原理思路

把 $y'=f(y)$（自治情形，非自治可增维）的真解在 $t_n$ 处泰勒展开：$y(t_n+h)=y+h f+\tfrac{h^2}{2}f_y f+\cdots$。再把数值解 $y_{n+1}=y_n+h\sum_i b_i k_i$ 也做泰勒展开（其中 $k_i$ 又依赖 $f$ 及其导数）。想要局部截断误差小到 $O(h^{p+1})$，就得让这两个展开的 $h,h^2,\dots,h^p$ 各项系数逐项相等。逐项比较就得到一组关于 $b_i,c_i,a_{ij}$ 的多项式方程——这就是阶条件。步数越多（$s$ 越大）可选组合越多，能被对齐的阶数越高。

## 三、定理的严格表述

考虑自治 ODE $y'=f(y)$，一个 $s$ 级 RK 方法由 Butcher 表格 $(a_{ij}, b_i, c_i)$ 给出。方法具有 $p$ 阶精度，当且仅当下列阶条件成立：

**一阶**

$$
\sum_{i=1}^s b_i=1.
$$

**二阶**（在上一基础上累加）

$$
\sum_{i=1}^s b_i c_i=\frac12.
$$

**三阶**（在上述基础上累加）

$$
\sum_{i=1}^s b_i c_i^2=\frac13,\qquad \sum_{i,j=1}^s b_i a_{ij} c_j=\frac16.
$$

**四阶**（在上述基础上累加）

$$
\sum_{i=1}^s b_i c_i^3=\frac14,\qquad \sum_{i,j=1}^s b_i c_i a_{ij} c_j=\frac18,
$$
$$
\sum_{i,j=1}^s b_i a_{ij} c_j^2=\frac{1}{12},\qquad
\sum_{i,j,k=1}^s b_i a_{ij} a_{jk} c_k=\frac{1}{24}.
$$

其中 $c_i=\sum_{j=1}^s a_{ij}$。

## 四、证明思路与关键步骤

1. **真解展开**。$y'=f(y)$ 的各阶导数用 $f$ 及其导数表示：$y'=f$，$y''=f_y f$，$y'''=f_{yy}(f,f)+f_y f_y f$，于是
   $$
   y(t_n+h)=y_n+h f+\frac{h^2}{2}f_y f+\frac{h^3}{6}\big(f_{yy}(f,f)+f_y f_y f\big)+O(h^4).
   $$
2. **数值解展开**。$k_i=f(y_n+h\sum_j a_{ij}k_j)$ 逐层代回：
   $$
   y_{n+1}=y_n+h\sum_i b_i f+h^2\sum_{i,j}b_i a_{ij}f_y f+\frac{h^3}{2}\sum_i b_i f_{yy}\Big(\sum_j a_{ij}f,\sum_j a_{ij}f\Big)+h^3\sum_{i,j,k}b_i a_{ij}a_{jk}f_y f_y f+O(h^4).
   $$
3. **逐项比较**。比较 $h$ 次项得 $\sum_i b_i=1$；比较 $h^2$ 项得 $\sum_{i,j}b_i a_{ij}=\tfrac12$，即 $\sum_i b_i c_i=\tfrac12$；比较 $h^3$ 的两类贡献分别给出 $\sum_i b_i c_i^2=\tfrac13$ 与 $\sum_{i,j,k}b_i a_{ij}a_{jk}=\tfrac16$（等价于 $\sum b_i a_{ij}c_j$ 形式）；继续到 $h^4$ 即得四阶那四个方程。
4. **根树系统性**.更高阶条件可用 Butcher 的**根树理论**（rooted trees）系统化生成：每个阶条件对应一棵根树，方程个数等于 $p$ 阶以内根树的数目。$\blacksquare$

## 五、应用与意义

- **方法构造**：由阶条件可反解设计 RK4、RK5、自适应 RK（如 Fehlberg、Dormand-Prince 用两组不同阶系数估计误差并自动变步长）。
- **精度控制**：实际求解器依据"最大允许阶条件"自动选择步长，兼顾精度与效率。
- **与线性多步法互补**：单步法（RK）便于变步长与并行，但阶条件复杂；多步法阶条件简单但步长受稳定性（零稳定）限制。
- **理论地位**：阶条件揭示"方法精度由系数组合决定"，是数值 ODE 分析的基础框架。