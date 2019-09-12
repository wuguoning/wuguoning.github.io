---
title: "Real Analysis For Undergraduate"
collection: teaching
type: "Workshop"
permalink: /teaching/series
venue: "China University of Petroleum at Beijing, Science"
date: 2019-03-28
location: "City, Country"
---
**`These are lectures notes and tests for real analysis.`**

# series

## Basics
In this section we will introduce the topic of infinite series. Let's start with a sequence $\left\{a_n\right\}$ and define the following:
$$ 
\begin{aligned}
     & s_1 = a_1 \\
     & s_2 = a_1 + a_2\\
     & s_3 = a_1 + a_2 + a_3 \\
     & \vdots \\
     & s_n = a_1 + a_2 + \cdots + a_n = \sum\limits_{i=1}^{n}a_i
\end{aligned}
$$
The $s_n$ are called **partial sums**. Now let we take a look at the partial sums, $\left\{s_n\right\}$. 
$$
	\lim\limits_{n \to \infty} s_n = \lim\limits_{n \to \infty} \sum\limits_{i=1}^n a_i 
	= \sum\limits_{i=1}^{\infty} a_i 
	\tag{1}
$$
and we will call $\sum\limits_{i=1}^{\infty} a_i$ an **infinite series**.  It is important to note that $\sum\limits_{i=1}^{\infty} a_i$ is really nothing more than a conveniet notation for $\lim\limits_{n\to \infty}\sum\limits_{i=1}^n a_i$ so we do not need to keep writing the limit down. 

If the partial sums, $\left\{s_n\right\}$, is convergent and its limit is a finite number then we call the infinite series, $\sum\limits_{i=1}^{\infty} a_i$ **convergent**, otherwise, if the partial sums is divergent the the infinite series is also called **divergent**.




