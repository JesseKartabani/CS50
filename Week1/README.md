# CS50 Week 1

https://cs50.harvard.edu/x/2021/weeks/1/

# Hello.c

Prompts the user for their name via command line and outputs Hello (name).

# Population.c

Determines how many years it takes for a population to reach a particular size by prompting the user for a starting population size and the ending population size, then calculates the integer using the formula below.

Say we have a population of n llamas. Each year, n/3 new llamas are born, and n/4 llamas pass away. 

If we were to start with n = 1000 llamas, at the end of the year, we would have 1000 / 3 = 333.33 new llamas. We can’t have a decimal portion of a llama, though, so we’ll truncate the decimal to get 333 new llamas born. 1000 / 4 = 250 llamas will pass away, so we’ll end up with a total of 1000 + 333 - 250 = 1083 llamas at the end of the year.

# Mario.c

Recreates the structure of pyramid blocks from Super Mario Brothers using hashes with the height decided by the users input.

![pyramid](https://user-images.githubusercontent.com/69617120/135387973-c86da784-620d-43de-b4d8-aad89f19bdaf.png)

# Cash.c

Using a greedy algorithm cash.c calculates the minimum number of coins owed as change for a cashier. Initially prompting the user for change owed, then printing the minimum number of coins with which that change can be made.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems.”

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America’s currency (and also the European Union’s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible.
