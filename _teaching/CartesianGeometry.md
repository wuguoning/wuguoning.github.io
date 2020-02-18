---
title: "解析几何初步"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/CartesianGeometry
venue: "China University of Petroleum at Beijing, Department of Science"
date: 2020-02-02
location: "Beijing, CN"
---

这部分主要介绍笛卡尔解析几何。

## 教学日历:

  + [2019-2020-2高等数学A](http://wuguoning.github.io/files/calculus/docs/2019-2020-2-A-syllabus.docx)

  + [2019-2020-2高等数学B](http://wuguoning.github.io/files/calculus/docs/2019-2020-2-B-syllabus.pdf)

## 目录
+ [第一节 向量及其运算](#cotes1)
+ [第二节 数量积、向量积、混合积](#cotes2)
+ [第三节 空间平面](#cotes3)
+ [第四节 空间直线及其方程](#cotes4)
+ [第五节 旋转曲面、柱面和锥面](#cotes5)
+ [第六节 三元二次曲面](#cotes6)
+ [第七节 空间曲线](#cotes7)


<a name="cotes1"></a>
### 第一节 向量及其运算
---

📌**1. 向量和标量**

“速度”和“位移”是向量，“速率”和“长度”是标量。几何上向量是有大小和方向的有向线段。向量描述事物间的位移和相对位置，向量不包括“位置”的概念。“点”有位置，但没有大小和厚度。

向量的表示：$\bf{a, b, c,} \cdots $

或者: $\vec{a}, \vec{b}, \vec{c}, \cdots$

两个向量的夹角:  $<\widehat{\bf{a},\bf{b}}> = \phi$

---

📌**2. 向量的线性运算**

**向量的加法和减法**：

<center>
  <a href="https://www.geogebra.org/classic/rjccuqws">
  <img src="./imags/vector_add.png"  width="400" height="300" />
  </a>
</center>

向量的加法符合以下规律：

  + 交换律： $\bf{a + b = b + a} $;

  + 结合律：$\bf{(a + b) + c = a + (b + c)}$   

**数乘**

向量与数的乘积满足以下运算规律：

  + 结合律：$\lambda (\mu \bf{a}) = (\lambda \mu)\bf{a}$;

  + 分配律：$(\lambda + \mu)\bf{a} = \lambda \bf{a} + \mu \bf{a}$,  $\lambda (\bf{a + b}) = \lambda \bf{a} + \lambda \bf{b}$.


---

<span style="color:blue">
 **定理1**
设向量$\bf{a} \ne \bf{0}$，则向量$\bf{b}$平行于$\bf{a}$的充分必要条件为：$\bf{b} = \lambda \bf{a}$.
</span>

---

**📌3. 空间直角坐标系**

在空间取定一定点$O$和三个两两相互垂直的单位向量$\bf{i, j, k}$就确定了三条都以$O$为原点的两两相互垂直的数轴，依次记为$x$轴(横轴)，$y$轴(纵轴)，$z$轴(竖轴)，统称为<span style="color:red">**坐标轴**</span>。它们构成空间的一个<span style="color:red">**直角坐标系**</span>，如下图所示：

<center>
  <a href="https://www.geogebra.org/classic/pmheaygy">
    <img src="./imags/xyz_coordinate_system.png"  width="400" height="300" />
  </a>
</center>


三条坐标轴的任意两条可以确定一个平面，这样确定的三个坐标平面统称为<span style="color:red">**坐标平面**</span>。$x$轴及$y$轴所确定的坐标平面叫做<span style="color:red">$xOy$面</span>等等。坐标平面把空间分割为8个<span style="color:red">**卦限**</span>。如下图所示：

<center>
  <img src="./imags/eight_parts.png"  width="400" height="600" />
</center>


---

**📌4. 向量坐标表示**

$$M \leftrightarrow \bf{r} \leftrightarrow \vec{OM} = x\bf{i} + y\bf{j} + z\bf{k} \leftrightarrow (x, y, z) $$

例如向量：$\bf{r} = \vec{OM} = 3\bf{i} + 4\bf{j} + 5\bf{k}$

<center>
  <a href="https://www.geogebra.org/classic/umvuxkaj">
    <img src="./imags/vector_repr_xyz.png"  width="400" height="300" />
  </a>
</center>



$n$维空间向量的<span style="color:red">Enstein表示</span>为：
<center>
$M \leftrightarrow \bf{r} \leftrightarrow \vec{OM} = x^1\bf{e_1} + x^2\bf{e_2} + \cdots +  x^n\bf{e_n} \leftrightarrow (x^1, x^2, \cdots, x^n) = x^i \bf{e_i}$
</center>


---

**📌5. 利用坐标作向量的线形运算、向量的模、方向角、投影**

设向量$\bf{a} = a_x\bf{i} + a_y\bf{j} + a_z\bf{k}$, $\bf{b} = b_x\bf{i} + b_y\bf{j} + b_z\bf{k}$，则有：
  
  + $\bf{a} + \bf{b}= (a_x + b_x)\bf{i} + (a_y + b_y)\bf{j} + (a_z + b_z)\bf{k}$;
  
  + $\bf{a} - \bf{b}= (a_x - b_x)\bf{i} + (a_y - b_y)\bf{j} + (a_z - b_z)\bf{k}$;
  
  + $\lambda\bf{a} = (\lambda a_x )\bf{i} + (\lambda a_y )\bf{j} + (\lambda a_z )\bf{k}$;
  
  + $(a_x, a_y, a_z) + (b_x, b_y, b_z) = (a_x+b_x, a_y+b_y, a_z+b_z)$;

  + $(a_x, a_y, a_z) - (b_x, b_y, b_z) = (a_x-b_x, a_y-b_y, a_z-b_z)$;

  + $\lambda (a_x, a_y, a_z)  = (\lambda a_x, \lambda a_y, \lambda a_z)$



<center>
  <a href="https://www.geogebra.org/3d/vdheapjg">
    <img src="./imags/scalar_mult.png"  width="400" height="300" />
  </a>
</center> 



---
**例子**
已知两点$A(x_1, y_1, z_1), B(x_2, y_2, z_2)$以及$\lambda \ne -1$，在直线$AB$上求点$M$，使
$$\vec{AM} = \lambda \vec{MB}$$

<details>
<summary>⬇️ Click to expand!</summary>

解： $\vec{AM} = \vec{OM} - \vec{OA}$, $\vec{MB} = \vec{OB} - \vec{OM}$，所以有：

$$\vec{OM} - \vec{OA} = \lambda (\vec{OB} - \vec{OM})$$，

故

$$\vec{OM} = \dfrac{1}{1+\lambda}\left(\vec{OA} + \lambda \vec{OB}\right)$$

将坐标带入得到：

$$\vec{OM} = \left(\dfrac{x_1 + \lambda x_2}{1 + \lambda}, \dfrac{y_1 + \lambda y_2}{1 + \lambda}, \dfrac{z_1 + \lambda z_2}{1 + \lambda}\right)$$
</details>

---
**向量长度**

设向量$\bf{a} = (a_x, a_y, a_z)$，则向量的长度为：

$$\|\bf{a}\| = \sqrt{a_x^2 + a_y^2 + a_z^2}$$

---
**方向余弦**

$$\left(\cos \alpha, \cos \beta, \cos \gamma\right) = \left(\dfrac{a_x}{\|a\|}, \dfrac{a_y}{\|a\|}, \dfrac{a_z}{\|a\|}\right) = \dfrac{1}{\|a\|}\left(a_x, a_y, a_z\right)$$

$$\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = \dfrac{\|a\|^2}{\|a\|^2} = 1 $$

---
**方向角**

上式中的$\alpha, \beta, \gamma$称为向量$\bf{a}$的方向角。

---
**例子**
已知两点$M_1(2, 2, \sqrt{2}), M_2(1, 3, 0)$，计算向量$\vec{M_1 M_2}$的模、方向余弦和方向角。

<details>
<summary>⬇️ Click to expand!</summary>
解： 
$$\|\vec{M_1 M_2}\| = \|(-1, 1, -\sqrt{2})\| = 2$$

$$\left(\cos \alpha, \cos \beta, \cos \gamma\right) = \left(-\dfrac{1}{2}, \dfrac{1}{2}, -\dfrac{\sqrt{2}}{2}\right)$$

$$\alpha = \dfrac{2\pi}{3}, \beta = \dfrac{\pi}{3}, \gamma = \dfrac{3\pi}{4}$$

</details>

---
**投影**

<center>
  <a href="https://www.geogebra.org/graphing/zg5s38n4">
    <img src="./imags/vector_proj.png"  width="400" height="300" />
  </a>
</center> 

---
   + 同济大学高等数学书中的投影是一个标量，也就这上图中的分数$\dfrac{35}{49}$。其实，向量$Proj_{\vec{v}}\vec{u}$若看成一个向量更符合实际的几何意义。
 
   + 若按照同济大学教科书，投影的计算方法为：$$Proj_{\vec{v}}\vec{u} = \dfrac{\vec{u}\cdot \vec{v}}{\|\vec{v}\|}$$

---
📚<span style="color:red"> 
**第一次作业:**
</span>

1. 已知两点$M_1(0, 1, 2)$和$M_2(1, -1, 0)$，试用坐标表示向量$\vec{M_1M_2}, -2\vec{M_1M_2}$.

2. 求点$P(a, b, c)$关于(1)各坐标平面;(2)各坐标轴;(3)坐标原点的对称点的坐标。

3. 证明以三点$A(4, 1, 9), B(10, -1, 6), C(2, 4, 3)$为顶点的三角形是等腰直角三角形。

4. 设已知两点$M_1(4, \sqrt{2}, 1)$和$M_2(3, 0, 2)$，计算向量$\vec{M_1M_2}$的模、方向余弦和方向角。


---

<a name="cotes2"></a>
### 第二节 数量积、向量积、混合积
---
**📌 数量积**
由物理学知识知道：物体在常力$\bf{F}$的作用下产生了直线位移$\bf{S}$，则力所做的功为：

$$W = \|\bf{F}\|\|\bf{S}\|\cos <\widehat{\bf{F},\bf{S}}>$$

受此启发，我们定义向量 $\bf{a}$ 和 $\bf{b}$ 的数量积(内积, scalar product)为: 
<center>
$\|\bf{a}\|\|\bf{b}\|\cos <\widehat{\bf{a},\bf{b}}>$
</center>

记为：

$$\bf{a} \cdot \bf{b} = \|\bf{a}\|\|\bf{b}\|\cos <\widehat{\bf{a},\bf{b}}>$$

**由定义可以推出数量积具有以下性质**：

  + $\bf{a} \cdot \bf{a} = \|a\|^2$;

  + $\bf{a} \cdot \bf{b} = \bf{b} \cdot \bf{a} $;

  + $(\bf{a} + \bf{b} ) \cdot \bf{c} = \bf{a} \cdot \bf{c} + \bf{b} \cdot \bf{c} $;

  + $(\lambda\bf{a}) \cdot \bf{b} = \lambda (\bf{a} \cdot \bf{b} )$.

**数量积在坐标下的计算方法**

设$\bf{a} = (a_x, a_y, a_z), \bf{b} = (b_x, b_y, b_z)$，则有：
$$\bf{a} \cdot \bf{b} = (a_x \bf{i} + a_y \bf{j} + a_z \bf{k}) \cdot (b_x \bf{i} + b_y \bf{j} + b_z \bf{k})$$

<details>
<summary>⬇️ Click to expand!</summary>
$
\begin{split} & = a_xb_x\bf{i}\cdot\bf{i} + a_xb_y\bf{i}\cdot\bf{j} + a_xb_z\bf{i}\cdot\bf{k} \newline
               & +  a_yb_x\bf{j}\cdot\bf{i} + a_yb_y\bf{j}\cdot\bf{j} + a_yb_z\bf{j}\cdot\bf{k} \newline
               & + a_zb_x\bf{k}\cdot\bf{i} + a_zb_y\bf{k}\cdot\bf{j} + a_zb_z\bf{k}\cdot\bf{k}
\end{split}
$
</details>
<center>
$=(a_xb_x + a_yb_y + a_zb_z)$
</center>

下图展示了向量的数量积概念。

<center>
  <a href="https://www.geogebra.org/graphing/ux9zuwtd">
    <img src="./imags/vector_scalar_prod.png"  width="500" height="400" />
  </a>
</center> 



---
**例子**
已知三点$M(1,1,1), A(2,2,1), B(2,1,2)$，求$\angle{AMB}$

<details>
<summary>Click to expand!</summary>

$\cos \angle{AMB} = \dfrac{\vec{MA} \cdot \vec{MB}}{\|\vec{MA}\|\|\vec{MB}\|} = \dfrac{1}{\sqrt{2}\sqrt{2}} = \dfrac{1}{2}$

所以有，
$$\angle{AMB} = \dfrac{\pi}{3}$$
</details>

---

**📌2. 两个向量的向量积**

 > “Give me a fulcrum, and I shall move the world!”

 > "给我一个支点我将反转地球！"-阿基米德。

设$\bf{O}$为一根杠杆的支点。有一个力$\bf{F}$作用在这根杠杆的$P$点处夹角为$\theta$，由力学规定，力$\bf{F}$对支点$\bf{O}$的力矩是一个向量$\bf{M}$，该向量的长度为：
<center>
$\|\bf{M}\| = \|\vec{OP}\|\|\bf{F}\|\sin <\widehat{\vec{OP}, \bf{F}}> $
</center>

$\bf{M}$所在的方向垂直于$\vec{OP}$和$\bf{F}$所决定的平面，它的方向为按照右手规则从$\vec{OP}$以不超过$\pi$的角度转向$\bf{F}$来确定。受此启发我们定义两个向量的向量积如下：

设$\bf{a}, \bf{b}$为两个向量，向量$\bf{a, b}$的<span style="color:red">**向量积**</span>(**一个新的向量**)$\bf{a}\times\bf{b}$(cross product)定义为：

  + 大小: $\|\bf{a} \times \bf{b}\| = \|a\|\|b\|\sin <\widehat{\bf{a}, \bf{b}}>$;

  + 方向：垂直于向量$\bf{a, b}$所在的平面，方向为按右手法则从向量$\bf{a}$以不超过$\pi$的角转向向量$\bf{b}$.

下图直观展示了向量$\bf{a}\times\bf{b}$：

<center>
<img src="./imags/right_hand_rule.png"  width="200" height="140" />
<img src="./imags/right_hand_rule1.png"  width="200" height="140" />
</center> 


**向量积性质**

  + $\bf{a} \times \bf{a} = \bf{0}$;

  + $\bf{a} \times \bf{b} = -\bf{b} \times \bf{a}$;

  + $(\bf{a} + \bf{b}) \times \bf{c} = \bf{a} \times \bf{c} + \bf{b} \times \bf{c}$;

  + $ (\lambda \bf{a}) \times \bf{b} = \bf{a} \times (\lambda \bf{b})$.

**向量积在坐标下的计算方法**


设$\bf{a} = (a_x, a_y, a_z), \bf{b} = (b_x, b_y, b_z)$，则有：
$$\bf{a} \times \bf{b} = (a_x \bf{i} + a_y \bf{j} + a_z \bf{k}) \times (b_x \bf{i} + b_y \bf{j} + b_z \bf{k})$$

<details>
<summary>⬇️ Click to expand!</summary>
$\begin{split}
  = & a_xb_x\bf{i}\times\bf{i} + a_xb_y\bf{i}\times\bf{j} + a_xb_z\bf{i}\times\bf{k}\newline
    & +  a_yb_x\bf{j}\times\bf{i} + a_yb_y\bf{j}\times\bf{j} + a_yb_z\bf{j}\times\bf{k} \newline
    & + a_zb_x\bf{k}\times\bf{i} + a_zb_y\bf{k}\times\bf{j} + a_zb_z\bf{k}\times\bf{k}  \newline
    & \left(\bf{i}\times\bf{i} = \bf{j}\times\bf{j} = \bf{k}\times\bf{k} = \bf{0}\right)\newline
    & \left(\bf{i}\times\bf{j} = \bf{k}, \bf{j}\times\bf{k} = \bf{i}, \bf{k}\times\bf{i} = \bf{j}\right),\newline
    & \left(\bf{i}\times\bf{k} = -\bf{j},\bf{j}\times\bf{i} = -\bf{k},\bf{k}\times\bf{j} = -\bf{i}\right)
 \end{split}
$
</details>

$ = (a_yb_z - a_zb_y) \bf{i} + (a_zb_x - a_xb_z) \bf{j} + (a_xb_y-a_yb_x)\bf{k}$

写成代数中行列式的方式为：

<center>
$
\bf{a}\times\bf{b} = 
\left|\begin{array}{ccc}
i & j & k \newline
a_x & a_y & a_z \newline
b_x & b_y & b_z
\end{array}\right|
$
</center>

<center>
  <a href="https://www.geogebra.org/3d/kvtmmqex">
    <img src="./imags/cross_prod.png"  width="500" height="400" />
  </a>
</center> 


---
**例子**
已知三角形的顶点分别是$A(1,2,3), B(3,4,5), C(2,4,7)$求三角形$ABC$的面积。

<details>
<summary>⬇️ Click to expand!</summary>
解：三角形的面积为$\dfrac{1}{2}\|\vec{AB} \times \vec{AC}\|$

</details>

---
**📌3.三个向量的混合积**
已知三个向量$\bf{a, b, c}$，先作两个向量$\bf{a}$和向量$\bf{b}$的向量积$\bf{a} \times \bf{b}$，再把得到的向量与第三个向量$\bf{c}$作数量积$(\bf{a} \times \bf{b}) \cdot \bf{c}$，这样得到的数称为向量$\bf{a, b, c}$的混合积。记作$[\bf{abc}]$。

**性质**

  +  $\bf{[abc]} = \bf{[bca]} = \bf{[cab]}$

**坐标下的计算方法**

<center>
$\bf{[abc]}  = \left|\begin{array}{ccc}
a_x & a_y & a_z \newline
b_x & b_y & b_z \newline
c_x & c_y & c_z
\end{array}\right|$
</center>

<center>
  <a href="https://www.geogebra.org/3d/kegrnjnc">
    <img src="./imags/scalar_trip_prod.png"  width="400" height="400" />
  </a>
</center> 

---
**例子**
已知不在平面上的四点：$A_i(x_i, y_i, z_i), i=1,2,3,4$，求四面体$A_1A_2A_3A_4$的体积。

<details>
<summary>⬇️ Click to expand!</summary>

解：四面体的体积为$\bf{V} = \dfrac{1}{6}\left|\left[\vec{A_1A_2} \vec{A_1A_3} \vec{A_1A_4}\right]\right| = \pm \dfrac{1}{6} \left|\begin{array}{ccc} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \newline x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \newline x_4 - x_1 & y_4 - y_1 & z_4 - z_1 \end{array} \right| $

</details>

 
---
<span style="color:red"> 
📚**第二次作业:**
</span>

1. 设向量$\bf{a} = (3, -1, -2), \bf{b} = (1, 2, -1)$，求

  - $\bf{a} \cdot \bf{b}$;

  - $(-2\bf{a}) \cdot 3\bf{b}$;

  - $\bf{a} \times 2\bf{b}$;

  - $\bf{a, b}$夹角的余弦。

2. 已知$M_1(1, -1, 2), M_2(3, 3, 1), M_3(3, 1, 3)$，求与$\vec{M_1M_2}, \vec{M_2M_3}$同时垂直的单位向量。

3. 求向量$\bf{a} = (4, -3, 4)$在向量$\bf{b} = (2, 2, 1)$上的投影。

4. 已知向量$\bf{a} = (2, -3, 1), \bf{b} = (1, -1, 3), \bf{c}=(1, -2, 0)$，求

  - $\bf{(a \cdot b)c - (a \cdot c)b}$;

  - $\bf{(a + b)\times (b + c)}$;

  - $\bf{(a \times b) \cdot c}$.

---

<a name="cotes3"></a>
### 第三节 空间平面

---
**1. 平面方程**

**📌点法式**

如果一个向量和平面垂直，我们称该向量为平面的一个法向量。如果已知平面上的一个点$M_0(x_0, y_0, z_0)$和任意一个法向量$\bf{n} = (A, B, C)$(法向量不唯一)我们可以建立该平面的方程。

假设$M(x, y, z)$为平面上的任意一点，则有$\bf{n} \cdot \bf{\vec{M_0 M}} = 0$，即

$$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$$

下图为点法式建立平面示意图

<center>
  <a href="https://www.geogebra.org/3d/wx2brsg7">
    <img src="./imags/plane_equa.png"  width="400" height="300" />
  </a>
</center> 


---
**例子**
求过三点$M_i(x_i, y_i, z_i), i=1, 2, 3$的平面方程。

<details>
<summary>⬇️ Click to expand!</summary>
解：法向量为
$\bf{n} = \left|\begin{array}{ccc} 
          \bf{i} & \bf{j} & \bf{j} \newline
          x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \newline
          x_3 - x_1 & y_3 - y_1 & z_3 - z_1
          \end{array}\right|
$

由点法式得到平面方程$\Pi$为：
$$
  \bf{n} \cdot \vec{M_0M} = 
  \left|\begin{array}{ccc}
          x - x_1 & y - y_1 & z - z_1 \newline
          x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \newline
          x_3 - x_1 & y_3 - y_1 & z_3 - z_1
        \end{array}
  \right| = 0
$$

</details>

---

**📌一般式**

因为平面方程为一个<span style="color:red">**三元一次方程**</span>，反过来，设有一个三元一次方程：

$$Ax + By + Cz + D = 0$$

我们任取满足方程的一个点$(x_0, y_0, z_0)$: 

$$Ax_0 + By_0 + Cz_0 + D = 0$$

两个式子相减得到：

$$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$$

这说明任意一个三元一次方程代表空间的一张平面。

🛠 **思考以下平面的特点**

  * $D = 0, Ax + By + Cz = 0$;
  
  * $A = 0, By + Cz + D = 0$;

  * $B = 0, Ax + Cz + D = 0$;

  * $A = D = 0, By + Cz = 0$;

  * $A = B = D = 0, Cz = 0$

🍺[Hands on](https://www.geogebra.org/m/bFuCp5Ys)

---
**例子**
设一平面与$x, y, z$轴的交点依次为$P(a, 0, 0), Q(0, b, 0), R(0, 0, c)$三点$(abc \ne 0)$。求此平面方程。

<details>
<summary>⬇️ Click to expand!</summary>
解： 设所求平面方程为:$Ax + By + Cz + D = 0$，则有：
$aA + D = 0,  bB + D = 0, cC + D = 0$
解之得，

$$\dfrac{x}{a} + \dfrac{y}{b} + \dfrac{z}{c} = 1$$.

</details>

---

**📌参数式**

设平面$\Pi$过$M_0(x_0, y_0, z_0)$点，平行于两个不共线的两个向量$\bf{u_1}(X_1, Y_1, Z_1), \bf{u_2}(X_2, Y_2, Z_2)$，于是$M(x, y, z)$在该平面上的的充分必要条件为向量$\vec{M_0M}, \bf{u_1, u_2}$共面。由于$\bf{u_1, u_2}$不共线，所以存在实数$s, t$使得：

$$\vec{M_0M} = s\bf{u_1} + t\bf{u_2}$$

上述方程写成分量的形式为：

$$
\left\{\begin{array}{c} 
x - x_0 = sX_1 + tX_2 \newline 
y - y_0 = sY_1 + tY_2 \newline
z - z_0 = sZ_1 + tZ_2 
\end{array}\right.
(s, t) \in \mathcal{R}
$$

即，

$$
\left\{\begin{array}{c} 
x = x_0 + sX_1 + tX_2 \newline 
y = y_0 + sY_1 + tY_2 \newline
z = z_0 + sZ_1 + tZ_2 
\end{array}\right.
(s, t) \in \mathcal{R}
$$

另外，常用的是一般式程，其表达式为：

<center>
$
\left|\begin{array}{ccc}
x - x_0 & y - y_0 & z - z_0 \newline
X_1 & Y_1 & Z_1 \newline
X_2 & Y_2 & Z_2 
\end{array}\right| = 0
$
</center>



---
**📌两平面的位置关系**

<span style="color:blue">两张平面的位置关系有：相交、平行两种情况。判断方法为:</span>

在直角坐标系中，两张平面：
$\Pi_i: A_ix + B_iy + C_iz + D_i = 0, i=1,2$

  + $\Pi_1$平行于$\Pi_2$的充分必要条件为：$\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2}$;

  + $\Pi_1$等于$\Pi_2$的充分必要条件为：$\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2} = \dfrac{D_1}{D_2}$.

在直角坐标系中，三张平面：
$\Pi_i: A_ix + B_iy + C_iz + D_i = 0, i=1,2,3$
相交于一点的充分必要条件为：
<center>
$
\left|\begin{array}{ccc}
A_1 & B_1 & C_1 \newline
A_2 & B_2 & C_2 \newline
A_3 & B_3 & C_3 
\end{array}\right|\ne 0
$</center>


---
**📌两平面的夹角**


<center>
<a href="https://www.geogebra.org/3d/qpnanhce">
<img src="./imags/angle_2planes.png"  width="500" height="300" />
</a>
</center> 


两平面法向量的夹角(通常指锐角或直角)称为两平面的夹角。
在直角坐标系中，两张平面：

$$\Pi_i: A_ix + B_iy + C_iz + D_i = 0, i=1,2$$

则夹角的余弦为，

$$\cos \theta = \dfrac{\left|A_1A_2 + B_1B_2 + C_1C_2\right|}{\sqrt{A_1^2 + B_1^2 + C_1^2}\sqrt{A_2^2 + B_2^2 + C_2^2}}$$

---
**例子**
求两张平面$x-y+2z-6=0$和$2x+y+z-5=0$的夹角。
<details>
<summary>⬇️ Click to expand!</summary>
解：

$\cos \theta = \dfrac{|1 \times 2 + (-1) \times 1 + 2 \times 1 }{\sqrt{1^2 + (-1)^2 + 2^2}\sqrt{2^2 + 1^2 + 1^2}} = \dfrac{1}{2}$

所以$\theta = \dfrac{\pi}{3}$
</details>


---
**📌点到平面的距离**

设空间一平面$\Pi: Ax + By + Cz + D = 0$其法向量为$\bf{n} = (A, B, C)$，另设$Q(x, y, z)$为平面外一点，点$Q$到平面$\Pi$的距离为：

在平面$\Pi$上任取一点$P(x_0, y_0, z_0)$，距离为：

$$
d = \dfrac{|\vec{PQ} \cdot \bf{n}|}{\|\bf{n}\|} = 
  = \dfrac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}
$$

见下图：

<center>
  <a href="https://www.geogebra.org/3d/vnazjmse">
    <img src="./imags/point_2plane_dist.png"  width="500" height="400" />
  </a>
</center> 


---
**例子**
求点$(1, 2, 1)$到平面$x + 2y + 2z - 10 = 0$的距离。
<details>
<summary>⬇️ Click to expand!</summary>
解：在平面上任取一点$P(0, 0, 5)$,法向量$\bf{n} = (1, 2, 2)$,

<center>
$
d = \dfrac{|\vec{PQ} \cdot \bf{n}|}{\|\bf{n}\|} = 
  = \dfrac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}
$
$
  = \dfrac{|1 \times 1 + 2 \times 2 + 2 \times 1  - 10|}{\sqrt{1^2 + 2^2 + 2^2}}
  = \dfrac{3}{3} = 1.
$

</center>
</details>


---

📚<span style="color:red"> 
**第三次作业:**
</span>

1. 求过点$(3, 0, -1)$且与平面$3x - 7y + 5z -12 = 0$平行的平面方程。

2. 求过三点$M_1(2, 9, -6), M_2(-2, -2, 2), M_3(1, -1, 2)$的平面方程。

3. 求平面$2x - 2y + z + 5 = 0$与各坐标平面的夹角。

4. 求三平面$x + 3y + z = 1, 2x - y - z = 0, -x + 2y + 2z = 3$的交点。


---

<a name="cotes4"></a>
### 第四节 空间直线及其方程

---
**📌空间直线方程**

设直线$l$经过$M_0(x_0, y_0, z_0)$，平行于非零向量(方向向量)($\bf{u} = (X, Y, Z)$)，则$M(x,y,z)\in l$的充分必要条件为：

<center>
$\vec{M_0M} \parallel \bf{u}$
</center>

写成坐标的形式，得到了<span style="color:red">**直线的标准方程**:</span>

$$\dfrac{x - x_0}{X} = \dfrac{y - y_0}{Y} = \dfrac{z - z_0}{Z}$$

又因为$\bf{u} \ne \bf{0}$，所以$\vec{M_0M} \parallel \bf{u}$的充分且必要条件是：存在实数$\lambda$使得

<center>
$\vec{M_0M} = \lambda \bf{u}$
</center>
用坐标写出，即得到了<span style="color:red">**直线的参数方程**:</span>

$$
\left\{\begin{array}{c} x = x_0 + \lambda X \newline 
                        y = y_0 + \lambda Y \newline
                        z = z_0 + \lambda Z
       \end{array}\right.
$$

直线的这两种方程虽然在形式上不同，但它们的直接表现处出直线的几何意义，即它的方向和所经过的点。我们把这两种方法统称为<span style="color:red">**直线的点向式方程**。</span>

<center>
  <a href="https://www.geogebra.org/3d/kfcyckrg">
    <img src="./imags/point_vector_line.png"  width="500" height="400" />
  </a>
</center> 

确定直线的另外一种方法是把它作为两张平面的交线，即三元一次方程组：

$$
\left\{\begin{array}{c} A_1x + B_1y + C_1z + D_1 = 0 \newline
                        A_2x + B_2y + C_2z + D_2 = 0
       \end{array}\right.
$$

以上方程为直线的<span style="color:red">**一般方程**</span>.

---
**例子**
给定平面$\Pi: 3x - y + 2z - 1 = 0$，直线$l: \dfrac{x-1}{4} = \dfrac{y-3}{-2} = \dfrac{z}{1}$和点$M_0(0, 0, -2)$。写出过$M_0$点平行于平面$\Pi$且和直线$l$相交的直线方程。

<details>
<summary>⬇️ Click to expand! </summary>
解：设所求直线的方程为$l_1$，设$\Pi_1$过$M_0$且平行于平面$\Pi$，$\Pi_2$过$M_0$和直线$l$，则他们都通过$l_1$.

因为$\Pi_1$平行于平面$\Pi$，故可设其方程为：$3x - y + 2z + d = 0$，再将$M_0$的坐标带代入得到$d = 4$，得到平面$\Pi_1$的方程为：$3x - y + 2z + 4 = 0$
$\Pi_2$经过$M_0$和$M_1(1, 3, 0)$，平行于向量$\bf{u} = (4, -2, 1)$，也就是由点$M_0$和向量$\vec{M_0M}(1, 3, 2)$和$\bf{u}$所决定的平面，得到$\Pi_2$的一般方程为：$x + y - 2z - 4 = 0$
于是所求直线方程为

$
\left\{\begin{array}{c} x + y -2z - 4 = 0 \newline
                        3x - y + 2z + 4 = 0
       \end{array}\right.
$

</details>

---
**例子**
设直线的一般方程为:
<center>
$\left\{\begin{array}{c} 2x + y -2z + 1 = 0 \newline 4x - 2y + 2z - 1 = 0 \end{array}\right.$
</center>


求它的参数方程。
<details>
<summary>⬇️ Click to expand!</summary>
直线的方向向量为：

$
 \left|\begin{array}{cc} 1 & -2 \newline -2 & 2 \end{array}\right|, \left|\begin{array}{cc} -2 & 2 \newline 2 & 4 \end{array}\right|, \left|\begin{array}{cc} 2 & 1 \newline 4 & -2 \end{array}\right|
$

$
 = (-2, -12, 8)
$
在直线上找一点$(0, 0, 0.5)$，所以直线的参数方程为：

$
 \left\{\begin{array}{c} x = \lambda \newline y = 6\lambda \newline z = 0.5 + 4\lambda \end{array}\right.
$
</details>

---

**📌空间直线与平面**

直线与平面的位置关系有：
  + 相交(只有一个交点);

  + 直线在平面上;

  + 以及没有交点.

三种情况，后两种统称为平行。

设平面$\Pi$的方程为$Ax + By + Cz + D = 0$。直线$l$过点$M_0(x_0, y_0, z_0)$，平行于非零向量$\bf{u}(X, Y, Z)$。则$l$平行于$\Pi$;$l$在$\Pi$上的条件为：

$$
l \parallel \Pi \iff AX + BY + CZ = 0
$$


$$
l \in \Pi \iff \left\{\begin{array}{c}AX + BY + CZ = 0 \newline Ax_0 + By_0 + Cz_0 + D =0 \end{array}\right.
$$


设直线$l$的一般方程为:

<center>
$
\left\{\begin{array}{c} A_1x + B_1y + C_1z + D_1 = 0 \newline A_2x + B_2y + C_2z + D_2 =0 \end{array}\right.
$
</center>

设平面$\Pi$的方程为：
<center>
$ Ax + By + Cz + D = 0$
</center>
则有下述结果：

---
<span style="color:red">**命题**</span>

  1. 直线$l$和平面$\Pi$相交的充分必要条件为：<center> $\left|\begin{array}{ccc} A_1 & B_1 & C_1 \newline A_2 & B_2 & C_2 \newline A & B & C \end{array}\right| \ne 0$ </center>

  2. 直线$l$和平面$\Pi$无交点的充分必要条件为：线形方程组<center>$\left\{\begin{array}{l} A_1x + B_1y + C_1z + D_1 = 0 \newline A_2x + B_2y + C_2z + D_2 = 0 \newline Ax + By + Cz + D = 0 \end{array}\right.$ </center>无解。

  3. 直线$l$在平面$\Pi$上的充分必要条件为：线形方程组<center>$\left\{\begin{array}{l} A_1x + B_1y + C_1z + D_1 = 0 \newline A_2x + B_2y + C_2z + D_2 = 0 \newline Ax + By + Cz + D = 0\end{array}\right.$</center>有无穷多解。

我们把经过同一条直线的所有平面构成的集合称为以$l$为轴的<span style="color:red">**共轴平面系**</span>。如果$l$的一般方程为

<center>
$
\left\{\begin{array}{l} A_1x + B_1y + C_1z + D_1 = 0 \newline A_2x + B_2y + C_2z + D_2 =0 \end{array}\right.
$
</center>

则以$l$为轴的共轴平面系中平面方程的一般形式为：


<center>
$
\lambda(A_1x + B_1y + C_1z + D_1) + \mu(A_2x + B_2y + C_2z + D_2) = 0
$
</center>

其中$\lambda^2 + \mu^2 \ne 0$.

---
**例子**
已知$l$在$\Pi$上，其中$l$的一般方程为：
<center>
$
\left\{\begin{array}{l} 3x + 2y - z + 1 = 0 \newline x - 2z = 0 \end{array}\right.
$</center>
平面$\Pi$的方程为$4x + ay + 2z + b = 0$，求$a, b$.

<details>
<summary>⬇️ Click to expand!</summary>
设$4x + ay + 2z + b = \lambda(3x + 2y - z + 1) + \mu(x - 2z)$，解之得，$\lambda = 2, \mu = -2$从而有$a = 4, b = 2$.
</details>

---

**📌空间直线与直线位置关系**

空间直线与直线的位置关系有异面、相交、重合、平行而不重合四种情况。设直线$l_i$的方向向量为$\bf{u_i}$且分别通过$M_i$点$i=1,2$，则有：

---
<span style="color:blue">
**命题**
</span>
  1. $l_1 \parallel l_2 \iff \bf{u_1} \parallel \bf{u_2}$;

  2. $l_1, l_2$共面$\iff$ $[\vec{M_1M_2 \bf{u_1} \bf{u_2}}] = 0$(混合积为零);

  3. $l_1, l_2$重合 $\iff$ $\vec{M_1M_2}, \bf{u_1}, \bf{u_2}$共线。

🛠**上述命题的分量表达式应该为什么？**

---

**📌空间直线与直线的夹角**

两直线方向向量的夹角(通常知锐角或直角)叫做两直线的夹角。设直线$l_i$的方向向量为$\bf{u_i} = (X_i, Y_i, Z_i), i=1,2$，则两直线夹角$\phi$的余弦为：

$$
\cos \phi = \dfrac{|X_1X_2 + Y_1Y_2 + Z_1Z_2|}{\sqrt{X_1^2 + Y_1^2 + Z_1^2}\sqrt{X_2^2 + Y_2^2 + Z_2^2}}
$$

<center>
  <a href="https://www.geogebra.org/3d/fjrx7vcj">
    <img src="./imags/angle_2lines.png"  width="500" height="400" />
  </a>
</center> 



---

**📌空间直线与平面的夹角**

直线与平面的夹角，即直线与它在平面上正射影的夹角。设直线$l$平行于非零向量$\bf{u}(X, Y, Z)$，平面$\Pi$的法向量为$\bf{n}(A, B, C)$，则它们的夹角为：

$$
\theta = arccos(|\sin <\widehat{\bf{u}, \bf{n}}>|)
$$

$$
\sin \theta = \dfrac{|AX + BY + CZ|}{\sqrt{A^2 + B^2 + C^2}\sqrt{X^2 + Y^2 + Z^2}}
$$

<center>
  <a href="https://www.geogebra.org/3d/bnxrq9ad">
    <img src="./imags/angle_line_plane.png"  width="700" height="300" />
  </a>
</center> 




---

**📌空间点到直线的距离**

设直线$l$经过点$M_0(x_0, y_0, z_0)$，平行于非零向量$\bf{u}(X, Y, Z)$
，则点$P(x, y, z)$到$l$的距离为：

$$
d = \dfrac{|\bf{u} \times \vec{M_0P}|}{|\bf{u}|}
$$

<center>
  <a href="https://www.geogebra.org/m/qcNwb4bk">
    <img src="./imags/dist_point_line.png" width="200" height="200"/>
  </a>
</center>


---
📚<span style="color:red"> 
**第四次作业:**
</span>

+ 求过点$(4, -1, 3)$且平行于直线$\dfrac{x - 3}{2} = \dfrac{y}{1} = \dfrac{z - 1}{5}$ 的直线方程。


+ 用对称式及参数方程表示直线
  <center>
  $\left\{\begin{array}{l} x - y + z = 1 \newline 2x + y + z = 4 \end{array}\right.$
  </center>

+ 求直线
  <center>
  $\left\{\begin{array}{l} 5x - 3y + 3z -9 = 0 \newline 3x - 2y + z -1 = 0 \end{array}\right.$ 
  </center>
  与直线
  <center>
  $\left\{\begin{array} 2x + 2y - z + 23= 0 \newline 3x + 8y + z -18 = 0 \end{array}\right.$ 
  </center>
  的夹角。


+ 求直线
  <center>
  $\left\{\begin{array}{l} 2x - 4y + z = 0 \newline 3x - y - 2z - 9 = 0 \end{array}\right.$
  </center>
  在平面$4x - y + z = 1$投影直线的方程。

---

<a name="cotes5"></a>
### 第五节 旋转曲面、柱面和锥面

---

**📌旋转曲面**

一条曲线$\Gamma$绕一条直线$l$旋转所得的曲面称为<span style="color:red">**旋转曲面**</span>。$l$称为<span style="color:red">**轴**</span>，$\Gamma$称为<span style="color:red">**母线**</span>。

母线$\Gamma$上每个点$M_0$绕$l$旋转得到的圆，称为<span style="color:red">**纬圆**</span>，纬圆与轴线垂直。过$l$的半平面与旋转曲面的交线称为<span style="color:red">**经线**</span>。经线可以作为母线，但母线不一定是经线。

<center>
  <a href="https://www.geogebra.org/3d/gpyagmtp">
  <img src="./imags/rotational_surf.png" width="500" height="300"/>
  </a>
</center>

现在假设旋转轴为$z$轴，母线$\Gamma$在$yoz$平面上，其方程为：

<center>
$\left\{\begin{array}{l} f(y,z) = 0 \newline x = 0 \end{array}\right.$
</center>

则点$M(x, y, z)$在旋转曲面上的充分条件为:

<center>
$\left\{\begin{array}{l} f(y_0,z_0) = 0 \newline x_0 = 0 \newline x^2 + y^2 = x_0^2 + y_0^2 \newline 1 \cdot (z - z_0) = 0 \end{array}\right.$
</center>

这里$M_0(x_0, y_0, z_0)$为过$M$的纬圆在母线上的对应点。

消去$x_0, y_0, z_0$得到

$$f(\pm\sqrt{x^2 + y^2}, z) = 0$$


---
📝<span style="color:red">**小结**</span>

为了得到$yOz$平面上的曲线$\Gamma$绕$z$轴旋转所得到的旋转曲线，只要将母线$\Gamma$在$yOz$平面上的方程中$y$改成$\pm\sqrt{x^2 + y^2}$，$z$不动。坐标平面上的曲线绕坐标轴旋转所得到的旋转曲面的方程都有类似的规律。

---
**例子**
母线$\Gamma$为
<center>
$\left\{\begin{array}{l} y^2 = 2pz \newline x = 0 \end{array}\right.$
</center>
绕$z$轴旋转所得到的旋转曲面方程为：
<center>
$x^2 + y^2 = 2pz$.
</center>

<center>
  <a href="https://www.geogebra.org/classic/tjcyukcx">
    <img src="./imags/rotational_parabo.png" width="400" height="300"/>
  </a>
</center>


---
**例子**
母线$\Gamma$为
<center>
$\left\{\begin{array}{l} \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1 \newline z = 0 \end{array}\right.$
</center>
绕$x$轴旋转所得到的旋转曲面方程为(双叶双曲面)：
<center>
$\dfrac{x^2}{a^2} - \dfrac{y^2 + z^2}{b^2} = 1$.
</center>

<center>
  <a href="https://www.geogebra.org/classic/tdmrwwy5">
    <img src="./imags/para_2sheets.png" width="500" height="300"/>
  </a>
</center>


绕$y$轴旋转所得到的旋转曲面方程为(单叶双曲面)：
<center>
$\dfrac{x^2 + z^2}{a^2} - \dfrac{y^2}{b^2} = 1$.
</center>

<center>
  <a href="https://www.geogebra.org/3d/ewgcjsee">
    <img src="./imags/para_1sheet.png" width="300" height="500"/>
  </a>
</center>


---
**例子**
母线$\Gamma$为
<center>
$\left\{\begin{array}{l} 4x^2 + 9y^2 = 36 \newline z = 0 \end{array}\right.$
</center>
绕$x$轴旋转所得到的旋转曲面方程为：
<center>
$4x^2 + 9(y^2 + z^2) = 36$.
</center>

<center>
  <a href="https://www.geogebra.org/3d/y22upztm">
    <img src="./imags/rotational_ellip.png" width="600" height="300"/>
  </a>
</center>


---

**📌柱面**

若一条直线$l$沿着一条空间曲线$C$平行移动时所形成的曲面称为<span style="color:red">**柱面**</span>。$l$称为<span style="color:red">**母线**</span>，$C$称为<span style="color:red">**准线**</span>。

<center>
<a href="https://www.geogebra.org/m/AWr5ag7a">
<img src="./imags/cylinder.png" width="400" height="300"/>
</a>
</center>

**柱面方程的建立**

设柱面的母线方向为$\bf{v}(l, m, n)$，准线$C$的方程为
<center>
$\left\{\begin{array}{l} F(x, y, z) = 0 \newline G(x, y, z) = 0 \end{array}\right.$
</center>

假设$M(x,y,z)$为柱面上的任意一点，则有$M$在过准线上的一点$M_0(x_0, y_0, z_0)$，且方向为$\bf{v}$的直线上。因此有：

<center>
$\left\{\begin{array}{l} F(x_0, y_0, z_0) = 0 \newline G(x_0, y_0, z_0) = 0 \newline x = x_0 + lu \newline y = y_0 + mu \newline z = z_0 + nu \end{array}\right.$
</center>
消去$x_0, y_0, z_0,u$，得到柱面方程。

**圆柱面、点的柱坐标**

圆柱面有一条对称轴$l$，圆柱面上每一点到轴的距离相等，这个距离称为圆柱面面的半径。如果知道圆柱面的半径为$r$，母线的方向为$\bf{v}(l, m, n)$以及圆柱面的对称轴$l_0$经过$M_0(x_0, y_0, z_0)$，则点$M(x,y,z)$在圆柱面上的充分且必要条件为$M$到轴$l_0$的距离等于$r$，即
<center>
$\dfrac{\|\vec{MM_0} \times \bf{v}\|}{\|\bf{v}\|} = r$
</center>

特别的，若圆柱面的半径为$r$，对称轴为$z$轴，则这个圆柱面的方程为：

$$x^2 + y^2  = r^2$$

<center>
<a href="https://www.geogebra.org/3d/perzz6xa">
<img src="./imags/cylinder1.png" width="300" height="400"/>
</a>
</center>

空间中的任意一点$M(x, y, z)$必在以$r = \sqrt{x^2 + y^2}$为半径，以$z$轴为对称轴的圆柱面上。这个圆柱面的参数方程为：

<center>
$\left\{\begin{array}{l} x = r\cos \theta \newline y = r \sin \theta \newline z = u \end{array}\right. 0 \le \theta < 2\pi, -\infty < u < +\infty$
</center>

因此，圆柱面上的点$M$被$(\theta, u)$所确定。从而空间中的任意一点被有序的三元实数组$(r, \theta, u)$所确定。$(r, \theta, u)$称为点$M$的<span style="color:red">**柱面坐标**</span>。

下图点$B''$在柱坐标下的参数为$(r, \theta, u) = (4, 2, 5)$

<center>
  <a href="https://www.geogebra.org/3d/zhqbgbmj">
    <img src="./imags/cylinder_cood.png" width="400" height="300"/>
  </a>
</center>

直角坐标与柱坐标的相互关系为：
<center>
$\left\{\begin{array}{l} x = r\cos \theta \newline y = r \sin \theta \newline z = u \end{array}\right. r \ge 0, 0 \le \theta < 2\pi, -\infty < u < +\infty$
</center>

---
**柱面坐标的特点**

<span style="color:red"> 
若一个柱面的母线平行于$z$轴(或$x$轴，或$y$轴)，则它的方程中不含有$z$(或$x$，或$y$)；反之，一个三元方程如果不含有$z$(或$x$，或$y$)，则它一定表示一个母线平行于$z$轴(或$x$轴，或$y$轴)的柱面。
</span>

---
**例子**

下图分别为:
+ 椭圆柱面($\dfrac{x^2}{2^2} + \dfrac{y^2}{3^2} = 1$);

+ 抛物柱面($z = x^2$);

+ 双曲柱面($\dfrac{x^2}{4} - \dfrac{y^2}{2} = 1$)。

<center>
  <a href="https://www.geogebra.org/m/sk9n55wr">
    <img src="./imags/cylinders2.png" width="400" height="400"/>
  </a>
</center>

---
**📌圆锥面**

对于圆锥面，它有一根对称轴$l$，它的每一条母线与轴$l$夹的角都相等，这个锐角称为圆锥面的<span style="color:red">**半顶角**</span>。与轴$l$垂直的平面截圆锥面所得的交线为圆。如果知道圆锥面的顶点$M_0(x_0, y_0, z_0)$，圆锥面轴的方向向量$\bf{v}$以及半顶角$\alpha$，则$M(x, y, z)$在圆锥面上的充分必要条件为：

<center>
$<\vec{M_0M}, \bf{v}> = \alpha$或者$\pi - \alpha$,
</center>

因此有：

<center>
$|\cos <\vec{M_0M}, \bf{v}>| = \cos \alpha $
</center>


<center>
  <a href="https://www.geogebra.org/3d/hnxdn7az">
    <img src="./imags/rotational_cone.png" width="500" height="400"/>
  </a>
</center>

---
**例子**

求以三根坐标轴为母线的圆锥面的方程。

<details>
<summary>⬇️iClick to expand!</summary>
显然这个圆锥面的顶点为原点，设轴$l$的方向为$\bf{v}$，因为三个坐标轴为母线，所以有：
<center>
$|\cos <\bf{e_1}, \bf{v}>| = |\cos <\bf{e_2}, \bf{v}>| = |\cos <\bf{e_3}, \bf{v}>| $
</center>

考察方向向量$\bf{v}$为$(1, 1, 1)$的情况，其它情况($(1, 1, -1), (1, -1, 1), (1, -1, -1)$)。$M(x, y, z)$在锥面上的充分必要条件为：

<center>
$|\cos<\vec{OM}, \bf{v}>| = |\cos<e_1, \bf{v}>|$
</center>

即

<center>
$\dfrac{|\vec{OM} \cdot \bf{v}|}{\|\vec{OM}\|\|\bf{v}\|} = \dfrac{|\bf{e_1} \cdot \bf{v}|}{\|\bf{v}\|}$
</center>

得到

<center>
$xy + yz + xz = 0$
</center>


</details>




<a name="cotes6"></a>
### 第六节 三元二次曲面

---
**📌旋转二次曲面**

<center>
<a href="https://en.wikipedia.org/wiki/Quadric">
<img src="./imags/quad_revo.png" width="600" height="1000"/>
</a>
</center>

---
**📌非退化二次曲面**

<center>
<a href="https://en.wikipedia.org/wiki/Quadric">
<img src="./imags/nondeg_quad_surf.png" width="600" height="1000"/>
</a>
</center>


---
**📌退化二次曲面**

<center>
<a href="https://en.wikipedia.org/wiki/Quadric">
<img src="./imags/dege_quad_surf.png" width="600" height="1000"/>
</a>
</center>

---
📚<span style="color:red"> 
**第五次作业:**
</span>

1. 将$xOy$坐标面上的双曲线$4x^2 - 9y^2 = 36$分别绕$x$轴及$y$轴旋转一周，求得到的旋转曲面的方程，并作图。

2. 指出下列方程表示的曲面并作图：

  + $4x^2 + y^2 -z^2 = 4$;

  + $\dfrac{z}{3} = \dfrac{y^2}{9}$;

  + $\dfrac{x^2}{3^2} + \dfrac{y^2}{4^2} - \dfrac{z^2}{5^2} = \pm 1$;
  
  + $\dfrac{x^2}{3^2} + \dfrac{y^2}{4^2} - \dfrac{z^2}{5^2} = 0$;

  + $\dfrac{x^2}{3^2} + \dfrac{y^2}{4^2} + \dfrac{z^2}{5^2} = 1$.

---
### 强调几个曲面

**📌双曲抛物面**

<span style="color:red">**双曲抛物面又称马鞍面**</span>，该曲面的的标准方程为$z = \dfrac{x^2}{p^2} - \dfrac{y^2}{q^2}$，特别的$z = xy$为一马鞍面。


<center>
  <a href="https://www.geogebra.org/classic/g4dqpkk4 ">
    <img src="./imags/Hypobolic_paraboloid.png" width="400" height="400"/>
  </a>

  <a href="https://www.geogebra.org/classic/nsypppjd">
    <img src="./imags/Hypobolic_paraboloid_xy.png" width="500" height="500"/>
  </a>
</center>

---

**📌直纹面**

一曲面$S$称为<span style="color:red">**直纹面**</span>，如果存在一簇直线是的这一簇中的每一条直线都在$S$上；并且$S$上的每一个点都在这一簇的某一条直线上。这样一簇直线称为$S$的<span style="color:red">**一簇直母线**</span>。

二次曲面中：二次柱面和锥面都是直纹面，椭球面不是直纹面，因为它有界。双叶双曲面不是直纹面，椭圆抛物面也不是直纹面。剩下的：单叶双曲面和双叶双曲面都是直纹面。


<center>
  <img src="./imags/ruled_surf.png" width="500" height="200"/>
</center>

---

<a name="cotes7"></a>
### 第七节 空间曲线

---
**📌空间曲线的方程**

**空间曲线一般式方程**

空间曲线可以看成两个曲面的交线。其方程为：

$$\left\{\begin{array}{l} F(x, y, z) = 0 \newline G(x, y, z) = 0 \end{array}\right. $$

---
**例子**

方程组
<center>
  $\left\{\begin{array}{l} x^2 + y^2 + z^2 = a^2 \newline (x - a/2)^2 + y^2 = (a/2)^2 \end{array}\right.$
</center>
为<span style="color:red">**Viviani曲线**</span>。下图为$a=4$的情形。

<center>
  <a href="https://www.geogebra.org/classic/kkjsbgcn ">
    <img src="./imags/Viviani's_curve.png" width="400" height="400"/>
  </a>
</center>

---
**例子**

方程组
<center>
  $\left\{\begin{array}{l}x^2 + y^2 = 1 \newline 2x + 3y = 1 \end{array}\right. $
</center>
表示的曲线见下图。
<center>
  <a href="https://www.geogebra.org/classic/kwfhk7wg">
    <img src="./imags/line_in3d_1.png" width="400" height="400"/>
  </a>
</center>

---

**空间曲线的参数方程**

空间曲线可以看成是一个质点的移动轨迹，其<span style="color:red">**参数方程为**</span>：
<center>
$\left\{\begin{array}{l} x = x(t) \newline y = y(t) \newline z = z(t) \end{array}\right.$
</center>

---
**例子**

<span style="color:red">**螺旋线**</span>：在圆柱面$x^2 + y^2 = a^2$上以角速度$\omega$绕$z$轴旋转，同时又以线速度$v$沿平行于$z$轴的正方向上升，那么点形成的轨迹称为螺旋线，其参数方程为：

<center>
$\left\{\begin{array}{l} x = a\cos t \newline y = a\sin t \newline z = vt \end{array}\right.$
</center>

<center>
  <a href="https://www.geogebra.org/classic/bcqxkxsp">
    <img src="./imags/curve_3d_2.png" width="400" height="400"/>
  </a>
</center>

**空间曲线在坐标平面上的投影，投影柱面**

设空间曲线$C$方程为

<center>
$\left\{\begin{array}{l} F(x, y, z) = 0 \newline G(x, y, z) = 0 \end{array}\right. $
</center>

消去变量$z$(如果可能的话)，所得到的方程为
$$H(x, y) = 0$$
得到过曲线$C$的<span style="color:red">**投影柱面**</span>，而

$$
  \left\{\begin{array}{l} H(x, y) = 0 \newline z = 0 \end{array}\right.
$$

所表示的曲线为曲线$C$在$xOy$平面上的<span style="color:red">**投影曲线**</span>，投影曲线围成的区域为空间曲线$C$在$xOy$平面上的<span style="color:red">**投影区域**</span>。

---
**例子**

求下列曲面的交线在坐标平面上的投影。
<center>
$x^2 + y^2 = 2z, x^2 + y^2 = 4x$
</center>

<details>
解：$x^2 + y^2 = 2z$是椭圆抛物面，$x^2 + y^2 = 4x$是圆柱面。椭圆抛物面与柱面的交线$\Gamma$为：
<center>
  $\left\{\begin{array}{l} x^2 + y^2 = 2z \newline x^2 + y^2 = 4x \end{array}\right.$
</center>
$\Gamma$在$xOy$面上的投影为
<center>
  $\left\{\begin{array}{l} z = 0 \newline x^2 + y^2 = 4x \end{array}\right.$
</center>

$\Gamma$在$xOz$面上的投影为
<center>
  $\left\{\begin{array}{l} z = 2x \newline y = 0 \end{array}\right.$
</center>

<center>
<a href="https://www.geogebra.org/3d/hkctfegq">
   <img src="./imags/cyli_para_inter.png" width="400" height="400"/>
</a>
</center>

</details>

---
📚<span style="color:red"> 
**第六次作业:**
</span>

+ 分别求母线平行于$x$轴，$y$轴而且通过曲线
<center>
    $
      \left\{\begin{array}{l} 2x^2 + y^2 + z^2 = 16 \newline x^2 + z^2 - y^2 = 0 \end{array}\right.
    $
</center>
   的柱面方程。

+ 将曲线
<center>
    $
      \left\{\begin{array}{l} x^2 + y^2 + z^2 = 9 \newline y = x \end{array}\right.
    $
</center>
   化为参数方程。

+ 求螺旋线
<center>
   $
      \left\{\begin{array}{l} x = a\cos \theta \newline y = a \sin \theta \newline z = b\theta \end{array}\right.
   $
</center>
   在三个坐标平面上的投影曲线的直角坐标方程。


---
## 📚参考书目
📖1. 《高等数学》上下册（第七版），同济大学，高等教育出版社，2014.7.

📖2. 《解析几何》，邱维声，北京大学出版社，1988.

📖3. 《解析几何》，尤承业，北京大学出版社，2004.


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
