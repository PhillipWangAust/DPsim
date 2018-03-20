import random
import math

randBinList = lambda n: [random.randint(0,1) for b in range(1,n+1)]

def laplace(stddev):
    uniform = random.random() - 0.5
    return stddev * math.copysign(1,uniform) * math.log(1 - 2.0 * math.fabs(uniform))

class Record(object):
    def __init__(self,count):
        self.original_count = count


    def count(self):
        return self.original_count

    def NoisyCount(self,epsilon):
        if epsilon < 0.0:
            print "negative epsilon not permitted"

        return self.count() + laplace(1.0/epsilon)
