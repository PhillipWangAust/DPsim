from utils import *
from random import shuffle
import ast
size_records = 1000
n_runs = 1000
thresholds= [-200,-0.5,-0.25,0.0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,3,5,7,10]
epsilon = 0.1
budget_initial = 20
original_counts = randBinList(size_records)
original_counts = [1]*250 + [0]*750
with open('file','r') as f:
    original_counts = ast.literal_eval(f.read())
#shuffle(original_counts)
size_records = len(original_counts)
records = []
total_claims = [0]*len(thresholds)
correct_claims = [0]*len(thresholds)
trials = [0]*len(thresholds)
calculated_counts = []
counts = [0]*size_records
counts_t = [0]*len(thresholds)
for i in original_counts:
    records.append(Record(i))

confidence_improvements = []
for j,t in enumerate(thresholds):
    confidence_improvement = []
    counts = [0]*size_records
    q_pos = [0]*size_records
    for k in range(n_runs):
        budget = budget_initial
        flag_budget = 0
        for c_i,r in enumerate(records):
            if budget >= epsilon:
                q_pos[c_i] += 1
                trials[j] += 1
                count_this = r.NoisyCount(epsilon)
                counts[c_i] += count_this
                budget -= epsilon
                #print count_this
            else:
                flag_budget=1
                break
   # trials[j] = trials[j]/n_runs

    for c in range(len(counts)):
        if q_pos[c]:
            counts[c] = float(counts[c])/float(q_pos[c])
    for c in range(len(counts)):
        if counts[c] > t and counts[c]>0:
            total_claims[j] += 1
            if records[c].count() == 1:
                correct_claims[j] += 1

        #else:
         #   calculated_counts.append(0)

base_confidence = float(sum(original_counts))/float(size_records)
print "Base confidence:  %.2f    Budget: %d    Epsilon: %.2f   No. of runs: %d" %(base_confidence,budget_initial,epsilon,n_runs)
confidences = []
denom = float(budget_initial)/float(epsilon)
print total_claims
print correct_claims
for i in range(len(total_claims)):
    if total_claims[i]:
        confidences.append(float(correct_claims[i])/float(total_claims[i]))
for i in range(len(total_claims)):
    if total_claims[i]:
        confidence_improvement.append(100*((confidences[i]-base_confidence)/(1-base_confidence)))
        print "Threshold: %.2f  correct/total: %d/ %d    Confidence: %.2f  CI: %.2f  Trials: %d  Probability: %.5f" %( thresholds[i], correct_claims[i],  total_claims[i], confidences[i],100*((confidences[i]-base_confidence)/(1-base_confidence)), trials[i], float(total_claims[i])/denom)
#print calculated_counts
print confidence_improvement


