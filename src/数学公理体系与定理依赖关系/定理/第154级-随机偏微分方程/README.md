# 第154级-随机偏微分方程

> 一句话级别概述：随机偏微分方程研究被噪声驱动的场：把 Brown 运动搬到函数空间，再让无穷维噪声与微分算子耦合，得到描述涨落界面的方程。

## 级别简介

本级别先处理无穷维 Brown 运动与柱测度带来的技术困难，再给出随机热方程与二维随机 Navier-Stokes 的适定性；随后进入 Freidlin-Wentzell 大偏差、KPZ 与 Φ4 的重正化，最后以受控粗糙路径（遍及理论）与随机波动方程收束。

## 本级别定理

- [无穷维 Brown 运动与柱测度](./无穷维Brown运动与柱测度.md)：无限维 Hilbert 空间上的柱测度不可数可加，$Q$-Wiener 过程只能取值于 $Q^{1/2}H$ 的更大空间。
- [随机热方程的存在唯一性](./随机热方程的存在唯一性.md)：$\mathrm dX=(AX+f(X))\,\mathrm dt+B\,\mathrm dW$ 在温和解意义下存在唯一解（Da Prato-Zabczyk）。
- [二维随机 Navier-Stokes 方程的适定性](./二维随机Navier-Stokes方程的适定性.md)：二维随机 Navier-Stokes 方程对任意初值存在唯一全局强解。
- [Freidlin-Wentzell 大偏差原理](./Freidlin-Wentzell大偏差原理.md)：小噪声扩散 $\mathrm dX^\varepsilon=b(X^\varepsilon)\mathrm dt+\sqrt\varepsilon\sigma\,\mathrm dW$ 满足 $\varepsilon\log P(\cdot)\to-I(\varphi)$，速率函数为作用量泛函。
- [KPZ 方程与正则性结构](./KPZ方程与正则性结构.md)：$h_t=\partial_x^2h+(\partial_xh)^2+\xi$ 需重正化后才能局部适定，Hairer 的正则性结构给出统一框架。
- [随机量化与 $\Phi^4_3$ 测度](./随机量化与Φ4测度.md)：三维 $\Phi^4$ 测度经质量重正化后可构造，对应 $\Phi^4_3$ 量子场论的数学实现。
- [遍及理论与受控粗糙路径](./遍及理论与受控粗糙路径.md)：Gubinelli 的受控粗糙路径/遍及分布把 SPDE 的解写成"粗糙项 + 光滑修正"，给出统一的适定性判据。
- [随机波动方程与 Strichartz 估计](./随机波动方程与Strichartz估计.md)：随机波动方程借助 Strichartz 估计与随机卷积得到局部适定性与正则性提升。

## 前置知识

概率论与 Itô 积分、算子半群、Sobolev 空间与 Littlewood-Paley 分解、PDE 的弱解理论。

## 后继用途

为统计物理的界面涨落、随机量化、随机流体与金融中的无穷维模型提供严格分析框架。

## 关键定理速览

- 柱测度不可数可加，Q-Wiener 过程只能取值于更大空间。
- 随机热方程的温和解存在唯一（Da Prato-Zabczyk）。
- 二维随机 NSE 全局强解存在唯一；三维仍是开放问题。
- KPZ 与 Φ4 必须重正化后才适定。
- 受控粗糙路径给出统一的适定性判据。
