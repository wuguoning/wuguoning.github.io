#  Derivative
## Differentiable Functions

**Definition 1.1**
    A function $$f: E \to \mathbb{R}$$ defined on a set $$E$$ is differentiable 
    at a point $$a \in E$$ that is a limit point of $$E$$, if there exists a 
    linear function $$A(x-a)$$  of the increment $$x-a$$ of the argument such 
    that $$f(x) - f(a)$$ can be represented as 
    \begin{equation}
        f(x) - f(a) = A(x-a) + \circ(x-a) \text{ as } x \to a, a \in E  {\tag 1}
        \label{eq:eq1}
    \end{equation}

In other words, a function is differentiable at a point $$a$$ if the change in 
its values in a neighborhood of the point in question is linear up to a 
correction that is infinitesimal compared with the magnitude of the displacement 
$$x - a$$ for the point $$a$$.

**Definition 1.2**
  The linear function $$A(x-a)$$ in \eqref{eq:eq1} is called the differential 
  of the function $$f$$ at $$a$$. The number $$A$$ is unambiguously determined 
  due to the uniqueness of the limit.

**Definition 1.3**
    The number 
    \begin{equation}
        f'(a) = \lim_{x \to a} \frac{f(x)-f(a)}{x-a} {\tag 2}
        \label{eq:eq2}
    \end{equation} is called the derivative of the function $$f$$ at $$a$$.

Relation \eqref{eq:eq2} can be rewritten in the equivalent form
\begin{equation}
    \frac{f(x) - f(a)}{x - a} = f'(a) + \alpha(x)
\end{equation}
where 
\begin{equation}
    \alpha(x) \to 0 \quad {\rm{as}}\quad x \to a, x \in E
\end{equation}
which is equivalent to 
\begin{equation}
    f(x) - f(a) = f'(a)(x-a) + o(x-a) {\quad\rm{as}\quad} x \to a, x \in E
\end{equation}

Graphically, this definition says that the derivative of $$f$$ at $$a$$ 
is the slope of the tangent line to $$y = f(x)$$ at $$a$$, which is the 
limit as $$x \to a$$ of the slopes of the lines through $$(x,f(x))$$ and 
$$(a,f(a))$$.

We can also write 
\begin{equation}
    f'(a) = \lim_{\Delta x \to 0} \frac{f(a+\Delta x) - f(a)}{\Delta x}
\end{equation}


**Definition 1.4**
A function $$f: E \to \mathbb{R}$$ defined on a set $$E \subset \mathbb{R}$$ 
is differentiable at a point $$x \in E$$ that is a limit point of $$E$$, if 
    \begin{equation}
        f(x+h) - f(x) = A(x)h + \alpha(x;h){\tag 3}
        \label{eq:eq3}
    \end{equation} 
where $$h \to A(x)h$$ is a linear function in $$h$$ and $$\alpha(x;h) = \circ(h)$$
as $$h \to 0, x+h \in E$$.

**Definition 1.5**
    The function $$h \to A(x)h$$ of Definition \eqref{eq:eq3} , 
    which is linear in $$h$$, is called the differential of the 
    function $$f: E \to \mathbb{R}$$ at the point $$x \in E$$ and is denoted 
    as $$df(x)$$ or $$Df(x)$$. Thus, $$df(x)(h) = A(x)h.$$

From definitions \eqref{eq:eq2} and \eqref{eq:eq3} we have
\begin{equation}
    \Delta f(x;h) - df(x)(h) = \alpha(x;h)
\end{equation}

---

## The Tangent line, Geometric Meaning of the Derivative and Differential
If we were seeking a polynomial 
\begin{equation}
    P_n(x) = c_0 + c_1(x - x_0) + \cdots + c_n(x - x_0)^n + o((x - x_0)^n)
\end{equation}
such that 
\begin{equation}
    f(x) = c_0 + c_1(x - x_0) + \cdots + c_n(x - x_0)^n + o((x - x_0)^n)
\end{equation}
as $$x \to x_0, x \in E$$

We could find successively,
$$ \begin{array}{c} \displaystyle c_0 = \lim_{x \to x_0} f(x) \newline  
\displaystyle c_1 = \lim_{x \to x_0} \frac{f(x) - c_0}{x - x_0} \newline
\vdots \newline
\displaystyle c_n = \lim_{x \to x_0} \frac{f(x) - [c_0 + c_1(x - x_0) + \cdots + c_n(x - x_0)^{n-1}] }{(x - x_0)^n}
\end{array} $$

**Proposition 1.1** 
A function $$f: E \to \mathbb{R}$$ that is continuous at a point $$x_0 \in E$$ 
that is a limit of $$E \subset \mathbb{R}$$ admits a linear approximation $$f(x) 
= c_0 + c_1(x - x_0) + o(x - x_0)$$ if and only if it is differentiable at the point.


**Definition 1.6** 
If a function $$f:E \to \mathbb{R}$$ is defined on a set $$E \subset \mathbb{R}$$ 
and differentiable at a point $$x \in E$$, the line defined by $$y - f'(x_0) = 
f'(x_0)(x - x_0)$$ is called the tangent to the graph of this function at the 
point $$(x_0, f(x_0))$$.

![](./Figs/tangent.png)
  
---
 
## Some Examples

**Example 1**
Let $$f(x) = \sin x$$. We shall show that $$f'(x) = \cos x$$.

**Example 2**
We shall show that $$\cos'(x) = - \sin x$$.

**Example 3**
If $$f(t) = r\sin \omega t$$, then $$f'(t) = r\omega \cos \omega t.$$
If $$f(t) = r\cos \omega t$$, then $$f'(t) = -r\omega \sin \omega t.$$

**Example 4**
The instantaneous velocity and instantaneous acceleration of a point mass. 
Suppose a point mass is moving in a plane and that in some given coordinate 
system its motion is described by differentiable function of time 
$$x = x(t), y=y(t)$$ In particular, this motion is written as in the form 
$$r(t) = \left(r\cos (\omega t + \alpha), r\sin (\omega t+ \alpha)\right)$$

**Example 5**
The optic property of a parabolic mirror. Let us consider the 
parabola $$y = \frac{1}{2p}x^2(p>0)$$, and construct the tangent to it at 
the point $$(x_0, y_0) = (x_0, \frac{1}{2p}x_0^2)$$.  

**Example 6**
$$f(x) = \left\{\begin{array}{cc} x^2\sin \frac{1}{x}, &\text{ if } x \ne 0 
\newline 0, &\text{ if } x = 0. \end{array} \right.$$
{% graph %}
{
    "title": "x*x * sin (1/x)",
    "grid": true,
    "xAxis": {
        "domain": [-0.1, 0.1]
    },
    "yAxis": {
        "domain": [-0.02, 0.02]
    },
    "data": [{
        "fn": "x*x * sin(1/x)",
        "closed": true
    }]
}
{% endgraph %}**Example 7**
We shall show that $$e^{x+h} - e^x = e^xh + \circ(h) \quad as \quad h \to 0$$.

**Example 8**
    If $$a > 0$$, then $$a^{x+h} - a^x = a^h(\ln a)h + \circ(h)$$ as $$h \to 0.$$


