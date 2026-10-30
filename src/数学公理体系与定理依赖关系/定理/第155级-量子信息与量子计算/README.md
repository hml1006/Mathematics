# 第155级-量子信息与量子计算

> 一句话级别概述：量子信息把状态、信道、熵、纠错变成可计算的数学对象：用密度矩阵与完全正映射描述物理过程，用熵与容量刻画信息传输的极限。

## 级别简介

本级别从密度矩阵与纯化出发，建立量子信道的 Kraus 表示与不可克隆定理；随后讨论 Bell 与 CHSH 违反、von Neumann 熵与相对熵、Holevo 界与信道容量；最后进入量子纠错码的 Knill-Laflamme 条件与 Shor 算法的量子 Fourier 加速。

## 本级别定理

- [密度矩阵与纯化](./密度矩阵与纯化.md)：量子态由 $\rho\ge0,\ \mathrm{tr}\rho=1$ 描述；任意混合态都可纯化为更大系统上的纯态 $|\Psi\rangle$，且 $\rho=\mathrm{tr}_B|\Psi\rangle\langle\Psi|$。
- [量子信道与 Kraus 表示](./量子信道与Kraus表示.md)：完全正迹 preserving 映射可写为 $\Phi(\rho)=\sum_iK_i\rho K_i^\dagger$，$\sum_iK_i^\dagger K_i=I$。
- [量子不可克隆定理](./量子不可克隆定理.md)：不存在 CPTP 映射把任意未知 $|\psi\rangle$ 复制为 $|\psi\rangle|\psi\rangle$。
- [Bell 不等式与 CHSH](./Bell不等式与CHSH.md)：局域隐变量模型满足 $|S|\le2$，而量子力学取 $S=2\sqrt2$，违反 CHSH 不等式。
- [von Neumann 熵与量子相对熵](./vonNeumann熵与量子相对熵.md)：$S(\rho)=-\mathrm{tr}\rho\log\rho$，$D(\rho\|\sigma)=\mathrm{tr}\rho(\log\rho-\log\sigma)\ge0$，且满足数据处理不等式。
- [Holevo 界与量子信道容量](./Holevo界与量子信道容量.md)：经典信息经量子信道传输的可达速率受 $\chi=\sum_ip_iS(\rho_i)-S(\sum_ip_i\rho_i)$ 约束。
- [量子纠错码与 Knill-Laflamme 条件](./量子纠错码与Knill-Laflamme条件.md)：子空间 $\mathcal C$ 可纠错误集 $\{E_a\}$ 当且仅当 $P E_a^\dagger E_bP=C_{ab}P$。
- [Shor 算法与量子 Fourier 变换](./Shor算法与量子Fourier变换.md)：整数分解归约为求阶问题，量子 Fourier 变换在 $O((\log N)^2)$ 门内完成周期提取，给出指数加速。

## 前置知识

线性代数与 Hilbert 空间、张量积、概率论、编码理论的基本概念。

## 后继用途

为量子计算、量子通信、量子纠错与量子密码提供数学基础，也是算子代数与表示论的应用出口。

## 关键定理速览

- 量子信道 = CPTP 映射，可写为 Kraus 和。
- 不可克隆定理：未知量子态无法复制。
- CHSH：局域隐变量上界 2，量子可达 2√2。
- Holevo 界给出经典容量上界。
- Knill-Laflamme 条件判定可纠错子空间。
