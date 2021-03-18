# Coins: Amount of cents that we outputted into the least amount of coins
# Dollars: Amount of dollars that we output into least amount of bills
# Hundred, Fifty, Twenty, Ten, Five, One

# Ask the User for an amount of dollars
money = int(input("Enter a number of dollars: "))

hundred = 0
fifty = 0
twenty = 0
ten = 0 
five = 0 
one = 0

if(money >= 100):
  hundred = money // 100
  money = money % 100
if(money >= 50):
  fifty = money // 50
  money = money % 50
if(money >= 20):
  twenty = money // 20
  money = money % 20
if(money >= 10):
  ten = money // 10
  money = money % 10
if(money >= 5):
  five = money // 5
  money = five % 5
if(money >= 1):
  one = money // 1
  money = one % 1

print("Hundreds: " + str(hundred))
print("Fifties: " + str(fifty))
print("Twenties: " + str(twenty))
print("Tens: " + str(ten))
print("Fives: " + str(five))
print("Ones: " + str(one))