import matplotlib.pyplot as plt
from utils import *
from random import shuffle
import ast
from pylab import *
size_records = 1000
n_runs = 1000
thresholds= [-0.5,-0.25,0.0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,3,5,7,10]
epsilons = [0.1,0.2,0.3]
budget_initial = 20
with open('file','r') as f:
    original_counts = ast.literal_eval(f.read())

file_out = open('budget_20.txt','a')
size_records = len(original_counts)
records = []
calculated_counts = []
for i in original_counts:
    records.append(Record(i))

for epsilon in epsilons:
    total_claims = [0]*len(thresholds)
    correct_claims = [0]*len(thresholds)
    trials = [0]*len(thresholds)
    confidence_improvements = []
    for j,t in enumerate(thresholds):
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
    out_line = "Base confidence:  %.2f    Budget: %d    Epsilon: %.2f   No. of runs: %d" %(base_confidence,budget_initial,epsilon,n_runs)
    print out_line
    file_out.write(out_line+"\n")
    file_out.write("-------------------------------------------------------------------\n")
    confidences = []
    denom = float(budget_initial)/float(epsilon)
    print total_claims
    print correct_claims
    for i in range(len(total_claims)):
        if total_claims[i]:
            confidences.append(float(correct_claims[i])/float(total_claims[i]))
    for i in range(len(total_claims)):
        if total_claims[i]:
            confidence_improvements.append(100*((confidences[i]-base_confidence)/(1-base_confidence)))
            out_line =  "Threshold: %.2f  correct/total: %d/ %d    Confidence: %.2f  CI: %.2f  Trials: %d  Probability: %.5f" %( thresholds[i], correct_claims[i],  total_claims[i], confidences[i],100*((confidences[i]-base_confidence)/(1-base_confidence)), trials[i], float(total_claims[i])/denom)
            print out_line
            file_out.write(out_line+"\n")
    #print calculated_counts
    print confidence_improvements
    plt.plot(thresholds[:len(confidence_improvements)],confidence_improvements)

legends = []
for e in epsilons:
    legends.append('e = %.1f' %e)
plt.legend(legends, loc='upper left')
plt.title('Budget=%d' %budget_initial)
plt.xlabel('Thresholds')
plt.ylabel('Confidence Improvement(%)')
figure_name = 'budget_%d.png' %budget_initial
plt.savefig(figure_name)
#fig = plt.figure()
#fig.savefig('budget_30')
plt.show()
print "Done"
file_out.close()


