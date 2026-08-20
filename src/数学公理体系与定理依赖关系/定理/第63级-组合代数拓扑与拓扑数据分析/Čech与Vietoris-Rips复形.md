# Čech 与 Vietoris-Rips 复形：点云拓扑重建

> **一句话大白话**：把散落的采样点变成一组随时间半径膨胀的三角网络——什么时候点连成线、线围成面，随着半径变大逐级浮现，就重建出了底层空间的形状结构。
>
> **小例子**：取圆环上的采样点，半径大到每点与相邻点重叠成三角形时，Čech/Rips 复形呈现出圆环形状，其 $H_1$ 给出一个环（Betti 数 $1$）。

## 一、定理介绍

点云（point cloud）是拓扑数据分析的常见输入。Čech 复形与 Vietoris–Rips 复形是从点云构造单纯复形的两类核心方法：前者记录以给定点为中心、半径 $r$ 的球何时有公共交；后者把任意直径不超过 $r$ 的点集连成一个单纯形。二者都随半径 $r$ 变化形成 filtration，并通过 nerve 定理或包含关系实现对底层空间拓扑的近似重建。

## 二、原理思路

1. **Nerve 定理**：若一族拓扑空间 $\{U_\alpha\}$ 构成“好覆盖”（即任意非空交可缩），则这些交的 nerve 复形与覆盖的并空间同伦等价。
2. **Čech 复形**：取点云 $X$ 中每点为中心、半径 $r$ 的球，其 nerve 就是 Čech 复形；在欧氏空间中这些球构成好覆盖，因此 Čech 复形同伦等价于这些球的并。
3. **Vietoris–Rips 复形**：仅依赖点云自身的度量，把所有直径不超过 $r$ 的子集作为单纯形，计算更简单但可能包含伪洞。
4. **二者关系**：在任意度量空间中，Vietoris–Rips 与 Čech 复形互相夹逼，形成计算与拓扑精度之间的权衡。

## 三、定理的严格表述

设 $(X,d)$ 为度量空间，$X$ 为有限点集，$r>0$。

**Čech 复形**：
$$
\operatorname{\check{C}ech}(X,r) = \left\{ \sigma\subseteq X \;:\; \bigcap_{x\in\sigma} B(x,r) \neq \varnothing \right\},
$$
其中 $B(x,r)=\{y\in X\text{ 所在空间}: d(x,y)<r\}$。

**Vietoris–Rips 复形**：
$$
\operatorname{VR}(X,r) = \left\{ \sigma\subseteq X \;:\; \operatorname{diam}(\sigma)\le r \right\},
$$
其中 $\operatorname{diam}(\sigma)=\max_{x,y\in\sigma} d(x,y)$。

**Nerve 定理**：若 $\mathcal{U}=\{B(x,r)\}_{x\in X}$ 是欧氏空间（或更一般地、任意非空交可缩的空间）中的好覆盖，则
$$
\operatorname{\check{C}ech}(X,r) \simeq \bigcup_{x\in X} B(x,r).
$$

**Čech–Vietoris–Rips 夹逼关系**：在任意度量空间中，有包含
$$
\operatorname{VR}(X,r) \subseteq \operatorname{\check{C}ech}(X,r) \subseteq \operatorname{VR}(X,2r).
$$
进一步，若 $X$ 所在空间满足每个直径不超过 $2r$ 的集合可缩（例如欧氏空间中的凸集），则上述包含诱导的同调映射在适当尺度下是可控的，从而可用 Vietoris–Rips 复形的 filtration 逼近 Čech filtration 的持久同调。

## 四、证明过程

**步骤 1：Vietoris–Rips 包含于 Čech。**
若 $\sigma\in\operatorname{VR}(X,r)$，则 $\operatorname{diam}(\sigma)\le r$。任取 $y\in\sigma$，对任意 $x\in\sigma$ 有 $d(x,y)\le r$，故 $y\in B(x,r)$。于是 $y\in\bigcap_{x\in\sigma}B(x,r)$，交非空，$\sigma\in\operatorname{\check{C}ech}(X,r)$。

**步骤 2：Čech 包含于 Vietoris–Rips(2r)。**
若 $\sigma\in\operatorname{\check{C}ech}(X,r)$，则存在 $y$ 使得 $d(x,y)<r$ 对所有 $x\in\sigma$ 成立。于是对任意 $x,x'\in\sigma$，
$$
d(x,x')\le d(x,y)+d(y,x')<2r,
$$
故 $\operatorname{diam}(\sigma)<2r$，$\sigma\in\operatorname{VR}(X,2r)$。

**步骤 3：Nerve 定理的证明概要。**
构造 nerve 复形 $N(\mathcal{U})$ 与并空间 $Y=\bigcup U_\alpha$ 之间的同伦等价。取单位分解 $\{\phi_\alpha\}$ 从属于覆盖，定义映射 $g:Y\to |N(\mathcal{U})|$ 为 $g(y)=\sum_\alpha \phi_\alpha(y)\,e_\alpha$（重心坐标），其中 $e_\alpha$ 是 nerve 中对应 $U_\alpha$ 的顶点。反之，由每个非空 nerve 单形对应覆盖中可缩交，可收缩地定义 $|N(\mathcal{U})|\to Y$。这两个映射互为同伦逆。

**步骤 4：持久同调的逼近。**
由夹逼关系， filtration $\{\operatorname{VR}(X,r)\}_r$ 与 $\{\operatorname{\check{C}ech}(X,r)\}_r$ 是 $2$-interleaved，故它们诱导的持久同调在 bottleneck 距离下相差不超过 $\log 2$（若取对数尺度则相差常数），结合稳定性定理即得可控的拓扑重建误差。

## 五、应用与意义

- **点云形状推断**：从采样点恢复未知流形的同调，应用于计算机图形学、机器人感知与材料科学。
- **计算权衡**：Čech 复形拓扑精确但构造复杂（需检查高维交）；Vietoris–Rips 复形完全由成对距离决定，可用邻接矩阵高效实现，适合高维数据。
- **多尺度分析**：随半径 $r$ 变化形成的 filtration 与持久同调结合，可区分噪声与真实拓扑特征。
