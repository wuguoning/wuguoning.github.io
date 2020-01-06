
# coding: utf-8

# # Riemann Sums With Random Sampling

# ## Introduction 

# **Numerical Integration** comprises a broad family of algorithms for calculating the numerical value of a definite integral. The term **numerical quadrature** (often abbreviated to **quadrature**) is more or less a synonym for numerical integration, especially as applied to one-demensional integrals and for those functions that their antiderivatives are not expressible in elementary functions such as $e^{x^2}, \dfrac{\sin x}{x}, \dfrac{1}{\label{\ln}x}$ etc. 
# 
# The basic problem in numerical integration is to compute an approximation solution to a definite integral $\int_a^b f(x)\mathrm{d}x$ to a given degree of accuracy.
# 
# Quadrature is a historical mathematical term that means calculating area. The Pythagorean understood calculation of area as the process of constructing geometrically a square having the same area (squaring). That is why the process was named quadrature. There are several reasons for carrying out numerical integration:
#   1. The integrand $f(x)$ may be known only at certain points, such as obtained by sampling.
#   2. The antiderivative of a function is not expressible in terms of elementary functions.
#   3. It may be possible to find an antiderivative symbolically, but it may be easier to compute a numerical approximation than to compute the antiderivative. That may be the case antiderivative is given as an infinite series or product, or if its evaluation requires a special function that is not available.
#   
# Numerical integration methods can generally be describled as combining evaluations of the integrand to get an approxmation to the integral. The integrand is evaluated at a finite set of points and a weighted sum of these values is used to approximate the integral, such as the rectangle rule, the trapezoidal rule and the Simpson's rule etc. The quadrature rules discussed so far are all designed to compute one-dimensional integrals. To compute integrals in multiple dimensions, one approach is to phrase the multiple integral as repeated one-dimensional integrals by applying Fubini's theorem (the tensor product rule). This approach requires the function evaluations to grow exponentially as the number of dimensions increases. Three methods are known to overcome this so-called **curse of dimensionality**. Another method is the **Monte Carlo Integration**, which is a technique for numerical integration using random numbers. While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly choose points at which the integrand is evaluated. This method is particularly useful for higher-dimensional integrals.
# 
# In this article, we consider randomly sampled Riemann sums. Specifically, let the points $\xi_i$ be independently and uniformly randomly chosen in the interval $\left[\dfrac{k-1}{n}, \dfrac{k}{n}\right]$, where $k = 1,2 \cdots,n$. We show numerically that the Riemann sum 
# $$\sum_{i=1}^n f(\xi_i)\dfrac{b-a}{n}$$
# as a function of random variables has a Gaussian distribution as the greatest length of the subintervals is in some degree small.

# ## Random Variable Method

# First, import some modules.

# In[71]:


# Standard data science
import pandas as pd
import numpy as np

np.random.seed(42)

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# Visualizations
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot

# Cufflinks for dataframes
import cufflinks as cf
cf.go_offline()
cf.set_config_file(world_readable=True, theme='pearl')


# For the definite integral of the form $\int_a^b f(x)\mathrm{d}x$, the integral interval $[a,b]$ is uniformly divided into $n$ subintervals
# $$\left[\dfrac{0}{n}, \dfrac{1}{n}\right], \left[\dfrac{1}{n}, \dfrac{2}{n}\right],\cdots, \left[\dfrac{n-1}{n}, \dfrac{n}{n}\right]$$
# For each fixed $n$, we take a collection of independent random variables $\left\{\xi_{n1}, \xi_{n2}, \cdots, \xi_{nn}\right\}$ with $\xi_{nk}$ being uniformly distribution over $\Delta_{nk} = \left[\dfrac{k-1}{n}, \dfrac{k}{n}\right]$.The Riemann sum 
# $$\sigma_n = \dfrac{b-a}{n}\sum_{k=1}^{n}f(\xi_{nk})$$
# will be a function of random variables. We will simulate the distribution the $\sigma_n$.

# Warm up! we consider the integral $\int_0^1 x^2 \mathrm{d}x$.

# In[72]:


# Define the plot function
def plot_hist(x, title='', summary=True):
    df = pd.DataFrame(x)
    df.iplot(kind='hist', xTitle='Values',
             yTitle='Count', title=title)
    if summary:
        print(df.describe())
        
def plot_pdf(x, p_x, title=''):
    # Plot PDF of Poisson distribution
    df = pd.DataFrame({'x': x, 'y': p_x})
    df.iplot(kind='scatter',
             mode='lines+markers',
             x='x', y='y', xTitle='Numbers',
             yTitle='Values',
             title=title)
def plot_pdf1(x, p_x, title=''):
    # Plot PDF of Poisson distribution
    df = pd.DataFrame({'x': x, 'y': p_x})
    df.iplot(kind='scatter',
             mode='lines',
             x='x', y='y', xTitle='Numbers',
             yTitle='Values',
             title=title)
def plot_spread(x, p_x, title=''):
    # Plot PDF of Poisson distribution
    df = pd.DataFrame({'x': x, 'y': p_x})
    df.iplot(kind='spread',
             xTitle='x',
             yTitle='Value',
             title=title)
def plot_scatter(x, y1, y2, title=''):
    fig = go.Figure()
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y1,
                    mode='lines+markers',
                    name=title))
    fig.add_trace(go.Scatter(x=x, y=y2,
                  mode='lines+markers',
                  name=title))
    
    fig.show()


# In[73]:


# Define the functions
def func(x):
    return x**2
def func_0(x):
    return np.exp(-x*x)
def func_1(x):
    return np.exp(x*x)
def func_2(x):
    return np.sin(x*x)
def func_3(x):
    return np.cos(x*x)
def func_4(x):
    return np.sin(x)/(x)
def func_5(x):
    return 1.0/np.log(x)


# In[74]:


# Define the definite integral of f(x) on [a,b]
def cal_def_int_avg(trials, f, a, b, n):
    xs = np.arange(a, b+(b-a)/n, (b-a)/n)
    sub_intvals = [[x, y] for x, y in zip(xs[0:-1], xs[1:])]
    vals = []
    val_avg = 0.0
    for i in range(trials):
        val = 0.0
        for k, int_val in enumerate(sub_intvals):
            xi = int_val[0] + (int_val[1] - int_val[0])*np.random.uniform(0, 1)
            val = val + f(xi)*(b-a)/n
        val_avg = (val_avg + val)
        vals.append(val_avg/(i+1))

    return vals


# In[49]:


# Number of trials
trials = 100
# number of subintervals
n = 10
a = 0
b = 1

vals = cal_def_int_avg(trials, func, a, b, n)
tt = np.arange(trials)+1
plot_pdf(tt, vals, title='')


# In[50]:


# Number of trials
trials = 10000
# number of subintervals
n = 10
a = 0
b = 1

vals = cal_def_int_avg(trials, func, a, b, n)
tt = np.arange(trials)+1
plot_pdf1(tt, vals, title='')


# In[58]:


# Define the definite integral of f(x) on [a,b]
def cal_def_int(trials, f, a, b, n):
    xs = np.arange(a, b+(b-a)/n, (b-a)/n)
    sub_intvals = [[x, y] for x, y in zip(xs[0:-1], xs[1:])]
    vals = []
    for i in range(trials):
        val = 0.
        for k, int_val in enumerate(sub_intvals):
            xi = int_val[0] + (int_val[1] - int_val[0])*np.random.uniform(0, 1)
            val = val + f(xi)*(b-a)/n
        vals.append(val)

    return vals


# In[69]:


trials = 10000
nums = np.arange(10,500,10)
means = []
stds = []
for n in nums:
    means.append(np.mean(cal_def_int(trials, func, a, b, n)))
    stds.append(np.std(cal_def_int(trials, func, a, b, n)))
plot_pdf(nums, means, title='')
plot_pdf(nums, stds, title='')


# In[21]:


# Number of trials
trials = 10000
# number of subintervals
n = 10
a = 0
b = 1

vals = cal_def_int(trials, func, a, b, n)
plot_hist(vals, title='')

tt = np.arange(trials)
plot_pdf(tt, vals, title='PDF of Normal Distribution')

tt = np.ones(trials)*1.0/3
plot_spread(tt, vals, title='')


# In[23]:


# Number of trials
trials = 10000
# number of subintervals
n = 100
a = 0
b = 1

vals = cal_def_int(trials, func, a, b, n)
plot_hist(vals, title='')

tt = np.arange(trials)
plot_pdf(tt, vals, title='PDF of Normal Distribution')

tt = np.ones(trials)*1.0/3
plot_spread(tt, vals, title='')


# In[24]:


# Number of trials
trials = 100000
# number of subintervals
n = 10
a = 0
b = 1

vals = cal_def_int(trials, func, a, b, n)
plot_hist(vals, title='')

tt = np.arange(trials)
plot_pdf(tt, vals, title='PDF of Normal Distribution')

tt = np.ones(trials)*1.0/3
plot_spread(tt, vals, title='')


# In[25]:


def plot_pdf(x, p_x, title=''):
    # Plot PDF of Poisson distribution
    df = pd.DataFrame({'x': x, 'y': p_x})
    df.iplot(kind='scatter',
             mode='markers+lines',
             x='x', y='y', xTitle='x',
             yTitle='Values',
             title=title)
    
trials = 10000
nums = np.arange(10,100,10)
means = []
stds = []
for n in nums:
    means.append(np.mean(cal_def_int(trials, func, a, b, n)))
    stds.append(np.std(cal_def_int(trials, func, a, b, n)))


# In[68]:


# Number of trials
trials = 10000
# number of subintervals
n = 50
a = 0
b = 1

vals = cal_def_int(trials, func_0, a, b, n)
plot_hist(vals, title='')

tt = np.arange(trials)
plot_pdf(tt, vals, title='')


# ## Monte Carlo Method 

# Monte Carlo method for the estimation of the irational number $\pi$.

# In[75]:


N = 100000

count = 0  #count will store the number of random points
           #that fell within the unit circle
for i in range(N):
    x, y = np.random.random(), np.random.random()
    if x**2 + y**2 < 1: #sqrt(1-x**2) < y
        count += 1
    
print(4.0*count/N)


# In[76]:


# Monte Carlo simulation of the 2d function: points below and above the given line.
def monte_carlo_simu_2d(N, fun, a, b):
    df = pd.DataFrame()
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    x = np.arange(a,b,0.01)
    y = fun(x)
    fmax = max(y)
    xrand = a + (b-a)*np.random.random(N)
    yrand = fmax*np.random.random(N)
    ind_below = np.where(yrand < fun(xrand))
    ind_above = np.where(yrand >= fun(xrand))
    df['x'] = x
    df['y'] = y
    df1['xbelow'] = xrand[ind_below]
    df1['ybelow'] = yrand[ind_below]
    df2['xabove'] = xrand[ind_above]
    df2['yabove'] = yrand[ind_above]
    
    return df, df1, df2, fmax
    
def monte_carlo_simu_plot2d(df, df1, df2):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df1['xbelow'],
            y=df1['ybelow'],
            mode='markers',
            name='Below',
            marker=dict(
                color='Blue',
                size=6,
                line=dict(
                    color='MediumPurple',
                    width=0
                )
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df2['xabove'],
            y=df2['yabove'],
            mode='markers',
            name='Above',
            marker=dict(
                color='orange',
                size=6,
                line=dict(
                    color='MediumPurple',
                    width=0
                )
            )
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df['x'],
            y=df['y'],
            mode='lines',
            name='func',
            marker=dict(
                color='red',
                size=0,
                line=dict(
                    color='red',
                    width=3
                )
            )
        )
    )
    fig.layout.update(title='')
    fig.show()


# In[81]:


# Define the function
def fun(x):
    return np.sqrt(1-x**2)

N = 10000
a = 0
b = 1
df, df1, df2, fmax = monte_carlo_simu_2d(N, fun, a, b)
monte_carlo_simu_plot2d(df, df1, df2)


# In[65]:


print('The integral approxiamtion: {}'.format(len(df1)/N*fmax*4.0))


# In[82]:


def fun(x):
    return x**np.cos(x)+2
N = 5000
a = 1
b = 15
df, df1, df2, fmax = monte_carlo_simu_2d(N, fun, a, b)
monte_carlo_simu_plot2d(df, df1, df2)


# In[61]:


print('The integral approxiamtion: {}'.format(len(df1)/N*(b-a)*fmax))


# In[111]:


def fun(x):
    return np.exp(-x*x)

N = 10000
a = 0
b = 1
df, df1, df2, fmax = monte_carlo_simu_2d(N, fun, a, b)
monte_carlo_simu_plot2d(df, df1, df2)


# In[109]:


print('The integral approxiamtion: {}'.format(len(df1)/N*(b-a)*fmax))


# In[100]:


# Define the function
def fun(x):
    return np.divide(np.sin(x), x, out=np.ones_like(x), where=x!=0)

N = 5000
a = 0
b = np.pi/2
df, df1, df2, fmax = monte_carlo_simu_2d(N, fun, a, b)
monte_carlo_simu_plot2d(df, df1, df2)


# In[60]:


print('The integral approxiamtion: {}'.format(len(df1)/N*(b-a)*fmax))


# In[77]:


def fun(x):
    return x*x

N = 10000
a = 0
b = 1
df, df1, df2, fmax = monte_carlo_simu_2d(N, fun, a, b)
monte_carlo_simu_plot2d(df, df1, df2)


# In[78]:


print('The integral approxiamtion: {}'.format(len(df1)/N*(b-a)*fmax))


# ## Radom sampled Riemann sum VS Monte Carlo method 

# In[112]:


def fun(x):
    return x*x

N = 10000
n = 10

a = 0
b = 1
monte_carlo_vals = []
random_riemann_vals = []
for i in range(100, 10100, 100):
    df, df1, df2, fmax = monte_carlo_simu_2d(i, fun, a, b)
    val = len(df1)/i*(b-a)*fmax
    monte_carlo_vals.append(val)
    
    vals = cal_def_int(i//10, fun, a, b, n)
    vals = np.array(vals)
    random_riemann_vals.append(vals.sum()/i*10)
    
    


# In[114]:


tt = np.arange(100, 10100, 100)

def data_comparison(tt, data1, data2, title=''):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=tt,
            y=data1,
            mode='markers+lines',
            name='M. Carlo',
            marker=dict(
                color='blue',
                size=3,
                line=dict(
                    color='blue',
                    width=3
                )
            )
        )
    )
    fig.add_trace(
        go.Scatter(
            x=tt,
            y=data2,
            mode='markers+lines',
            name='Riemann',
            marker=dict(
                color='red',
                size=3,
                line=dict(
                    color='red',
                    width=3
                )
            )
        )
    )
    fig.layout.update(title='')
    fig.show()
    
data_comparison(tt, monte_carlo_vals, random_riemann_vals, title='')


# In[115]:


def func_0(x):
    return np.exp(-x*x)

N = 10000
n = 10

a = 0
b = 1
monte_carlo_vals = []
random_riemann_vals = []
for i in range(100, 10100, 100):
    df, df1, df2, fmax = monte_carlo_simu_2d(i, func_0, a, b)
    val = len(df1)/i*(b-a)*fmax
    monte_carlo_vals.append(val)
    
    vals = cal_def_int(i//n, func_0, a, b, n)
    vals = np.array(vals)
    random_riemann_vals.append(vals.sum()/i*n)

data_comparison(tt, monte_carlo_vals, random_riemann_vals, title='')


# In[116]:


def fun(x):
    return np.divide(np.sin(x), x, out=np.ones_like(x), where=x!=0)
N = 10000
a = 0
b = np.pi/2
n=10

monte_carlo_vals = []
random_riemann_vals = []
for i in range(100, 10100, 100):
    df, df1, df2, fmax = monte_carlo_simu_2d(i, func_0, a, b)
    val = len(df1)/i*(b-a)*fmax
    monte_carlo_vals.append(val)
    
    vals = cal_def_int(i//n, func_0, a, b, n)
    vals = np.array(vals)
    random_riemann_vals.append(vals.sum()/i*n)

data_comparison(tt, monte_carlo_vals, random_riemann_vals, title='')


# In[117]:


def func(x):
    return 1.0/np.log(x)

N = 10000
a = 2
b = np.exp(2)
n=10

monte_carlo_vals = []
random_riemann_vals = []
for i in range(100, 10100, 100):
    df, df1, df2, fmax = monte_carlo_simu_2d(i, func_0, a, b)
    val = len(df1)/i*(b-a)*fmax
    monte_carlo_vals.append(val)
    
    vals = cal_def_int(i//n, func_0, a, b, n)
    vals = np.array(vals)
    random_riemann_vals.append(vals.sum()/i*n)

data_comparison(tt, monte_carlo_vals, random_riemann_vals, title='')

