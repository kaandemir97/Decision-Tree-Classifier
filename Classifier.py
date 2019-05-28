class Classify:

    def __init__(self, root, testInstances, dict):
        self.root = root
        self.test = testInstances
        self.dict = dict
        self.classifiers = []
        self.average = 0
        return

    #Basically searches the tree and appends final classifier object to result list
    def run(self):
        for inst in self.test:
            label = self.findLeaf(self.root, inst)
            self.classifiers.append(ClassInst(label, inst[0]))
        return

    #Recursive descent to find matching leaf node
    def findLeaf(self, root, inst):
        if root.isLeafNode():
            return root.att
        attr = root.att
        index = self.dict[attr]
        observedVal = inst[index]
        if observedVal == 'true': #This caused a nasty bug as i was comparing to boolean
            return self.findLeaf(root.left, inst)
        else:
            return self.findLeaf(root.right, inst)
        return


    #Prints result of tree to a csv file in root folder
    def printres(self,trainingdata):
        accuracy = 0
        filename = "classifierDT_results_"+str(trainingdata)+".csv"
        with open(filename, "w") as fp:
            for inst in self.classifiers:
                fp.write("Prediction: "+inst.prediction+" True: "+inst.true+" Correct: "+str(inst.correct)+"\n")
                if inst.correct:
                    accuracy += 1
            accuracy = accuracy/len(self.classifiers)*100
            self.average = accuracy
            fp.write("Overall Accuracy: "+str(accuracy)+"%")
            fp.close()
        return


    #Calculates baseline out of results list
    def predictedBaseline(self, labels):
        c1 = 0
        c2 = 0
        for cls in self.classifiers:
            if cls.prediction == labels[0]:
                c1 +=1
            else:
                c2 +=1
        maxim = max(c1,c2)
        label = None
        if maxim == c1:
            label = labels[0]
        else:
            label = labels[1]
        prob = maxim/len(self.classifiers)
        print("Baseline prediction: "+str(label)+" "+str(prob)+"\n")

        return

class ClassInst:

    def __init__(self, prediction, true):
        self.prediction = prediction
        self.true = str(true)
        self.correct = prediction==true
        return
