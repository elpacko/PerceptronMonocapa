import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def column(matrix, i):
    return [row[i] for row in matrix]


W = [np.random.rand() * 10, np.random.rand() * 10, np.random.rand() * 10]
tableAND = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
tableOR = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
table = tableOR
hasError = True
epoch = 0
while hasError and epoch < 500:
    epoch = epoch + 1
    print ("epoch#" + str(epoch))
    hasError = False
    for i in range(len(table)):
        print ("doing sample:" + str(i))
        wsum = W[0] + W[1] * table[i][0] + W[2] * table[i][1]
        yn = 1 if wsum >= 0 else 0
        err = table[i][2] - yn
        err = table[i][2] - yn
        if err != 0:
            hasError = True
            W = [W[0] + err, W[1] + err * table[i][0], W[2] + err * table[i][0]]
print("Done")
print(W)

# fig, ax = plt.subplots()
# ax.plot(W)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#
# # fig.savefig("test.png")
# plt.show()
