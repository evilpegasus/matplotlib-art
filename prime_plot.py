import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
p = []
max = 10000
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
c = ax.scatter(p, p, c='darkturquoise', s=1)

ax.axis('off')
plt.show()
#plt.savefig('graph1.png', facecolor='black')