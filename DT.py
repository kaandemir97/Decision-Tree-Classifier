from DTNode import Node
from DTNode import LeafNode

class decisionTree:
    def __init__(self, training, test, trainAttr, testAttr, trainClass, testClass):
        self.training = training
        self.test = test
        self.trainAttr = trainAttr
        self.testAttr = testAttr
        self.trainClass = trainClass
        self.testClass = testClass
        #Index position of attribute in instance array
        self.trainDict = {}
        for i in range(len(self.trainAttr)):
            self.trainDict[self.trainAttr[i]] = i+1
        self.baseline, self.baselineProbability = self.majorityClass(self.training)
        return

    #Algorithm identical to one given in brief
    def buildTree(self, instances, attributes):

        if len(instances) == 0:
            label, probability = self.majorityClass(self.training) #Baseline predictor across whole dataset
            return LeafNode(label, probability)
        elif self.purity(instances) == 0: #Case where m = 0 or n = 0
            return LeafNode(instances[0][0], 1) #Same class label and probability
        elif len(attributes) == 0:
            label, probability = self.majorityClass(instances)
            return LeafNode(label, probability) #Predictor of majority class in instances

        else: #Find best attribute
            bestPurity = None
            bestAttribute = None
            bestAttrTrue = None
            bestAttrFalse = None
            for att in attributes:
                AttrTrue = self.partition(instances, "true", self.trainDict[att])
                AttrFalse = self.partition(instances, "false", self.trainDict[att])
                PTrue = len(AttrTrue)/len(instances)
                PFalse = len(AttrFalse)/len(instances)
                weightAvPur = self.weightedAveragePurity(PTrue,PFalse,AttrTrue,AttrFalse)
                if bestPurity == None:
                    bestPurity = weightAvPur
                    bestAttribute = att
                    bestAttrTrue = AttrTrue
                    bestAttrFalse = AttrFalse
                elif weightAvPur < bestPurity:
                    bestPurity = weightAvPur
                    bestAttribute = att
                    bestAttrTrue = AttrTrue
                    bestAttrFalse = AttrFalse
            attributes.remove(bestAttribute)
            left = self.buildTree(bestAttrTrue,attributes)
            right = self.buildTree(bestAttrFalse,attributes)
            return Node(bestAttribute, left, right)

    def weightedAveragePurity(self, prob1, prob2, partition1, partition2):
        sum = 0
        if len(partition1) >0:
            sum = prob1*self.purity(partition1)
        if len(partition2) >0:
            sum += prob2*self.purity(partition2)
        return sum

    #purity of training data
    def purity(self, instances):
        p = 0
        n = 0
        for inst in instances:
            if inst[0] == self.trainClass[0]:
                p+=1
            elif inst[0] == self.trainClass[1]:
                n+=1
        return (p*n)/((p+n)**2)

    #Seperates instances for which the attribute at index is either false or true
    def partition(self, instances, classs, index):
        partition = []
        for inst in instances:
            if inst[index] == classs:
                partition.append(inst)
        return partition
    #Calculates the majority class and probability of a given set of instances
    def majorityClass(self, instances):
        c1 = 0
        c2 = 0
        label = None
        for inst in instances:
            if inst[0] == self.trainClass[0]:
                c1+=1
            else:
                c2+=1
        majorityClass = max(c1,c2)
        if majorityClass == c1:
            label = self.trainClass[0]
        else:
            label = self.trainClass[1]
        probability = majorityClass/len(instances)
        return label, probability
