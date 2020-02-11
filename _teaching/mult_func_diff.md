---
title: "多元函数微分及其应用"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/mult_func__diff
venue: "China University of Petroleum at Beijing, Department of Science"
date: 2020-02-10
location: "Beijing, CN"
---

这部分介绍多元函数微分及其应用。

## 目录
+ [第一节 平面点集与多元函数](#cotes1)


## 多元函数的基本概念


<a name="cotes1"></a>
### 📌**1. 平面点集与多元函数**

<span style="color:red">**多元函数**</span>是指自变量为两个或两个以上的函数。作为一元函数的推广自身保留了一元函数的许多性质，但是也产生了许多新的不同于一元函数的性质。本章主要针对于二元函数展开讨论，在掌握了二元函数的理论后可以推广到$n$元函数中去。

**平面点集**

当平面上确定一个坐标系后，所有的有序二元数组$(x,y)$与平面上的点之间建立了一一对应关系(数形对应)，这种确定了坐标系的平面称为<span style="color:red">**坐标平面**</span>。

坐标平面上满足某些条件$P$的点的集合称为平面点集，记作

<center>
  $E = \left\{(x,y) \vert (x,y)满足条件P\right\}$
</center>

下图为平面上三个不同<span style="color:red">**距离**</span>定义下的单位圆：

  + 欧几里德距离: $Dist(P_1(x_1, y_1), P_2(x_2, y_2)) = \sqrt{(x_1 - x^2)^2 + (y_1 - y_2)^2}$;

  + 切比雪夫距离: $Dist(P_1(x_1, y_1), P_2(x_2, y_2)) = \max \left(\vert x_1 - x_2 \vert, \vert y_1 - y_2\vert \right)$;

  + 曼哈顿德距离: $Dist(P_1(x_1, y_1), P_2(x_2, y_2)) = \vert x_1 - x_2\vert + \vert y_1 - y_2\vert$;

<center>
  <a href="https://www.geogebra.org/geometry/dedtwqnf">
  <img src="./imags/calculus/unit_set.png"  width="400" height="400" />
  </a>
</center>

如果不作声明，我们一般🈯️欧几里得距离。

若$P(x_0, y_0) \in \mathbf{R}^2$，我们称到点$P_0$的距离小于$\delta$的所有点的集合称为$P_0$的$\delta$邻域，记作$U(P_0, \delta)$.

---

**点集与集合之间的关系**

假设$E \subset \mathcal{R}^2$, 有：

+ 内点: 若存在点$P$的邻域$U(P)$，使得$U(P) \subset E$;

+ 边界点: 若$P$的任何一个邻域既含有$E$中的点，又含有不属于$E$中的点；

+ 外点: 若存在$P$的一个邻域$U(P)$，使得$U(P) \cap E = \emptyset$


<center>
  <a href="https://www.geogebra.org/geometry/nkjmkqvy">
  <img src="./imags/calculus/point_2set.png"  width="400" height="400" />
  </a>
</center>

另外点$P$与集合$E$的另一种关系为：

+ 聚点: 若点$P$的任何一个空心邻域$\mathring{U}(P, \delta)$都含有$E$中的点，则$P$称为$E$的聚点；

+ 孤立点: 若$P \in E$但不是$E$的聚点。

**一些重要的平面点集的定义**

+ <span style="color:red">**开集**</span>: 若平面点集$E$中的每一个点都为$E$的内点；

+ <span style="color:red">**闭集**</span>: 若点集$E$中的所有聚点都属于$E$，或者$E^C$($E$的补集)为开集；

+ <span style="color:red">**有界集**</span>: 若集合$E$中的点到$O(0,)$的最大距离为一个有限数；

+ <span style="color:red">**开域**</span>: 若非空开集合$E$具有<span style="color:red">**连通性**</span>即$E$中的任意两点都可以用属于$E$中的折线相连接；

+ <span style="color:red">**闭域**</span>: 开域连同其边界形成的点集；

+ <span style="color:red">**区域**</span>: 开域、闭域、或者开域连同一部分边界点形成的点集。

---

**多元函数**

---
设$D \subset \mathcal{R}^2$，若按照某个对应法则$f$，$D$中的每一个点$P(x,y)$都有一个确定的实数$z$与之对应，则称$f$
为定义在$D$上的一个<span style="color:red">**二元函数**</span>，记作

<center>
  $f: D \to \mathcal{R}$
</center>

称$D$为$f$的<span style="color:red">**定义域**</span>。若$P \in D$称与$P$所对应的$z$为点$P$的<span style="color:red">**函数值**</span>，记为$z = f(P)$。全体函数值的集合为$f$的<span style="color:red">**值域**</span>。$(x,y)$称为$f$的<span style="color:red">**自变量**</span>，而把$z$称为<span style="color:red">**因变量**</span>。


<center>
  <a href="https://www.geogebra.org/3d/svpcxqhq">
  <img src="./imags/calculus/2d_func.png"  width="400" height="400" />
  </a>
</center>

---

**$n$元函数**

设$D \subset \mathcal{R}^n$，若按照某个对应法则$f$，$D$中的每一个点$P(x_1, x_2, \cdots, x_n)$都有一个确定的实数$z$与之对应，则称$f$
为定义在$D$上的一个<span style="color:red">**$n$元函数**</span>，记作

<center>
  $f: D \to \mathcal{R}$
</center>

---
<span style="color:red"> 
📚**第一次作业:**
</span>

+ 求下列函数的定义域：
  - $f(x,y) = \sqrt{x^2 + y^2}$

  - $f(x, y) = \ln (y - x)$

  - $f(x, y, z) = \sqrt{R^2 - x^2 - y^2} + \dfrac{1}{\sqrt{x^2 + y^2 + z^2}}(R > r)$

---
<a name="cotes2"></a>
### 📌**2. 二元函数的极限**

---
设二元函数$f(x,y)$的定义域为$D \subset \mathcal{R}^2$, $P_0$为$D$的一个聚点，$A$是一个确定的实数。如果对于任意的$\epsilon > 0$，总存在某一个正数$\delta > 0$，使得当$P \in \mathring{U}(P_0, \delta)$时($\|P - P_0\| < \delta$)时，有$\vert f(P) - A \vert < \epsilon$。则称$f(x, y)$当$P \to P_0$时极限为$A$，记为：
<center>
  $\lim\limits_{P \to P_0}f(P) = A.$
</center>

<span style="color:red">
**数学逻辑语言为:**
</span>

<center>
  $\lim\limits_{P \to P_0}f(P) = A \iff \forall \epsilon > 0 \exists \delta > 0, \forall P \in \mathring{U}(P_0, \delta) \Rightarrow \vert f(P) - A \vert < \epsilon.$
</center>
---
**例子**

设$f(x,y) = (x^2 + y^2)\sin \dfrac{1}{\sqrt{x^2 + y^2}}$，求极限$\lim\limits_{(x,y)\to(0,0)}f(x,y) = 0$

---



---

## 📚参考书目
📖1. 《高等数学》上下册（第七版），同济大学，高等教育出版社，2014.7.

📖2. 《数学分析》上下册（第二版），陈纪修、於崇华、金路，高等教育出版社，2004.

📖3. 《数学分析》上下册（第二版），华东师范大学数学系，高等教育出版社，2010.

📖4.  Mathematical Analysis I,II, 2nd ed. V. A. Zorich,  Springer, 2015.

📖5.  数学分析中的典型问题与方法, 裴礼文, 高等教育出版社, 2015.

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
