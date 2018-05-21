import pickle

class accounts():
    def __init__(self):
        self.accountDict = {}
        self.highestID = 0

    def add_account (self, ATM_object):
        print (ATM_object.name)
        if ATM_object.name in self.accountDict.keys():
            print("Account Name already taken.")
        else:
            self.highestID += 1
            self.accountDict[ATM_object.name] = self.highestID
            pickle.dump(ATM_object, open(str(self.highestID), "wb"))
        print (self.accountDict)

    def get_id(self,name):
        return self.accountDict.get(name)

    def saveToFile(self, ATM_object):
        id = self.accountDict.get(ATM_object.name)
        pickle.dump(ATM_object, open(str(id),"wb"))

