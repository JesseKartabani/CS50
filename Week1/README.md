# CS50 Week 1

https://cs50.harvard.edu/x/2021/weeks/1/

## Hello.c

Promts the user for their name via command line and outputs Hello (name).

## Population.c

determines how long it takes for a population to reach a particular size.

$ ./population
Start size: 100
End size: 200
Years: 9

Say we have a population of n llamas. Each year, n/3 new llamas are born, and n/4 llamas pass away. 

If we were to start with n = 1000 llamas, at the end of the year, we would have 1000 / 3 = 333.33 new llamas. We can’t have a decimal portion of a llama, though, so we’ll truncate the decimal to get 333 new llamas born. 1000 / 4 = 250 llamas will pass away, so we’ll end up with a total of 1000 + 333 - 250 = 1083 llamas at the end of the year.
