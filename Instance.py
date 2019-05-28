class IN:
    def __init__(self, classs, *args):
        self.classs = classs
        self.attributes = []
        for i in args:
            self.attributes.append(i)
        return
