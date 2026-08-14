# Markdown 中 LaTeX 公式书写教程

> 本教程面向需要在 Markdown 文档中熟练书写数学公式的学习者。目标：掌握在 Markdown 中用 LaTeX 语法书写 **inline（行内）公式** 与 **多行公式**，达到能流畅撰写数学笔记、讲义与习题解答的水平。

---

## 目录

- [一、两种公式模式：inline 与 display](#一两种公式模式inline-与-display)
- [二、基础语法速览](#二基础语法速览)
- [三、上下标与常见结构](#三上下标与常见结构)
- [四、运算符与常用函数](#四运算符与常用函数)
- [五、希腊字母与特殊符号](#五希腊字母与特殊符号)
  - [11. 字体样式](#11-字体样式)
  - [12. 重音标记](#12-重音标记)
  - [13. 省略号与排列](#13-省略号与排列)
  - [14. 大型运算符](#14-大型运算符)
  - [15. 间距控制](#15-间距控制)
  - [16. 空格与换行](#16-空格与换行)
  - [17. 颜色](#17-颜色部分渲染器支持)
- [六、括号与尺寸控制](#六括号与尺寸控制)
- [七、多行公式详解](#七多行公式详解)
- [八、矩阵与分段函数](#八矩阵与分段函数)
- [九、方程组与对齐](#九方程组与对齐)
- [十、常见错误与调试技巧](#十常见错误与调试技巧)
- [十一、速查表](#十一速查表)

---

## 一、两种公式模式：inline 与 display

Markdown 中嵌入 LaTeX 公式有两种方式，对应两种排版形态。

### 1. Inline（行内）公式

用单个美元符 `$...$` 包裹，公式嵌在正文文字当**中**，不单独成行：

```markdown
勾股定理 $a^2 + b^2 = c^2$ 是平面几何的核心定理。
```

显示效果：勾股定理 $a^2 + b^2 = c^2$ 是平面几何的核心定理。

**适用场景**：在句子中引用一个符号或短公式，如"设 $x$ 为实数"、"当 $n \to \infty$ 时"。

### 2. Display（块级）公式

用双美元符 `$$...$$` 包裹，公式**单独成行、居中、居中占一行**：

```markdown
一元二次方程的求根公式为：
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

显示效果：

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

**适用场景**：重要公式、需要突出展示、或多行推导。

> **关键区别记忆**：
> - `$...$` → 行内公式，随正文排版，不换行。
> - `$$...$$` → 块级公式，单独成行居中。
>
> **注意**：inline 公式中若包含 `\lim`、`\sum`、`\int` 等，其上下标默认显示在**右侧**（紧凑模式）；块级公式中则显示在**上下方**（展开模式）。

---

## 二、基础语法速览

| 语法 | 代码 | 效果 |
|:----:|:-----|:----:|
| 下标 | `x_i` | $x_i$ |
| 上标 | `x^2` | $x^2$ |
| 同时上下标 | `x_i^2` | $x_i^2$ |
| 分式 | `\frac{a}{b}` | $\frac{a}{b}$ |
| 平方根 | `\sqrt{x}` | $\sqrt{x}$ |
| n 次根 | `\sqrt[n]{x}` | $\sqrt[n]{x}$ |
| 求和 | `\sum_{i=1}^{n} a_i` | $\sum_{i=1}^{n} a_i$ |
| 积分 | `\int_a^b f(x)\,dx` | $\int_a^b f(x)\,dx$ |
| 极限 | `\lim_{x \to 0} \frac{\sin x}{x}` | $\lim_{x \to 0} \frac{\sin x}{x}$ |
| 无穷 | `\infty` | $\infty$ |

---

## 三、上下标与常见结构

### 1. 上下标

- 上标用 `^`，下标用 `_`。
- 若下标/上标由**多个字符**组成，必须用 `{}` 括起来。

```markdown
错误：$x^10$   → $x^10$（只把 1 作为上标）
正确：$x^{10}$ → $x^{10}$
```

```markdown
$a_{ij}$（双下标）    → $a_{ij}$
$e^{i\theta}$         → $e^{i\theta}$
$f^{(n)}(x)$（n阶导） → $f^{(n)}(x)$
```

### 2. 分式

- 用 `\frac{分子}{分母}`。
- 分子分母比较复杂时，可用 `\dfrac`（强制大号）或 `\tfrac`（强制小号）。

```markdown
行内：$\frac{a}{b}$            → $\frac{a}{b}$
块级分数：$\dfrac{a+b}{c+d}$   → $\dfrac{a+b}{c+d}$
连续分式：$\frac{1}{1 + \frac{1}{x}}$ → $\frac{1}{1 + \frac{1}{x}}$
```

### 3. 根式

```markdown
$\sqrt{2}$         → $\sqrt{2}$
$\sqrt[3]{8}$      → $\sqrt[3]{8}$
$\sqrt{x^2 + y^2}$ → $\sqrt{x^2 + y^2}$
```

### 4. 求和、积分、极限的上下限

```markdown
求和：$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$
积分：$\int_{0}^{1} x^2 \, dx = \frac{1}{3}$
极限：$\lim_{n \to \infty} a_n = 0$
```

- 在 inline 中这些上下限靠右（紧凑）；在 display 中上下限在符号上下方（展开）。若想在 inline 中也强制展开，可用 `\limits`：

```markdown
inline 强制展开：$\sum\limits_{k=1}^{n} k$
```

---

## 四、运算符与常用函数

### 1. 二元运算符

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 加减 | `a \pm b` | $a \pm b$ | 减加 | `a \mp b` | $a \mp b$ |
| 乘 | `a \times b` | $a \times b$ | 点乘 | `a \cdot b` | $a \cdot b$ |
| 除 | `a \div b` | $a \div b$ | 星号 | `a \ast b` | $a \ast b$ |
| 星号 | `a \star b` | $a \star b$ | 复合 | `f \circ g` | $f \circ g$ |
| 张量积 | `a \otimes b` | $a \otimes b$ | 直和 | `a \oplus b` | $a \oplus b$ |
| 逻辑与 | `p \wedge q` | $p \wedge q$ | 逻辑或 | `p \vee q` | $p \vee q$ |
| 卷积 | `f * g` | $f * g$ | 集合差 | `A \setminus B` | $A \setminus B$ |

### 2. 关系符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 小于等于 | `a \le b` | $a \le b$ | 大于等于 | `a \ge b` | $a \ge b$ |
| 不等于 | `a \ne b` | $a \ne b$ | 约等于 | `a \approx b` | $a \approx b$ |
| 正比 | `a \propto b` | $a \propto b$ | 恒等 | `a \equiv b` | $a \equiv b$ |
| 严格小于 | `a \ll b` | $a \ll b$ | 严格大于 | `a \gg b` | $a \gg b$ |
| 相似 | `A \sim B` | $A \sim B$ | 不相似 | `A \nsim B` | $A \nsim B$ |
| 同构 | `A \cong B` | $A \cong B$ | 不恒等 | `a \not\equiv b` | $a \not\equiv b$ |
| 整除 | `a \mid b` | $a \mid b$ | 不整除 | `a \nmid b` | $a \nmid b$ |
| 平行 | `l_1 \parallel l_2` | $l_1 \parallel l_2$ | 不平行 | `l_1 \nparallel l_2` | $l_1 \nparallel l_2$ |
| 垂直 | `l_1 \perp l_2` | $l_1 \perp l_2$ | 渐近 | `f \asymp g` | $f \asymp g$ |
| 定义等于 | `a \triangleq b` | $a \triangleq b$ | 对应 | `a \simeq b` | $a \simeq b$ |

### 3. 标准函数（用反斜杠转义，得到正体罗马字）

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 正弦 | `\sin x` | $\sin x$ | 余弦 | `\cos x` | $\cos x$ |
| 正切 | `\tan x` | $\tan x$ | 余切 | `\cot x` | $\cot x$ |
| 正割 | `\sec x` | $\sec x$ | 余割 | `\csc x` | $\csc x$ |
| 反正弦 | `\arcsin x` | $\arcsin x$ | 反余弦 | `\arccos x` | $\arccos x$ |
| 反正切 | `\arctan x` | $\arctan x$ | 双曲正弦 | `\sinh x` | $\sinh x$ |
| 双曲余弦 | `\cosh x` | $\cosh x$ | 双曲正切 | `\tanh x` | $\tanh x$ |
| 对数 | `\log x` | $\log x$ | 自然对数 | `\ln x` | $\ln x$ |
| 指数 | `\exp x` | $\exp x$ | 行列式 | `\det A` | $\det A$ |
| 极限 | `\lim_{x \to 0}` | $\lim_{x \to 0}$ | 最大值 | `\max` | $\max$ |
| 最小值 | `\min` | $\min$ | 上确界 | `\sup` | $\sup$ |
| 下确界 | `\inf` | $\inf$ | 最大公约数 | `\gcd(a, b)` | $\gcd(a, b)$ |
| 维度 | `\dim V` | $\dim V$ | 核 | `\ker f` | $\ker f$ |
| 次数 | `\deg f` | $\deg f$ | 同态 | `\operatorname{Hom}` | $\operatorname{Hom}$ |
| 迹 | `\operatorname{tr} A` | $\operatorname{tr} A$ | 秩 | `\operatorname{rank} A` | $\operatorname{rank} A$ |
| 期望 | `\mathbb{E}[X]` | $\mathbb{E}[X]$ | 方差 | `\operatorname{Var}(X)` | $\operatorname{Var}(X)$ |
| 协方差 | `\operatorname{Cov}(X,Y)` | $\operatorname{Cov}(X,Y)$ | 条件概率 | `P(A \mid B)` | $P(A \mid B)$ |
| mod | `a \bmod b` | $a \bmod b$ | 同余 | `a \equiv b \pmod{n}` | $a \equiv b \pmod{n}$ |

> **重点**：`\sin`、`\log` 等必须加反斜杠，否则 `sin` 会被视为三个连乘的变量 $s i n$，排版错误。

### 4. 函数名（自定义运算符）

若需要自定义函数名（如 $\operatorname{argmax}$），用 `\operatorname`：

```markdown
$\operatorname{argmax}_{x} f(x)$
$\operatorname{sgn}(x)$
$\operatorname{dist}(x, y)$
```

---

## 五、希腊字母与特殊符号

### 1. 完整希腊字母表

**小写希腊字母**：

| 代码 | 效果 | 代码 | 效果 | 代码 | 效果 | 代码 | 效果 |
|:-----|:----:|:-----|:----:|:-----|:----:|:-----|:----:|
| `\alpha` | $\alpha$ | `\beta` | $\beta$ | `\gamma` | $\gamma$ | `\delta` | $\delta$ |
| `\epsilon` | $\epsilon$ | `\varepsilon` | $\varepsilon$ | `\zeta` | $\zeta$ | `\eta` | $\eta$ |
| `\theta` | $\theta$ | `\vartheta` | $\vartheta$ | `\iota` | $\iota$ | `\kappa` | $\kappa$ |
| `\lambda` | $\lambda$ | `\mu` | $\mu$ | `\nu` | $\nu$ | `\xi` | $\xi$ |
| `\pi` | $\pi$ | `\varpi` | $\varpi$ | `\rho` | $\rho$ | `\varrho` | $\varrho$ |
| `\sigma` | $\sigma$ | `\varsigma` | $\varsigma$ | `\tau` | $\tau$ | `\upsilon` | $\upsilon$ |
| `\phi` | $\phi$ | `\varphi` | $\varphi$ | `\chi` | $\chi$ | `\psi` | $\psi$ |
| `\omega` | $\omega$ | | | | | | |

**大写希腊字母**：

| 代码 | 效果 | 代码 | 效果 | 代码 | 效果 | 代码 | 效果 |
|:-----|:----:|:-----|:----:|:-----|:----:|:-----|:----:|
| `\Gamma` | $\Gamma$ | `\Delta` | $\Delta$ | `\Theta` | $\Theta$ | `\Lambda` | $\Lambda$ |
| `\Xi` | $\Xi$ | `\Pi` | $\Pi$ | `\Sigma` | $\Sigma$ | `\Upsilon` | $\Upsilon$ |
| `\Phi` | $\Phi$ | `\Psi` | $\Psi$ | `\Omega` | $\Omega$ | | |

> **注意**：部分小写字母有变体形式（如 `\varepsilon` vs `\epsilon`、`\varphi` vs `\phi`），数学中通常用变体形式。大写希腊字母中，与拉丁字母相同的（如 A、B、E）没有专门的 LaTeX 命令，直接写字母即可。

### 2. 集合符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 属于 | `x \in A` | $x \in A$ | 不属于 | `x \notin A` | $x \notin A$ |
| 包含于 | `A \subset B` | $A \subset B$ | 包含于或等于 | `A \subseteq B` | $A \subseteq B$ |
| 真子集 | `A \subsetneq B` | $A \subsetneq B$ | 真子集（或等于） | `A \subseteq B` | $A \subseteq B$ |
| 包含 | `A \supset B` | $A \supset B$ | 包含或等于 | `A \supseteq B` | $A \supseteq B$ |
| 并 | `A \cup B` | $A \cup B$ | 交 | `A \cap B` | $A \cap B$ |
| 差集 | `A \setminus B` | $A \setminus B$ | 补集 | `A^c` 或 `\complement A` | $A^c$ / $\complement A$ |
| 对称差 | `A \triangle B` | $A \triangle B$ | 空集 | `\emptyset` | $\emptyset$ |
| 空集（变体） | `\varnothing` | $\varnothing$ | 幂集 | `\mathcal{P}(A)` | $\mathcal{P}(A)$ |
| 基数 | `\lvert A \rvert` | $\lvert A \rvert$ | 连续统 | `\mathfrak{c}` | $\mathfrak{c}$ |

### 3. 逻辑符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 任意 | `\forall x` | $\forall x$ | 存在 | `\exists x` | $\exists x$ |
| 不存在 | `\nexists x` | $\nexists x$ | 否定 | `\neg p` | $\neg p$ |
| 非 | `\lnot p` | $\lnot p$ | 且 | `p \land q` | $p \land q$ |
| 或 | `p \lor q` | $p \lor q$ | 蕴含 | `p \Rightarrow q` | $p \Rightarrow q$ |
| 等价 | `p \Leftrightarrow q` | $p \Leftrightarrow q$ | 推出 | `p \implies q` | $p \implies q$ |
| 当且仅当 | `p \iff q` | $p \iff q$ | 因此 | `\therefore` | $\therefore$ |
| 因为 | `\because` | $\because$ | 矛盾 | `\bot` | $\bot$ |
| 永真 | `\top` | $\top$ | 可证 | `\vdash` | $\vdash$ |
| 语义蕴含 | `\models` | $\models$ | 不可证 | `\nvdash` | $\nvdash$ |

### 4. 箭头符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 左箭头 | `\leftarrow` | $\leftarrow$ | 右箭头 | `\rightarrow` | $\rightarrow$ |
| 上箭头 | `\uparrow` | $\uparrow$ | 下箭头 | `\downarrow` | $\downarrow$ |
| 双向箭头 | `\leftrightarrow` | $\leftrightarrow$ | 左双箭头 | `\Leftarrow` | $\Leftarrow$ |
| 右双箭头 | `\Rightarrow` | $\Rightarrow$ | 双向双箭头 | `\Leftrightarrow` | $\Leftrightarrow$ |
| 映射 | `\mapsto` | $\mapsto$ | 长映射 | `\longmapsto` | $\longmapsto$ |
| 趋向 | `\to` | $\to$ | 长趋向 | `\longrightarrow` | $\longrightarrow$ |
| 左钩箭头 | `\hookleftarrow` | $\hookleftarrow$ | 右钩箭头 | `\hookrightarrow` | $\hookrightarrow$ |
| 左上箭头 | `\nwarrow` | $\nwarrow$ | 右上箭头 | `\nearrow` | $\nearrow$ |
| 左下箭头 | `\swarrow` | $\swarrow$ | 右下箭头 | `\searrow` | $\searrow$ |
| 带文字箭头 | `\xrightarrow{f}` | $\xrightarrow{f}$ | 带文字下箭头 | `\xleftarrow{g}` | $\xleftarrow{g}$ |

### 5. 常用数集

```markdown
$\mathbb{N}$ 自然数   → $\mathbb{N}$
$\mathbb{Z}$ 整数     → $\mathbb{Z}$
$\mathbb{Q}$ 有理数   → $\mathbb{Q}$
$\mathbb{R}$ 实数     → $\mathbb{R}$
$\mathbb{C}$ 复数     → $\mathbb{C}$
$\mathbb{R}^n$ n维实向量空间 → $\mathbb{R}^n$
$\mathbb{Z}^+$ 正整数 → $\mathbb{Z}^+$
$\mathbb{R}_{\ge 0}$ 非负实数 → $\mathbb{R}_{\ge 0}$
```

### 6. 微积分与分析符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 偏导 | `\partial` | $\partial$ | 梯度 | `\nabla` | $\nabla$ |
| 无穷 | `\infty` | $\infty$ | 微分 | `dx` | $dx$ |
| 积分 | `\int` | $\int$ | 二重积分 | `\iint` | $\iint$ |
| 三重积分 | `\iiint` | $\iiint$ | 围道积分 | `\oint` | $\oint$ |
| 散度 | `\operatorname{div}` | $\operatorname{div}$ | 旋度 | `\operatorname{curl}` | $\operatorname{curl}$ |
| 拉普拉斯 | `\Delta` | $\Delta$ | 达朗贝尔 | `\square` | $\square$ |
| 上极限 | `\limsup` | $\limsup$ | 下极限 | `\liminf` | $\liminf$ |
| 收敛 | `\to` | $\to$ | 一致收敛 | `\rightrightarrows` | $\rightrightarrows$ |
| 弱收敛 | `\rightharpoonup` | $\rightharpoonup$ | 弱星收敛 | `\overset{*}{\rightharpoonup}` | $\overset{*}{\rightharpoonup}$ |

### 7. 线性代数符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 转置 | `A^T` 或 `A^\top` | $A^T$ / $A^\top$ | 共轭转置 | `A^*` 或 `A^\dagger` | $A^*$ / $A^\dagger$ |
| 逆矩阵 | `A^{-1}` | $A^{-1}$ | 伴随矩阵 | `A^*` | $A^*$ |
| 行列式 | `\det A` 或 `\lvert A \rvert` | $\det A$ / $\lvert A \rvert$ | 迹 | `\operatorname{tr} A` | $\operatorname{tr} A$ |
| 秩 | `\operatorname{rank} A` | $\operatorname{rank} A$ | 零空间 | `\ker A` 或 `\operatorname{Null}(A)` | $\ker A$ |
| 像空间 | `\operatorname{Im} A` | $\operatorname{Im} A$ | 范数 | `\lVert x \rVert` | $\lVert x \rVert$ |
| 内积 | `\langle x, y \rangle` | $\langle x, y \rangle$ | 正交 | `x \perp y` | $x \perp y$ |
| 张成空间 | `\operatorname{span}` | $\operatorname{span}$ | 直和 | `V \oplus W` | $V \oplus W$ |
| 商空间 | `V / W` | $V / W$ | 对偶空间 | `V^*` | $V^*$ |

### 8. 概率与统计符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 概率 | `P(A)` | $P(A)$ | 条件概率 | `P(A \mid B)` | $P(A \mid B)$ |
| 期望 | `\mathbb{E}[X]` | $\mathbb{E}[X]$ | 方差 | `\operatorname{Var}(X)` | $\operatorname{Var}(X)$ |
| 标准差 | `\sigma_X` | $\sigma_X$ | 协方差 | `\operatorname{Cov}(X,Y)` | $\operatorname{Cov}(X,Y)$ |
| 相关系数 | `\rho_{X,Y}` | $\rho_{X,Y}$ | 分布 | `X \sim N(\mu, \sigma^2)` | $X \sim N(\mu, \sigma^2)$ |
| 独立 | `X \perp Y` | $X \perp Y$ | 条件独立 | `X \perp Y \mid Z` | $X \perp Y \mid Z$ |
| 几乎必然 | `\text{a.s.}` | $\text{a.s.}$ | 依概率 | `\xrightarrow{P}` | $\xrightarrow{P}$ |
| 依分布 | `\xrightarrow{d}` | $\xrightarrow{d}$ | 大数定律 | `\bar{X}_n \xrightarrow{P} \mu` | $\bar{X}_n \xrightarrow{P} \mu$ |
| 中心极限 | `\xrightarrow{d} N(0,1)` | $\xrightarrow{d} N(0,1)$ | 似然函数 | `L(\theta \mid x)` | $L(\theta \mid x)$ |

### 9. 几何与拓扑符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 角 | `\angle ABC` | $\angle ABC$ | 直角 | `\angle = 90^\circ` | $\angle = 90^\circ$ |
| 三角形 | `\triangle ABC` | $\triangle ABC$ | 圆 | `\bigcirc` | $\bigcirc$ |
| 平行 | `AB \parallel CD` | $AB \parallel CD$ | 垂直 | `AB \perp CD` | $AB \perp CD$ |
| 相似 | `\triangle ABC \sim \triangle DEF` | $\triangle ABC \sim \triangle DEF$ | 全等 | `\triangle ABC \cong \triangle DEF` | $\triangle ABC \cong \triangle DEF$ |
| 同胚 | `X \cong Y` | $X \cong Y$ | 基本群 | `\pi_1(X)` | $\pi_1(X)$ |
| 维数 | `\dim X` | $\dim X$ | 边界 | `\partial M` | $\partial M$ |

### 10. 其他常用特殊符号

| 含义 | 代码 | 效果 | 含义 | 代码 | 效果 |
|:----:|:-----|:----:|:----:|:-----|:----:|
| 无穷大 | `\infty` | $\infty$ | 阿列夫零 | `\aleph_0` | $\aleph_0$ |
| 阿列夫 | `\aleph` | $\aleph$ | 虚数单位 | `i` 或 `\mathrm{i}` | $\mathrm{i}$ |
| 自然底数 | `e` 或 `\mathrm{e}` | $\mathrm{e}$ | 圆周率 | `\pi` | $\pi$ |
| 约化普朗克常数 | `\hbar` | $\hbar$ | 普朗克常数 | `h` | $h$ |
| 实部 | `\operatorname{Re} z` | $\operatorname{Re} z$ | 虚部 | `\operatorname{Im} z` | $\operatorname{Im} z$ |
| 共轭 | `\bar{z}` | $\bar{z}$ | 模 | `\lvert z \rvert` | $\lvert z \rvert$ |
| 幅角 | `\arg z` | $\arg z$ | 指示函数 | `\mathbf{1}_A` | $\mathbf{1}_A$ |
| 克罗内克δ | `\delta_{ij}` | $\delta_{ij}$ | 狄拉克δ | `\delta(x)` | $\delta(x)$ |
| 勒让德符号 | `\left(\frac{a}{p}\right)` | $\left(\frac{a}{p}\right)$ | 二项式系数 | `\binom{n}{k}` | $\binom{n}{k}$ |
| 下降阶乘 | `(n)_k` | $(n)_k$ | 上升阶乘 | `n^{(k)}` | $n^{(k)}$ |
| 阶乘 | `n!` | $n!$ | 双阶乘 | `n!!` | $n!!$ |
| 多项式系数 | `\binom{n}{k_1, \ldots, k_m}` | $\binom{n}{k_1, \ldots, k_m}$ | 组合数 | `C_n^k` 或 `\binom{n}{k}` | $C_n^k$ / $\binom{n}{k}$ |

### 11. 字体样式

数学公式中经常需要切换字体来区分不同含义的符号。

| 含义 | 代码 | 效果 |
|:----:|:-----|:----:|
| 斜体（默认） | `x` | $x$ |
| 正体（罗马体） | `\mathrm{abc}` | $\mathrm{abc}$ |
| 粗体 | `\mathbf{abc}` | $\mathbf{abc}$ |
| 粗斜体 | `\boldsymbol{x}` | $\boldsymbol{x}$ |
| 花体 | `\mathcal{ABC}` | $\mathcal{ABC}$ |
| 花体（双线） | `\mathbb{ABC}` | $\mathbb{ABC}$ |
| 哥特体 | `\mathfrak{abc}` | $\mathfrak{abc}$ |
| 无衬线体 | `\mathsf{abc}` | $\mathsf{abc}$ |
| 打字机体 | `\mathtt{abc}` | $\mathtt{abc}$ |
| 斜体数学符号 | `\mathit{abc}` | $\mathit{abc}$ |

**常见用例**：

```markdown
向量：$\mathbf{v}$ 或 $\boldsymbol{v}$ → $\mathbf{v}$ / $\boldsymbol{v}$
矩阵：$\mathbf{A}$ 或 $\boldsymbol{A}$ → $\mathbf{A}$ / $\boldsymbol{A}$
数集：$\mathbb{R}, \mathbb{Z}, \mathbb{N}$ → $\mathbb{R}, \mathbb{Z}, \mathbb{N}$
函数空间：$\mathcal{F}, \mathcal{L}$ → $\mathcal{F}, \mathcal{L}$
理想/环：$\mathfrak{a}, \mathfrak{p}$ → $\mathfrak{a}, \mathfrak{p}$
微分算子：$\mathrm{d}x$ → $\mathrm{d}x$（正体 d）
单位：$\mathrm{kg}, \mathrm{m/s}$ → $\mathrm{kg}, \mathrm{m/s}$
```

### 12. 重音标记

在向量、均值、估计值等场景中，需要在符号上方添加标记。

| 含义 | 代码 | 效果 |
|:----:|:-----|:----:|
| 上划线（平均） | `\bar{x}` | $\bar{x}$ |
| 上波浪线 | `\tilde{x}` | $\tilde{x}$ |
| 上宽波浪线 | `\widetilde{AB}` | $\widetilde{AB}$ |
| 上尖帽 | `\hat{x}` | $\hat{x}$ |
| 上宽尖帽 | `\widehat{AB}` | $\widehat{AB}$ |
| 上点（导数） | `\dot{x}` | $\dot{x}$ |
| 上双点（二阶导数） | `\ddot{x}` | $\ddot{x}$ |
| 上向量箭头 | `\vec{x}` | $\vec{x}$ |
| 上宽向量箭头 | `\overrightarrow{AB}` | $\overrightarrow{AB}$ |
| 上检查符 | `\check{x}` | $\check{x}$ |
| 上 breve | `\breve{x}` | $\breve{x}$ |
| 上圆圈 | `\mathring{x}` | $\mathring{x}$ |
| 上横线（宽） | `\overline{AB}` | $\overline{AB}$ |
| 下划线 | `\underline{AB}` | $\underline{AB}$ |
| 下花括号 | `\underbrace{AB}` | $\underbrace{AB}$ |
| 上花括号 | `\overbrace{AB}` | $\overbrace{AB}$ |

**带文字的下花括号标注**：

```markdown
$$
\underbrace{a + b + c}_{\text{三项之和}}
$$
```

显示：

$$
\underbrace{a + b + c}_{\text{三项之和}}
$$

### 13. 省略号与排列

| 含义 | 代码 | 效果 |
|:----:|:-----|:----:|
| 水平省略号（底线） | `\ldots` 或 `\dots` | $x_1, \ldots, x_n$ |
| 水平省略号（中线） | `\cdots` | $x_1 + \cdots + x_n$ |
| 垂直省略号 | `\vdots` | $\vdots$ |
| 对角省略号 | `\ddots` | $\ddots$ |
| 反对角省略号 | `\iddots` | $\iddots$（需 `mathdots` 宏包） |

**不同场景的使用对比**：

```markdown
数列：$1, 2, \ldots, n$        → $1, 2, \ldots, n$
求和：$x_1 + x_2 + \cdots + x_n$ → $x_1 + x_2 + \cdots + x_n$
矩阵：
$$
\begin{pmatrix}
a_{11} & \cdots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \cdots & a_{mn}
\end{pmatrix}
$$
```

### 14. 大型运算符

| 含义 | 代码 | 效果 |
|:----:|:-----|:----:|
| 求和 | `\sum_{i=1}^{n}` | $\sum_{i=1}^{n}$ |
| 求积 | `\prod_{i=1}^{n}` | $\prod_{i=1}^{n}$ |
| 余积 | `\coprod_{i=1}^{n}` | $\coprod_{i=1}^{n}$ |
| 积分 | `\int` | $\int$ |
| 二重积分 | `\iint` | $\iint$ |
| 三重积分 | `\iiint` | $\iiint$ |
| 四重积分 | `\int\!\!\!\!\!\!\int\!\!\!\!\!\!\int\!\!\!\!\!\!\int` | $\int\!\!\!\!\!\!\int\!\!\!\!\!\!\int\!\!\!\!\!\!\int$ |
| 围道积分 | `\oint` | $\oint$ |
| 二重围道积分 | `\oiint` | $\oiint$ |
| 三重围道积分 | `\oiiint` | $\oiiint$ |
| 并集 | `\bigcup_{i=1}^{n}` | $\bigcup_{i=1}^{n}$ |
| 交集 | `\bigcap_{i=1}^{n}` | $\bigcap_{i=1}^{n}$ |
| 逻辑与 | `\bigwedge_{i=1}^{n}` | $\bigwedge_{i=1}^{n}$ |
| 逻辑或 | `\bigvee_{i=1}^{n}` | $\bigvee_{i=1}^{n}$ |
| 直和 | `\bigoplus_{i=1}^{n}` | $\bigoplus_{i=1}^{n}$ |
| 张量积 | `\bigotimes_{i=1}^{n}` | $\bigotimes_{i=1}^{n}$ |

### 15. 间距控制

公式中精确控制空格宽度的命令。

| 间距宽度 | 代码 | 效果 |
|:------:|:-----|:----:|
| 无间距 | `ab` | $ab$ |
| 小间距 | `a\,b` | $a\,b$ |
| 中间距 | `a\;b` | $a\;b$ |
| 大间距 | `a\quad b` | $a\quad b$ |
| 双大间距 | `a\qquad b` | $a\qquad b$ |
| 负间距 | `a\!b` | $a\!b$ |
| 文字间距 | `a\text{ }b` | $a\text{ }b$ |

**常见用例**：

```markdown
积分微分间：$\int f(x)\,dx$       → $\int f(x)\,dx$
条件概率：$P(A\mid B)$            → $P(A \mid B)$
定义：$f(x) \triangleq x^2$       → $f(x) \triangleq x^2$
定义式分隔：$a = b, \quad c = d$   → $a = b, \quad c = d$
```

### 16. 空格与换行

| 含义 | 代码 | 效果 |
|:----:|:-----|:----:|
| 强制空格 | `\quad` | $a \quad b$ |
| 双空格 | `\qquad` | $a \qquad b$ |
| 换行 | `\\` | 用于 `aligned`、`matrix` 等环境 |
| 不换行空格 | `\nobreakspace` | $a \nobreakspace b$ |

### 17. 颜色（部分渲染器支持）

```markdown
$\color{red}{x^2}$ → $\color{red}{x^2}$
$\color{blue}{y^2}$ → $\color{blue}{y^2}$
```

> **注意**：颜色命令在部分 Markdown 渲染器中可能不支持，建议谨慎使用，优先用文字说明代替。

---

## 六、括号与尺寸控制

### 1. 普通括号

直接写 `()`、`[]`、`{}`（花括号需转义 `\{`）：

```markdown
$(a + b)$            → $(a + b)$
$[a, b]$             → $[a, b]$
$\{x \in \mathbb{R} \mid x > 0\}$ → $\{x \in \mathbb{R} \mid x > 0\}$
```

### 2. 自动调整大小的括号

当括号内是分式、求和等大结构时，用 `\left` 和 `\right` 让括号自动伸缩：

```markdown
$\left( \frac{a}{b} \right)^2$
```

显示：$\left( \frac{a}{b} \right)^2$

对比用普通括号 `(\frac{a}{b})^2` → $(\frac{a}{b})^2$，前者括号更大、更美观。

```markdown
$\left[ \sum_{i=1}^{n} a_i \right]$
$\left\{ \frac{1}{x} \right\}$
$\left| \frac{a}{b} \right|$
```

### 3. 手动设定大小

| 命令 | 效果 |
|:----:|:----:|
| `\big` | $\big( \big)$ |
| `\Big` | $\Big vs \big$(尺寸更大) |
| `\bigg` | $\bigg( \bigg)$ |
| `\Bigg` | $\Bigg( \Bigg)$ |

```markdown
$\Big( \frac{a}{b} \Big)$
```

### 4. 分隔符（绝对值、范数、取整）

```markdown
绝对值：$\lvert x \rvert$   → $\lvert x \rvert$
范数：  $\lVert x \rVert$   → $\lVert x \rVert$
向下取整：$\lfloor x \rfloor$ → $\lfloor x \rfloor$
向上取整：$\lceil x \rceil$   → $\lceil x \rceil$
```

---

## 七、多行公式详解

多行公式是本次学习的目标重点。Markdown 的 `$$...$$` 块内，可以通过特定环境换行排版。

### 1. 多行居中（`align` 或 `aligned`）

用 `&` 指定对齐点（通常放在等号前），用 `\\` 换行：

```markdown
$$
\begin{aligned}
a^2 - b^2 &= (a + b)(a - b) \\
(a + b)^2 &= a^2 + 2ab + b^2
\end{aligned}
$$
```

显示：

$$
\begin{aligned}
a^2 - b^2 &= (a + b)(a - b) \\
(a + b)^2 &= a^2 + 2ab + b^2
\end{aligned}
$$

> `aligned` 是"内嵌对齐"环境，适合在 `$$...$$` 中直接使用；`align` 环境本身也可用，但 `aligned` 更通用、兼容性更好。

### 2. 长推导（分布对等号）

```markdown
$$
\begin{aligned}
\frac{d}{dx} (x^3) &= \lim_{h \to 0} \frac{(x+h)^3 - x^3}{h} \\
&= \lim_{h \to 0} \frac{3x^2 h + 3xh^2 + h^3}{h} \\
&= 3x^2
\end{aligned}
$$
```

显示：

$$
\begin{aligned}
\frac{d}{dx} (x^3) &= \lim_{h \to 0} \frac{(x+h)^3 - x^3}{h} \\
&= \lim_{h \to 0} \frac{3x^2 h + 3xh^2 + h^3}{h} \\
&= 3x^2
\end{aligned}
$$

**要点**：每行用一个 `&=`（对齐点在等号），`\\` 换行，这样多行等号能竖直对齐，非常清晰。

### 3. 多行独立公式（`gathered`）

若不需要对齐，只想多地排几行居中的公式，用 `gathered`：

```markdown
$$
\begin{gathered}
e^{i\pi} + 1 = 0 \\
a^2 + b^2 = c^2
\end{gathered}
$$
```

显示：

$$
\begin{gathered}
e^{i\pi} + 1 = 0 \\
a^2 + b^2 = c^2
\end{gathered}
$$

### 4. 带编号的多行公式（`align`）

在 `equation*`/`align` 环境中可自动编号（部分渲染器支持）：

```markdown
$$
\begin{align}
a &= b + c \\
c &= d + e
\end{align}
$$
```

> 若渲染器不支持编号或不想显示编号，统一推荐使用 `aligned` / `gathered`。

### 5. 在行内公式中换行（尽量避免）

inline 公式不应换行。若确实需要，尽量避免，优先改为块级公式。

---

## 八、矩阵与分段函数

### 1. 矩阵（`matrix`、`pmatrix`、`bmatrix`）

```markdown
圆括号矩阵：
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

方括号矩阵：
$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$
```

显示：

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\qquad
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

用 `&` 分隔列，用 `\\` 分隔行。

### 2. 行列式（`vmatrix`）

```markdown
$$
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
$$
```

显示：

$$
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
$$

### 3. 分段函数（`cases`）

```markdown
$$
|x| =
\begin{cases}
x, & x \ge 0 \\
-x, & x < 0
\end{cases}
$$
```

显示：

$$
|x| =
\begin{cases}
x, & x \ge 0 \\
-x, & x < 0
\end{cases}
$$

**要点**：`cases` 中第一列是公式内容，`&` 后是条件说明，`\\` 分行。

另一个常见例子（狄利克雷函数）：

```markdown
$$
D(x) =
\begin{cases}
1, & x \in \mathbb{Q} \\
0, & x \notin \mathbb{Q}
\end{cases}
$$
```

---

## 九、方程组与对齐

### 1. 方程组

```markdown
$$
\begin{cases}
x + y = 3 \\
2x - y = 0
\end{cases}
$$
```

显示：

$$
\begin{cases}
x + y = 3 \\
2x - y = 0
\end{cases}
$$

### 2. 多行分式的对齐

```markdown
$$
\begin{aligned}
\frac{a}{b} &= \frac{ac}{bc} \\
&= \frac{a}{b}
\end{aligned}
$$
```

### 3. 文本与公式混排

在公式中插入文字说明，用 `\text{...}`：

```markdown
$$
f(x) = \sin x, \quad \text{其中 } x \in \mathbb{R}
$$
```

显示：

$$
f(x) = \sin x, \quad \text{其中 } x \in \mathbb{R}
$$

- `\quad` 插入一个空格（间距），`\qquad` 插入两个。
- `\,` 插入小间距（常用于积分前 `\int f(x)\,dx`）。

---

## 十、常见错误与调试技巧

### 1. 常见错误对照

| 错误写法 | 问题 | 正确写法 |
|:---------|:-----|:---------|
| `x^10` | 只把 1 当上标 | `x^{10}` |
| `sin x` | sin 被当作变量连乘 | `\sin x` |
| `a_{ij + 1}` | 下标包含运算 | `a_{ij + 1}`（已用花括号，正确）|
| 花括号 `{}` 未转义 | 在公式中表示分组而非集合 | 集合用 `\{x\}` |
| `\left( ... \right)` 不配对 | 必须成对出现 | 确保左右配对 |
| inline 公式内换行 | 行内不能换行 | 改为块级公式 |
| 缺少 `{}` 分组 | 上下标/分式作用域混乱 | 用 `{}` 明确分组 |

### 2. 调试技巧

1. **分批验证**：先写最小公式确认渲染正常，再逐步添加内容。若某段不渲染，多半是括号不配对或 `&`/`\\` 使用错误。
2. **检查 `\\`**：多行环境换行必须用 `\\`（两个反斜杠），不是 `\n` 或单个 `\`。
3. **检查 `&` 数量**：矩阵每行用 `&` 分隔的列数必须一致，否则渲染错位。
4. **转义花括号**：公式中要输入集合 `{}` 时，写成 `\{` 和 `\}`。
5. **反斜杠补全**：`\left` 必须与 `\right` 成对（即使一边用 `.` 表示空，如 `\left. \frac{a}{b} \right|_0^1`）。

### 3. 特殊字符的转义

在公式中需要输入 `$`、`\`、`{`、`}` 等特殊字符时的处理：

```markdown
美元符：$\$5$      → 公式内美元符需转义为 \$
反斜杠：$\backslash$ → $\backslash$
花括号：$\{ \}$      → $\{ \}$
```

---

## 十一、速查表

### 1. 常用结构速查

| 结构 | 代码 |
|:----:|:-----|
| 行内公式 | `$...$` |
| 块级公式 | `$$...$$` |
| 分式 | `\frac{a}{b}` |
| 根式 | `\sqrt{x}`, `\sqrt[n]{x}` |
| 上标 | `x^n`, `x^{n+1}` |
| 下标 | `x_i`, `x_{ij}` |
| 求和 | `\sum_{i=1}^{n}` |
| 积分 | `\int_a^b` |
| 极限 | `\lim_{x \to 0}` |
| 多行对齐 | `\begin{aligned} ... \end{aligned}` |
| 分段 | `\begin{cases} ... \end{cases}` |
| 矩阵 | `\begin{pmatrix} ... \end{pmatrix}` |

### 2. 多行公式模板

**模板 A：多行推导（推荐）**

```markdown
$$
\begin{aligned}
\text{左式} &= \text{第一步} \\
&= \text{第二步} \\
&= \text{结果}
\end{aligned}
$$
```

**模板 B：分段函数**

```markdown
$$
f(x) =
\begin{cases}
\text{表达式 1}, & \text{条件 1} \\
\text{表达式 2}, & \text{条件 2}
\end{cases}
$$
```

**模板 C：方程组**

```markdown
$$
\begin{cases}
\text{方程 1} \\
\text{方程 2}
\end{cases}
$$
```

**模板 D：矩阵**

```markdown
$$
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
$$
```

---

## 配套练习

1. 写出 $e^{i\pi} + 1 = 0$ 的 inline 形式。
2. 用多行公式推导 $\frac{1}{1-x} = 1 + x + x^2 + \cdots$（等比求和）。
3. 用 `cases` 写出符号函数 $\operatorname{sgn}(x)$ 的定义。
4. 用 `aligned` 写出 $\cos 2\theta = \cos^2\theta - \sin^2\theta$ 的推导。

> 本教程配合课程 [README](README.md) 使用，是本教程书写所有数学笔记的通用公式规范。