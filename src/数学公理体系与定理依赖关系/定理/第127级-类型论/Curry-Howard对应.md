# Curry-Howard 对应

> **一句话大白话**："命题＝类型，证明＝程序"。一条逻辑命题被证明，就等价于相应类型"被占据"（存在一个该类型的项）；逻辑推导规则与类型推理规则一一对应。
>
> **小例子**：命题 $A\to(B\to A)$ 对应类型 $A\to(B\to A)$，其证明正是 λ 项 $\lambda x:A.\,\lambda y:B.\,x$。合取对应序对、蕴含对应 λ 抽象、析取对应注入——"会证明"就是"会写程序"。

## 一、定理介绍

Curry-Howard 对应（Curry-Howard 同构）揭示了逻辑证明与程序、命题与类型之间的深层同一关系：直觉主义命题逻辑的自然演绎系统与简单类型 λ 演算一一对应，使"证明"与"程序"、规范化与 $\beta$-归约互相等同。它是类型论与依赖类型理论的基石，也是程序语言理论与逻辑之间的桥梁。

## 二、原理思路

构造显式映射 $\lfloor-\rfloor$ 从命题到类型：原子命题对类型变元，$A\to B$ 对函数类型，$A\land B$ 对积类型，$A\lor B$ 对余积等。再归纳于证明/项的结构，验证自然演绎规则逐一对应显然的类型规则（蕴含引入 $\Leftrightarrow$ λ 抽象等）。最后把证明规范化步骤（如 $\beta$-归约）对到 λ 项的 $\beta$-归约，并给出逆方向构造双射。

## 三、定理的严格表述

**定理（Curry-Howard 对应）**：直觉主义命题逻辑的自然演绎与简单类型 λ 演算存在一一对应，使：
1. 命题 $A$ 可证当且仅当类型 $A$ 可居留（inhabited）；
2. 证明与 λ 项一一对应；
3. 证明规范化对应项的 $\beta$-归约。

## 四、证明过程

**证明（构造对应）**：

**步骤1（映射 $\lfloor-\rfloor$）**：
$$
\lfloor P\rfloor=p,\quad \lfloor A\to B\rfloor=\lfloor A\rfloor\to\lfloor B\rfloor,\quad \lfloor A\land B\rfloor=\lfloor A\rfloor\times\lfloor B\rfloor,\quad \lfloor A\lor B\rfloor=\lfloor A\rfloor+\lfloor B\rfloor.
$$

**步骤2（项与证明对应）**：由证明 $\Gamma\vdash A$ 归纳构造 λ 项：
- 公理 $\Gamma,A\vdash A$ 对应变量规则 $\Gamma,x:\lfloor A\rfloor\vdash x:\lfloor A\rfloor$；
- 蕴含引入 $(\to I)$ 对应 λ 抽象：从 $\Gamma,x:\lfloor A\rfloor\vdash t:\lfloor B\rfloor$ 得 $\Gamma\vdash\lambda x:\lfloor A\rfloor.\,t:\lfloor A\rfloor\to\lfloor B\rfloor$；
- 蕴含消去 $(\to E)$ 对应函数应用 $t_1\,t_2$；
- 合取引入/消去对应序对 $(t_1,t_2)$ 与投影 $\text{fst},\text{snd}$；析取对应注入 $\text{inl},\text{inr}$ 与 $\text{case}$。

**步骤3（规范化对应 $\beta$-归约）**：证明规范化步骤
$$
\Gamma,x:\lfloor A\rfloor\vdash t:\lfloor B\rfloor,\ \Gamma\vdash u:\lfloor A\rfloor\ \Rightarrow\ \Gamma\vdash t[u/x]:\lfloor B\rfloor
$$
对应的项变换是 $(\lambda x:\lfloor A\rfloor.\,t)\,u\to_\beta t[u/x]$，恰为 $\beta$-归约。

**步骤4（双向）**：逆映射从类型良好项构造自然演绎证明，故建立双射。$\square$

## 五、应用与意义

Curry-Howard 对应是逻辑—计算同构的典范：它支撑依赖类型编程（Agda、Coq、Lean 中"证明就是程序"的证明自动化）、抛光类型理论（命题即类型）、以及程序语言理论中的类型系统设计。它把"证明数学定理"一以贯之地变成"写出能类型检查的程序"，是现代形式化数学的根基。