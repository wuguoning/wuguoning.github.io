---
title: "定积分的应用"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/univ_integral
venue: "China University of Petroleum at Beijing, Department of Science"
date: 2020-02-27
location: "Beijing, CN"
---

这部分介绍一元函数定积分的应用。

## 目录

+ [第一节 求平面图形的面积](#cotes1)
+ [第二节 由平行截面求体积](#cotes2)
+ [第三节 平面曲线的弧长和曲率](#cotes3)
+ [第四节 物理应用](#cotes4)


---

<a name="cotes1"></a>
## 📌**<span style="color:blue">1. 求平面图形面积</span>**

**直角坐标下求面积**

一般地，求由$y = f_2(x), y = f_x(x)$以及两条直线$x = a, x = b$所围成的图形的面积为：

<center>
  $A = \int_a^b \vert f_2(x) - f_1(x) \vert\, \mathrm{d}x$
</center>


<center>
  <a href="https://www.geogebra.org/classic/ck2yr2ws">
  <img src="./imags/integral1d/Integral_area_between_functions.png"  width="600" height="700" />
  </a>
</center>

**参数方程下求面积**

<center>
  <a href="https://www.geogebra.org/classic/pf6sg96c">
  <img src="./imags/integral1d/para_curve_area.png"  width="600" height="500" />
  </a>
</center>
**极坐标下求二重积**
  
  首先推导一下极坐标下求二重积分。设区域$R: \alpha \le \theta \le \beta, g_1(\theta) \le r \le g_2(\theta)$。采用
  <center>
  $\Delta r, 2\Delta r, 3\Delta r, \cdots, m \Delta r$
  </center>
  <center>
  $\alpha = \theta, \theta = \alpha + \Delta \theta, \theta = \alpha + 2\Delta \theta, \cdots, \theta = \alpha +  m'\Delta \theta = \beta$
  </center>
  分割该区域，则定义在区域$R$上的二重积分可以近似的表示为：

  <center>
  $S_n = \sum\limits_{k=1}^n f(r_k, \theta_k)\Delta A_k$
  </center>

这里$\Delta A_k$表示第$k$块小区域的面积，$r_k, \theta_k$为在地$k$块区域上的取值。见下图：

  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/Polar_Double_elem.png" width="600" height="500"/>
  </a>
  </center>

二重积分可表示为：
<center>
  $$\lim\limits_{n \to \infty}S_n = \iint\limits_{R}f(r,\theta)\mathrm{d}A \tag {8}$$
</center>

接下来我们来分析$(8)$式中$\mathrm{d}A$的表示。

  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/Polar_Double_elem1.png" width="300" height="500"/>
  </a>
  </center>

<center>
$\Delta A_k = \dfrac{1}{2}\left(r_k + \dfrac{\Delta r}{2}\right) - \dfrac{1}{2}\left(r_k - \dfrac{\Delta r}{2}\right) = r_k \Delta r \Delta \theta$
</center>

所以有：

  <center>
  $S_n = \sum\limits_{k=1}^n f(r_k, \theta_k)r_k \Delta r \Delta \theta$
  </center>

故

<center>
  $$\lim\limits_{n \to \infty}S_n = \iint\limits_{R}f(r,\theta) r \mathrm{d}r  \mathrm{d}\theta \tag {9}$$
</center>

---
**确定积分范围的步骤**

+ 画出图形，写出边界曲线方程和交点的坐标；

  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/double_polar_step1.png" width="300" height="300"/>
  </a>
  </center>

+ 找到极坐标中$r$的上下限，通俗的讲，找到极径的起始穿入边界和终止穿出边界。

  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/double_polar_step2.png" width="400" height="300"/>
  </a>
  </center>

+ 找到极坐标中$\theta$的上下限，找到$\theta$的最小、最大值使积分区域落入该区域中。

  <center>
  <a href="https://www.pearsonhighered.com/thomas13einfo/">
     <img src="./imags/calculus/double_polar_step3.png" width="300" height="300"/>
  </a>
  </center>

+ 写出积分表达式：
  <center>
  $\iint\limits_{R} f(x,y)\mathrm{d}A = \int_{\dfrac{\pi}{4}}^{\dfrac{\pi}{2}} f(r, \theta) r \mathrm{d}r\mathrm{d}\theta$
  </center>
---
**✏️例子**

求位于曲线$r = 1$的外面，$r = 1 + \cos \theta$内部区域的面积。
  <center>
  <a href="https://www.geogebra.org/classic/zbmvscgy">
     <img src="./imags/calculus/polar_double_exp1.png" width="500" height="400"/>
  </a>
  </center>

<details>
解： 
$S = \iint\limits_{D} 1\mathrm{d}A = \int_{\dfrac{-\pi}{2}}^{\dfrac{\pi}{2}} \int_{1}^{1+\cos \theta}r \mathrm{d}r\mathrm{d}\theta = \int_{\dfrac{\pi}{2}}^{\dfrac{\pi}{2}} \dfrac{1}{2}(1 + \cos \theta)^2 - \dfrac{1}{2} \mathrm{d}\theta = 2 + \dfrac{\pi}{2}$
</details>


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
