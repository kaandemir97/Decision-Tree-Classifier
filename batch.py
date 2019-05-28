import main_dt as dt
AverageRes = 0
list = []
#Runs main_dt.py (DT classifier training) 0<x<11 times using data hepatitis-<type>-run<x>.dat
#Prints results for each test, and then average accuracy accross all tests
#The helper file was used manually to create the 10 test and training files - mine does not include the leading 0 for single digit test numbers
for i in range(10):
    train = "hepatitis-test-run"+str(i+1)+".dat"
    test = "hepatitis-training-run"+str(i+1)+".dat"
    argv = [train, test]
    average = dt.main(argv)
    list.append(average)
    AverageRes += average
AverageRes = AverageRes/10
print("Accuracies: \n")
for i in range(10):
    print("Run "+str(i+1)+": "+str(list[i]))
print("\n")
print("Average accuracy over 10 runs: "+str(AverageRes)+"\n")
