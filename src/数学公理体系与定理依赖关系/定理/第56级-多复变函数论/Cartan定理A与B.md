# Cartan 定理 A 与 B

> **一句话大白话**：在"好的"复空间（Stein空间）上，任何局部松散的几何数据都能"焊"成全局对象：定理A说处处可造的组合能补齐成整体（生成元充足），定理B说高位层级障碍为0（高阶同调消失）——这保证多复变里很多"拼接"问题都能解。
>
> **小例子**：对 Stein 空间 $X$ 及解析凝聚层 $\mathcal{F}$，定理A：$\mathcal{F}$ 处处由全局截面生成；定理B：$H^q(X,\mathcal{F})=0$（$q\ge1$）；合起来让"局部解拼全局解"畅通无阻，如同说在好地盘上"拼接没有暗礁"。

## 一、定理介绍

> **前置依赖**：凝聚层、Stein 流形、层上同调、Dolbeault 定理、$\bar{\partial}$ 方程的可解性。

Cartan 定理 A 与 B 是法国数学家 Henri Cartan 在 1951–1954 年间建立的关于 **凝聚层在 Stein 流形上上同调** 的两个基本定理，是多复变函数论与复几何的基石。

- **定理 A** 断言：Stein 流形上的凝聚层 $\mathcal{F}$ 由其全局截面"逐点生成"，即 $\mathcal{F}_x$ 由 $H^0(X, \mathcal{F})$ 生成。
- **定理 B** 断言：Stein 流形上凝聚层的高阶上同调消失：$H^q(X, \mathcal{F}) = 0$，$\forall q \geq 1$。

定理 B 是定理 A 的深远推广，是 Oka 原理、Stein 流形理论、$\bar{\partial}$ 方程可解性的统一代数表达。Cartan 通过这些定理将多复变函数论从古典的"函数论"提升到现代的"层论与上同调"框架。Serre 在 1953 年将这一框架应用到代数几何，提出 GAGA 原理，奠定了现代代数几何的层论基础。

## 二、原理思路

Cartan 定理 A 与 B 的核心是 **Stein 流形上"全局截面丰富"** 这一思想的层论表达。

**关键观察**：
1. Stein 流形上整体全纯函数丰富（分离点、给局部坐标、全纯凸性），这提示凝聚层的整体截面也应丰富。
2. 凝聚层是局部有限展示的层，可视为"由全纯函数的有限关系定义"的层。
3. 上同调 $H^q(X, \mathcal{F})$（$q \geq 1$）消失意味着局部数据总能整体拼接——这是 Stein 性的层论刻画。

**证明思路**（Cartan 的原始方法 + 现代 $\bar{\partial}$ 方法）：
- 由 $\mathcal{F}$ 的凝聚性，局部地化为 $\mathcal{O}^p \to \mathcal{O}^q \to \mathcal{F} \to 0$。
- 利用 $\mathcal{O}$ 在 Stein 流形上的丰富性，将局部截面拼接为整体截面。
- 通过归纳（Cartan 的"奇偶性归纳"）证明 $H^q(X, \mathcal{O}) = 0$ 与凝聚层的高阶上同调消失。

## 三、定理的严格表述

设 $X$ 为 Stein 流形，$\mathcal{F}$ 为 $\mathcal{O}_X$-凝聚层（即 $\mathcal{O}_X$ 上有限展示的层）。

### Cartan 定理 A

**定理 A**：对任意 $x \in X$，自然映射
$$H^0(X, \mathcal{F}) \to \mathcal{F}_x$$
是满射。换言之，$\mathcal{F}$ 的茎 $\mathcal{F}_x$ 由全局截面生成。

更一般地，对任意凝聚层 $\mathcal{F}$，存在 $X$ 上的全纯向量丛 $E$（即自由层 $\mathcal{O}^{\oplus N}$）与满射层态射
$$\mathcal{O}^{\oplus N} \to \mathcal{F} \to 0.$$

### Cartan 定理 B

**定理 B**：对任意凝聚层 $\mathcal{F}$ 与任意 $q \geq 1$，
$$H^q(X, \mathcal{F}) = 0.$$

### 重要推论

1. **Cousin 问题可解**：$H^1(X, \mathcal{O}) = 0$ 给出第一 Cousin 问题在 Stein 流形上的可解性。
2. **除子与线丛**：$H^1(X, \mathcal{O}^*) \cong H^2(X, \mathbb{Z})$（指数层正合序列），故线丛分类化为拓扑问题（即 Oka–Grauert 原理）。
3. **整体全纯截面生成**：任何凝聚理想层整体生成，从而可由全局方程描述。

## 四、证明过程

### 定理 A 的证明概要

设 $\mathcal{F}$ 凝聚，$x \in X$。

**步骤 1：局部展示**。由凝聚性，存在 $x$ 的邻域 $U$ 与正合
$$\mathcal{O}(U)^{\oplus p} \xrightarrow{\alpha} \mathcal{O}(U)^{\oplus q} \to \mathcal{F}|_U \to 0.$$
元素 $s \in \mathcal{F}_x$ 可由 $\mathcal{O}(U)^{\oplus q}$ 中的元素 $v$ 代表。

**步骤 2：利用 Stein 性扩展**。需将 $v$ 扩展为整体截面 $\tilde{v} \in H^0(X, \mathcal{O}^{\oplus q})$，使其像在 $\mathcal{F}$ 中为整体截面 $s'$ 满足 $s'_x = s$。

由 Cartan 定理 B（待证），$H^1$ 消失保证这种扩展可行。但为避免循环论证，需用 Oka 的方法直接证明定理 A。

**步骤 3：Oka–Cartan 的构造**。利用 $\mathcal{O}$ 在 Stein 流形上的逼近性质与凝聚层的 Weierstrass 预备定理，直接构造整体截面 $s'$ 使 $s'_x = s$。关键工具是 Oka 的"准逆"与凝聚性定理。

**步骤 4：有限性**。通过凝聚性，将局部生成元个数有限化，得到 $\mathcal{O}^{\oplus N} \to \mathcal{F}$ 满射。$\square$

### 定理 B 的证明概要

**步骤 1：先证 $H^q(X, \mathcal{O}) = 0$，$\forall q \geq 1$**。

利用 Dolbeault 定理：$H^q(X, \mathcal{O}) \cong H^{0,q}_{\bar{\partial}}(X)$。在 Stein 流形上，$\bar{\partial}$ 方程的可解性（Hörmander 的 $L^2$ 理论或 Cartan 的构造性方法）给出：对任意 $\bar{\partial}$-闭 $(0,q)$-形式 $f$（$q \geq 1$），存在 $(0, q-1)$-形式 $u$ 使 $\bar{\partial} u = f$。这等价于 $H^{0,q}_{\bar{\partial}}(X) = 0$，即 $H^q(X, \mathcal{O}) = 0$。

**步骤 2：推广到自由层 $\mathcal{O}^{\oplus N}$**。$H^q(X, \mathcal{O}^{\oplus N}) = H^q(X, \mathcal{O})^{\oplus N} = 0$。

**步骤 3：凝聚层归纳**。设 $\mathcal{F}$ 凝聚，由定理 A 存在正合
$$\mathcal{O}^{\oplus p} \to \mathcal{O}^{\oplus q} \to \mathcal{F} \to 0.$$
设 $K = \ker(\mathcal{O}^{\oplus q} \to \mathcal{F})$，则 $K$ 凝聚（凝聚层在 Oka–Cartan 意义下对核封闭），且正合列
$$0 \to K \to \mathcal{O}^{\oplus q} \to \mathcal{F} \to 0$$
给出长正合序列
$$\cdots \to H^q(X, \mathcal{O}^{\oplus p}) \to H^q(X, K) \to H^{q+1}(X, \mathcal{F}) \to H^{q+1}(X, \mathcal{O}^{\oplus q}) \to \cdots$$

由步骤 2，$H^q(X, \mathcal{O}^{\oplus q}) = 0$（$q \geq 1$），所以 $H^{q+1}(X, \mathcal{F}) \cong H^q(X, K)$（对 $q \geq 1$）。

**步骤 4：归纳**。利用对层 $K$ 的"秩"或"层数"的归纳，逐次降阶。最终化为 $H^1(X, \mathcal{F}) = 0$，这又由 $H^0(X, \mathcal{O}^{\oplus q}) \to H^0(X, \mathcal{F})$ 的满射性（即定理 A）得到。这即是 Cartan 的"奇偶性归纳法"。

具体而言：从 $H^1(X, \mathcal{F}) \to H^1(X, \mathcal{O}^{\oplus q}) = 0$，得 $H^1(X, \mathcal{F}) = 0$。然后由长正合序列，$H^2(X, \mathcal{F}) \cong H^1(X, K) = 0$，依此类推。

**步骤 5**：所有 $H^q(X, \mathcal{F}) = 0$，$q \geq 1$。$\square$

注：定理 A 与 B 互相依赖（定理 A 用到 B 的"幂零"形式，定理 B 用到 A），完整的证明需要更精细的并行归纳，详见 Cartan 的原始论文或 Hörmander 的《An Introduction to Complex Analysis in Several Variables》。

## 五、应用与意义

Cartan 定理 A 与 B 在现代数学中具有纲领性地位：

1. **多复变函数论的统一框架**：定理 A、B 是 Stein 流形上多复变函数论的"基本定理"，统一了 Cousin 问题、除子问题、向量丛分类、$\bar{\partial}$ 方程可解性等所有古典问题。

2. **Oka 原理的层论基础**：Oka 原理的严格证明依赖 Cartan 定理 B。Stein 流形上凝聚上同调消失是 Oka 原理可应用于"层次构造"的根本。

3. **代数几何的层论革命**：Serre 1953 年将 Cartan 的层论方法移植到代数几何，建立 GAGA 原理（解析与代数上同调一致），引发代数几何的现代革命。Grothendieck 进一步将凝聚层理论发展为概形理论的基础。

4. **复几何与代数拓扑桥梁**：通过指数层正合序列
$$0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^* \to 0,$$
定理 B 给出 $\text{Pic}(X) \cong H^1(X, \mathcal{O}^*) \cong H^2(X, \mathbb{Z})$，将解析分类化为拓扑分类。

5. **凝聚层理论的发展**：Cartan 引入凝聚层概念，是现代层论与同调代数的基石。Forster、Grauert、Hironaka 等的工作直接继承自 Cartan 的思想。

6. **现代研究影响**：高维代数几何中 Kodaira 消灭定理、Kawamata–Viehweg 消灭定理都是 Cartan 定理 B 在紧 Kähler 流形上的对应发展；非紧复几何中 Takegoshi 消灭定理、Ohsawa–Takegoshi $L^2$ 延拓定理等都是其后续。
