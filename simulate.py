from utils import *
size_records = 100
n_runs = 5
thresholds= [-0.5,0.0,0.5,1,1.5,2,3,5,7,10]
epsilon = 0.1
original_counts = randBinList(size_records)
original_counts = [1]*593
records = []
total_claims = [0]*len(thresholds)
correct_claims = [0]*len(thresholds)
calculated_counts = []
for i in original_counts:
    records.append(Record(i))

for k in range(n_runs):
    for r in records:
        count_this = r.NoisyCount(epsilon)
        print count_this
        for j,t in enumerate(thresholds):
            if count_this > t:
            #  calculated_counts.append(1)
                total_claims[j] += 1
                if r.count() == 1:
                    correct_claims[j] += 1
        #else:
         #   calculated_counts.append(0)


print "Number of 1's:  %d" %sum(original_counts)
for i in range(len(total_claims)):
    print "Threshold: %.1f  correct/total: %d/ %d    Confidence: %.2f" %( thresholds[i], correct_claims[i],  total_claims[i], float(correct_claims[i])/float(total_claims[i]))
#print calculated_counts



