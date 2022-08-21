from matplotlib import pyplot as plt
import random

# function for our experiment.
# It has a parameter flag which show us which question we are dealing with.
def do_experiments(flag):
    results = []
    dice_number = 5
    N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    for k in N:
        match = 0
        result = None
        experiment_number = 0
        for n in range(k):
            experiment_number = n
            for i in range(dice_number):
                # if it is not the first question then we have to consider even dice
                even_index = random.choice(range(dice_number))
                if flag != 1:
                    if i == even_index:
                        current_dice = random.choice([2, 4, 6])
                    # if it is a second question, there's one known even dice, but others can also be even.
                    elif flag == 2:
                        current_dice = random.choice([1, 2, 3, 4, 5, 6])
                        if current_dice == 3:
                            match += 1
                            break
                    # if it is a third question, there's only one even dice; so for the remaining,
                    # sample space is just odd numbers.
                    elif flag == 3:
                        current_dice = random.choice([1, 3, 5])
                        if current_dice == 3:
                            match += 1
                            break
                # if it is a first question, we don't need to consider even dice.
                else:
                    current_dice = random.choice([1, 2, 3, 4, 5, 6])
                    if current_dice == 3:
                        match += 1
                        break
            result = match / float(n+1)
        print('Result from {} repeated experiment is {:.4f}%'.format(experiment_number+1, result * 100))
        results.append(result)

    print()
    theo = [theories[flag - 1] for i in range(len(N))]
    plt.plot(N, results, color="darkred")
    plt.plot(N, theo, color="darkblue")
    plt.title("For the question {}\nTheoretical result(Blue Line): {:.4f}".format(flag, theories[flag - 1]))
    plt.xlim(min(N), max(N))
    plt.xscale('log')
    plt.show()


# for theoretical calculation
theories = []
# p 1
# The probability that at least one dice is 3.
complement_1 = (5 / 6.0) * (5 / 6.0) * (5 / 6.0) * (5 / 6.0) * (5 / 6.0)
theoric_result_1 = 1 - complement_1
print("Theoric p1: ", theoric_result_1)
theories.append(theoric_result_1)
# p 2
# The probability that at least one dice is 3 given one of the dice is even.
complement_2 = (5 / 6.0) * (5 / 6.0) * (5 / 6.0) * (5 / 6.0) * 1
theoric_result_2 = 1 - complement_2
print("Theoric p2: ", theoric_result_2)
theories.append(theoric_result_2)
# p 3
# The probability that at least one dice is 3 given only one of the dice is even.
complement_3 = (2 / 3.0) * (2 / 3.0) * (2 / 3.0) * (2 / 3.0) * 1
theoric_result_3 = 1 - complement_3
print("Theoric p3: ", theoric_result_3)
theories.append(theoric_result_3)
print()
do_experiments(1)
do_experiments(2)
do_experiments(3)