#Banking app
#Class based
#Withdrawel and Deposit
#Write the transaction to a Python file
#While True:
#input
#classes
#open()
#

class BankStatement:
    last_line = 0

    def getStatus(self, FileName):
        print("Opening file", FileName)
        with open(FileName, "r") as file:
            self.last_line = file.readlines()[-1]
        print(self.last_line)
        return self.last_line

    def UpdateAccount(self, FileName, NewAmount):
        print("Opening for deposit", FileName)
        with open(FileName, "a") as file:
            file.write("\n" + str(NewAmount))




class Bank:

    bdeposit = False
    myChoise = ""

    def bankAction(self):
        try:
            self.myChoise = input("How much do you want to deposit or withdraw ")
            self.myChoise = int(self.myChoise)

        except ValueError:
            print(self.myChoise, "Was not a valid number")

        except ZeroDivisionError:
            print("Zero division")

        except Exception as e:
            print("Exception was caught")
            print(type(e))
            self.myChoise = "unknown"

        if(self.myChoise > 0):
            print("You selected deposit")
            self.bdeposit = True

        elif(self.myChoise < 0 ):
            print("You selected withdrawal")
            self.bdeposit = False

        return self.myChoise



myBank = Bank()
myBankStatement = BankStatement()

newAmount = int(myBank.bankAction())
print(newAmount)

oldAmount = int(myBankStatement.getStatus("bankStatement.txt"))
print(oldAmount)

myBankStatement.UpdateAccount("bankStatement.txt", oldAmount + newAmount)




