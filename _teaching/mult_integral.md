---
title: "重积分"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/mult_integral
venue: "China University of Petroleum at Beijing, Department of Science"
date: 2020-02-10
location: "Beijing, CN"
---

这部分介绍多元函数重积分及其应用。

## 目录
+ [第一节 二重积分概念](#cotes1)
+ [第二节 二重积分计算方法](#cotes2)
+ [第三节 三重积分概念](#cotes3)
+ [第四节 三重积分计算方法](#cotes4)
+ [第五节 重积分的应用](#cotes5)
+ [第六节 复合函数求导法则](#cotes6)
+ [附录一 直角坐标与极坐标系](#cotes7)
+ [附录二 直角坐标、柱坐标与球坐标](#cotes8)

---

<a name="cotes1"></a>
## 📌**1. 二重积分的概念与性质**

☘︎ **二重积分的概念**

考察一个<span style="color:red">**曲顶柱体**</span>: 它的底是$xOy$面上的具有零边界的有界区域$D$，顶是非负连续函数$z = f(x,y), (x,y) \in D$所确定的曲面，侧面是以$D$的边界曲线为准线，母线平行于$z$轴的柱面。如下图所示([本图来源于Thomas' Calculus, 13/e](https://www.pearsonhighered.com/thomas13einfo/))：

<center>
<a href="https://www.pearsonhighered.com/thomas13einfo/">
   <img src="./imags/calculus/curve_cylinder.png" width="400" height="400"/>
</a>
</center>

为了得到该曲顶柱体的体积:

+ 我们采用一系列平行于坐标轴的直线把区域$D$分割为一系列的小矩形(这个分割记为$P$)。第$k$个小矩形的面积为$\Delta A = \Delta x \Delta y (k=1,2,\cdots,n)$，见下图：

<center>
<a href="https://www.pearsonhighered.com/thomas13einfo/">
   <img src="./imags/calculus/double_inte_grid.png" width="400" height="400"/>
</a>
</center>

+ 在第$k$个小矩形上任意去一点$(x_k, y_k) \in A_k(k=1,2,\cdots,n)$，然后求和(<span style="color:red">**黎曼和**</span>)得到：

  <center>
  $S_n = \sum\limits_{k=1}^n f(x_k, y_k)\Delta A_k$
  </center>

  <center>
  <a href="https://www.geogebra.org/3d/mrqw8ehc">
     <img src="./imags/calculus/Double_Integral.png" width="500" height="500"/>
     <img src="./imags/calculus/Double_Integral_all_colo.png" width="500" height="500"/>
  </a>
  </center>

+ 把每个小矩形的<span style="color:red">**直径**</span>记为$\lambda_k$，这里直径指的是小矩形中两点连线最长的长度。令
  <center>
  $\Vert P \Vert = \mathbf{max}_{1 \le k \le n}\left\{\lambda_k\right\}$
  </center>
  称$\Vert P \Vert$为<span style="color:red">**分割细度**</span>。黎曼和对分割的细度取极限，讨论极限：

  <center>
  $\lim\limits_{\Vert P \Vert \to 0} \sum\limits_{k=1}^n f(x_k,y_k)\Delta A_k$
  </center>

  <center>
  <a href="https://www.geogebra.org/3d/mrqw8ehc">
     <img src="./imags/calculus/double_stacks.png" width="800" height="500"/>
  </a>
  </center>

如果随着分割细度趋于零，黎曼和的极限存在，我们称此极限值为$f(x,y)$在$D$上的<span style="color:red">**定积分**</span>。记为：

<center>
$\iint\limits_{D} f(x, y)\mathrm{d}A$ 或者 $\iint\limits_{D} f(x, y)\mathrm{d}x\mathrm{d}y$  
</center>

---
<span style="color:red">**除了采用平行于坐标轴的直线网分割外，也可以采用曲线网分割定义域。不同的分割会得到不同的积分方法。**</span>

---
☘︎**二重积分的性质**

二重积分$\iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y$具有以下性质：
  
  + 线性： $\iint\limits_{D} \left(\alpha f(x, y) + \beta g(x,y)\right)\mathrm{d}x \mathrm{d}y = \alpha \iint\limits_{D} f(x,y) \mathrm{d}x \mathrm{d}y+ \beta \iint\limits_{D} g(x,y)\mathrm{d}x \mathrm{d}y$;

  + 区域可加性：$\iint\limits_{\substack{D_1 \cup D_2 \newline D_1 \cap D_2 = \emptyset}} f(x, y)\mathrm{d}x \mathrm{d}y = \iint\limits_{D_1} f(x, y)\mathrm{d}x \mathrm{d}y +  \iint\limits_{D_2} f(x, y)\mathrm{d}x \mathrm{d}y $;

  + 保号性：如果在$D$上，$f(x,y) \le g(x,y)$，那么有：$\iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y \le \iint\limits_{D} g(x, y)\mathrm{d}x \mathrm{d}y$;

  + 特别的有：$\left\vert\iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y\right\vert \le \iint\limits_{D}\left\vert f(x, y)\right\vert\mathrm{d}x \mathrm{d}y$;

  + 设$M \ge f(x,y) \ge m$，则有：$ms(D) \le \iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y \le Ms(D)$，其中$s(D)$表示区域$D$的面积;

  + 中值定理：设函数$f(x,y)$在闭区域$D$上连续，$s(D)$表示区域$D$的面积，则至少存在一点$(\xi, \eta) \in D$满足：$\iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y = f(\xi,\eta)s(D)$.

---

<a name="cotes1"></a>
## 📌**2. 二重积分的计算方法**

下面讨论二重积分$\iint\limits_{D} f(x, y)\mathrm{d}x \mathrm{d}y$的🧮计算问题。

---
**直交坐标下二重积分的计算：Fubini定理**

假设我们计算由$z = f(x,y)$在区域$D: -1 \le x \le 3, -2 \le y \le 3$上围成的曲顶柱体的体积。由截面法求体积得到，该曲顶柱体的体积为：

<center>
$$V = \int_{-1}^3 A(x)\mathrm{d}x \tag {1}$$
</center>

其中$A(x)$为：

<center>
$$A(x) = \int_{-2}^3 f(x,y)\mathrm{d}y \tag {2}$$
</center>

将$(2)$式代入$(1)$式得到：


<center>
$$V = \int_{-1}^3 A(x)\mathrm{d}x = \int_{-1}^3 \left(\int_{-2}^3 f(x,y)\mathrm{d}y\right)\mathrm{d}x \tag {3}$$
</center>

见下图：

  <center>
  <a href="https://www.geogebra.org/3d/hmb9zbyq">
     <img src="./imags/calculus/Iterated_Double_Integrals.png" width="800" height="600"/>
  </a>
  </center>

对称地，先对坐标$x$积分，然后对坐标$y$积分，得到：

<center>
$$V = \int_{-2}^3 A(y)\mathrm{d}y = \int_{-2}^3 \left(\int_{-1}^3 f(x,y)\mathrm{d}x\right)\mathrm{d}y \tag {4}$$
</center>

见下图：

  <center>
  <a href="https://www.geogebra.org/3d/hmb9zbyq">
     <img src="./imags/calculus/Iterated_Double_Integrals_1.png" width="800" height="600"/>
  </a>
  </center>

---
<span style="color:red">**Fubini定理**</span>

设$z = f(x,y)$在区域$D: a \le x \le b, c \le y \le d$上连续，则有：
<center>
$$\iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y = \int_{c}^d \left(\int_{a}^b f(x,y)\mathrm{d}x\right)\mathrm{d}y = \int_{a}^b \left(\int_{c}^d f(x,y)\mathrm{d}y\right)\mathrm{d}x  \tag {5}$$
</center>

---
对于一般性区域$D$，分析以下两种情形：

+ 情形一： $D: a \le x \le b, g_1(x) \le y \le g_2(x)$. 对于该类型区域积分可以表示为：

  <center>
    $$\iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y = \int_{a}^b \left(\int_{g_1(x)}^{g_2(x)} f(x,y)\mathrm{d}y\right)\mathrm{d}x  \tag {6}$$
  </center>

+ 情形二： $D: c \le y \le d, h_1(y) \le x \le h_2(y)$. 对于该类型区域积分可以表示为：

  <center>
    $$\iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y = \int_{c}^d \left(\int_{h_1(y)}^{h_2(y)} f(x,y)\mathrm{d}x\right)\mathrm{d}y  \tag {7}$$
  </center>

见下图([本图来源于Thomas' Calculus, 13/e](https://www.pearsonhighered.com/thomas13einfo/))：


  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/Iterated_Double_Integrals_2.png" width="800" height="500"/>
  </a>
  </center>

---







---

## 📚参考书目

📖1. 《高等数学》上下册（第七版），同济大学，高等教育出版社，2014.7.

📖2. 《数学分析》上下册（第二版），陈纪修、於崇华、金路，高等教育出版社，2004.

📖3. 《数学分析》上下册（第二版），华东师范大学数学系，高等教育出版社，2010.

📖4.  Mathematical Analysis I,II, 2nd ed. V. A. Zorich,  Springer, 2015.

📖5.  数学分析中的典型问题与方法, 裴礼文, 高等教育出版社, 2015.

📖6.  Thomas's Calculus, Weir, Maurice D etc., Addison-Wesley, 2010.


---

# Calculus and its Visualization: an Introduction

<center>
<a href="https://www.geogebra.org/material/edit/id/yxadpqun#bookcontent">
   <img src="./imags/surface.png" width="200" height="200"/>
</a>
</center>


---

# 👏 THANKS

<center>

<a href="https://www.geogebra.org">
   <img src="./imags/geogebra.png" width="200" height="60"/>
</a>

<a href="https://www.geogebra.org">
   <img src="./imags/github.png" width="200" height="60"/>
</a>

<a href="https://www.wikipedia.org/">
   <img src="./imags/wiki.png" width="200" height="50"/>
</a>
</center>

