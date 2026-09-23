# 第118级-流体力学

本目录收录以下定理：

- [Navier-Stokes方程的推导](./Navier-Stokes方程的推导.md)
- [伯努利定理的严格证明](./伯努利定理的严格证明.md)
- [Kutta-Joukowski定理](./Kutta-Joukowski定理.md)
- [Stokes定理](./Stokes定理.md)
- [Kelvin涡量定理](./Kelvin涡量定理.md)
- [Blasius定理](./Blasius定理.md)：二维不可压缩势流中，物体受到的合力与力矩不必逐点积分压力，只要把复速度的平方沿物体边界绕一圈做复围道积分就行了。
- [向量恒等式](./向量恒等式.md)：向量场的"对流项"可以拆开写成 $\boldsymbol u\cdot\nabla\boldsymbol u=\nabla\big(\tfrac12\lvert \boldsymbol u\rvert ^2\big)-\boldsymbol u\times(\nabla\times\boldsymbol u)$。这一步把沿流线的加速度项化成"动能梯度"与"涡量交叉项"之和，是推导伯努利定理的关键。
- [围道积分与Cauchy积分定理](./围道积分与Cauchy积分定理.md)：复变函数沿一条曲线做的积分叫围道积分；Cauchy 积分定理说：只要函数在这条闭曲线围成的区域里全纯（处处可导），绕一圈积出来一定是零。这条"绕圈为零"把复杂的边界积分变成只依赖少数奇点的计算。
- [牛顿第二定律](./牛顿第二定律.md)：物体动量的变化率等于它所受的合力——$\boldsymbol F=\dfrac{d\boldsymbol p}{dt}$。质量不变时它就是熟悉的 $\boldsymbol F=m\boldsymbol a$；质量会变时（如火箭），必须用动量形式，不能简单写成 $ma$。
