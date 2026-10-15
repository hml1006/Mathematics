# SVM的间隔最大化原理

> **一句话大白话**：线性可分数据里，SVM 要找"离两类样本都尽量远"的分离超平面，这等价于求一个凸二次规划：最小化 $\frac12\|w\|^2$。
>
> **小例子**：两个单点类 $(x_1,y_1=+1),(x_2,y_2=-1)$，最优超平面就是两点连线的中垂线，此时间隔最大、分类最稳健。

## 一、定理介绍

> **前置依赖**：点到超平面的距离公式、凸二次规划、Lagrange 对偶、KKT 条件（互补松弛）、几何间隔的概念。

对线性可分的二分类数据集 $\{(x_i,y_i)\}$，$y_i\in\{-1,1\}$，求解最大化几何间隔
$$
\max_{w,b}\frac1{\|w\|}\min_i y_i(\langle w,x_i\rangle+b)
$$
等价于求解凸二次规划
$$
\min_{w,b}\frac12\|w\|^2\quad\text{s.t.}\quad y_i(\langle w,x_i\rangle+b)\ge1,\;i=1,\dots,n.
$$
该等价揭示了 SVM 的目标结构，并能进一步化为对偶问题、引入核技巧。

## 二、原理思路

几何间隔是样本到超平面最小距离的 $\|w\|$ 归一化形式。由于间隔表达式在 $(w,b)$ 的尺度缩放（$w\mapsto cw,b\mapsto cb$）下不变，可以固定约束为 $y_i(\langle w,x_i\rangle+b)\ge1$（即 $\|w\|=1/\gamma$），此时最大化间隔 $\gamma=1/\|w\|$ 等价于最小化 $\|w\|$，也等价于最小化 $\frac12\|w\|^2$。

## 三、定理的严格表述

### 几何间隔

点 $x_i$ 到超平面 $\langle w,x\rangle+b=0$ 的几何距离为 $\frac{|\langle w,x_i\rangle+b|}{\|w\|}$，训练集的最小间隔为
$$
\gamma=\min_i\frac{y_i(\langle w,x_i\rangle+b)}{\|w\|}.
$$

### 等价优化问题

最大化 $\gamma$ 问题：
$$
\max_{w,b,\gamma}\gamma\quad\text{s.t.}\quad\frac{y_i(\langle w,x_i\rangle+b)}{\|w\|}\ge\gamma,\;i=1,\dots,n
$$
等价于（经 $\|w\|=1/\gamma$ 归一化后）
$$
\min_{w,b}\frac12\|w\|^2\quad\text{s.t.}\quad y_i(\langle w,x_i\rangle+b)\ge1,\;i=1,\dots,n.
$$

### 对偶问题

引入 Lagrange 乘子 $\alpha_i\ge0$，对 $w,b$ 求偏导为零得 $w=\sum_i\alpha_iy_ix_i$、$\sum_i\alpha_iy_i=0$，代入得对偶问题
$$
\max_{\alpha}\sum_{i=1}^n\alpha_i-\frac12\sum_{i,j=1}^n\alpha_i\alpha_jy_iy_j\langle x_i,x_j\rangle,
$$
约束为 $\alpha_i\ge0$ 且 $\sum_i\alpha_iy_i=0$。

## 四、证明过程

**步骤1：几何间隔定义。** 如严格表述中定义 $\gamma$。

**步骤2：最大化问题。** 将最大化 $\gamma$ 写成带约束的优化。

**步骤3：尺度归一化。** 因间隔对尺度缩放不变，固定 $\|w\|=1/\gamma$，即 $\gamma=1/\|w\|$，约束化为 $y_i(\langle w,x_i\rangle+b)\ge1$。

**步骤4：目标转化。** 最大化 $\gamma=1/\|w\|$ 等价于最小化 $\|w\|$，再等价于最小化 $\frac12\|w\|^2$，得凸二次规划。

**步骤5：Lagrange 对偶。** 构造 $\mathcal{L}(w,b,\alpha)=\frac12\|w\|^2-\sum_i\alpha_i[y_i(\langle w,x_i\rangle+b)-1]$，令对 $w,b$ 的偏导为零，回代得对偶问题。

**步骤6：KKT 与支持向量。** 由互补松弛 $\alpha_i[y_i(\langle w,x_i\rangle+b)-1]=0$，$\alpha_i>0$ 的样本满足 $y_i(\langle w,x_i\rangle+b)=1$，即位于间隔边界上的支持向量。

**步骤7：决策函数。** $f(x)=\text{sign}\big(\sum_i\alpha_iy_i\langle x_i,x\rangle+b\big)$，求和仅对支持向量进行。$\square$

## 五、应用与意义

间隔最大化原理给出了 SVM 作为凸二次规划、对偶可解、仅依赖支持向量的理论依据。对偶形式自然引入核技巧，使 SVM 能处理非线性可分数据；间隔最大化也提供了泛化与稳健性的直觉（更大间隔对应更可靠的分类），是现代核方法的奠基性结果。

## 课堂问答

**老师**：最大化几何间隔怎么就和最小化 $\frac12\|w\|^2$ 等价了？

**学生**：结论：因为间隔对 $(w,b)$ 的整体缩放不变。几何间隔

$$
\gamma=\min_i\frac{y_i(\langle w,x_i\rangle+b)}{\|w\|},
$$

在 $w\mapsto cw,\ b\mapsto cb$ 下不变，所以可约定 $\|w\|=1/\gamma$，约束就化为 $y_i(\langle w,x_i\rangle+b)\ge1$。此时最大化 $\gamma=1/\|w\|$ 等价于最小化 $\|w\|$，也就是最小化 $\frac12\|w\|^2$ 这个凸二次规划。

**老师（追问）**：对偶问题与支持向量是怎么冒出来的？

**学生**：引入乘子 $\alpha_i\ge0$，对 $w,b$ 求偏导为零得 $w=\sum_i\alpha_iy_ix_i$、$\sum_i\alpha_iy_i=0$，回代得对偶

$$
\max_{\alpha}\ \sum_{i=1}^n\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_j\langle x_i,x_j\rangle .
$$

由互补松弛 $\alpha_i\big[y_i(\langle w,x_i\rangle+b)-1\big]=0$，只有 $\alpha_i>0$ 的样本满足 $y_i(\langle w,x_i\rangle+b)=1$，它们正是落在间隔边界上的支持向量，决策函数 $f(x)=\operatorname{sign}\big(\sum_i\alpha_iy_i\langle x_i,x\rangle+b\big)$ 只对它们求和。

**老师（拓展）**：对偶形式最重要的副产品是什么？

**学生**：是核技巧。对偶里样本只以内积 $\langle x_i,x_j\rangle$ 出现，把它换成核 $K(x_i,x_j)$ 就等价于在某个高维特征空间里做同样的事，无需显式构造映射。误区是以为非支持向量的样本也影响决策——由互补松弛，它们对应的 $\alpha_i=0$，对 $w$ 与 $b$ 没有贡献。
