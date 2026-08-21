# Boosting算法的理论保证（AdaBoost）

> **一句话大白话**：只要每个弱学习器都"略好于随机猜测"，AdaBoost 把它们轮流加权组合后，训练误差就会随轮数指数级地降到零。
>
> **小例子**：若每轮弱学习器准确率 $0.75$（优势 $\gamma=0.25$），则 $T=50$ 轮后训练误差约 $e^{-50\times2\times0.25^2}\approx e^{-6.25}$，近乎为零。

## 一、定理介绍

> **前置依赖**：指数损失函数、经验风险最小化、权重归一化（转化为概率分布）、凸函数极值（一阶条件求最优 $\alpha$）、对数函数不等式 $\log(1-u)\le -u$。

设 $\{h_t\}$ 为 AdaBoost 第 $t$ 轮选择的弱学习器，加权训练误差 $\varepsilon_t$，$\alpha_t=\frac12\log\frac{1-\varepsilon_t}{\varepsilon_t}$。最终分类器 $H(x)=\text{sign}\big(\sum_{t=1}^T\alpha_th_t(x)\big)$ 的训练误差满足
$$
\hat R_n(H)\le\exp\left(-2\sum_{t=1}^T\gamma_t^2\right),
$$
其中 $\gamma_t=1/2-\varepsilon_t$ 为优势。若每个 $\gamma_t\ge\gamma>0$，则 $\hat R_n(H)\le e^{-2\gamma^2T}$。

## 二、原理思路

AdaBoost 隐式最小化指数损失 $L(y,F)=e^{-yF(x)}$。利用权重更新与归一化因子 $Z_t$ 的关系，可把训练误差上界化约为 $\prod_t Z_t$；再在最优 $\alpha_t$ 处计算 $Z_t=2\sqrt{\varepsilon_t(1-\varepsilon_t)}$，并由 $\sqrt{1-4\gamma^2}\le e^{-2\gamma^2}$ 得到指数衰减。

## 三、定理的严格表述

令 $F_T=\sum_{t=1}^T\alpha_th_t$，$H=\text{sign}(F_T)$，$\varepsilon_t=\sum_{i:y_i\ne h_t(x_i)}w_i^{(t)}$。则
$$
\hat R_n(H)\le\prod_{t=1}^T Z_t,\qquad Z_t=(1-\varepsilon_t)e^{-\alpha_t}+\varepsilon_te^{\alpha_t}.
$$
在 $\alpha_t=\frac12\log\frac{1-\varepsilon_t}{\varepsilon_t}$ 下 $Z_t=2\sqrt{\varepsilon_t(1-\varepsilon_t)}$，故
$$
\hat R_n(H)\le\exp\left(-2\sum_{t=1}^T\gamma_t^2\right)\le e^{-2\gamma^2T}.
$$

## 四、证明过程

**步骤1：指数损失。** 因 $\mathbf1_{\{y\ne H(x)\}}\le e^{-yF(x)}$，训练误差 $\hat R_n(H)\le\frac1n\sum_ie^{-y_iF_T(x_i)}$。

**步骤2：权重关系。** 样本权重按 $w_i^{(t+1)}=\frac{w_i^{(t)}e^{-\alpha_ty_ih_t(x_i)}}{Z_t}$ 更新，递推得 $\frac1n\sum_ie^{-y_iF_T(x_i)}=\prod_{t=1}^TZ_t$，故 $\hat R_n(H)\le\prod_tZ_t$。

**步骤3：计算 $Z_t$。** 按正确/错误划分两项，
$$
Z_t=(1-\varepsilon_t)e^{-\alpha_t}+\varepsilon_te^{\alpha_t}.
$$

**步骤4：最优 $\alpha_t$。** 令 $\frac{\partial Z_t}{\partial\alpha_t}=0$ 解得 $\alpha_t=\frac12\log\frac{1-\varepsilon_t}{\varepsilon_t}$。

**步骤5：代入化简。** 代入得 $Z_t=2\sqrt{\varepsilon_t(1-\varepsilon_t)}=\sqrt{1-4\gamma_t^2}\le e^{-2\gamma_t^2}$（后者因 $\log(1-u)\le-u$）。

**步骤6：结论。** $\hat R_n(H)\le\prod_te^{-2\gamma_t^2}=\exp(-2\sum_t\gamma_t^2)$；若 $\gamma_t\ge\gamma$，则 $\le e^{-2\gamma^2T}$。$\square$

## 五、应用与意义

AdaBoost 的理论保证说明"弱学习器集成"可以变成强学习器，其指数误差界是 Boosting 家族（Gradient Boosting、XGBoost 等）的经典理论支柱。界式还给出了关键时刻：当优势过小或 $\sum_t\gamma_t^2$ 收敛时误差才有正下界，从而指导弱学习器设计与轮数选取。