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
$\sum\limits_{n=1}^{+\infty}\left(\alpha a_n + \beta b_n\right) = \alpha A + \beta B$

2. 在级数中去掉、增加或者改变级数的有限项不影响级数的敛散性。

3. 如果级数$\sum\limits_{n=1}^{+\infty}u_n$收敛，那么对这个级数的项任意添加括弧后形成的级数仍收敛，且和不变。

4. 如果级数$\sum\limits_{n=1}^{+\infty}u_n$收敛，则$\lim\limits_{n \to \infty}u_n = 0$.

---
**例子**
讨论级数：
<center>
$\sum\limits_{n=1}^{\infty} \frac{2n - 1}{2^n}$
</center>
的敛散性。

<details>
提示： $S_n = 2S_n - S_n$
</details>

---
**例子**
讨论级数：
<center>
$\sum_{n=1}^{\infty} \arctan\frac{1}{2n^2}$
</center>
的敛散性。
<details>
提示：
<center>
$\arctan x - \arctan y = \arctan \frac{x - y}{1 + xy}
\arctan \frac{1}{2n^2} = \arctan \frac{1}{2n-1} - 
        \arctan \frac{1}{2n + 1}$
</center>
</details>

---
**柯西收敛原理**

级数$\sum\limits_{n=1}^{\infty} u_n$ 收敛的充分必要条件为：
    任给$\epsilon>0$，总存在正数$N$，使得当$m > N$ 以及对于任意的正整数$p$，
    都有：
<center>
$\left| u_{m+1} + u_{m+2} + \cdots + u_{m+p} \right| < \epsilon.$
</center>

---
**第一次作业**

**证明下列级数收敛，并求其和**

   + $\left(\frac{1}{2} + \frac{1}{3}\right) + 
        \left(\frac{1}{2^2} + \frac{1}{3^2}\right) + \cdots + 
        \left(\frac{1}{2^n} + \frac{1}{3^n}\right) + \cdots $
<details>
  提示：$\left(\frac{1}{2} + \frac{1}{3}\right) + 
  \left(\frac{1}{2^2} + \frac{1}{3^2}\right) + \cdots + 
  \left(\frac{1}{2^n} + \frac{1}{3^n}\right)
  =\sum\limits_{n=1}^{+\infty} \dfrac{1}{2^n} + 
  \sum\limits_{n=1}^{+\infty} \dfrac{1}{3^n}
$
</details>

  + $\sum\limits_{n=1}^{\infty} \dfrac{1}{n(n+1)(n+2)}$ 
<details>
  提示：$
  \dfrac{1}{n(n+1)(n+2)} =\dfrac{1}{2} \left[\dfrac{1}{n(n+1)} - \dfrac{1}{(n+1)(n+2)}\right]
$
</details>

+ $\sum\limits_{n=1}^{\infty} \left(\sqrt{n+2} - 2\sqrt{n+1}
        + \sqrt{n} \right)$ 
<details>
提示：$
  \sqrt{n+2} - 2\sqrt{n+1} + \sqrt{n} = \sqrt{n+2} - \sqrt{n+1} - 
  \left(\sqrt{n+1} - \sqrt{n}\right)
$
</details>

---

<a name="cotes2"></a>
### 第二节 正项级数

---
**正向级数收敛性的一般判别法则**

若数项级数的各项符号相同，则称它为同号级数。对于同号级数，只需研究各项都是正数组成的级数--正项级数。

---

正向级数$\sum\limits_{n=1}^{\infty} u_n$ 收敛的充要条件是：部分和数列$S_n$有界。

---
**比较判别法**

设$\sum\limits_{n=1}^{\infty} u_n, \sum\limits_{n=1}^{\infty} v_n$ 是两个正向级数，如果存在某个正数$N$ ，对于一切$n > N$，都有：
<center>
    $u_n \le v_n$
</center>
则：

  +  若级数$\sum\limits_{n=1}^{\infty} v_n$ 收敛，则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 收敛；
  + 若级数$\sum\limits_{n=1}^{\infty} u_n$ 发散，则级数$\displaystyle \sum\limits_{n=1}^{\infty} v_n$ 发散。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \dfrac{1}{n^2 - n + 1}$的敛散性。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \sin \dfrac{\pi}{n}$的敛散性。

---
**比较判别法的极限形式**

设$\sum\limits_{n=1}^{\infty} u_n, \sum\limits_{n=1}^{\infty} v_n$ 是两个正向级数，如果
<center>
  $\lim\limits_{n \to \infty} \dfrac{u_n}{v_n} = l$
</center>
则：

  + 当$0 < l < \infty$，则级数$\displaystyle \sum\limits_{n=1}^{\infty} v_n, \sum\limits_{n=1}^{\infty} u_n$ 同时收敛或同时发散；
  + 当$l = 0$，级数$\displaystyle \sum\limits_{n=1}^{\infty} v_n$ 收敛时，则级数
            $\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 收敛;
  + 当$l = +\infty$，级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 发散时，则级数
            $\displaystyle \sum\limits_{n=1}^{\infty} v_n$ 发散.

---
**例子**

讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \dfrac{1}{2^n-n}$的敛散性。

---
**例子**

讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \sin \dfrac{1}{n}$的敛散性。

---
**例子**
讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \left(1 - \cos \frac{\pi}{n}\right)$的敛散性。

---
**比值判别法和根值判别法**

---
设$\sum\limits_{n=1}^{\infty} u_n$ 为正项级数，且存在某正数$N_0$及常数 $q (0 < q < 1).$ 

  + 对于一切$n > N_0$，成立不等式$\dfrac{u_{n+1}}{u_n} \le q$,
 则级数$\sum\limits_{n=1}^{\infty} u_n$ 收敛。
  + 对于一切$n > N_0$，成立不等式$\dfrac{u_{n+1}}{u_n} \ge 1$,
        则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 发散。
        
---
设$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 为正项级数，且
<center>
$\lim\limits_{n \to \infty} \dfrac{u_{n+1}}{u_n} = q$
</center>
则，

  + 当$q < 1$，则级数$\sum\limits_{n=1}^{\infty} u_n$ 收敛。
  + 当$q > 1$ 或$q = \infty$，则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 发散。

---
当$q=1$时，级数可能收敛，也可能发散。例如：$\displaystyle \sum\limits_{n=1}^{\infty} \dfrac{1}{n^2}, \sum\limits_{n=1}^{\infty}\dfrac{1}{n}$.

---
**d'Alembert判别法**
    设$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$是正项级数，
    
   + 当$\displaystyle \overline{\lim\limits_{n\to\infty}} \dfrac{x_{n+1}}{x_n} = \overline{r} < 1$, 则级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$收敛；
   + 当$\displaystyle \underline{\lim\limits_{n\to\infty}} \dfrac{x_{n+1}}{x_n} = \underline{r} > 1$, 则级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$发散；
   + 当$\displaystyle \overline{r} \ge 1$或$\displaystyle \underline{r} \le 1$, 判别法失效，即级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$可能收敛，也可能发散。

---
设$\{x_n\}$是正项数列，则有：
<center>
   $
        \underline{\lim\limits_{n\to \infty}}\dfrac{x_{n+1}}{x_n} \le 
        \underline{\lim\limits_{n\to \infty}}\sqrt[n]{x_n} \le
        \overline{\lim\limits_{n \to \infty}}\sqrt[n]{x_n} 
        \le  \overline{\lim\limits_{n\to \infty}}\dfrac{x_{n+1}}{x_n}
   $
</center>
---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} nx^{n-1}(x>0)$ 的敛散性。
    
---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \frac{n!}{n^n}$ 的敛散性。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} x_n = \dfrac{1}{2} + \dfrac{1}{3} + 
    \dfrac{1}{2^2} + \dfrac{1}{3^2} + \dfrac{1}{2^3} + \dfrac{1}{3^3} 
    + \cdots $的敛散性。

---
设$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 为正项级数，且存在某正数$N_0$及常数$q (0 < q < 1).$ 

+  对于一切$n > N_0$，成立不等式
      $
          \sqrt[n]{u_n} \le q
      $
     则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 收敛。
+  对于一切$n > N_0$，成立不等式
      $
                \sqrt[n]{u_n} \ge 1
      $
      则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 发散。


---
设$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 为正项级数，且$\lim\limits_{n \to \infty} \sqrt[n]{u_n} = q$, 则

+ 当$q < 1$，则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 收敛。
+ 当$q > 1$，则级数$\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 发散。

---
**Cauchy判别法**

设$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$是正项级数, $\displaystyle r = \overline{\lim\limits_{n\to \infty}}\sqrt[n]{x_n}$,则，

+ 当$r<1$时，级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$收敛；
+ 当$r>1$时，级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$发散；
+ 当$r=1$时，级数$\displaystyle \sum\limits_{n=1}^{\infty}x_n(x_n \ne 0)$可能收敛，也可能发散。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \frac{2 + (-1)^n}{2^n}$ 的敛散性。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \frac{x^n}{1 + x^{2n}}$ 的敛散性。

---
**例子**
    讨论下列级数的敛散性$\displaystyle \sum\limits_{n=1}^{\infty} \frac{(n!)^2}{(2n)!}$ ,
    $\displaystyle \sum\limits_{n=1}^{\infty} \frac{n^2}{\left(2 + \frac{1}{n}\right)^n}$

---
**积分判别法**

---
设 $f$ 为 $[1, +\infty)$ 上非负递减函数，那么正向级数$\sum\limits_{n=1}^{\infty} f(n)$ 与反常积分 $\displaystyle \int_1^{+\infty} f(x)\,\mathrm{d}x$同时收敛或发散。

---
**例子**
    讨论级数$\displaystyle \sum\limits_{n=1}^{\infty} \frac{1}{x^p}$ 的敛散性。

---
**例子**
    讨论下列级数的敛散性$\displaystyle \sum\limits_{n=1}^{\infty} \frac{1}{n\left(\ln n\right)^n}$ ,
    $\displaystyle \sum\limits_{n=1}^{\infty} \frac{1}{n \ln n \left(\ln \ln n\right)^n}$

---
**Raabe判别法**

对于正项级数$\displaystyle \sum\limits_{n=1}^{\infty} x_n$，成立$\displaystyle \lim\limits_{n\to \infty} \dfrac{x_{n+1}}{x_n} = 1$,这时Cauchy判别法和d'Alembert判别法失效。

设$\displaystyle \sum\limits_{n=1}^{\infty} x_n$为正项级数， $\displaystyle \lim\limits_{n\to \infty}n\left(\dfrac{x_n}{x_{n+1}}-1\right) = r$，则

+ 当$r > 1$时，级数收敛；
+ 当$r < 1$时，级数发散。；

<details>
    设$\displaystyle s > t > 1, f(x) = 1 + sx - (1+x)^t$, 由于$\displaystyle f(0) = 0, f'(0) = s - t > 0$，可知存在$\delta > 0 $ 成立
$$
        1 + sx > (1 + x)^t
$$
当$r > 1$时，取$r > s > t > 1$,由于$\displaystyle \lim\limits_{n \to \infty}n \left(\dfrac{x_n}{x_{n+1}} - 1\right) = r$ , 对于充分大的$n$, 成立
$$
        \dfrac{x_n}{x_{n+1}} > 1 + \dfrac{s}{n} > 
          (1 + \dfrac{1}{n})^t = \dfrac{(n+1)^t}{n^t}
$$
这说明正项数列$\displaystyle \left\{n^t x_n\right\}$ 从某项开始单调减少，因而有上界。设
$$
        n^t x_n \le A
$$
与时有，
$$
        x_n \le \dfrac{A}{n^t}
$$
根据比较判别法，知级数收敛。

当$\displaystyle \lim\limits_{n\to \infty}n\left(\dfrac{x_n}{x_{n+1}}-1\right) = r < 1$，则对于充分大的n, 有
$$
        \dfrac{x_n}{x_{n+1}} < 1 + \dfrac{1}{n} = \dfrac{n+1}{n}
$$
这说明正项数列$\displaystyle\left\{nx_n\right\}$从某项开始单调增加，因而存在正整数$N$与实数$a>0$，使得
$$
        nx_n > a
$$
于是有，
$$
        x_n > \dfrac{a}{n}
$$
所以原级数发散。
</details>

---
**例子**

判别级数$\displaystyle 1 + \sum\limits_{n=1}^{\infty} \dfrac{(2n-1)!!}{(2n)!!}\cdot \dfrac{1}{2n+1}$的敛散性。






## 📚参考书目
📖1. 《高等数学》上下册（第七版），同济大学，高等教育出版社，2014.7.

📖2. 《解析几何》，邱维声，北京大学出版社，1988.

📖3. 《解析几何》，尤承业，北京大学出版社，2004.


## 教学日历:

  + [2019-2020-2高等数学A](http://wuguoning.github.io/files/calculus/docs/19-20-2-A-syllabus.pdf)
  + [2019-2020-2高等数学B](http://wuguoning.github.io/files/calculus/docs/19-20-2-B-syllabus.pdf)



# Calculus and its Visualization: an Introduction

<center>
<a href="https://www.geogebra.org/material/edit/id/yxadpqun#bookcontent">
   <img src="./imags/surface.png" width="200" height="200"/>
</a>
</center>


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
