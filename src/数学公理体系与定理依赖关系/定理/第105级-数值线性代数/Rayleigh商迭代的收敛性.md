# Rayleigh商迭代的收敛性

> **一句话大白话**：用 Rayleigh 商作为"反馈给逆幂法的位移"，每一轮都让位移越来越逼近某个特征值，于是收敛像 Newton 法一样"三次方"地加速。
>
> **小例子**：对对称矩阵，一般逆幂法线性收敛，而 Rayleigh 商迭代从较好的初值出发，误差 $|x^{(k)}-\lambda|$ 按 $O(C^{3^k})$ 量级骤降——三次收敛。

## 一、定理介绍

Rayleigh 商迭代（RQI）是计算对称矩阵单个特征值（特征向量）最精巧的方法之一：以当前迭代向量 $x_k$ 的 Rayleigh 商 $\rho(x_k)=x_k^\top A x_k/(x_k^\top x_k)$ 作为逆幂法的位移，求解 $(A-\rho_k I)y=x_k$ 并归一化 $x_{k+1}=y/\|y\|$。它的收敛速度远优于固定位移的幂法或逆幂法。

## 二、原理思路

其收敛性"三次"来自二阶信息。Rayleigh 商迭代可看作对函数"$\min\|(A-\lambda I)x\|$（受 $\|x\|=1$）"（即特征问题）应用 Newton 型方法的一种实现。对 Hermite/对称矩阵，可用几何论证：把 $x_k$ 分解为主特征向量方向 $v_1$ 和正交分量 $e_k$，Rayleigh 商沿 $v_1$ 与沿 $e_k$ 的贡献在小角度下只差一阶，导致每迭代一步角度被"立方地"压缩。

## 三、定理的严格表述

设 $A$ 为对称矩阵，$\lambda_1$ 为其主特征值（简洁地取简单特征值 $\lambda=\lambda_1$，单位特征向量 $v$），初始单位向量 $x_0$ 与 $v$ 夹角足够小。Rayleigh 商迭代：
$$
\rho_k=\frac{x_k^\top A x_k}{x_k^\top x_k},\qquad
y_{k+1}=(A-\rho_k I)^{-1}x_k,\qquad x_{k+1}=\frac{y_{k+1}}{\|y_{k+1}\|},
$$
则存在关于 $A$ 的特征间隙的正常数 $c_1,c_2$（$0<c_1<\sigma$，$\sigma$ 表示 $\lambda_1$ 与其余特征值的最小间隙）使
$$
\tan\theta_{k+1}\le c_1\,(\tan\theta_k)^3,\qquad
e_{k+1}:=\tan\theta_k\le c_2\,e_k^3,
$$
其中 $\theta_k$ 为 $x_k$ 与 $v$ 的夹角。即（对足够好的初值）三次收敛。

## 四、证明过程（对称情形）

1. 设在主特征方向 $v$ 的规范正交方向张成的子空间把 $x_k$ 写为 $x_k=v\cos\theta_k+u_k\sin\theta_k$（$u_k\perp v$，单位）。则 $A$ 在子空间 $v+\operatorname{span}\{u_k\}$ 上的作用沿 $v$ 与 $u_k$ 分解，$Ax_k=\lambda_1 v\cos\theta_k+(\text{$u_k$ 方向的贡献})$。

2. 计算 Rayleigh 商 $\rho_k=x_k^\top Ax_k$。因 $v^\top A u_k=0$（对称，特征向量正交）且 $u_k^\top A u_k\le\lambda_2\ne\lambda_1$，展开：
   $$
   \rho_k=\lambda_1\cos^2\theta_k+O(\sin^2\theta_k).
   $$
3. 逆幂法一步：$y_{k+1}=(A-\rho_k I)^{-1}x_k$。在 $v$ 方向，$A-\rho_k I\approx(\lambda_1-\rho_k)$。因 $\lambda_1-\rho_k\approx\lambda_1\sin^2\theta_k$ 很小，主方向被放大（约 $1/\sin^2\theta_k$ 倍）；正交分量被放大约 $\frac{1}{\lambda_1-\rho_k-\lambda_2}$，故 $\tan\theta_{k+1}$ 量级为"正交贡献/主贡献"，即 $O(\sin^3\theta_k)$：
   $$
   \tan\theta_{k+1}
   =\frac{\text{$x_k$ 中正交分量的放大}}{\text{$x_k$ 中主分量的放大}}
   \le C\,\frac{\sin\theta_k\,/(\lambda_1-\rho_k-\lambda_2)}{\cos\theta_k\,/(\lambda_1-\rho_k)}
   \le C\left(\frac{\lambda_1-\rho_k}{\lambda_1-\rho_k-\lambda_2}\right)\tan\theta_k
   \le C'(\tan\theta_k)^3,
   $$
   利用 $\lambda_1-\rho_k\asymp\sin^2\theta_k$ 且间隙 $\lambda_1-\lambda_2$ 有下界。三次收敛得证。

4. **Hurwitz 论证**：只要 $\theta_0$ 小于某阈值（如 $\tan\theta_0<1$ 在小间隙下仍可选足以收敛的初值），由三次界可推出角度单调收缩到 $0$，最终收敛到特征方向。$\blacksquare$

**注。** 对非对称矩阵 RQI 一般退化为二次收敛；对 Hermite 情况三次是典型。实用中为防奇异需加少量位移减阻，或用"受约束 Newton"解释。

## 五、应用与意义

- **快速特征向量**：在需要单个特征对（主特征对或近特定值特征对）且已有较好初值时，RQI 收敛极快，是反幂法与位移选择技巧的集大成。
- **与 Arnoldi/Lanczos 衔接**：RQI 常用作大稀疏问题中局部收敛阶段的精化器。
- **理论价值**：展示了"把特征问题视为极小化问题并用 Newton 思想加速"的机制，是位移选择与收敛速度分析的代表作。
- **局限**：每步需解 $(A-\rho I)y=x$ 的新线性系统（无预分解基时代价高）；初值不好时可能收敛到非预期特征值。