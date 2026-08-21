# Jackson定理与Bernstein定理

> **一句话大白话**：函数越光滑，多项式逼近得越好（Jackson 定理给出"上界"）；反过来，只有很光滑的函数才可能被多项式快速逼近（Bernstein 逆定理给出"必要条件"）。
>
> **小例子**：$f\in C^{k}$ 可用次数 $n$ 的多项式逼近到 $O(n^{-k})$；而若逼近误差是 $O(\rho^n)$（$\rho<1$），则 $f$ 必为解析函数——光滑性与逼近速率互为镜子。

## 一、定理介绍

Weierstrass 定理只回答"能逼近"，而逼近的**速率**取决于函数的**光滑性**。Jackson 定理（正定理）给出：若 $f$ 具有 $k$ 阶连续导数，则最优多项式逼近误差 $\le C_k\,n^{-k}\|f^{(k)}\|_\infty$；Bernstein 逆定理（反定理）断言：若逼近误差衰减得足够快，则 $f$ 必具有相应的光滑性（乃至解析性）。二者合起来刻画了"逼近速率 $\leftrightarrow$ 光滑性"的精确对应，是逼近论最核心的量化结果。

## 二、原理思路

Jackson 用"磨光（用三角多项式/卷积核光滑化，再局部多项式化）"或在超精节点上插值，把 $f^{(k)}$ 的有界性转化为逼近误差的幂次衰减；常通过三角逼近加上 Bernstein 的"多项式到三角"转换完成。Bernstein 逆定理则用"有限差分/磨光算子"与逼近核对 $f$ 的导数进行估计，把小的逼近误差反推为 $f$ 的高阶可微性。两者的桥是"权多项式与磨光算子"控制定理。

## 三、定理的严格表述

**Jackson 定理（正定理，一维情形）**：设 $f^{(k)}\in\operatorname{Lip}\alpha$（$0<\alpha\le1$）或有界，则存在常数 $C_k$ 使 $f$ 在 $[a,b]$ 上次数 $\le n$ 的多项式最佳逼近满足
$$
E_n(f)=\inf_{\deg P\le n}\|f-P\|_\infty\ \le\ C_k\,n^{-(k+\alpha)}\,[f^{(k)}]_{\operatorname{Lip}\alpha},
$$
其中 $[g]_{\operatorname{Lip}\alpha}=\sup_{x\ne y}|g(x)-g(y)|/|x-y|^\alpha$。特别地，$f\in C^k$ 推出 $E_n(f)=O(n^{-k})$；$f$ 解析推出 $E_n=O(\rho^n)$（$\rho<1$）。

**Bernstein 逆定理**：若 $\sum_{n}n^{k-1}E_n(f)<\infty$（或 $E_n(f)=O(n^{-(k+\alpha)})$，$0<\alpha<1$），则 $f\in C^k$ 且 $f^{(k)}\in\operatorname{Lip}\alpha$。若 $E_n(f)=O(\rho^n)$，$\rho<1$，则 $f$ 在 $[a,b]$ 内解析。

## 四、证明过程

**Jackson 的上界估计（代表）**：设 $f\in C^k$。用 $n$ 阶三角/多项式逼近。核心思想是先对 $f^{(k)}$ 用 Bernstein 算子的卷积核做磨光：
1. 记 $f^{(k)}$ 有界。则对区间上的光滑逼近，可用"磨光算子" $K_m*f$（$m$ 阶 Fejér 或 Jackson 核）在离散点上插值。由 Jackson 核的正性、偶性及矩条件，卷积核 $K_m$ 满足 $K_m\ge0$、$\int K_m=1$、$\int |x|^r K_m=O(m^{-r})$。
2. 对 $h\sim1/n$ 的平移差分逼近，利用 $f^{(k)}$ 的 Lipschitz/有界，估计差商：
   $$
   \|f-K_n*f\|_\infty\le C\,m^{-k}\|f^{(k)}\|_\infty.
   $$
3. 将连续卷积在 $n+1$ 个 Chebyshev 节点上的插值多项式 $P_n$ 与 $K_n*f$ 比较，由插值误差定理和余项界得到 $E_n(f)=\|f-P_n\|_\infty\le C\,n^{-k}[f^{(k)}]_\bullet$。组装即得 Jackson 界。$\blacksquare$

**Bernstein 逆定理的反推（代表）**：设 $E_n(f)\le C n^{-(k+\alpha)}$。
1. 对任意 $h>0$，取 $m$ 阶"逆磨光"：用有限差分 $\Delta_h$ 与最佳逼近多项式结合，
   $$
   |\Delta_h^{r}f(x)|\le C\,(h)\,E_{\lfloor n\rfloor}(f)^{1/2}\cdots
   $$
   以控制 $r$ 阶差分，随 $h\to0$ 提取各阶导数。
2. 由 $k$-阶差分的 $O(h^\alpha)$ 估计推出 $f^{(k)}$ 存在且属 $\operatorname{Lip}\alpha$。解析情形：若 $E_n=O(\rho^n)$，则 $f$ 的一致控制使 Taylor 展开在实轴上收敛，再由解析延拓得区间内解析。$\blacksquare$

**注（Bernstein 的三项经验承担）** 通常先用 Bernstein 算子的一阶差分 + 三角形/多项式同构完成"差分配对"，保证导数阶与指数 $k+\alpha$ 精确匹配。

## 五、应用与意义

- **光滑性 ↔ 逼近速率的标尺**：给出逼近论基础的量化对应关系，是所有"收敛阶分析"的理论依据。
- **数值方法**：多项式插值、谱方法、有限元的收敛阶结论都可从 Jackson 型估计得到解释；反向的 Bernstein 逆定理说明为何不光滑函数用高次多项式逼近不划算。
- **Banach 空间刻画**：可用于刻画分数 Sobolev 空间、Lipschitz 空间、Besov 空间的函数类（最佳逼近的衰减刻画函数类），是现代逼近论与调和分析的交汇点。
- **实际意义**：指导如何选择逼近基与结点配置，以匹配目标函数的实际光滑度，避免 "Runge 现象"式的过度拆解。