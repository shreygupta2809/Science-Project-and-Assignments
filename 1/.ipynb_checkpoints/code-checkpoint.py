import math
import matplotlib.pyplot as plt
import random

"""
This takes long time to run due to number of iteration in the simulations.
If you wish to check the code please reduce number of iterations to 1000. This speeds the result up considerably
but the final graph obtained due to simulation deviates more (not a good fit) from the analytical solution.
"""
random.seed(4)

# Question 1 a


num_sim = 10000

calc_list = []
sim_list = []
for n in range(1, 100):
    ans = 0
    for times in range(num_sim):
        x = 0
        y = 0
        for i in range(1, n + 1):
            x += [-1, 1][random.randint(0, 1)]
            y += [-1, 1][random.randint(0, 1)]
        if x == y:
            ans = ans + 1
    sim = ans / num_sim
    calc = math.factorial(2 * n) / ((math.factorial(n) ** 2) * (2 ** (2 * n)))
    sim_list.append(sim)
    calc_list.append(calc)

plt.figure()
plt.subplot(221)
plt.title("Probability of Meeting vs N")
plt.xlabel("N")
plt.ylabel("Probability")
plt.plot(calc_list, label="Analytical")
plt.plot(sim_list, label="Simulation")
plt.legend()


# Question 1 b


num_sim = 10000

calc_list = []
sim_list = []
for n in range(1, 100):
    ans = 0
    for times in range(num_sim):
        x = 0
        for i in range(1, n + 1):
            x += [-1, 1][random.randint(0, 1)]
        if x == 0:
            ans = ans + 1
    sim = ans / num_sim
    if n % 2 == 0:
        calc = math.factorial(n) / ((math.factorial(n / 2) ** 2) * (2 ** (n)))
    else:
        calc = 0
    sim_list.append(sim)
    calc_list.append(calc)

plt.subplot(222)
plt.title("Probability of Reaching Origin vs N")
plt.xlabel("N")
plt.ylabel("Probability")
plt.plot(calc_list, label="Analytical")
plt.plot(sim_list, label="Simulation")
plt.legend()


# Question 1 c


num_sim = 10000

calc_list = []
sim_list = []
for n in range(1, 200):
    ans = 0
    for times in range(num_sim):
        x = 0
        for i in range(1, n + 1):
            x += [-1, 1][random.randint(0, 1)]
        ans = ans + x
    sim = ans / num_sim    
    calc = 0
    sim_list.append(sim)
    calc_list.append(calc)

plt.subplot(223)
plt.title("Mean Displacement vs N")
plt.xlabel("N")
plt.ylabel("Mean Displacement")
plt.plot(calc_list, label="Analytical")
plt.plot(sim_list, label="Simulation")
plt.legend()


# Question 1 d


num_sim = 10000

calc_list = []
sim_list = []
for n in range(1, 100):
    ans = 0
    for times in range(num_sim):
        x = 0
        for i in range(1, n + 1):
            x += [-1, 1][random.randint(0, 1)]
        ans = ans + (x ** 2)
    sim = ans / num_sim    
    calc = n
    sim_list.append(sim)
    calc_list.append(calc)

plt.subplot(224)
plt.title("Mean Square Displacement vs N")
plt.xlabel("N")
plt.ylabel("Mean Square Displacement")
plt.plot(calc_list, label="Analytical")
plt.plot(sim_list, label="Simulation")
plt.legend()
plt.show()