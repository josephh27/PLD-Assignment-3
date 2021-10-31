
def applesBought():
    myApples = int(input("How many apples do you wish to buy? "))
    return myApples

def orangesBought():
    myOranges = int(input("How many oranges do you wish to buy? "))
    return myOranges

def totalPrice():
    totalCost = myApples*20 + myOranges*25
    return totalCost

def postShopping(myApples, myOranges, myPrice):
    print(f'{myApples}(20) + {myOranges}(25) = {myPrice}')

def thankYou():
    print("Please come back again before we go bankrupt")

myApples = applesBought()
myOranges = orangesBought()
myPrice = totalPrice()
postShopping(myApples, myOranges, myPrice)
thankYou()