---
title: "Data-driven Time-Frequency Analysis: A Survey"
collection: talks
type: "Tutorial"
permalink: /talks/Data_Driven_TF_Survey
venue: "China University of Petroleum-Bejing"
date: 2019-09-19
location: "Beijing, CN"
author: Guoning Wu
---
[![data-driven](./figs/data-driven.png)](https://wuguoning.github.io/talks/Data_Driven_TF_Survey)

# Abstract
This is a **Tutorial** of data-driven time-frequency analysis methods.

# Introduction
Non-stationary signal processing methods have developed a lot. One way 
is the linear time-frequency transforms that includes short time Fourier 
transform, wavelet transform, Stockewell transform(@Stockwell1996) etc. A downside of 
linear transforms is that the atoms are fixed and predetermined. The time-
frequency distribution is blurred due to the Heisenberg uncertainty 
principle.

One other way started in the late nineties when Huang et al. proposed 
the empirical mode decomposition(EMD)(@emd), which extracts intrinsic mode 
functions from the input signal recursively using sifting processing.
The EMD method has been widely used in many areas despite its shortage of 
a consolidate theoretical background. To overcome that difficulty, some
other methods have been proposed, such as synchrosqueezing wavelet transform(@daubechies), 
synchrosqueezing Fourier transform, empirical wavelet transform, singular 
spectrum analysis(SSA), variational mode decomposition(VMD) etc.

While efforts to develop fully data driven yet mathematically sound algorithms for signal decompositon and TF analysis of nonstationary data continume to grow, there has been a lot of interest in extending existing data driven approaches to process nonstationary multidimensional and multivariate data sets.


# References
