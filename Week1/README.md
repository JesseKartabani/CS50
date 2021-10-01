# CS50 Week 1

https://cs50.harvard.edu/x/2021/weeks/1/

# Hello.c

Prompts the user for their name via command line and outputs Hello (name).

# Population.c

Determines how many years it takes for a population to reach a particular size by prompting the user for a starting population size and the ending population size, then calculating the integer using the formula below.

Say we have a population of n llamas. Each year, n/3 new llamas are born, and n/4 llamas pass away. 

![Example](https://user-images.githubusercontent.com/69617120/135576740-c2f7d9c0-3f6d-400b-8f66-702268173bd3.PNG)

If we were to start with n = 1000 llamas, at the end of the year, we would have 1000 / 3 = 333.33 new llamas. We can’t have a decimal portion of a llama, though, so we’ll truncate the decimal to get 333 new llamas born. 1000 / 4 = 250 llamas will pass away, so we’ll end up with a total of 1000 + 333 - 250 = 1083 llamas at the end of the year.

### ***Implementation Details***

Complete the implementation of population.c, such that it calculates the number of years required for the population to grow from the start size to the end size.

- Your program should first prompt the user for a starting population size.
  - If the user enters a number less than 9 (the minimum allowed population size), the user should be re-prompted to enter a starting population size until they enter a number that is greater than or equal to 9. (If we start with fewer than 9 llamas, the population of llamas will quickly become stagnant!)
- Your program should then prompt the user for an ending population size.
  - If the user enters a number less than the starting population size, the user should be re-prompted to enter an ending population size until they enter a number that is greater than or equal to the starting population size. (After all, we want the population of llamas to grow!)
- Your program should then calculate the (integer) number of years required for the population to reach at least the size of the end value.
- Finally, your program should print the number of years required for the llama population to reach that end size, as by printing to the terminal Years: n, where n is the number of years.

# Mario.c

Recreates the structure of pyramid blocks from Super Mario Brothers using hashes with the height decided by the users input.

![pyramid](https://user-images.githubusercontent.com/69617120/135387973-c86da784-620d-43de-b4d8-aad89f19bdaf.png)

# Cash.c

Using a greedy algorithm cash.c calculates the minimum number of coins owed as change for a cashier. Initially prompting the user for change owed, then printing the minimum number of coins with which that change can be made.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems.”

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America’s currency (and also the European Union’s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible.
