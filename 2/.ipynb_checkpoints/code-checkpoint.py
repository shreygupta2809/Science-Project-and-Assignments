import math
import matplotlib.pyplot as plt
import random

random.seed(4)

num_sim = 100

pi_list = []
for n in range(1, 400):
    fans = 0
    for times in range(num_sim):
        ans = 0
        for i in range(1, n + 1):
            x = random.random()
            y = random.random()
            if (x ** 2) + (y ** 2) <= 1:
                ans = ans + 1
        fans += (4 * ans) / n
    pi = fans / num_sim 
    pi_list.append(pi)

plt.title("Pi vs N")
plt.xlabel("N")
plt.ylabel("Value of Pi")
plt.plot(pi_list)
plt.show()