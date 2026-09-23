# Hamilton 张量极值原理

> **一句话大白话**：张量方程里的"扩散项"（Laplacian）本身只会把张量的极值方向磨平，真正可能把某个方向"由正变负"的只有反应项；只要反应项在临界（特征值为零）的方向上不把张量往负方向推，那么初始非负的张量就永远非负。

> **小例子**：Ricci 流中曲率算子 $R$ 满足 $\partial_t R=\Delta R+\Phi(R)$；若 $\Phi$ 是"零特征向量保持"的（对 $R$ 的零特征方向 $v$ 有 $v^{\mathsf T}\Phi\,v\ge 0$），则 $R\ge 0$ 在流下保持。Hamilton 用这一原理证明 Ricci 流保持非负曲率算子，进而得到三维流形的曲率夹逼。

## 一、定理介绍

> **前置依赖**：极大值原理、Laplace–Beltrami 算子与热方程、对称张量的谱分解、Riemann 曲率张量、Bochner公式。

Hamilton 张量极值原理（1982）是 Richard Hamilton 为研究 Ricci 流而建立的核心工具。标量极值原理断言：若 $u$ 满足 $\partial_t u\le\Delta u+c\,u$ 且初值非正，则 $u$ 保持非正；它在张量上失效，因为张量的"非负"不是一个数，而是一个在切空间上逐点取值的凸性条件，而 Laplacian 与逐点凸性的相互作用需要仔细分析。

Hamilton 的观察是：Laplacian 对张量最"坏"的方向恰好是它自身的最小特征方向，而在该方向上扩散项的贡献可以被最小特征函数的二阶导数所控制；因此只要反应项 $\Phi$ 不把处于临界（零特征值）方向的分量推向负值，正性就能保持。这一原理是几何流中"曲率条件保持"类结论的统一入口，后被 Böhm–Wilking 推广到一般闭凸集的情形。

## 二、原理思路

1. **把张量条件化为数量条件**：对对称 2-张量 $S$，命 $f(S)=\lambda_{\min}(S)$。$S\ge0$ 等价于 $f\ge0$，而 $f$ 关于 $S$ 是凹函数（最小特征值是线性函数的下确界），凹性正是极值原理在非光滑情形仍然可用的关键。
2. **求 $f$ 的演化不等式**：在使 $\lambda_{\min}$ 达到时空最小值的点 $p$ 处，取 $S$ 的特征标架使 $v$ 为最小特征方向；计算 $\partial_t\lambda_{\min}=v^{\mathsf T}\partial_t S\,v$，并把 $v^{\mathsf T}(\Delta S)v$ 与 $\Delta\lambda_{\min}$ 比较，得到抛物不等式 $\partial_t f\ge\Delta f+(\text{低阶项})$。
3. **用"零特征向量"条件控制反应项**：临界情形下 $f=0$，反应项的符号由 $v^{\mathsf T}\Phi v$ 决定。
4. **收尾**：若首次出现 $f<0$，则在时空内点取到 $f$ 的负极小值，与该点处抛物极值原理矛盾。

## 三、定理的严格表述

设 $M$ 是紧流形，$S(t)$ 是沿 $M\times[0,T)$ 的对称 2-张量族，$\Phi$ 是由 $S$ 与 $\nabla S$ 决定的对称 2-张量（"反应项"），满足

$$
\partial_t S=\Delta S+\Phi(S,\nabla S),\qquad S(0)=S_0 .
$$

**定理（Hamilton 张量极值原理）**：设 $\Phi$ 是**零特征向量保持**的，即对任意 $x\in M$ 与任意 $t$，只要 $S\ge0$ 且 $v$ 满足 $S v=0,\ |v|=1$，就有

$$
v^{\mathsf T}\,\Phi\,v\ \ge\ 0 ,
$$

则 $S_0\ge0$ 蕴含 $S(t)\ge0$ 对一切 $t\in[0,T)$ 成立。

**凸集形式（Böhm–Wilking）**：把"$S\ge0$"换成"$S$ 的谱落在 $\mathbb R^n$ 中某个 $\mathrm{O}(n)$-不变的闭凸集 $C$ 内"，把"零特征向量条件"换成"$C$ 在 $S$ 处的切锥条件"，结论同样成立。

## 四、证明过程

**步骤 1（最小特征函数的凸性与 $f=0$ 处的标架）。** 命 $f=\lambda_{\min}(S)$。因 $f(S)=\inf_{|v|=1}v^{\mathsf T}Sv$，它是 $S$ 的凹函数。设时空区域中首次出现 $f<0$，则由 $M$ 紧故 $f$ 在某内点 $(p,t_0)$ 取得严格负的时空极小值。在 $p$ 处取 $S$ 的特征标架 $e_1,\dots,e_n$，使 $f=\lambda_1$，对应单位特征向量 $v=e_1$。若 $f(p,t_0)<0$，则 $\lambda_1<0$；关键处在于把结论归结为"临界"情形 $\lambda_1=0$：令 $\tilde S=S-f\,g$，则 $\tilde S\ge0$ 且在 $(p,t_0)$ 的 $\lambda_{\min}(\tilde S)=0$，而常数平移只改变反应项的时间项，不影响下面的空间估计。故只需处理 $v^{\mathsf T}\tilde S v=0$。

**步骤 2（扩散项的比较）。** 取 $p$ 处测地法坐标，使 $\nabla g$ 的一阶项消失。在 $(p,t_0)$ 有 $\Delta f\le v^{\mathsf T}(\Delta S)v$：这是因为在时空极小点处 $\nabla f=0$，而 $\nabla^2 f\le\nabla^2(v^{\mathsf T}Sv)$（$f$ 是线性函数族的下确界，且 $v$ 在该点实现下确界），于是 $\Delta f=\mathrm{tr}\nabla^2 f\le \mathrm{tr}\big(v^{\mathsf T}\nabla^2 S\,v\big)=v^{\mathsf T}\Delta S\,v$。

**步骤 3（演化不等式）。** 由 $\partial_t f=v^{\mathsf T}\partial_tS\,v+v^{\mathsf T}S\,\partial_tv$ 及 $\partial_tv\perp v$（$v$ 是单位特征向量），第二项为零，故

$$
\partial_t f=v^{\mathsf T}\Delta S\,v+v^{\mathsf T}\Phi v\ \ge\ \Delta f+v^{\mathsf T}\Phi v .
$$

**步骤 4（矛盾）。** 在 $f=0$ 的临界点处，$v$ 是零特征向量，故由假设 $v^{\mathsf T}\Phi v\ge0$，从而 $\partial_t f\ge\Delta f$。而在时空极小点处 $\partial_t f\le0$ 且 $\Delta f\ge0$，于是 $\Delta f=0$ 且不等式取等；但这要求 $f\equiv0$ 于该点附近的所有方向（时空极小点处 $\Delta f\ge0,\ \partial_tf\le0$ 与 $\partial_tf\ge\Delta f$ 只能同时取零），与"首次出现 $f<0$"矛盾。故 $f\ge0$ 恒成立，即 $S(t)\ge0$。

**步骤 5（凸集推广的要点）。** 对一般闭凸集，用"距离函数 $\mathrm{dist}(\cdot,C)$ 的光滑化 + 支撑函数表示"替换 $\lambda_{\min}$：$C$ 在 $S$ 处的内法锥由"使 $S$ 的谱落到边界"的方向描述，凸性保证距离函数沿张量方向仍凹，切锥条件保证反应项不把 $S$ 推出 $C$；其余步骤与上面完全平行。$\square$

## 五、应用与意义

- **Ricci 流**：Hamilton 用它证明 $\mathrm{Ric}\ge0$、非负曲率算子等条件在流下保持，是三维球面定理与曲率夹逼（pinching）估计的技术基础。
- **平均曲率流**：对应的张量极值原理用于保持第二基本形式的正性（凸超曲面保持凸性）。
- **一般几何流**：Böhm–Wilking 的闭凸集版本统一了各类"曲率条件保持"结论，成为曲率流研究的标准工具。

## 相关条目

- [平均曲率流](./平均曲率流.md)：张量极值原理保证凸性在流下保持。
- [曲率估计与单调公式](./曲率估计与单调公式.md)：用张量极值原理导出曲率夹逼估计。
- [Riemann 曲率张量](../第33级-微分几何/Riemann曲率张量.md)：张量极值原理作用的对象。
- [极大值原理](../第49级-黎曼几何/极大值原理.md)：标量极值原理，是张量版本的出发点。
- [Bochner公式](../第49级-黎曼几何/Bochner公式.md)：确定扩散项（Weitzenböck 型公式）的符号结构。
