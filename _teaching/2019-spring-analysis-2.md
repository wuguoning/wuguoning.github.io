---
title: "Real Analysis For Undergraduate"
collection: teaching
type: "Workshop"
permalink: /teaching/2019-spring-analysis-2
venue: "China University of Petroleum at Beijing, Science"
date: 2019-03-28
location: "City, Country"
---


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

Introduction 
------------
* **Volume Problem** Find the volume $V$ of the solid $G$ enclosed between the surface $z = f(x,y)$ and the region $R$ in the $xy-$plane where $f(x,y)$ is continuous and non-negative on $R$.

   <img src="/images/multi_int_vol1.png" alt="drawing" width = "200"/>
* **Mass Problem** Find the mass $M$ of a lamina (a region $R$ in the $xy-$plane) whose density is a continuous nonnegative function $\rho(x,y)$

    <img src="/images/mul_int_mass1.png" alt="drawing" width = "200"/>

Let us consider the **Volume Problem**

  <img src="/images/mul_int_vol2.png" alt="drawing" width = "600"/>

* Divide the rectangle enclosing $R$ into subrectangles, and exclude all those rectangles that contain points outside $R$. Let $n$ be the number of all the rectangles inside $R$, and let $\Delta A_k = \Delta x_k \Delta y_k$ be the area of the $k-$th subrectangle.
* Choose any point $(\xi_k, \eta_k)$ in the $k-$th subrectangle. The volume of a rectangular parallelepiped with base area $\Delta A_k$ and height $f(\xi_k, \eta_k)$ is $\Delta V_k = f(\xi_k, \eta_k)\Delta A_k$, thus,

$$ \begin{equation} V \approx \sum_{k=1}^n \Delta V_k = \sum_{k=1}^n f(\xi_k, \eta_k)\Delta A_k = \sum_{k=1}^n f(\xi_k, \eta_k)\Delta x_k \Delta y_k\label{eq:mul_int_1} \tag{1}\end{equation}$$ 

This sum is called the <span style="color:red">**Rimann sum**</span>.
* Take the sides of all the subrectangles to 0, and get 

$$ \begin{equation} V = \lim_{\lambda(P)\to 0} \sum_{k=1}^n f(\xi_k, \eta_k)\Delta A_k = \iint_R f(x,y)\, \mathrm{d}A \label{eq:mul_int_2} \tag{2}\end{equation}$$

The last term is the notation for the limit of the Riemann sum, and it is called the **double integral** of $f(x,y)$ over $R$.

The Darboux Criterion
---------------------
Let us consider another criterion for Riemann integrability of a function, which is applicable only to real-valued function.

**Lower and Upper Darboux Sums** Let $f$ be a real-valued function on the interval $I$ and $P = {I_i}$ a partition of the interval $I$. We set 
    \begin{equation} 
        m_i = \inf_{x \in I_i} f(x), M_i = \sup_{x \in I_i}f(x).
        \label{eq:mul_int_3} \tag{3}
    \end{equation}

The quantities
    \begin{equation}
        s(f, P) = \sum_i m_i |I_i|, S(f, P) = \sum_i M_i |I_i|
        \label{eq:mul_int_4}\tag{4}
    \end{equation}
    are called the **lower** and **upper sums** of the function $f$ over the interval $I$ corresponding to the partion $P$ of the interval.

The following relations hold between the Darboux sums a a function $f: I \to \mathbb{R}$:
  1. $s(f, P) = \inf_{\xi} \sigma(f, P, \xi) \le \sigma(f, P, \xi) \le \sup_{\xi}\sigma(f, P, \xi)  = S(f, P)$
  2. If the partition $P'$ of the interval $I$ is obtained by refining intervals of the partion $P$, then 
         $s(f, P) \le s(f, P') \le S(f, P') \le S(f, P)$
  3. The inequality $s(f, P_1) \le S(f, P_2)$ holds for any pair of partition $P_1, P_2$ of the interval $I$.

Lower and Upper Integrals
-------------------------
The **lower** and **upper** Darboux integrals of the function $f: I \to \mathbb{R}$ over the interval $I$ are respectively 
\begin{equation} 
    \underline{I} = \sup_{P} s(f, P), \overline{I} = \inf_{P} S(f, P) 
        \label{eq:mul_int_5}\tag{5}
\end{equation}
where the supremum and infimum are taken over all partitions $P$ of the interval $I$.

```{theorem}
For any bounded function: 
```
$f: I \to \mathbb{R}$, 
\begin{equation}
  \lim_{\lambda(P)\to 0}s(f, P) = \underline{I},
  \lim_{\lambda(P)\to 0}S(f, P) = \overline{I}
\end{equation}.


The Darboux Criterion for Integrability of a Real-valued Function
-----------------------------------------------------------------







Real Analysis III
======


