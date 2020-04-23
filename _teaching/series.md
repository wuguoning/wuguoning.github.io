---
title: "级数"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/series
venue: "China University of Petroleum at Beijing, Department of Science"
date: 2020-04-23
location: "Beijing, CN"
---

这部分主要介绍无穷级数。

---

早在公元前450年，古希腊有一位名叫Zeno的学者，曾提出若干个在
数学发展史上产生过重大影响的悖论，"Achilles（希腊神话中的英雄）
追赶乌龟"即是其中较为著名的一个。

有限$-->$ 无限。

这种“无限多个数相加，相乘是否一定有意义？若不一定，怎么来判
別，无限多个数相加是否符合交换律，结合律等等。对于无限多个函数，
......."

## 目录
+ [第一节 常数项级数](#cotes1)
+ [第二节 正项级数](#cotes2)
+ [第三节 幂级数](#cotes3)
+ [第四节 函数展开称为幂级数](#cotes4)
+ [第五节 幂级数应用](#cotes5)
+ [第六节 傅里叶级数](#cotes6)

---

<a name="cotes1"></a>
### 第一节 常数项级数

设$x_1, x_2, \cdots, x_n, \cdots$ 是无限可列个实数，则称
<center>
$x_1 + x_2 + \cdots + x_n + \cdots$
</center>
为<span style="color:red">无穷项级数（简称级数）</span>，记为$\sum\limits_{n=1}^{\infty} x_n$,
其中，$x_n$ 称为级数的<span style="color:red">通项或一般项</span>。

数项级数的<span style="color:red">部分和数列</span>${S_n}$定义为：
<center>
$\begin{split}
        S_1 &= x_1 \newline
        S_2 &= x_1 + x_2 \newline
    \vdots\newline
        S_n &= x_1 + x_2 + \cdots + x_n
\end{split}
$
</center>

---
如果部分和数列${S_n}$ 收敛于有限数$S$，则称无穷级数
$\sum\limits_{n=1}^{\infty}x_n$ 收敛，且和为$S$ ，记为：
<center>
    $S = \sum\limits_{n=1}^{\infty} x_n$
</center>
如果部分和数列发散，则称无穷级数发散。

---
**例子**

设$\vert q \vert < 1$, 讨论几何级数（等比级数）

<center>
$\sum\limits_{n=1}^{\infty} q^{n-1} = 1 + q + q^2 + \cdots + q^n + \cdots$
</center>

的敛散性。

<details>
<center>
$S_n = 1 + q + q^2 + \cdots + q^n = \dfrac{1-q^n}{1-q}$
</center>
所以，当$\vert q \vert < 1$时，级数收敛于$\dfrac{1}{1-q}$.
</details>

---
**例子**
讨论数项级数
<center>
$\dfrac{1}{1\cdot 2} + \dfrac{1}{2\cdot 3} + \cdots +
        \dfrac{1}{n(n+1)} + \cdots
$
</center>
的收敛性。

<details>
<center>
$S_n = \dfrac{1}{1} - \dfrac{1}{2} + \dfrac{1}{2} - \dfrac{1}{3} + \cdots + 
       \dfrac{1}{n} - \dfrac{1}{n+1} = 1 - \dfrac{1}{n+1}$
</center>
所以级数收敛于$1$.
</details>

---
**例子**
讨论数项级数
<center>
$1 + \dfrac{1}{2} + \dfrac{1}{3} + \cdots +
        \dfrac{1}{n} + \cdots
$
</center>
的收敛性。

<details>
<center>
$\begin{split} S_n & = 1 + \dfrac{1}{2} + \left(\dfrac{1}{3} + \dfrac{1}{4}\right) \newline 
                   & + \left(\dfrac{1}{5} + \cdots + \dfrac{1}{8}\right) \newline 
                   & + \left(\dfrac{1}{9} + \cdots + \dfrac{1}{16}\right)\newline 
                   & + \cdots \newline
                   & + \left(\dfrac{1}{2^n+1} + \cdots + \dfrac{1}{2^n}\right) \newline
                   & + \cdots \newline 
                   & > 1 + \dfrac{1}{2} + \dfrac{1}{2} + \cdots + \dfrac{1}{2} + \cdots
\end{split}
$
</center>
所以级数发散。
</details>

---
**例子**
讨论级数：
<center>
$\sum\limits_{n=1}^{\infty} (-1)^{n-1} = 1 - 1 + 1 + \cdots + 
        (-1)^{n-1} + \cdots
$
</center>
的敛散性。

<details>
<center>
$S_{2n} = 0, S_{2n+1} = 1$,所以级数发散。
</center>
</details>

---
**收敛级数的性质**

1. 线性。设$\sum\limits_{n=1}^{+\infty}a_n = A, \sum\limits_{n=1}^{+\infty}b_n = B, 
\alpha, \beta$为两个常数，则有：
<center>
$\sum\limits_{n=1}^{+\infty}\left(\alpha a_n + \beta b_n\right) = \alpha A + \beta B$
</center>

2. 在级数中去掉、增加或者改变级数的有限项不影响级数的敛散性。

3. 如果级数$\sum\limits_{n=1}^{+\infty}u_n$收敛，那么对这个级数的项任意添加括弧后形成的级数仍收敛，且和不变。


---
## 📚参考书目
📖1. 《高等数学》上下册（第七版），同济大学，高等教育出版社，2014.7.

📖2. 《解析几何》，邱维声，北京大学出版社，1988.

📖3. 《解析几何》，尤承业，北京大学出版社，2004.

---
## 教学日历:

  + [2019-2020-2高等数学A](http://wuguoning.github.io/files/calculus/docs/19-20-2-A-syllabus.pdf)
  + [2019-2020-2高等数学B](http://wuguoning.github.io/files/calculus/docs/19-20-2-B-syllabus.pdf)

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
