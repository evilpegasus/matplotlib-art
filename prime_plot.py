import numpy as np
import matplotlib.pyplot as plt
 
p = []
for n in range(1, 1000):
    print(n)
    root = int(np.around(np.sqrt(n)) + 0.5)
    for x in range(2, root):
        if n % x == 0:
            break
    else:
        p.append(n)
print(p)


fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(p, p, c='darkturquoise', s=1)

ax.axis('off')
plt.show()
plt.savefig('graph1.png', facecolor='black')
