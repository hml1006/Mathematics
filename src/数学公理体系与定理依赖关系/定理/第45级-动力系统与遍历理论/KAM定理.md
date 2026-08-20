# KAM定理

> **一句话大白话**：给一个"完美转动的钟摆"（可积系统）加一点点小扰动，忽略有理性条件的轨道或许会乱套，但"足够无理"的那批不变环面绝大多数依然坚持存在、只是轻微变形——微扰破坏不了整套秩序。
>
> **小例子**：对刚体或摆的小参数周期扰动，只要频率向量远离共振且扰动够小，绝大多数不变环面（拟周期轨道）保持存在，这解释了太阳系许多轨道长期稳定。

## 介绍

KAM定理（Kolmogorov-Arnold-Moser定理）是动力系统理论中最深刻的成果之一，由Andrey Kolmogorov（1954年提出猜想）、Vladimir Arnold（1963年证明解析情形）和Jürgen Moser（1962年证明光滑情形）共同建立。该定理研究近可积Hamilton系统在微扰下不变环面的存留问题，断言：在足够小的、光滑的微扰下，可积Hamilton系统中的大部分不变环面（KAM环面）不会消失，而只是发生微小形变。KAM定理解决了天体力学中长期悬而未决的"小分母问题"，为理解太阳系的稳定性提供了理论基础，是Hamilton动力系统发展史上的里程碑。

## 分析

**前置依赖**：Hamilton力学、可积系统、作用-角变量、正则变换、小分母问题、Diophantine条件、隐函数定理、Nash-Moser迭代。

**定理内容**：考虑近可积Hamilton系统
$$H(I, \theta) = H_0(I) + \varepsilon H_1(I, \theta)$$
其中 $(I, \theta) \in \mathbb{R}^n \times \mathbb{T}^n$ 是作用-角坐标，$H_0$ 是可积部分，$\varepsilon$ 是小参数，$H_1$ 是微扰。若 $H_0$ 满足非退化条件
$$\det \left( \frac{\partial^2 H_0}{\partial I^2} \right) \neq 0$$
且频率 $\omega(I) = \partial H_0 / \partial I$ 满足Diophantine条件
$$|\langle k, \omega(I) \rangle| \geq \frac{\gamma}{|k|^\tau}, \quad \forall k \in \mathbb{Z}^n \setminus \{0\}$$
则对充分小的 $\varepsilon$，存在一个Cantor集 $\mathcal{C}_\varepsilon \subseteq \mathbb{R}^n$，使得对每个 $I \in \mathcal{C}_\varepsilon$，微扰系统仍存在一个不变环面，该环面接近未微扰时的环面 $\{I\} \times \mathbb{T}^n$，且其上运动是拟周期的，频率为 $\omega(I)$。这些不变环面的并集具有正测度。

**数学内涵**：
- 非退化条件（Kolmogorov条件）保证频率映射 $I \mapsto \omega(I)$ 是局部微分同胚。
- Diophantine条件排除了有理共振（小分母），保证了迭代过程的收敛性。
- 存留的不变环面形成Cantor集，其测度随 $\varepsilon \to 0$ 趋于满测度。
- 被破坏的环面对应于共振频率，共振区域由Arnold扩散填充。

**证明策略**：
1. 构造一个无穷迭代（Newton型迭代），每一步通过正则变换将微扰的阶数平方化。
2. 在每一步求解线性化方程，利用Diophantine条件控制小分母。
3. 证明迭代收敛到不变环面，且所有变换的复合仍然是光滑的（在Cantor集上）。
4. 估计被排除的共振区域的测度，证明存留环面的测度为正。

## 思考过程

KAM定理的核心困难在于"小分母问题"。在构造正则变换消除微扰时，需要求解形如
$$\langle k, \omega \rangle \, S_k = (H_1)_k$$
的方程，其中分母 $\langle k, \omega \rangle$ 可以任意小（尽管不为零），导致级数发散。Kolmogorov的天才之处在于采用了Newton型迭代（后称为KAM迭代）：每一步不是像经典微扰论那样做幂级数展开，而是将剩余微扰平方化，使得每一步的误差以超指数速度衰减，从而克服了小分母造成的收敛困难。

该定理的哲学意义在于：即使在强不可积的微扰下，Hamilton系统的相空间仍然被高度有序的KAM环面所占据，混沌运动只发生在共振层中。这解释了为什么尽管太阳系是"不可积"的，行星轨道在长时间尺度上仍然是稳定的。

## 证明过程

**定理**（KAM定理）：设 $H(I, \theta) = H_0(I) + \varepsilon H_1(I, \theta)$ 是实解析的，$H_0$ 满足非退化条件 $\det(H_0''(I)) \neq 0$。则存在 $\varepsilon_0 > 0$，使得对所有 $|\varepsilon| < \varepsilon_0$，存在Cantor集 $\Omega_\varepsilon \subseteq \mathbb{R}^n$，对每个 $\omega \in \Omega_\varepsilon$，微扰系统存在一个解析的不变环面，其上的流为 $\theta \mapsto \theta + \omega t$。

**证明**（Kolmogorov迭代法纲）：

### 1. 设置与符号

设 $H = H_0 + \varepsilon H_1$，其中 $H_0 = H_0(I)$，$H_1 = H_1(I, \theta)$ 是 $\theta$ 的周期函数。将 $H_1$ 展开为Fourier级数：
$$H_1(I, \theta) = \sum_{k \in \mathbb{Z}^n} \hat{H}_1^{(k)}(I) e^{i\langle k, \theta \rangle}$$
其中 $\hat{H}_1^{(0)}(I)$ 是平均部分。

### 2. 单步正则变换

寻找生成函数 $S(I', \theta) = \langle I', \theta \rangle + \varepsilon s(I', \theta)$，使得在新坐标 $(I', \theta')$ 下，Hamilton量变为
$$H'(I', \theta') = H_0(I') + \varepsilon [\hat{H}_1^{(0)}(I')] + O(\varepsilon^2)$$
即消除角度依赖到一阶。

由Hamilton-Jacobi方程，$s$ 需满足
$$\langle k, \omega(I') \rangle \, \hat{s}^{(k)}(I') = \hat{H}_1^{(k)}(I') - \hat{H}_1^{(0)}(I') \delta_{k,0}$$
其中 $\omega(I') = \partial H_0/\partial I (I')$。

### 3. 小分母估计

对满足Diophantine条件的频率 $\omega$：
$$|\langle k, \omega \rangle| \geq \frac{\gamma}{|k|^\tau}, \quad \forall k \neq 0$$
有
$$|\hat{s}^{(k)}| \leq \frac{|\hat{H}_1^{(k)}|}{\gamma} |k|^\tau$$
利用解析函数的Fourier系数指数衰减，可保证 $s$ 的收敛性。

### 4. 迭代与收敛

设第 $\nu$ 步的Hamilton量为 $H_\nu = N_\nu + R_\nu$，其中 $N_\nu$ 是可积部分，$R_\nu$ 是微扰。定义迭代：
1. 在频率满足Diophantine条件的区域上求解线性化方程。
2. 构造正则变换 $\Phi_\nu$ 将 $H_\nu$ 变为 $H_{\nu+1} = H_\nu \circ \Phi_\nu$。
3. 估计 $\|R_{\nu+1}\| \leq C_\nu \|R_\nu\|^2$（平方收敛）。
4. 适当选择参数序列 $\{\gamma_\nu\}$，使得排除的共振区域测度总和可控。

### 5. 不变环面的构造

令 $\Phi^\nu = \Phi_1 \circ \cdots \circ \Phi_\nu$，则 $\Phi^\nu$ 在Cantor集 $\Omega_\varepsilon$ 上一致收敛到 $\Phi^\infty$。原系统在 $\Phi^\infty$ 下的像为可积系统，因此原系统在 $\Phi^\infty(\mathbb{T}^n)$ 上存在不变环面。$\square$

**推论**：在KAM定理的条件下，近可积Hamilton系统在相空间中存在一个正测度的不变环面集，其上的运动是拟周期的。这表明即使系统不可积，其大部分轨道仍然表现出高度规则的行为。$\square$