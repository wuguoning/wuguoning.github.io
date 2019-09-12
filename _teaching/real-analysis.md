---
title: "Real Analysis"
collection: teaching
type: "Workshop"
permalink: /teaching/real-analysis
venue: "China University of Petroleum at Beijing, Science"
date: 2019-09-12
location: "City, Country"
---
**`These are lectures notes and tests for real analysis.`**


Real Analysis I
======
## Introduction
### The Motivation for Calculus
Following hard on the adoption of the function concept came the calculus, which, next to Euclidean geometry, is the greatest in all of mathematics. Though is was to some extent the answer  to problems already tackled by the Greeks, the calculus was created primarily to treat the major scientific problems of the seventeenth century.

There were four major types of problems. The first was: Given the formula for the distance a body covers as a function of time, to find the velocity and acceleration at any instant; and, conversely, given the formula describing the acceleration of a body as a function of the time, to find the velocity and the distance traveled.

The second type of problem was to find the tangent to a curve. It was a problem of pure geometry, and it was of great importance  for scientific applications.

The third problem was that of finding the maximum or minimum value of a function. The study of the motion of the planets involved maxima and minima problems, such as finding the greatest and least distances of a planet from the sun.

The fourth problem was finding the lengths of curves, for example, the distance covered by a planet in a given period of time; the area bounded by curves; volumes bounded by surfaces; centers of gravity of bodies; and the gravitational attraction that extended body, a planet for example, exerts on another body.

### Early Seventeenth-Century Work on the Calculus

The problems of the calculus were tackled by at least a dozen of the greatest mathematicians of the seventeenth century and by several dozen minor ones. All of their contributions were crowned by the achievements of Newton and Leibniz. Here we shall be able to note only the principle contributions of the precursors of these two masters.

Several methods were advanced to find the tangent to a curve. Gilles Persone de Roberval(1602-75) generalized a method Archimedes had used to find the tangent at any point on his spiral, which the tangent line of a projectile shot from a canon is the resultant diagonal line of the vertical and horizontal velocities.

While the notion of a tangent as a line having the direction of the resultant velocity was more complicated than the Greek definition of a line touching a curve, this newer concept applied to many curves for which the older one failed.

## The Real Numbers
### Sets and Elementary Operations on Them
In this note, we introduce some basic concepts for real 
analysis.

#### The Concept of a Set
Since the late nineteenth and early twentieth centuries 
the most universal language of mathematics has been the 
language of set theory. This is even manifest in one of 
the definitions of mathematics as the science that 
studies different structures (relations) on sets.

**"We take a set to be an assemblage of definite, 
perfectly distinguishable objects of our intuition or 
our thought into a coherent whole."** Thus did Georg 
Cantor\footnote{G.Cantor(1845-1918) - German 
mathematician, the creator of the theory of infinite 
sets and the progenitor of set theoretic language in 
mathematics.}, describe the concept of a set.
  1. A set may be consist of any distinguishable objects.
  2. A set is unambiguously determined by the collection of objects that comprise it.
  3. Any property defines the set of objects having that property.

If $x$ is an object, $P$ is a property, and $P(x)$ denotes the assertion that $x$ has property $P$, then the class of objects having the property $P$ is denoted $\{x\lvert P(x)\}$
And in fact the concept of the set of all sets, for example, is simply contradictory. This is the classical paradox of **Russell**.

  > B.Russell (1872-1970) - British logician, philosopher, sociologist ans social activist.

#### The Inclusion Relation

The statement, "$x$ is an element of the set $X$" is written 
briefly as
$$ x\in X $$
and its negation as
$$ x \notin X $$

When statements about sets are written, frequent use is 
made of the logical operators $\exists$ ("there exists" or "there
are") and $\forall$ ("every" or "for all") which are called the
\emph{existence} and \emph{generalization} respectively.

Thus two sets are equal if they consist of the same 
elements, this statement is usually written briefly as 
$$ A=B,$$
read as "$A$ equals $B$". The negation of equality is usually 
written as 
$$ A \ne B.$$
If every element of $A$ is an element of $B$, we write
$A\subset B$ and say that $A$ is a subset of 
$B$ or that $B$ contains $A$.

Thus 
$$A\subset B := \forall x\in A \Rightarrow x\in B$$
If $A\subset B$ and $A\ne B$, we shall say that the inclusion $A\subset B$ is 
**strict** or that $A$ is a proper subset of $B$.

Using these definitions, we can now conclude that
$$A=B \Leftrightarrow A\subset B \wedge B\subset A$$
If $M$ is a set, any property of $P$ distinguishes in M the subset
$$\{x\in M \vert P(x)\}$$
consisting of the elements of $M$ that have the property.

For example, it is obvious that 
$$M=\{x\in M \vert x\in M\},$$
and the \emph{empty} subset of $M$ is 
$$\emptyset = \{x\in M \vert x\ne x\}$$


#### Elementary Operations on Sets
\begin{figure}[htbp]
    \centering
    \begin{tikzpicture}[scale=0.75]
    \draw  (0,0) rectangle  (4,3);
        \node [below,black] at (2, 0) {(a)};
    \draw (2.5,1.5) circle (1);
    \draw (1.5,1.5) circle (1);
    \node [above left,green] at (1.5, 1.5) {$A$};
    \node [above right,blue] at (2.5, 1.5) {$B$};
    \clip (1.5,1.5) circle (1);
    \clip (2.5,1.5) circle (1);
    \draw [fill, blue!100] (0, 0) rectangle (4, 3);
    \node [black] at (2, 1.5) {$ A\cap B$};
\end{tikzpicture}
    \begin{tikzpicture}[scale=0.75]
    \draw  (0,0) rectangle  (4,3);
        \node [below,black] at (2, 0) {(b)};
    \draw [fill=green](2.5,1.5) circle (1);
    \draw [fill=green] (1.5,1.5) circle (1);
    \node [above left,black] at (1.5, 1.5) {$A$};
    \node [above right,black] at (2.5, 1.5) {$B$};
    \clip (1.5,1.5) circle (1);
    \clip (2.5,1.5) circle (1);
    \draw [fill, green] (0, 0) rectangle (4, 3);
\end{tikzpicture}
    \begin{tikzpicture}[scale=0.75]
    \draw  (0,0) rectangle  (4,3);
        \node [below,black] at (2, 0) {(c)};
    \draw [fill=red](1.5,1.5) circle (1);
    \draw (2.5,1.5) circle (1);
    \node [above left,black] at (1.5, 1.5) {$A$};
    \clip (0,0) rectangle  (4,3);
    \clip (2.5,1.5) circle (1);
    \draw [fill,black!0] (0, 0) rectangle (4, 3);
    \node [above right,black] at (2.5, 1.5) {$B$};
\end{tikzpicture}
    \begin{tikzpicture}[scale=0.75]
    \draw [fill=yellow] (0,0) rectangle  (4,3);
        \node [below,black] at (2, 0) {(d)};
    \draw (1.5,1.5) circle (1);
    \clip (1.5,1.5) circle (1);
    \draw [fill,yellow!0] (0, 0) rectangle (4,3);
    \node [above left,black] at (1.5, 1.5) {$A$};
\end{tikzpicture}
\label{sets}
    \caption{(a) Intersection. (b) Union. (c) Difference. (d) Complement. }
\end{figure}

## Limits

