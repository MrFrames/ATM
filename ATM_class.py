import hashlib

class ATM():
    def __init__(self,balance= 0,
                 period= 3,
                 interest= 2,
                 name= "Guy",
                 pin = "0000",
                 pin_salt = "0"):
        self.name = name
        self.__pinSalt = pin_salt
        self.__pin_hash = self.hashPin(pin)
        self.balance = balance
        self.period = period
        self.interest = interest
        self.history = [(balance,balance,True)]
        self.compound_data = []
        
    def populateData(self):
        # Produces a list of monthly balance data.
        factor = 1 + (self.interest/1200)
        new_data = []
        for i in range (0,self.period +1):
            print (self.balance)
            print (type(self.balance))
            print (type(factor**i))
            new_data.append(self.balance*factor**i)

        self.compound_data = new_data
        return self.compound_data

    def set_period(self,period):
        self.period = period
        self.populateData()

    def set_interest(self,interest):
        self.interest = interest
        self.populateData()

    def get_balance(self):
        return self.balance

    def get_period(self):
        return self.period

    def get_interest(self):
        return self.interest
    
    def get_history(self):
        return self.history
    
    def get_compoundData(self):
        return self.compound_data

    def hashPin(self,pin):
        # Generates a hash using sha256 and a UUID salt defined at account creation
        hashPin_object = hashlib.sha256()
        hashPin_object.update((self.__pinSalt + pin).encode())
        hashPin = hashPin_object.digest()
        return hashPin

    def login(self, name="guy", pin = "0000" ):
        # Checks if the hash of the pin + salt  and the name entered match
        # those storred inside the class instance.
        nameIn = name
        pinHash = self.hashPin(pin)
        if (pinHash == self.__pin_hash and nameIn == self.name):
            return True
        else:
            return False

    def change(self,amount,sign):
        if sign == -1 and self.balance - amount < 0:
            self.history.append((self.balance,amount*sign,False))
            return False
        else:
            self.balance = self.balance + amount*sign
            self.history.append((self.balance,amount*sign,True))
            return True

    def withdraw(self,amount):
        self.change(amount,-1)
        print (amount)

    def deposit (self,amount):
        self.change(amount,1)

