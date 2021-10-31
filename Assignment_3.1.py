
def applesBought():
    myApples = int(input("How many apples do you wish to buy? ")) #This is where the program gets informed on how many apples will be bought
    return myApples

def orangesBought():
    myOranges = int(input("How many oranges do you wish to buy? ")) #This is the information on how many oranges will be bought by the user
    return myOranges

def totalPrice():
    totalCost = myApples*20 + myOranges*25         #This function will calculate the total cost of the apples and oranges that the user tried to buy
    return totalCost

def postShopping(myApples, myOranges, myPrice):
    print(f'{myApples}(20) + {myOranges}(25) = {myPrice}')    #This is the part where we show visibility of the price calculations so that you are assured we didn't pickpocket your money

def thankYou():
    print("Please come back again before we go bankrupt")    #A reminder for the user

myApples = applesBought()
myOranges = orangesBought()
myPrice = totalPrice()
postShopping(myApples, myOranges, myPrice)
thankYou()