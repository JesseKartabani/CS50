from cs50 import get_float

# Prompt user for their change owed
while True:
    dollars = get_float("Change owed: ")
# Makes sure the user inputs a vaild number
    if dollars >= 0:
        break

# Finds out the total cents
cents = round(dollars * 100)
# initializes coins to 0
coins = 0

# Removes cents and counts coins
while cents >= 25:
    cents -= 25
    coins += 1
    
while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1

# Total number of coins owed
print(coins)