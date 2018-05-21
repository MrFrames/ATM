from ATM_class import ATM
from Accounts_class import accounts
from ATM_logic import*
import uuid
import hashlib
import pickle

#Below tests the ATM class

print ("ATM tests:")

test_pin = "0000"
testName = "Ben Storey"
testPinSalt = uuid.uuid4().hex
testBalance = 200
testPeriod = 24
testInterest = 3
expected_last_interest = 212

def test_assertTrue():
    assert True

def test_canInit():
    print ("Testing input init...")
    ben = ATM(balance=testBalance,
              period = testPeriod,
              interest = testInterest,
              name = testName,
              pin = test_pin,
              pin_salt = testPinSalt)
    print ("...Name: " + ben.name)
    print ("...Balance: £" + str(ben.balance))
    print ("...Period: {} months.".format(ben.period*12))
    print ("...Interest: " + str(ben.interest) + "%")
    print ("OK")

ben = ATM(balance=testBalance,
          period = testPeriod,
          interest = testInterest,
          name = testName,
          pin = test_pin,
          pin_salt = testPinSalt)

def test_initHistCompMonthInt():
    print ("Testing history, compound_data & monthly_interest init...")
    assert (ben.history[0] == (ben.balance,ben.balance,True))
    assert (ben.compound_data==[])
    print ("OK")

def test_populateData():
    print("testing interest calculation...")
    print(ben.populateData())
    assert (int(ben.compound_data[-1]) == expected_last_interest)
    print("Ok")

test2Period = 36
test2Interest = 4
expected_last_interest2 = 225

def test_sets():
    print("Testing set functions...")
    ben.set_interest(test2Interest)
    assert (ben.interest == test2Interest)
    ben.set_period(test2Period)
    assert (ben.period == test2Period)
    print("OK")

def test_gets():
    print("Testing get functions...")
    assert (ben.get_balance() == testBalance)
    assert (ben.get_interest() == test2Interest)
    assert (ben.get_period() ==  test2Period)
    assert (ben.get_history()[0] == (testBalance,testBalance,True))
    assert (int(ben.get_compoundData()[-1]) == expected_last_interest2)
    print ("OK")

print (ben.hashPin("0000"))

def test_login():
    print ("Testing login function...")
    assert (ben.login(pin = test_pin, name = testName) == True)
    print ("OK")

withdrawlHuge = 220
withdralOk = 40

def test_negativeChanges():
    print ("Testing withdrawl fail...")
    ben.change(withdrawlHuge,-1)
    assert (ben.history[-1] == (testBalance,-withdrawlHuge,False))
    print ("OK")
    print ("Testing withdrawl success...")
    ben.change(withdralOk,-1)
    assert (ben.history[-1] == (testBalance-withdralOk,-withdralOk,True))
    print ("OK")

depositAmount = 50

def test_positiveChange():
    print ("Testing deposit...")
    ben.change(depositAmount,1)
    assert (ben.history[-1] == (testBalance-withdralOk+depositAmount,depositAmount,True))
    print ("OK")
    print("Account history:")
    for transaction in ben.history:
        print (transaction)

def test_accountsInit():
    print ("Testing accounts init...")
    acc = accounts()
    assert (acc.highestID == 0 and acc.accountDict == {})
    print("OK")

#Below test account data class

acc = accounts()

def test_createAccountInstance():
    print("Testing add account to dict...")
    acc.add_account(ben)
    assert acc.accountDict.get(testName) == 1
    print ("OK")

def test_getName():
    print ("Testing get id...")
    id = acc.get_id(ben.name)
    assert id == 1
    print ("OK")

def test_saveToFile():
    print("Testing save to file function...")
    acc.saveToFile(ben)
    assert (pickle.load(open(str(acc.get_id(testName)),"rb")).history ==
            ben.history)
    print ("OK")

#Below test ATM interface logic

def test_newAccount():
    print ("Testing add new account to file...")
    newAccount(ben)
    print("OK")

def test_getAccountData():
    print ("Testing account data retrieval from file...")
    data = getAccounts()
    assert data.accountDict.get(testName) == 1
    print("Above 2 tests OK.")

def test_canInt():
    print("Testing canINT...")
    assert canInt("1234") == True
    assert canInt("13n5") == False
    print("OK")

def test_isName():
    print("Testing no Numbers...")
    assert isName("Terry Briggs") == True
    assert isName("T3rry 8r1ggs") == False
    print("OK")

def test_getID():
    print("Testing getID...")
    assert getID("Ben Storey") == 1
    print("OK")

def test_getAcc():
    print (str(getAcc(1).history))