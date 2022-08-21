import numpy as np
import matplotlib.pyplot as plt
import random
#Student: Çağın Tunç
#ID: 280201090

# for experiments 1, 2, 3
def create_standard_U(x):
    return np.random.uniform(0.0, 1.0, x)

def uniform_distribution_EXP5(x):
    samples = []
    for sample in range(x):
        a_b = create_standard_U(2)
        if a_b[1] > a_b[0]:
            x = np.random.uniform(a_b[0], a_b[1])
            samples.append((x - a_b[0])/(a_b[1] - a_b[0]))
        else:
            x = np.random.uniform(a_b[1], a_b[0])
            samples.append((x - a_b[1])/(a_b[0] - a_b[1]))
    return samples


def normal_prob_density_F(x, m, q):
    density = (1/(q*(((np.pi * 2))**0.5))) * np.exp(-0.5 * ((x - m) / q) ** 2)
    return density

def get_std(array, mean):
    upper_part = 0.0
    for i in array:
        upper_part += (i - mean) ** 2
    return (upper_part/(len(array) - 1)) ** 0.5

# for just experiment 4
def create_U(x):
    samples = []
    previous = 0.0
    total_sum = 0
    for i in range(x):
        if previous < 99:
            previous = random.choice(range(0, 201))
            samples.append(previous)
        else:
            previous = random.choice(range(98, 103))
            samples.append(previous)
        total_sum += previous
    return samples, total_sum/float(x)

# for experiment 1, 2, 3
def first_parts(flag):
    data = []
    theoretical_mean = None
    std_sample = None
    size = 0
    print()
    for i in range(200000):
        if flag == 1:
            sample = create_standard_U(2)
            data.append(sample[0] + sample[1])
            theoretical_mean = 2 * ((0.0 + 1.0) / 2)
            size = 2
        elif flag == 2:
            sample = create_standard_U(4)
            data.append(sample[0] + sample[1] + sample[2] + sample[3])
            theoretical_mean = 4 * ((0.0 + 1.0) / 2)
            size = 4
        else:
            sample = create_standard_U(50)
            sum = 0.0
            for j in sample:
                sum += j
            data.append(sum)
            theoretical_mean = 50 * (0.0 + 1.0) / 2
            size = 50

    std = np.std(data)
    mu = np.mean(data)
    print("For Example {}:\n E[X] = {}\n"
          " Variance: {}\n"
          " Standard Deviation: {}".format(flag, theoretical_mean, std ** 2, std))
    plt.hist(data, density=True, bins=100, label="Histogram")
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    pdf = normal_prob_density_F(x, mu, std)
    plt.title(f"For experiment {flag}:")
    plt.plot(x, pdf, linewidth=1, label="Normal distribution", color="red")
    plt.legend()
    plt.show()

# for experiment 4 and 5
def second_parts(flag):
    data = []
    mean = 0.0
    for i in range(200000):
        if flag == 4:
            U = create_U(50)
            mean += (50 * U[1])
            sum = 0.0
            for j in U[0]:
                sum += j
            data.append(sum)
        else:
            sample = uniform_distribution_EXP5(50)
            sum = 0.0
            for j in sample:
                sum += j
            data.append(sum)
            mean += sum
    mean_total = mean / 200000
    print()
    print("For Example {}:".format(flag))
    print(" Estimated E[X] of Sample: ", mean_total)
    std = get_std(data, mean_total)
    print(" Estimated Standard Deviation of Sample: ", std)
    print(" Estimated Var[X] of Sample: ", std ** 2)
    plt.hist(data, density=True, bins=100, label="Histogram")
    plt.title(f"For experiment {flag}: ")
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    pdf = normal_prob_density_F(x, mean_total, std)
    plt.plot(x, pdf, linewidth=1, label="Normal distribution", color="red")
    plt.legend()
    plt.show()


first_parts(1)
first_parts(2)
first_parts(3)
second_parts(4)
second_parts(5)


