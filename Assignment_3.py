
def inputMyName():
    myName = input("What is your name? ") #This is where the name goes
    return myName

def inputMyAge():
    inputAge = input("What is your age? ") #This is where the age goes
    return inputAge

def inputMyAddress():
    inputAge = input("What is your address? ") #This is where the address goes
    return inputAge

def personalInfo(myName, myAge, myAddress):
    print(f'Hi, my name is {myName} and I am {myAge} years old. I live in {myAddress}.') #This is where the accumulated information is printed out in a sentence manner

myName = inputMyName()
myAge = inputMyAge()
myAddress = inputMyAddress()
personalInfo(myName, myAge, myAddress)
print("I wish you all the best summoner")
print("I wish one more commit added") #This one is when I just tried to add committing

