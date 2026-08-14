# Dehn 手术定理

## 一、定理介绍

Dehn 手术是构造三维流形的经典方法：从三维球面 $S^3$ 中挖去一条纽结 $K$ 的管状邻域，得到纽结补集 $S^3 \setminus \mathring{N}(K)$，然后沿边界环面以不同的斜率重新粘合一个实心环面。这一过程可以产生极为丰富的闭三维流形。Dehn 手术定理（通常称为 Dehn 手术基本定理或 Wallace–Lickorish 定理）表明，每个闭可定向连通三维流形都可以从 $S^3$ 出发，通过沿某链环的分支施行适当斜率的 Dehn 手术得到。

## 二、原理思路

纽结补集 $M_K = S^3 \setminus \mathring{N}(K)$ 的边界为环面 $T^2$，其第一同调群 $H_1(\partial M_K; \mathbb{Z}) \cong \mathbb{Z}^2$ 由子午线 $\mu$ 和经线 $\lambda$ 生成。Dehn 手术沿一原始同调类

$$
p\mu + q\lambda \in H_1(\partial M_K; \mathbb{Z}), \quad \gcd(p,q)=1,
$$

进行，即将实心环面的子午线粘合到该斜率上。不同的互素整数对 $(p,q)$ 给出不同的闭三维流形 $K(p/q)$。 surgery 的关键在于：
- $p=0$ 对应于沿经线方向粘合，得到 $S^3$ 当且仅当 $K$ 平凡；
- $p=\pm 1$ 对应整数手术，是纽结 Floer 同调研究的核心；
- 一般有理斜率 $p/q$ 产生有理手术。

## 三、定理的严格表述

**定义（Dehn 手术）.** 设 $K \subset S^3$ 为纽结，$N(K) \cong S^1 \times D^2$ 为其管状邻域。取一原始同调类 $\gamma = p\mu + q\lambda \in H_1(\partial N(K); \mathbb{Z})$，其中 $\mu$ 为子午线、$\lambda$ 为经线，且 $\gcd(p,q)=1$。将 $N(K)$ 重新粘合到 $M_K = S^3 \setminus \mathring{N}(K)$ 上，使得新实心环面的子午线对应于 $\gamma$，所得闭三维流形记为 $K(p/q)$，称为沿斜率 $p/q$ 的 Dehn 手术结果。

**定理（Lickorish–Wallace）.** 每个闭可定向连通三维流形 $M$ 都同胚于沿 $S^3$ 中某个有向链环 $L = L_1 \cup \cdots \cup L_n$ 的各分支施行 Dehn 手术所得到的流形。换言之，存在互素整数对 $(p_i, q_i)$ 使得

$$
M \cong S^3(L_1(p_1/q_1), \dots, L_n(p_n/q_n)).
$$

更进一步，可以取 $q_i = \pm 1$ 对所有 $i$ 成立，即 $M$ 可由 $S^3$ 沿某链环施行 $\pm 1$ 整数手术得到。

## 四、证明过程

**Lickorish 证明概要.**

1. **映射环面的手术表示.** 任何闭可定向三维流形均可表示为映射环面或 Heegaard 分解。Lickorish 证明闭可定向曲面的映射类群由关于简单闭曲线的 Dehn 扭转生成。

2. **Dehn 扭转的几何实现.** 设 $\tau_c$ 为沿曲线 $c$ 的 Dehn 扭转。在 $S^3$ 中，沿围绕 $c$ 的平凡纽结施行 $\pm 1$ 整数手术，可以在边界曲面上实现 $\tau_c^{\pm 1}$。

3. **组合手术.** 将 Heegaard 分解的粘合同胚 $\varphi: \Sigma \to \Sigma$ 写成 Dehn 扭转的乘积
   $$
   \varphi = \tau_{c_1}^{\varepsilon_1} \circ \cdots \circ \tau_{c_m}^{\varepsilon_m}, \quad \varepsilon_j \in \{\pm 1\}.
   $$
   在 $S^3$ 中取围绕每条 $c_j$ 的 unknot 并做 $\varepsilon_j$ 手术，即可实现粘合映射，从而得到目标流形 $M$。

4. **化归为链环手术.** 这些 unknot  surgeries 可以组合为沿一条链环的分支进行的整数手术，完成定理证明。

## 五、应用与意义

Dehn 手术是低维拓扑中构造三维流形的万能方法。它深刻揭示了纽结理论与三维流形分类之间的联系：通过研究链环的手术结果，可以理解几乎所有闭三维流形的拓扑与几何性质。例如，Thurston 证明双曲纽结的绝大多数 Dehn 手术结果都具有双曲结构；Gordon–Luecke 定理指出，沿非平凡斜率的手术不会使纽结补集恢复为 $S^3$。Dehn 手术也是构造同调球面、Seifert 纤维空间和双曲流形的标准工具，并在量子拓扑、手术公式（如 Kirby 演算）以及 Casson 不变量、Ozsváth–Szabó 不变量的研究中占据核心地位。
