from DTParser import treeParse
from DT import decisionTree
from Classifier import Classify
import sys

#Code is straightforward, most of the work is done in DT.py and Classifier.py
#Main basically sets up various stages of the process, batch calls main 10 times and provides argv of the specific run training and test sets
def main(argv):
    if len(argv)!=2:
        print("Incorrect function call: main_dt.py <training-data.txt> <test-data.txt>")

    trainingdata = str(argv[0])
    testdata = str(argv[1])

    TP = treeParse(trainingdata, testdata)
    DT = decisionTree(TP.trainDat,TP.testDat, TP.attrDat, TP.tesAttrDat, TP.trainClass, TP.testClass)
    instances = TP.trainDat[:]
    attributes = TP.attrDat[:]

    ClassifierRoot = DT.buildTree(instances,attributes)
    ClassifierRoot.report("")

    testInstances = TP.testDat[:]
    classify = Classify(ClassifierRoot, testInstances, DT.trainDict)
    classify.run()
    classify.printres(trainingdata)
    print("Baseline statistics: "+str(DT.baseline)+" "+str(DT.baselineProbability)+"\n")
    classify.predictedBaseline(TP.testClass)

    return classify.average

def printres(self, root):

    return

if __name__ == "__main__":
    main(sys.argv[1:])
