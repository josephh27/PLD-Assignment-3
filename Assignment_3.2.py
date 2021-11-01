def askApplePrice():
    applePrice = float(input("What is the price of an apple? ")) #This is where the programs asks the price of the apple
    return applePrice

def askMoneyOfUser():
    userMoney = float(input("How much money do you possess? ")) #This is where the programs asks how much money do you have with you
    return userMoney

def affordableApple():
    apples = money//appleS    #This is the computation of how many apples can you buy with your apple using division excluding the remainder
    return apples

def moneyChange():         
    change = money%appleS    #Computation where your change will be computed via getting the remainder
    return change

def output(applePara, yourChangePara):
    print(f'You can buy {applePara} apple(s) and your change is {yourChangePara} PHP.')     #Summary of how many apples can you buy and the duly change


appleS = askApplePrice()
money = askMoneyOfUser()
yourChange = moneyChange()
apple1 = format(affordableApple(), '.2f')
output(apple1, yourChange)