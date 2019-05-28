from Instance import IN

class treeParse:
    def __init__(self, trainingdata, testdata):

        self.trainDat, self.trainClass, self.attrDat = self.parseData(trainingdata)
        self.testDat, self.testClass, self.tesAttrDat = self.parseData(testdata)

        return

    def parseData(self, data):

        parsedData = []
        classData = []
        attrData = []

        with open(data) as fp:
            for line in fp:
                #Parse class labels
                testline = line.split()
                if len(testline) == 2:
                    classData.append(str(testline[0]))
                    classData.append(str(testline[1]))
                    continue
                #Parse attribute labels
                if str(testline[0]) != classData[0] and str(testline[0]) != classData[1]:
                    for i in range(len(testline)):
                        attrData.append(str(testline[i]))
                    continue
                #Parse data
                else:
                    parsedData.append(testline)
            fp.close()

        return parsedData, classData, attrData

    def getData(self):
        return  self.trainDat, self.trainClass, self.attrDat, self.testDat, self.testClass, self.tesAttrDat
