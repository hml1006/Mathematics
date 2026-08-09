# -*- coding: utf-8 -*-
"""第16级-解析几何 极坐标方程图形生成脚本"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 注册中文字体
_cjk = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(_cjk)
_fp = fm.FontProperties(fname=_cjk)
plt.rcParams['font.sans-serif'] = [_fp.get_name()] + plt.rcParams.get('font.sans-serif', [])
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10,
                     'axes.titlesize': 12, 'axes.labelsize': 10})


def save(fig, name):
    fig.savefig(name, bbox_inches='tight')
    plt.close(fig)
    print('saved', name)


# ---------- 图1：极坐标与直角坐标的联系 ----------
def polar_grid(ax, rmax=2.5):
    ax.set_aspect('equal')
    ax.set_theta_zero_location('N')   # 0° 朝上
    ax.set_theta_direction(-1)        # 逆时针为正
    ax.grid(True, which='major', alpha=0.4)
    ax.set_rmax(rmax)
    ax.set_xticks(np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(['0°', '45°', '90°', '135°', '180°', '225°', '270°', '315°'])


fig, axes = plt.subplots(1, 2, figsize=(9, 4.2), subplot_kw={'projection': 'polar'})
# (a) 一个点的极坐标
axes[0].plot([0, np.deg2rad(60)], [0, 3], color='C0', lw=2)
axes[0].scatter([np.deg2rad(60)], [3], color='C0', zorder=5, s=30)
axes[0].annotate('(3, 60°)', xy=(np.deg2rad(60), 3.2), color='C0')
axes[0].set_title('(a) 用(距离, 角度)表示一个点')
polar_grid(axes[0], 3.5)
# (b) 极坐标网格
theta = np.deg2rad(np.linspace(0, 360, 360))
for r in [1, 2, 3]:
    axes[1].plot(theta, [r]*len(theta), color='gray', lw=0.8, alpha=0.6)
axes[1].set_title('(b) 极坐标网格：同心圆 + 射线')
polar_grid(axes[1], 3.5)
save(fig, 'polar-01-concept.svg')


# ---------- 图2：圆 ----------
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 2*np.pi, 500)
cases = [('r = a（圆心在极点）', np.full_like(theta, 2.0)),
         ('r = 2a·cosθ（过极点）', 4*np.cos(theta)),
         ('r = 2a·cos(θ-30°)，圆心偏转', 4*np.cos(theta - np.deg2rad(30)))]
for ax, (title, r) in zip(axes, cases):
    ax.plot(theta, r, lw=2, color='C2')
    ax.set_title(title)
    polar_grid(ax, 4.5)
save(fig, 'polar-02-circle.svg')


# ---------- 图3：直线 ----------
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6), subplot_kw={'projection': 'polar'})
# (a) 过极点的射线 θ = 45°
axes[0].plot([0, np.deg2rad(45)], [0, 4], lw=2, color='C1')
axes[0].set_title('(a) 过极点的射线 θ = 45°')
polar_grid(axes[0], 4.5)
# (b) 不过极点的直线 r = r0·sec(θ-γ)：即 x = r0
th = np.linspace(-0.9, 0.9, 200)
r = 2.0/np.cos(th - 0)  # r0 sec θ, 垂直于0°
axes[1].plot(th, r, lw=2, color='C3')
axes[1].set_title('(b) 直线 r = 2·secθ（即 x = 2）')
polar_grid(axes[1], 5)
save(fig, 'polar-03-line.svg')


# ---------- 图4：圆锥曲线（一个焦点在极点） ----------
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 2*np.pi, 600)
l = 2.0
for ax, eps, title in zip(axes, [0.5, 1.0, 1.5],
                          ['椭圆 ε=0.5', '抛物线 ε=1.0', '双曲线 ε=1.5']):
    r = l/(1 - eps*np.cos(theta))
    ax.plot(theta, r, lw=2, color='C4')
    ax.set_title(title)
    polar_grid(ax, 6)
save(fig, 'polar-04-conic.svg')


# ---------- 图5：玫瑰线 ----------
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), subplot_kw={'projection': 'polar'})
for ax, k, title in zip(axes, [3, 4, 6],
                        ['r = a·cos(3θ) 三叶', 'r = a·cos(4θ) 八叶', 'r = a·cos(6θ) 十二叶']):
    theta = np.linspace(0, 2*np.pi, 1000)
    ax.plot(theta, 2.5*np.cos(k*theta), lw=2, color='C5')
    ax.set_title(title)
    polar_grid(ax, 3)
save(fig, 'polar-05-rose.svg')


# ---------- 图6：螺线（阿基米德 + 对数） ----------
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6), subplot_kw={'projection': 'polar'})
# (a) 阿基米德螺线 r = a + bθ（等距）
axes[0].plot(np.linspace(0, 6*np.pi, 1200), 0.5*np.linspace(0, 6*np.pi, 1200), lw=2, color='C6')
axes[0].set_title('(a) 阿基米德螺线 r = a + bθ（圈距相等）')
polar_grid(axes[0], 10)
# (b) 对数螺线 r = a·e^{bθ}（等角）
axes[1].plot(np.linspace(0, 4*np.pi, 800), 0.3*np.exp(0.12*np.linspace(0, 4*np.pi, 800)), lw=2, color='C7')
axes[1].set_title('(b) 对数螺线 r = a·e^{bθ}（等角）')
polar_grid(axes[1], 12)
save(fig, 'polar-06-spiral.svg')


# ---------- 图7：心形线、双纽线、三叶玫瑰 ----------
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 2*np.pi, 800)
# (a) 心形线 r = a(1+cosθ)
axes[0].plot(theta, 2.5*(1+np.cos(theta)), lw=2, color='C1')
axes[0].set_title('(a) 心形线 r = a(1+cosθ)')
polar_grid(axes[0], 5.5)
# (b) 双纽线 r² = a²cos2θ
axes[1].plot(theta, np.sqrt(np.abs(2.5**2*np.cos(2*theta))), lw=2, color='C2')
axes[1].set_title('(b) 双纽线 r² = a²cos2θ')
polar_grid(axes[1], 3)
# (c) lemniscate style pascal
axes[2].plot(np.linspace(0, 2*np.pi, 800), np.abs(2.0*np.cos(2*theta))**(1/2), lw=2, color='C3')
axes[2].set_title('(c) 双纽线（另一叶）')
polar_grid(axes[2], 3)
save(fig, 'polar-07-cardioid-lemniscate.svg')


# ---------- 图8：对称性判定 ----------
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), subplot_kw={'projection': 'polar'})
# (a) 关于水平轴(0°/180°)对称：r(-θ)=r(θ) 用cos
axes[0].plot(theta, 2.5*np.cos(3*theta - 0), lw=2, color='C5')
axes[0].set_title('(a) 关于 0°/180° 对称')
polar_grid(axes[0], 3)
# (b) 关于竖直轴对称：r(π-θ)=r(θ)
axes[1].plot(theta, 3.0*np.abs(np.sin(theta)), lw=2, color='C6')
axes[1].set_title('(b) 关于 90°/270° 对称')
polar_grid(axes[1], 3.5)
# (c) 旋转对称
axes[2].plot(theta, 2.5*np.cos(4*theta), lw=2, color='C7')
axes[2].set_title('(c) 旋转对称（4叶）')
polar_grid(axes[2], 3)
save(fig, 'polar-08-symmetry.svg')

print('ALL DONE')