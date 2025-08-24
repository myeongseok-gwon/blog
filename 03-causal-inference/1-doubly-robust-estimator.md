# Doubly Robust Estimator

Before defining the Doubly-Robust Estimator, let me define a few functions and estimators. We denote the dependent variable as y, the binary treatment variable as D, and nuisance variables as X. We can create a model that predicts y using all variables (X and D=0) within the Control Group where D=0. Similarly, we can create a model for D=1. If the two groups are comparable, this alone might be a fairly good model. (Of course, for some Learners, due to the curse of dimensionality in numerous covariates, there's a possibility that regardless of whether D is 0 or 1, the effect may not be considered and predictions may be based solely on X, which could lead to underestimating a policy that actually has an effect.)

\begin{align}
g_0(x) := E[Y\mid D=0, X=x]\\
g_1(x) := E[Y\mid D=1, X=x]\\
g_{D_i}(x) := g_1(x) * D + g_0(x) * (1-D)\\
\end{align}

We can also create a propensity score model p(x) as follows. The q(x) is a model that predicts Y without using the D variable. (This is used for the residualization method employed in DML or Causal Forest.)

\begin{align}
p(x) := E[D\mid X=x] = \Pr(D=1\mid X=x)\\
q(x) := E[Y\mid X=x]\\
\end{align}

Note that when actually implementing, you can choose any machine learning method you want to obtain all the estimates described here. However, due to the overfitting problem, one rule when using these methods is to always perform cross-validation. For detailed implementation and application methods, please refer to the [link](/CATE-inference).

The reason it's called Doubly Robust is because even if the propensity score estimate {math}`\hat{p}(X_i)` is inaccurate, as long as {math}`\hat{g}_1(X_i)` and {math}`\hat{g}_0(X_i)` are accurate, the expected value becomes the correct ATE estimate, and conversely, even if {math}`\hat{g}_1(X_i)` and {math}`\hat{g}_0(X_i)` are inaccurate, as long as the propensity score estimate {math}`\hat{p}(X_i)` is accurate, the expected value likewise becomes the correct ATE estimate.

The Doubly Robust Estimator is defined as follows:

```{math}
:label: first
Y_i^{DR}(\hat{g},\hat{p}) := \hat{g}_1(X_i) - \hat{g}_0(X_i) + (Y_i - \hat{g}_{D_i}(X_i))\frac{D_i - \hat{p}(X_i)}{\hat{p}(X_i) (1-\hat{p}(X_i))}
```

It can then be used as follows. Here we only prove ATE, but it can similarly be shown that by organizing in terms of a given X, it can be used for CATE as well.

```{math}
ATE = E_n\left[Y^{DR}(\hat{g},\hat{p})\right], \quad CATE = \tau(X) = E[Y^{DR}(\hat{g}, \hat{p})|X]
```

---

## Proof of the Expected Value Properties of the Doubly Robust Estimator

### **1. Taking the Expectation**
Taking the expectation of the Estimator:

```{math}
:label: expectation
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\hat{g}_1(X) - \hat{g}_0(X) + (Y - \hat{g}_{D}(X))\frac{D - \hat{p}(X)}{\hat{p}(X)(1-\hat{p}(X))} \right]
```

---

### **2. Separating the Fraction Term**

The core term of the Doubly Robust Estimator  
```{math}
:label: core
(Y - \hat{g}_D(X)) \frac{D - \hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))}
```
is decomposed and expanded by dividing into the treatment group ({math}`D = 1`) and the control group ({math}`D = 0`).

---

#### **2-1. Trick for Decomposition**
First, we need a trick where we subtract and add {math}`D \hat{p}(X)` to {math}` D - \hat{p}(X) `.

```{math}
D - \hat{p}(X) = D - D \hat{p}(X) + D \hat{p}(X) - \hat{p}(X)
```

Rearranging this:

```{math}
D - \hat{p}(X) = D(1 - \hat{p}(X)) - (1-D) \hat{p}(X)
```

Substituting this into the original equation:

```{math}
(Y - \hat{g}_D(X)) \frac{D(1 - \hat{p}(X)) - (1-D)\hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))}
```

Separating this into two terms:

```{math}
:label: decomposed
(Y - \hat{g}_D(X)) \left( \frac{D(1 - \hat{p}(X))}{\hat{p}(X)(1 - \hat{p}(X))} - \frac{(1-D)\hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))} \right)
```

Thus, we can **separate the terms for the treatment group ({math}`D=1`) and the control group ({math}`D=0`)**.

---

#### **2-2. For the Treatment Group ({math}`D = 1`)**
In the treatment group where {math}`D = 1`:

```{math}
(Y - \hat{g}_1(X)) \left( \frac{1 - \hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))} - 0 \right)
```

```{math}
= (Y - \hat{g}_1(X)) \frac{1}{\hat{p}(X)}
```

---

#### **2-3. For the Control Group ({math}`D = 0`)**
In the control group where {math}`D = 0`:

```{math}
(Y - \hat{g}_0(X)) \left( 0 - \frac{\hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))} \right)
```

```{math}
= -(Y - \hat{g}_0(X)) \frac{1}{1 - \hat{p}(X)}
```

---

#### **2-4. Summary**
The core term [](#core) is now organized through [](#decomposed) as follows:

```{math}
:label: decomposed-2
(Y - \hat{g}_D(X)) \frac{D - \hat{p}(X)}{\hat{p}(X)(1 - \hat{p}(X))} = D*[(Y - \hat{g}_1(X)) \frac{1}{\hat{p}(X)}] - (1-D)*[(Y - \hat{g}_0(X)) \frac{1}{1 - \hat{p}(X)}]
```

---

### **3. Organizing the Complete Term**
Substituting [](#decomposed-2) into the expectation formula [](#expectation):
```{math}
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\hat{g}_1(X) - \hat{g}_0(X) + D*[(Y - \hat{g}_1(X)) \frac{1}{\hat{p}(X)}] - (1-D)*[(Y - \hat{g}_0(X)) \frac{1}{1 - \hat{p}(X)}] \right]
```

Dividing this into two main parts:
```{math}
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\hat{g}_1(X) + D*[(Y - \hat{g}_1(X)) \frac{1}{\hat{p}(X)}] \right]- E\left[\hat{g}_0(X) + (1-D)*[(Y - \hat{g}_0(X)) \frac{1}{1 - \hat{p}(X)}] \right]
```

Grouping the g-related terms internally:
```{math}
:label: decomposed-expectation
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\frac{DY}{\hat{p}(X)} - \left( \frac{D - \hat{p}(X)}{\hat{p}(X)}\right) \hat{g}_1(X)\right] - E\left[\frac{(1-D)Y}{1-\hat{p}(X)} - \left( \frac{(1-D) - (1-\hat{p}(X))}{1-\hat{p}(X)}\right) \hat{g}_0(X) \right]
```

---

### **4. Why is accurate ATE estimation possible if only one of the two is accurate?**
#### Assumption 1: Propensity score {math}`\hat{p}(X_i)` is inaccurate, but {math}`\hat{g}_1(X_i)` and {math}`\hat{g}_0(X_i)` are accurate
In [](#expectation), since {math}`(Y - \hat{g}_{D}(X))` always becomes 0, we can naturally confirm that it is an ATE estimator as follows, where all terms except the two below disappear from the expectation:
```{math}
:label: applied
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\hat{g}_1(X) - \hat{g}_0(X) \right] = E[Y_1] - E[Y_0] = ATE
```

<br/><br/>
#### Assumption 2: {math}`\hat{g}_1(X_i)` and {math}`\hat{g}_0(X_i)` are inaccurate, but the propensity score {math}`\hat{p}(X_i)` is accurate
In [](#decomposed-expectation), when the propensity score is accurate, since {math}`E[D - \hat{p}(X)] = 0`, only the following terms remain. From here, this part corresponds to the property of Inverse Propensity Weighting, and can be proven using the law of iterated expectations.

```{math}
E[Y^{DR}(\hat{g},\hat{p})] = E\left[\frac{DY}{\hat{p}(X)}\right] - E\left[\frac{(1-D)Y}{1-\hat{p}(X)}\right]
```

```{math}
= E\left[E\left[\frac{DY}{\hat{p}(X)}\Big| X\right]\right] - E\left[E\left[\frac{(1-D)Y}{1-\hat{p}(X)}\Big| X\right]\right]
```

Since {math}`E[DY|X] = \hat{p}(X) * E[Y|D=1, X]`:

```{math}
= E\left[E[Y|D=1, X]\right] - E\left[E[Y|D=0, X]\right] = E\left[E[Y_1,|X]\right] - E\left[E[Y_0|X]\right]
```

Using the law of iterated expectations once more, the proof is completed as follows:
```{math}
= E[Y_1] - E[Y_0] = ATE
```

## Example discussion
<script src="https://utteranc.es/client.js"
        repo="TeachBooks/manual"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>