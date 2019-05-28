COMP 307 Assignment 1 Part 2
Code can be executed in terminal (linux/KDE) by invoking
$ python main_dt.py <training.dat> <test.dat>
Batch for 10 trials
$ python batch.py

main_dt.py outputs a csv file with results named
"classifierDT_results_"+(<training.dat>)+".csv"
batch.py outputs a series of csv files containing results named
"classifierDT_results_"+(<training-testnum.dat>)+".csv"

Sample output csv for main_dt.py looks like this:

Prediction: live True: live Correct: True
Prediction: die True: live Correct: False
Prediction: live True: live Correct: True
.
.
.
Prediction: live True: live Correct: True
Prediction: live True: live Correct: True
Prediction: die True: live Correct: False
Overall Accuracy: 74.07407407407408%

Sample output of some iteration of the batch.py csv looks like this:

Prediction: live True: live Correct: True
Prediction: die True: live Correct: False
Prediction: live True: live Correct: True
.
.
.
Prediction: live True: live Correct: True
Prediction: live True: live Correct: True
Prediction: live True: live Correct: True
Overall Accuracy: 79.0%
