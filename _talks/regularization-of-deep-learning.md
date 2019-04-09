---
title: "Regularization of Deep Learning"
collection: talks
type: "Talk"
permalink: /talks/regularization-of-deep-learning
venue: "Department of Science, China University of Petroleum at Beijing"
date: 2019-04-09
location: "San Francisco, California"
---

This talk is about the regularization methods in deep learning.
## <span style="color:blue"> Introduction </span>
> Deep neural networks contain multiple non-linear hidden layers and this makes them very expressive models that can learn very complicated relationships between their inputs and outputs. With limited data, however, many of these complicated relationships will be the result of sampling noise, so they will exist in the training set but not in real test data even if it is drawn from the same distribution. This leads to overfitting and many methods have been developed for reducing it. These including:
* Stopping the training as soon as performance on a validation set starts to get wrose;
* Introducing weight penalties of various kinds such as:
    * $L1$ regularization;
    * $L2$ regularization;
    * Soft weight sharing;
    * Dropout method.


## <span style="color:blue"> Why does Dropout can conquer over-fitting? </span>

1. **平均作用** 每次应用Dropout时，相当于从原始网络中找到一个苗条(slim)的网络，如下图所示:
<figure>
  <img src="/images/dropout_slim_net.png" alt="my alt text"/>
  <figcaption>Dropout Neural Network.</figcaption>
</figure>
对于一个有N个节点的神经网络，根据Dropout原理可以看成训练不同的网络模型，
这些模型的参数数目是不变的，根据平均原理，或者投票原理来决定模型参数，从而
可以解决过拟合问题。
2. **减少神经元之间复杂的共适应关系**
3. **Dropout类似与性别在生物进化中的角色**

## <span style="color:blue">参考文献</span>
[1]. Srivastava N, Hinton G, Krizhevsky A, et al. Dropout: A simple way to prevent neural networks from overfitting[J]. The Journal of Machine Learning Research, 2014, 15(1): 1929-1958.

[2]. [Dropout as data augmentation.](http://arxiv.org/abs/1506.08700)
