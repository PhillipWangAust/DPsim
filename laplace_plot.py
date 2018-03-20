import utils
from pylab import *
from random import shuffle
import matplotlib.pyplot as plt
zero_list = [0]*3000
one_list = [1]*1000
counts = zero_list + one_list
shuffle(counts)
noises = []
epsilon = 0.3
for i in range(4000):
    noises.append(counts[i]+utils.laplace(1/epsilon))

myHist = plt.hist(noises, 10000, normed=True)
plt.show()
