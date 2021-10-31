
def inputMyName():
    myName = input("What is your name? ")
    return myName

def inputMyAge():
    inputAge = input("What is your age? ")
    return inputAge

def inputMyAddress():
    inputAge = input("What is your address? ")
    return inputAge

def personalInfo(myName, myAge, myAddress):
    print(f'Hi, my name is {myName} and I am {myAge} years old. I live in {myAddress}.')

myName = inputMyName()
myAge = inputMyAge()
myAddress = inputMyAddress()
personalInfo(myName, myAge, myAddress)
print("I wish you all the best summoner")
print("I wish one more commit added")

