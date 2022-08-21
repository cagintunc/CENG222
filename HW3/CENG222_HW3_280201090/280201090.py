import numpy as np
from matplotlib import pyplot as plt
# 280201090
# Çağın Tunç

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###
sum = 0
num = 0
mean = 0
variance = 0
N = 50000
for i in range(N):
    # first create a uniform random variable.
    u = np.random.rand()
    U.append(u)
    # by using the inverse transformation:
    # F(x) = u, and then solve for x.
    x = np.sqrt(u)
    Xa.append(x)
    num += 1
    sum += x
    # average
    average = np.mean(Xa)
    av_Xa.append(average)
    # variance
    variance = np.std(Xa)**2
    vr_Xa.append(variance)

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###
plt.figure()
plt.title("Averages for part a: ")
plt.plot(av_Xa, color="darkred")
plt.figure()
plt.title("Variances for part a: ")
plt.plot(vr_Xa, color="darkblue")

# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
### YOUR CODE HERE ###
def f(x):
    fx = 0
    if 0 <= x <= 1:
        fx = 2*x
    return fx

c = 2
a = 0
b = 1
i = 0
while i < 50000:
    u = np.random.rand()
    v =np.random.rand()
    x = (b - a) * u + a
    y = c * v
    if y <= f(x):
        Xb.append(x)
        # average
        average = np.mean(Xb)
        av_Xb.append(average)
        # variance
        variance = np.std(Xb) ** 2
        vr_Xb.append(variance)
        i += 1

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###
plt.figure()
plt.title("Averages for part b: ")
plt.plot(av_Xb, color="darkred")
plt.figure()
plt.title("Variances for part b: ")
plt.plot(vr_Xb, color="darkblue")
plt.show()