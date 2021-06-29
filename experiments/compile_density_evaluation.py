#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7

import csv
import numpy as np

TP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
TN = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
FP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
FN = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

with open('../evaluation_result.csv', 'r') as f1, open('../works_content.csv', 'r') as f2:
    f1_reader = csv.reader(f1)
    f2_reader = csv.reader(f2)

    work_list = []
    for work in f1_reader:
        work_list += [work]

    content_list = []
    for content in f2_reader:
        content_list += [content]
    for work in work_list:
        for content in content_list:
            if work[2] == content[0]:
                #print(work)
                #print(content)
                for i in range(0, 40):
                    if work[i+6] == content[1] == '1':
                        TP[i] += 1
                    elif work[i+6] == content[1] == '0':
                        TN[i] += 1
                    elif work[i+6] == '1' and content[1] == '0':
                        FP[i] += 1
                    elif work[i+6] == '0' and content[1] == '1':
                        FN[i] += 1

    print("element\t1-2,2-2,3-2,4-2,5-2,6-2,7-2,8-2,9-2,10-2,1-3,2-3,3-3,4-3,5-3,6-3,7-3,8-3,9-3,10-3,1-4,2-4,3-4,4-4,5-4,6-4,7-4,8-4,9-4,10-4,1-5,2-5,3-5,4-5,5-5,6-5,7-5,8-5,9-5,10-5")
    print("TP\t"+str(TP))
    print("TN\t"+str(TN))
    print("FP\t"+str(FP))
    print("FN\t"+str(FN))
    np_TP = np.array(TP)
    np_TN = np.array(TN)
    np_FP = np.array(FP)
    np_FN = np.array(FN)
    Precision = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    Recall = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    F_measure = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    Precision = np_TP / (np_TP + np_FP)
    Recall = np_TP / (np_TP + np_FN)
    F_measure = (2 * Precision * Recall) / (Precision + Recall)
    print("Precision\t"+str(Precision))
    print("Recall\t"+str(Recall))
    print("F_measure\t"+str(F_measure))
