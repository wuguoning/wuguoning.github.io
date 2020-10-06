---
title: "微積分的創立"
collection: talks
type: "Talk"
permalink: /talks/CreationCalculus
venue: "College of Science, China University of Petroleum"
date: 2020-09-20
location: "Beijing, CN"
---
  <figure>
    <img src="/images/Newton_and_Leibniz.png" alt="my alt text" style="width:400px"/>
  </figure>

>   他以幾乎神一樣的思維力，最先說明了行星的運動和圖像，彗星的軌道和大海的朝夕。
   
>   Nature and Nature's laws lay hid in night. God said,"Let Newton be!" and all was light.
   
>   遵法自然，久藏玄冥。
    天降牛頓，萬物生明。

>   Newton 墓誌銘

## 促使微積分產生的因素
緊隨函數概念的出現，產生了微積分，它是繼歐幾里德幾何之後，全部數學史中的一個最偉大創造。
微積分的創立，首先是為了處理十七世紀主要的科學問題。

有四種主要問題：

1. 已知物體的位移為時間的函數，求物體在任意時刻的速度和加速度；反過來，已知物體的加速度
   求速度和位移。困難在於：速度為時間的函數，求速度必然設計0/0，在當時是無意義的。
   
2. 求曲線的切線。這個問題來自於光學和幾何。透鏡的設計吸引了Fermat, Descarts, Huygens和
   Newton.要研究光線通過透鏡的通道，需要研究反射定律。
   
3. 求函數的最大值與最小值。砲彈的射程依賴與出射角。十七世紀初起，Galileo斷言（在真空中）
   最大射程的出射角是45度。
   
4. 求曲線的弧長、曲線圍成的面積、曲面圍城幾何體的體積、物體的重心。

## 十七世紀初期微積分的工作

微積分問題至少被十七世紀十幾個最偉大的數學家和幾十個數學家探索過。位於他們貢獻頂峰的是
Newton和Leibniz。

### Newton的工作
數學和科學中的巨大進展，幾乎總是建立在幾百年中許多人的點滴工作基礎之上。最後需要需要
一位具有能夠從紛亂的猜測中清理有價值的想法，能夠有足夠的想象力重組思想的碎片，該人就
是牛頓Newton. 

> 正所謂“天不生仲尼，萬古長如夜。”

> Nature and Nature's laws lay hid in night. God said,"Let Newton be!" and 
> all was light.

Newton(1642~1727)生於英格蘭烏爾斯托帕的一個小村莊裡，他的母親在那裡管理者丈夫遺留下來
的農莊，他的父親在他出生前的兩個月去世的。他在本地很普通的學校接受教育、而且除了對機械設計
有興趣外，沒有特殊才華的青年人。1661年他考取劍橋大學，他從老師那裡得到了很少的一點鼓勵，除了
Barrow外，他自己研究Descartes,Copernicus,Kepler,Galileo,Wallis和Barrow的著作。

Newton大學畢業後就遇到了倫敦地區鼠疫流行，他離開劍橋，在家鄉安靜的度過了1665和1666年。
在這段時期內，他認識到了引力的平方反比定律、獲得了解決微積分問題的一般方法。並通過實驗
發現了太陽光實際上是從紫色到紅色的不同顏色光混合而成的。
牛頓後來說：“所有這些“”是在1665年和1666兩個鼠疫年做出的，因為在這些日子裡，我正處在
發現力最盛時期，而且對於數學和哲學（自然哲學）的關心，比其它任何時候都多。”

起初，Newton並沒有公布他的發現。
> De Morgan說是“一種病態的害怕別人反對的心裡統治了他的一生。” 

Newton對於光學的研究成果遭到Robert Hooke和Huygens在內人的嘲諷。除了
天體力學、光學和化學工作意外，Newton還研究了靜體力學和流體力學。

關於微積分，Newton總結了已經由許多人發展了的思想，建立了成熟的方法。Newton給出了
求一個變量對於另一個變量的瞬時變化率的普遍方法。在寫於1671年但直到1736年才出版的
《流數法和無窮級數》書中，Newton把變量稱為流(fluent)，變量的變化率稱為流數(fluxion)。
對於流$x,y$的流數記為$\.{x},\.{y}$
 
![流和流數](./figs/fluent_fluxion.png)

### Leibniz的工作

在建立微積分中和Newton並列在一起的是Gottfried Wilhelm Leibniz(1646-1716).1714年
Leibniz寫了《微分學的歷史和起源》(Historiaet Origo Calculi Differentialis)，
在該書中，他給出了有關他自己思想發展的記載。 Leibniz研究數列的階差，用"omn."表示
和。Leibniz獲得$omn.yl = \frac{y^2}{2}$.
1675年10月
29日的手稿中，Leibniz界定用"$\int$"代替"omn." 記號"$\int$"是sum的第一個字母S的拉長。
可能是由於研究Barrow著作的關係，Leibniz很早就意識到，微分和積分（看作和）必定是相反
的過程。談到記號，Leibniz煞費苦心的工作，要把記號選得最好，他試著定義如
$$ddy = d^2y, dddy = d^3y$$等高階微分$d^n$。他引進了記號$\log x$.
Leibnin斷定一個事實：“作為求和過程的積分是為分的逆。” 除了這個斷言外，他並
不清楚怎樣從一組矩形得到曲線下面的面積，也不清楚怎樣從一個粗糙的求和表達式。
$$\sum y\,\mathrm{d}x$$去得到面積。Leibniz認為該表達式是非常多而又非常小的矩形和。
沒有極限的引入，這個概念不可能不嚴格化。

1676年6月26日的手稿中，他意思到求切線的最好的方法是求$\dfrac{dy}{dx}$，其中
$dy,dx$表示差商。

一般來說，Leibniz的工作，雖然富有啟發性而且意義深遠，但它是如此零碎不全，以至於幾乎不能
理解。幸好有Bernoulli兄弟，James和John，在Leibniz思想的影響和啟發下，把他的梗概性
文章做了細緻的加工，並做了大量的新發展。

### Newton於Leibniz工作的比較
微積分是應用於許多類函數的一種新的普遍的方法，這一發現主要歸功於Newton和Leibniz兩人。經過
他們的努力，微積分不再是古希臘幾何的附庸，而是一門獨立的科學，用來處理較為更廣泛的問題。兩個
人在代數概念的基礎上建立微積分，使得不同的幾何和物理問題用共同的方法處理。這項工作可以比肩於
Vieta的方程理論、Descartes和Fermat的幾何學。

Newton和Leibniz的第三個貢獻是把面積、體積和其他以前作為求和處理的問題歸結到反微分。因此，四個
主要問題：速率、切線、最大值和最小值、求和全部歸結為微分和反微分。

兩人工作的主要差異是：
>  <span style="color:red">Newton把$x,y$的無窮小增量作為求流數或導數的手段。當增量越來越小的時候，流數實際上就是增量比值的極限。Newton首先想到的是微分，微分是基礎。Newton的工作是經驗的、
> 具體的和謹慎的。</span>
>
> <span style="color:blue">Leibniz卻直接用$x,y$的無窮小增量求出它們之間的關係。Leibniz首先想到的是積分（和）。Leibniz的工作是富有想象的、大膽的。</span>

這個差別反應了Newton的物理方向和Leibniz的哲學方向。

### 優先權的爭論


1687年以前，Newton沒有發表過微積分方面的任何工作，雖然他從1665年到1687年結果通知了朋友。1673年
Leibniz訪問了巴黎，1673年訪問了倫敦，並且和一些知道了Newton的工作通信。然而，直到1984年
才發表微積分的著作。於是人們懷疑是否剽竊了Newton的工作。調查證明：雖然Newton的大部分
工作是在Leibniz之前得到的，但是Leibniz是微積分主要思想的獨立創造者。兩個人都受到Barrow
的很多啟發。大陸的數學家，尤其是Bernoulli兄弟，支持Leibniz，而英國數學家則捍衛Newton。
兩派針鋒相對導致英國和大陸的數學家停止了思想交換。在Newton去世後的一百年裡，英國人以其
《原理》中的幾何方法為主要工具，而大陸數學家繼續以Leibniz的分析方法。這些事情使得英國
數學家落在了研究的後面，從而是數學損失了一些最有才能的能應可作出的貢獻。



## 參考文獻

1. 《古今數學思想》，克萊因。