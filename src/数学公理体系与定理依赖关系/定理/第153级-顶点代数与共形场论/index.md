# 第153级-顶点代数与共形场论

> 一句话级别概述：顶点代数是二维共形场论的代数骨架：把无穷多个场算子打包成一条状态-场对应，用 Borcherds 恒等式统一编码算子乘积的奇异性。

## 级别简介

本级别从顶点代数与状态-场对应出发，建立 Virasoro 代数与中心荷，再引入顶点算子代数（VOA）的模不变性、Zhu 代数与 C2 余有限性；由此得到有理 VOA 的模张量范畴与 Verlinde 公式，最后以月光模与自由场实现收尾。

## 本级别定理

- [顶点代数的定义与 Borcherds 恒等式](./顶点代数的定义与Borcherds恒等式.md)：顶点代数 $(V,Y,\mathbf 1,\omega)$ 的状态-场对应 $Y(a,z)=\sum a_{(n)}z^{-n-1}$ 满足 Borcherds 恒等式 $\sum_{j\ge0}\binom{m}{j}(a_{(n+j)}b)_{(m+k-j)}=\sum_{j\ge0}(-1)^j\binom{n}{j}(a_{(m+n-j)}b_{(k+j)}-\dots)$。
- [Virasoro 代数与中心荷](./Virasoro代数与中心荷.md)：$[L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}(m^3-m)\delta_{m+n,0}$，$c$ 为中心荷，决定共形场论的"尺度反常"。
- [顶点算子代数与模不变性](./顶点算子代数与模不变性.md)：VOA 的配分函数 $Z(\tau)=\mathrm{tr}_{V}(q^{L_0-c/24})$ 在 $\mathrm{SL}_2(\mathbb Z)$ 下（投影）不变。
- [Zhu 代数与 $C_2$ 余有限性](./Zhu代数与C2余有限性.md)：$C_2$ 余有限（$\dim V/C_2(V)<\infty$）的 VOA 是有理的：模有限、半单，且 Zhu 代数为有限维半单代数。
- [有理顶点算子代数的模张量范畴](./有理顶点算子代数的模张量范畴.md)：有理 VOA 的模范畴构成模张量范畴，融合规则由模不变性与 Verlinde 公式给出。
- [Verlinde 公式](./Verlinde公式.md)：融合系数 $N_{ij}^{k}=\sum_{l}\frac{S_{il}S_{jl}\overline{S_{kl}}}{S_{0l}}$，其中 $S$ 为模变换矩阵。
- [Monstrous Moonshine 与 Borcherds 证明](./MonstrousMoonshine与Borcherds证明.md)：$j(\tau)-744=\sum_{n\ge-1}c(n)q^n$ 的系数 $c(n)$ 是 Monster 群不可约表示维数之和，由月光模 $V^\natural$ 的 graded 维数实现。
- [自由场实现与 Fock 空间](./自由场实现与Fock空间.md)：自由玻色子 Fock 空间上的顶点算子 $Y(a,z)=\exp(\dots)$ 构成 Heisenberg VOA，其 Virasoro 元素由 Sugawara 构造给出。

## 前置知识

李代数与表示论、形式幂级数与域算子、模形式、张量范畴。

## 后继用途

为共形场论、弦论与顶点算子代数的表示论、月光猜想与 Monstrous Moonshine、以及低维拓扑中的融合范畴提供代数基础。

## 关键定理速览

- 状态-场对应与 Borcherds 恒等式。
- Virasoro 代数与中心荷决定尺度反常。
- C2 余有限 + 有理 ⇒ 模有限、半单。
- Verlinde 公式：融合系数由模 S 矩阵给出。
- 月光模实现 Monster 群的 graded 维数。
