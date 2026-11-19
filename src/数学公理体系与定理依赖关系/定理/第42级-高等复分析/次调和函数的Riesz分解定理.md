# 次调和函数的 Riesz 分解定理

> **一句话大白话**：一个次调和函数可以拆成“没有源的调和背景”与“由内部质量分布产生的势”两部分；这份质量分布就是分布意义下的 $\Delta u$。
>
> **小例子**：平面上的 $u(x)=\log|x|$ 在 $x\ne0$ 处调和，在原点有次调和奇性。它的 Riesz 测度是 $2\pi\delta_0$，取含原点的区域后，调和部分可取下为零，势部分正是 $\log|x|$。

## 介绍

Riesz 分解定理是次调和函数论的局部结构定理。它把次调和性集中到一个非负 Radon 测度上，并使位势论中的测度、Green 表示公式、容量和 Perron 方法能够互相转换。定理的关键是“局部”：一般先在有紧包含于原区域的子区域上分解，而不是不加条件地声称全空间存在一个收敛的牛顿势。

## 分析

**前置依赖**：上半连续函数、分布与正分布、Laplace 算子基本解、Green 恒等式、Radon 测度、调和函数。

**定理内容**：设 $\Omega\subseteq\mathbb R^n$ 为区域，$u:\Omega\to[-\infty,\infty)$ 上半连续、$u\in L^1_{\mathrm{loc}}(\Omega)$，且为次调和函数（等价地，$\Delta u\ge0$ 以分布意义成立），并设 $u$ 不在任何连通分支上恒等于 $-\infty$。则存在唯一的非负 Radon 测度 $\mu_u$，称为 $u$ 的 **Riesz 测度**，使

$$
\Delta u=\mu_u
\qquad\text{于 }\mathcal D'(\Omega).
$$

对每个相对紧子区域 $D\Subset\Omega$，存在调和函数 $h_D$，使得

$$
u(x)=h_D(x)+N_D\mu_u(x),
\qquad
N_D\mu_u(x)=\int_D\Phi_n(x-y)\,\mathrm d\mu_u(y),
$$

其中等式按通常的次调和函数代表理解，势函数局部可积。这里采用 $\Delta\Phi_n=\delta_0$ 的基本解约定：

$$
\Phi_n(x)=
\begin{cases}
\dfrac{|x|}{2}, & n=1,\\[4pt]
\dfrac{1}{2\pi}\log|x|, & n=2,\\[4pt]
-\dfrac{1}{(n-2)\omega_n}|x|^{2-n}, & n\ge3,
\end{cases}
$$

$\omega_n$ 是单位球面 $S^{n-1}$ 的面积。因而 $n\ge3$ 时 $N_D\mu_u\le0$。若改用正核 $\Gamma_n=-\Phi_n$，即 $-\Delta\Gamma_n=\delta_0$，同一公式写成

$$
u=h_D-\int_D\Gamma_n(x-y)\,\mathrm d\mu_u(y).
$$

二维不能套用 $r^{2-n}$，必须使用对数核；三维时 $\Phi_3(x)=-1/(4\pi|x|)$。调和部分 $h_D$ 一般依赖于 $D$。

## 思考过程

光滑次调和函数满足 $\Delta u\ge0$，Green 表示公式已经把 $u$ 写成“$\Delta u$ 的基本解卷积”加边界调和项。一般次调和函数没有经典二阶导数，就用磨光把 $\Delta u$ 变成光滑非负函数，再让磨光参数趋于零。非负分布必为测度，而基本解卷积给出 Riesz 势；剩余部分的 Laplacian 为零，因而是调和函数。

## 证明过程

**证明纲要**：

1. **磨光**：在 $D$ 的一个稍大邻域内作标准磨光 $u_\varepsilon=u*\rho_\varepsilon$。则 $u_\varepsilon$ 光滑且次调和，$\Delta u_\varepsilon\ge0$，并且 $u_\varepsilon\to u$ 于 $L^1_{\mathrm{loc}}$。
2. **取出 Riesz 测度**：对任意非负试验函数 $\varphi\in C_c^\infty(\Omega)$，定义
   $$
   \langle\mu_u,\varphi\rangle=\langle u,\Delta\varphi\rangle .
   $$
   次调和性说明这是正分布；正分布由唯一非负 Radon 测度表示，且 $\Delta u_\varepsilon$ 以测度弱收敛到 $\mu_u$。因此 $\mu_u=\Delta u$ 是唯一的。
3. **使用 Green 表示**：在 $D$ 上把 $u_\varepsilon$ 写成基本解与 $\Delta u_\varepsilon$ 的卷积，再加上一个由边界项产生的调和函数 $h_{D,\varepsilon}$。固定基本解的上述符号，就有
   $$
   u_\varepsilon=h_{D,\varepsilon}+\Phi_n*(\Delta u_\varepsilon).
   $$
4. **取极限**：局部测度质量一致有界，使 $\Phi_n*(\Delta u_\varepsilon)$ 在局部可积意义下趋于 $N_D\mu_u$。相应的 $h_{D,\varepsilon}$ 在内部紧集上一致收敛到调和函数 $h_D$，得到所需分解。
5. **识别调和部分**：对分解式取分布 Laplacian，利用 $\Delta\Phi_n=\delta_0$ 得 $\Delta(u-h_D)=\mu_u$ 在 $D$ 内成立，故 $\Delta h_D=0$。Weyl 引理说明 $h_D$ 可取为经典光滑调和函数。$\square$

## 课堂问答

**老师**：为什么 Riesz 分解通常先写成局部公式，而不是直接在 $\Omega$ 上全局卷积？

**学生**：因为 $\mu_u$ 的总质量或其在无穷远的增长可能使全局势不收敛。取 $D\Subset\Omega$ 后只积分局部有限质量，收敛性有保障；代价是调和部分 $h_D$ 要随 $D$ 调整，额外条件满足时才能拼成全局表示。

**老师（追问）**：二维与高维的核为什么不能混写？

**学生**：基本解由维数决定。二维有 $\Delta((2\pi)^{-1}\log|x|)=\delta_0$；$n\ge3$ 才有带负号的 $r^{2-n}$ 核。二维若机械代入 $r^{2-n}$ 会得到常数 $1$，完全不可能是 $\delta_0$ 的基本解。

**老师（拓展）**：Riesz 测度与调和部分各自唯一吗？

**学生**：$\mu_u$ 作为分布 $\Delta u$ 在 $\Omega$ 上唯一。固定 $D$ 和势的上述定义后，$h_D=u-N_D\mu_u$ 也随之唯一且调和；但换子区域或改用不同边界归一化的 Green 核时，调和部分会相应改变，不能把它当成不依赖区域的全局常数项。

## 相关条目

- [Perron 方法与 Dirichlet 问题](./Perron方法与Dirichlet问题.md)
- [强极大值原理](../第49级-黎曼几何/强极大值原理.md)
- [主教程第55级：位势论](../../../05-高阶专题I-分析几何统计/第55级-位势论.md)
