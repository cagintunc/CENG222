import numpy as np
import matplotlib.pyplot as plt

def f(x, theta):
    return (2*(theta**2))/(x**3)

def get_sample_mean(X):
    n = 0
    sum = 0
    for i in X:
        sum += i
        n += 1
    return sum/n

def get_std(X, m):
    sum = 0
    n = 0
    for i in X:
        n += 1
        sum += (i - m)**2
    return (sum/(n-1))**0.5

def experiment_simulation(P, N):
    thetas_MoM = []
    thetas_MLE = []
    # sill
    for i in range(100000):
        samples = []
        indices = np.random.randint(low=0, high=len(P)-1, size=N)
        for j in indices:
            samples.append(P[j])
        thetas_MoM.append(MoM(samples))
        thetas_MLE.append(MLE(samples))
    mean_mom = get_sample_mean(thetas_MoM)
    mean_mle = get_sample_mean(thetas_MLE)
    print(f"For N = {N}:")
    print("MoM estimate mean: %.3f\tMoM estimate std: %.3f"%(mean_mom, get_std(thetas_MoM, mean_mom)))
    print("MLE estimate mean: %.3f\tMLE estimate std: %.3f\n"%(mean_mle, get_std(thetas_MLE, mean_mle)))
    plt.hist(thetas_MoM, color="blue", bins = np.linspace(0,4.8,100), density=True,
             alpha=0.4, label=f"MoM estimate histogram for N = {N}")
    plt.hist(thetas_MLE, color="orange", bins = np.linspace(0,4.8,100), density=True,
             alpha=0.4, label=f"MLE estimate histogram for N = {N}")
    plt.legend()
    plt.show()


def MoM(X):
    # For first moment: M_1 = m_1 and M_1 = E[X]
    # As we know E[X] is integration of x*f(x) over 0 to 1
    # Since we reach an equation which depends on theta we don't look the other moments
    # Then leave the estimated theta alone in the equation
    s_mean = np.mean(X)
    estimated_theta = s_mean/2
    return estimated_theta

def MLE(X):
    # trying to maximize the likelihood
    # since theta <= Xi for i = 1, 2, 3, 4
    estimated_theta = min(X)
    return estimated_theta

# Part a)
# X is a sample set
X = [0.3, 0.6, 0.8, 0.9]
print("MoM estimate for the sample is %.2f"%(MoM(X)))
print("MLE estimate for the sample is %.2f\n"%(MLE(X)))

# Part b)
P = []
N = 0
theta = 2.4
while N < 10000000:
    u = np.random.uniform(0, 1)
    if u != 0:
        x = theta/((u)**0.5)
        if x >= theta:
            P.append(x)
            N += 1

# Part C)
plt.hist(P, density=True, bins = np.linspace(theta,20,100), label="Histogram")
xmin, xmax = theta, 20
x = np.linspace(xmin, xmax)
pdf = f(x, theta)
plt.plot(x, pdf, linewidth=1, color="red", label="PDF")
plt.legend()
plt.show()

M = [1,2,3,4,5,10,50,100,500,1000]
for i in M:
    experiment_simulation(P, i)