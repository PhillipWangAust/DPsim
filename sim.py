from utils import *
size_records = 100
n_runs = 10000
thresholds= [-0.5,0.0,0.5,1,1.5,2,3,5,7,10]
epsilon = 0.1
budget_initial = 30
original_counts = randBinList(size_records)
original_counts = [1]*25 + [0]*75
records = []
total_claims = [0]*len(thresholds)
correct_claims = [0]*len(thresholds)
trials = [0]*len(thresholds)
calculated_counts = []
for i in original_counts:
    records.append(Record(i))

for j,t in enumerate(thresholds):
    for k in range(n_runs):
        budget = budget_initial
        flag_budget = 0
        for r in records:
            for m in range(4):
                if budget >= epsilon:
                    trials[j] += 1
                    count_this = r.NoisyCount(epsilon)
                    budget -= epsilon
                    #print count_this
                    if count_this > t:
                    #  calculated_counts.append(1)
                        total_claims[j] += 1
                        if r.count() == 1:
                            correct_claims[j] += 1
                        break
                else:
                    flag_budget=1
                    break
            if flag_budget:
                break
        #else:
         #   calculated_counts.append(0)

base_confidence = float(sum(original_counts))/float(size_records)
print "Base confidence:  %.2f    Budget: %d    Epsilon: %.2f   No. of runs: %d" %(base_confidence,budget_initial,epsilon,n_runs)
confidences = []
for i in range(len(total_claims)):
    confidences.append(float(correct_claims[i])/float(total_claims[i]))
for i in range(len(total_claims)):
    print "Threshold: %.1f  correct/total: %d/ %d    Confidence: %.2f  CI: %.2f  Trials: %d  Probability: %.2f" %( thresholds[i], correct_claims[i],  total_claims[i], confidences[i],100*((confidences[i]-base_confidence)/(1-base_confidence)), trials[i], float(total_claims[i])/float(trials[i]))
#print calculated_counts



