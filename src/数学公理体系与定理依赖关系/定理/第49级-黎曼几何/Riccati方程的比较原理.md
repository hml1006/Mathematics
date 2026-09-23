# Riccati方程的比较原理

> **一句话大白话**：对形如 $u'+u^2+k=0$ 的方程，初值大的一直大；若只满足不等式，也会被精确解压住，于是曲率的上下界就能变成几何量的上下界。

> **小例子**：$v'=-v^2$、$v(0)=1$ 的解是 $v(t)=\frac{1}{t+1}$。若 $u(0)=1$ 且 $u'\le-u^2$，则 $u(t)\le v(t)$：初值相同而不等式的方向使 $u$ 增长得更慢。

## 介绍

Riccati 方程得名于意大利数学家 Jacopo Riccati（1724 年研究该方程），形如 $u'+u^2+k(t)=0$ 的方程一般不能初等积出，但它的比较性质极强。在黎曼几何中，Riccati 方程的比较原理是"曲率控制几何"的核心机制：沿测地线的距离函数 $r$ 的 Laplacian $\Delta r$，以及测地极坐标下体积元的对数导数，都满足一条 Riccati 方程或不等式，其中的零阶项恰好是 Ricci 曲率。把它与模型空间（球面、欧氏空间、双曲空间）的精确解比较，就得到 Laplacian 比较定理、Bishop–Gromov 体积比较、Bonnet–Myers 直径估计以及 Cartan–Hadamard 定理。本质上，它把 Jacobi 场方程这一二阶线性方程化为一个一阶非线性方程的比较问题，使几何估计从线性代数转入常微分方程工具。

## 分析

**前置依赖**：测地线与 Jacobi 场、Jacobi 场方程、Ricci 曲率、Laplace–Beltrami 算子、一阶常微分方程解的存在唯一性、Gronwall 不等式。

**定理内容**：设 $k\in C^0[0,T)$，$u,v$ 在 $[0,T)$ 上可微，$v$ 满足等式

$$
v'(t)+v(t)^2+k(t)=0,
$$

而 $u$ 满足不等式

$$
u'(t)+u(t)^2+k(t)\le0 .
$$

若 $u(0)\le v(0)$，则在 $v$ 有定义的区间上 $u(t)\le v(t)$。若不等式与初值方向同时反向（$u'\ge0$ 型且 $u(0)\ge v(0)$），则 $u(t)\ge v(t)$。

几何中的常用形式：设 $\mathrm{Ric}\ge(n-1)k$，距离函数满足 $u'+\frac{u^2}{n-1}+(n-1)k\le0$（$u=\Delta r$），令 $w=\frac{\Delta r}{n-1}$ 即得 $w'+w^2+k\le0$，与模型空间满足等式 $w_0'+w_0^2+k=0$ 的解比较，便得 $\Delta r\le(n-1)w_0$。

**推论**：取 $k\equiv0$ 并令 $w_0\to+\infty$（$t\to0$）可得 $\Delta r\le\frac{n-1}{r}$ 等经典的 Laplacian 比较不等式。

## 思考过程

比较原理的标准证法是"首次接触点"论证：先假设某一时刻起 $u>v$，由连续性存在最小的 $t_0$ 使 $u(t_0)=v(t_0)$ 且之前 $u\le v$。于是在 $t_0$ 处 $u'\ge v'$（$u$ 从下方追上并即将超过）。另一方面把两个式子相减，在接触点 $u=v$ 处 $u^2=v^2$，故 $u'-v'\le-(u^2-v^2)=0$，即 $u'\le v'$，矛盾。这一论证的美妙之处在于：它避开了对 $u+v$ 变号的细致讨论，也避开了直接解不等式，只用到接触点处的代数事实。几何版本的难点在于先由 Jacobi 场或第二变分导出 $\Delta r$ 所满足的 Riccati 不等式。

## 证明过程

**步骤 1：化归到首次接触点。** 设结论不成立，即存在 $t\in[0,T)$ 使 $u(t)>v(t)$。由连续性，集合 $\{t:u(t)>v(t)\}$ 非空开，令

$$
t_0=\inf\{t\ge0: u(t)>v(t)\}.
$$

则 $t_0>0$（因为 $u(0)\le v(0)$），且 $u(t_0)=v(t_0)$、$u(t)\le v(t)$ 于 $[0,t_0]$。

**步骤 2：在接触点比较导数。** 差函数 $u-v$ 在 $[0,t_0]$ 上非正、在 $t_0$ 处等于零，故它在 $t_0$ 处以非正的方式到达零点，于是

$$
u'(t_0)-v'(t_0)\ge0 . \tag{$\ast$}
$$

**步骤 3：由方程与不等式导出相反结论。** 把两条式子相减：

$$
\big(u'(t_0)+u(t_0)^2+k(t_0)\big)-\big(v'(t_0)+v(t_0)^2+k(t_0)\big)\le0 .
$$

利用 $u(t_0)=v(t_0)$ 得 $u(t_0)^2=v(t_0)^2$，所以

$$
u'(t_0)-v'(t_0)\le0,
$$

与 $(\ast)$ 矛盾。

**步骤 4：结论。** 故不存在 $t$ 使 $u(t)>v(t)$，即 $u(t)\le v(t)$ 于 $[0,T)$。反向不等式的证明完全相同：把不等号全部反向，接触点处的导数条件变为 $u'(t_0)\le v'(t_0)$，而方程给出 $u'(t_0)\ge v'(t_0)$，同样矛盾。

**步骤 5：几何应用的关键一步。** 在测地极坐标下，设 $\mathcal A=\mathrm{Hess}\,r$ 为距离函数的 Hessian（限制在 $\dot\gamma$ 的正交补上），由 Jacobi 场方程 $J''+R(J,\dot\gamma)\dot\gamma=0$ 可得矩阵 Riccati 方程

$$
\mathcal A'+\mathcal A^2+R_\gamma=0,
$$

其中 $R_\gamma$ 是沿 $\gamma$ 的曲率算子。取迹并记 $u=\mathrm{tr}\,\mathcal A=\Delta r$，由 Cauchy–Schwarz 不等式 $\mathrm{tr}(\mathcal A^2)\ge\frac{(\mathrm{tr}\,\mathcal A)^2}{n-1}$ 得

$$
u'+\frac{u^2}{n-1}+\mathrm{Ric}(\dot\gamma,\dot\gamma)\le0 .
$$

若 $\mathrm{Ric}\ge(n-1)k$，则 $u'+\frac{u^2}{n-1}+(n-1)k\le0$。令 $w=\frac{u}{n-1}$，即 $w'+w^2+k\le0$；与模型空间（常曲率 $k$）中满足 $w_0'+w_0^2+k=0$ 的解比较，由步骤 4 得 $w\le w_0$，即 Laplacian 比较定理。

证毕。

## 相关条目

- [Laplacian比较定理](./Laplacian比较定理.md)：由距离函数满足的 Riccati 不等式与模型空间比较直接得到。
- [测地线与Jacobi场](./测地线与Jacobi场.md)：Jacobi 场方程取迹后化为这里的 Riccati 方程。
- [Rauch比较定理](./Rauch比较定理.md)：Jacobi 场长度与模型空间的比较，是 Riccati 比较的 Jacobi 场版本。
- [Gronwall不等式](../第23级-常微分方程/Gronwall不等式.md)：微分不等式的另一种比较工具，与首次接触点论证互为补充。
