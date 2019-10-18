import numpy as np
import matplotlib.pyplot as plt
import time

#Graphs primes up to max on a polar system with theta=prime and length=prime

start = time.time()
p = []
max = 100000
for n in range(1, max):
    print(n)
    root = int(np.around(np.sqrt(n)) + 0.5)
    for x in range(2, root):
        if n % x == 0:
            break
    else:
        p.append(n)
end = time.time()
print(p)
print("Time elapsed:", end-start, "seconds")
print(len(p), "prime numbers found between 0 and", max)

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(p, p, c='darkturquoise', s=.1)
ax.axis('off')

plt.show()
fig.savefig('plot.png', dpi=400, facecolor=fig.get_facecolor(), edgecolor='none')