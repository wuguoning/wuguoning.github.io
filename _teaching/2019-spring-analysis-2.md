---
title: "Real Analysis 《數學分析》"
collection: teaching
type: "Workshop"
permalink: /teaching/2019-spring-analysis-2
venue: "China University of Petroleum at Beijing, Science"
date: 2019-03-28
location: "City, Country"
---

These notes are basically based on the books below:

<img src="/images/zorich1.png" width = "80" height = "120">
<img src="/images/zorich2.png" width = "80" height = "120">
<img src="/images/huadongtext1.png" width = "90" height = "145">
<img src="/images/huadongtext2.png" width = "90" height = "125">
<img src="/images/fudantext.png" width = "130" height = "180">


Real Analysis I
======
## [<span style="color:blue">**Introduction.**</span>](http://wuguoning.github.io/files/introduction.pdf)
## [<span style="color:blue">**Limit of Sequence.**</span>](http://wuguoning.github.io/files/limits.pdf)
[<span style="color:red">**Test1.**</span>](http://wuguoning.github.io/files/test1.pdf)
## [<span style="color:blue">**Continuity.**</span>](http://wuguoning.github.io/files/continuity.pdf)
[<span style="color:red">**Test2.**</span>](http://wuguoning.github.io/files/test2.pdf)
## [<span style="color:blue">**Derivative of One Variable Function.**</span>](http://wuguoning.github.io/files/derivative.pdf)
[<span style="color:red">**Test3.**</span>](http://wuguoning.github.io/files/test3.pdf)
## [<span style="color:blue">**Primitive.**</span>](http://wuguoning.github.io/files/primitive.pdf)
[<span style="color:red">**Test4.**</span>](http://wuguoning.github.io/files/test4.pdf)
## [<span style="color:blue">**Midterm Test.**</span>](http://wuguoning.github.io/files/midtermtest18-19-1.pdf)

Real Analysis II
======
## [<span style="color:blue">**Definite Integral.**</span>](http://wuguoning.github.io/files/integral.pdf)
## [<span style="color:blue">**Multi-variable Function.**</span>](http://wuguoning.github.io/files/mul_var_fun.pdf)
## [<span style="color:blue">**Differential of Multi-variable Function.**</span>](http://wuguoning.github.io/files/diff_multi_var.pdf)
## <span style="color:blue">**Multiple Integral.**</span>
### Introduction 
* **Volume Problem** Find the volume $V$ of the solid $G$ enclosed between the surface $z = f(x,y)$ and the region $R$ in the $xy-$plane where $f(x,y)$ is continuous and non-negative on $R$.

   <img src="/images/multi_int_vol1.png" alt="drawing" width = "200"/>
* **Mass Problem** Find the mass $M$ of a lamina (a region $R$ in the $xy-$plane) whose density is a continuous nonnegative function $\rho(x,y)$

    <img src="/images/mul_int_mass1.png" alt="drawing" width = "200"/>

Let us consider the **Volume Problem**

  <img src="/images/mul_int_vol2.png" alt="drawing" width = "600"/>

1. Divide the rectangle enclosing $R$ into subrectangles, and exclude all those rectangles that contain points outside $R$. Let $n$ be the number of all the rectangles inside $R$, and let $\Delta A_k = \Delta x_k \Delta y_k$ be the area of the $k-$th subrectangle.
2. Choose any point $(\xi_k, \eta_k)$ in the $k-$th subrectangle. The volume of a rectangular parallelepiped with base area $\Delta A_k$ and height $f(\xi_k, \eta_k)$ is $\Delta V_k = f(\xi_k, \eta_k)\Delta A_k$, thus,$$ \begin{equation} V \approx \sum_{k=1}^n \Delta V_k = \sum_{k=1}^n f(\xi_k, \eta_k)\Delta A_k = \sum_{k=1}^n f(\xi_k, \eta_k)\Delta x_k \Delta y_k\label{eq:eq1} \tag{1}\end{equation}$$, This sum is called the <span style="color:red">**Rimann sum**</span>.
3. Take the sides of all the subrectangles to 0, and get $$ \begin{equation} V = \lim_{\lambda(P)\to 0} \sum_{k=1}^n f(\xi_k, \eta_k)\Delta A_k = \iint_R f(x,y)\, \mathrm{d}A \label{eq:eq2} \tag{2}\end{equation}$$.










Real Analysis III
======


