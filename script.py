import codecademylib
from matplotlib import pyplot as plt

x = range(1999, 2010)
y1 = [109, 102, 102, 98, 85, 95, 96, 98, 123, 94, 102]
y2 = [2, 2, 2, 3, 1, 1, 2, 3, 4, 1, 4]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, marker = 's', color = 'red')
ax2.plot(x, y2, marker = 'o', color = 'black')
ax1.set_title('Number of people who drowned by falling in a pool\n Corrolates with \n Number of films Nicholas Cage has been in')
ax1.set_xlabel('Years')
ax1.set_ylabel('Swimming Pool Drownings')
ax2.set_ylabel('Nicholas Cage Films')
ax1.set_xticks(x)
ax1.set_yticks([80, 100, 120, 140])
ax2.set_yticks([0, 2, 4, 6])
ax1.legend(['Swimming pool drownings'], loc = 2)
ax2.legend(['Nicholas Cage'], loc = 0)

plt.show()