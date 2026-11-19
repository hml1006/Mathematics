# Nelson-Aalen 估计

> **一句话大白话**：每到一个事件时刻，就用“当时仍可能被观察到发生事件的人数”作分母、实际事件数作分子，把这些瞬时风险贡献累加起来，就得到累积风险；风险集越大，单次事件带来的增量越小。
>
> **小例子**：在时刻 $1,2,3$ 的风险人数分别为 $5,4,2$，各发生一个事件，则 $\widehat\Lambda(3)=1/5+1/4+1/2=0.95$，相应方差估计为 $1/5^2+1/4^2+1/2^2=0.3525$。中间的删失只通过缩小后续风险集进入公式。

## 介绍

Nelson-Aalen 估计是右删失生存数据中累积风险函数的非参数估计。它不指定指数分布、Weibull 分布等参数形式，而是直接用计数过程记录事件、用风险过程记录每个时刻仍在观察且尚未发生事件的人。Aalen 的计数过程鞅理论给出了估计误差、方差估计与渐近正态性的统一解释，因此该结果不只是一个人为设定的求和公式。

## 分析

**前置依赖**：生存函数与风险函数、独立右删失、计数过程与强度过程、补偿子和鞅、可料二次变差、Lenglart 不等式及鞅中心极限定理。

**定理内容**：设 $(T_i,C_i)$ 独立同分布，$T_i$ 与 $C_i$ 相互独立，$T_i$ 具有共同风险 $\alpha$；观测为

$$
X_i=T_i\wedge C_i,
\qquad
\delta_i=\mathbf 1_{\{T_i\leq C_i\}}.
$$

定义个体及总计数过程、风险过程

$$
N_i(t)=\mathbf 1_{\{X_i\leq t,\delta_i=1\}},
\qquad Y_i(t)=\mathbf 1_{\{X_i\geq t\}},
$$

$$
N(t)=\sum_{i=1}^nN_i(t),
\qquad Y(t)=\sum_{i=1}^nY_i(t).
$$

$Y(t)$ 是时刻 $t$ 前一刻的风险集大小，$N(t)$ 是截至 $t$ 观察到的事件总数。令目标风险为 $\alpha(t)$，累积风险为 $\Lambda(t)=\int_0^t\alpha(s)\,ds$。在独立删失所保证的 Aalen 乘积强度模型下，$N$ 的强度为 $Y(t)\alpha(t)$，故

$$
M(t)=N(t)-\int_0^tY(s)\alpha(s)\,ds
$$

是鞅。令 $J(t)=\mathbf 1_{\{Y(t)>0\}}$，Nelson-Aalen 估计定义为

$$
\boxed{\widehat\Lambda(t)=\int_0^t\frac{J(s)}{Y(s)}\,dN(s)
=\sum_{T_{(j)}\leq t}\frac{d_j}{n_j}}
$$

其中 $T_{(j)}$ 是不同观测事件时刻，$d_j=\Delta N(T_{(j)})$，$n_j=Y(T_{(j)})$。积分中的 $J/Y$ 在 $Y=0$ 时按 $J/Y=0$ 理解。

其常用 Aalen 方差估计为

$$
\boxed{\widehat\sigma^2(t)
=\int_0^t\frac{J(s)}{Y(s)^2}\,dN(s)
=\sum_{T_{(j)}\leq t}\frac{d_j}{n_j^2}}.
$$

若在 $[0,\tau]$ 上 $Y(s)/n$ 一致依概率趋于正函数 $y(s)$，则 $\widehat\Lambda$ 一致相合，并且

$$
\sqrt n\{\widehat\Lambda(\cdot)-\Lambda(\cdot)\}
\Longrightarrow W(\sigma^2(\cdot)),
\qquad
\sigma^2(t)=\int_0^t\frac{\alpha(s)}{y(s)}\,ds,
$$

其中 $W$ 为 Wiener 过程，极限在适当 Skorokhod 空间中取得；同时 $n\widehat\sigma^2(t)\xrightarrow{p}\sigma^2(t)$。因此 $\widehat\sigma^2(t)$ 估计的是 $\widehat\Lambda(t)$ 的渐近方差，而不是 $\sqrt n$ 标准化后方差过程的尺度。

## 思考过程

在很短的时间间隔内，若风险集有 $Y(s)$ 人、单位时间风险为 $\alpha(s)$，期望事件数约为 $Y(s)\alpha(s)ds$。所以观测事件增量 $dN(s)$ 除以 $Y(s)$，就近似于 $\alpha(s)ds$。把所有增量相加便得到累积风险。

删失者不是被当成事件发生，而是在其最后观察时间之后离开风险集；事件者也在事件后离开。真正需要警惕的是 $Y=0$ 时无法估计风险，以及研究末尾风险集很小时 $1/Y$ 会放大波动。鞅分解把“可预测的系统风险”与“不可预测的随机波动”分开，方差估计则正来自随机波动部分的二次变差。

## 证明过程

### 1. 鞅误差分解

由 $dN=Y\alpha\,dt+dM$ 及 $J/Y\cdot Y=J$，有

$$
\begin{aligned}
\widehat\Lambda(t)-\Lambda(t)
&=\int_0^t\frac{J(s)}{Y(s)}\,dM(s)
+\int_0^t\{J(s)-1\}\alpha(s)\,ds\\
&=\int_0^t\frac{J(s)}{Y(s)}\,dM(s)
-\int_0^t(1-J(s))\alpha(s)\,ds .
\end{aligned}
$$

若整个 $[0,t]$ 上风险集始终非空，第二项为零；若风险集提前为空，则估计只恢复风险集可观察部分，不能无条件声称全区间无偏或相合。

### 2. 方差公式

在风险集非空的区间上，误差鞅为 $\widetilde M(t)=\int_0^tJ(s)Y(s)^{-1}dM(s)$。由随机积分的等距性质，

$$
\langle\widetilde M\rangle(t)
=\int_0^t\frac{J(s)}{Y(s)^2}\,d\langle M\rangle(s)
=\int_0^t\frac{J(s)}{Y(s)}\alpha(s)\,ds .
$$

以 $dN(s)$ 替换其可料补偿子 $Y(s)\alpha(s)ds$，得到可计算的方差估计

$$
\widehat\sigma^2(t)=\int_0^tJ(s)Y(s)^{-2}dN(s).
$$

这就是每个事件时刻加入 $d_j/n_j^2$ 的原因。

### 3. 一致性

若 $Y/n\xrightarrow{p}y$ 且 $y$ 在 $[0,\tau]$ 上有正下界，则

$$
\int_0^\tau\frac{nJ(s)}{Y(s)}\alpha(s)\,ds
\xrightarrow{p}\int_0^\tau\frac{\alpha(s)}{y(s)}\,ds<\infty,
$$

而未标准化的可料变差按 $n^{-1}$ 阶缩小。对误差鞅使用 Lenglart 不等式，可得

$$
\sup_{0\leq t\leq\tau}|\widehat\Lambda(t)-\Lambda(t)|\xrightarrow{p}0.
$$

### 4. 渐近正态与方差相合

对标准化鞅

$$
\sqrt n\{\widehat\Lambda(t)-\Lambda(t)\}
=\int_0^t\frac{\sqrt nJ(s)}{Y(s)}\,dM(s)
$$

验证鞅中心极限定理的可料变差收敛及跳跃渐近可忽略条件，便得到独立增量高斯极限，其方差函数为 $\sigma^2(t)$。同一收敛还给出

$$
n\widehat\sigma^2(t)
=\int_0^t\frac{nJ(s)}{Y(s)^2}dN(s)
\xrightarrow{p}\int_0^t\frac{\alpha(s)}{y(s)}ds.
$$

于是 $\widehat\Lambda(t)\pm z_{1-\alpha/2}\widehat\sigma(t)$ 给出逐点渐近置信区间；若构造同时置信带则需另行使用全过程分布，不能把逐点临界值直接当作全带临界值。$\square$

## 课堂问答

**老师**：Nelson-Aalen 公式里的风险集和计数过程各自做什么？

**学生**：$Y(t)$ 记录时刻 $t$ 仍在观察且尚未发生事件的人数，$N(t)$ 记录累计事件数。估计用 $\int J/Y\,dN$ 累加风险贡献，在事件时刻写为 $d_j/n_j$；删失只让个体退出后续风险集，不会被当成一次事件。

**老师（追问）**：为什么方差估计是 $\sum d_j/n_j^2$，而不是 $\sum d_j/n_j$？

**学生**：误差是随机积分 $\int J/Y\,dM$，被积函数为 $1/Y$，其可料二次变差带平方因子 $1/Y^2$。又因 $d\langle M\rangle=Y\alpha\,dt$，真实渐近尺度含 $\int\alpha/Y\,dt$，用 $dN$ 估计补偿子后就是 $\int J/Y^2dN=\sum d_j/n_j^2$。

**老师（拓展）**：公式是否自动保证研究末端也可靠？它与 Kaplan-Meier 估计怎样连接？

**学生**：不保证。末端 $Y$ 很小会放大误差，$Y=0$ 后还出现不可识别项 $-\int(1-J)\alpha\,dt$；一致性与渐近正态性需要 $Y/n$ 有正极限下界。Kaplan-Meier 使用乘积积分 $\widehat S(t)=\prod_{s\leq t}(1-d\widehat\Lambda(s))$，在无同时事件的连续模型中可写成 $\prod(1-d_j/n_j)$；它与 $e^{-\widehat\Lambda}$ 相近，但二者不是逐字相同的定义。

## 相关条目

- [Kaplan-Meier 估计的一致性](./Kaplan-Meier估计的一致性.md)
- [Log-rank 检验的渐近分布](./Log-rank检验的渐近分布.md)
- [可料二次变差与可选采样恒等式](./可料二次变差与可选采样恒等式.md)
- [鞅不等式](./鞅不等式.md)
- [鞅中心极限定理](../第41级-随机过程/鞅中心极限定理.md)：直接前置依赖。
