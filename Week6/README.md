# CS50 Week 6

https://cs50.harvard.edu/x/2021/weeks/6/

# Lab 6 Tournament.py

Program that predicts the percentage chance of winning the FIFA World Cup for each team.

![Captu423re](https://user-images.githubusercontent.com/69617120/135570976-7763a233-fa20-48b2-a51b-975541cbecd6.PNG)

Distribution code was included for this project, work I completed encompasses everything listed below implementation details. 

### ***Background***

In soccer’s World Cup, the knockout round consists of 16 teams. In each round, each team plays another team and the losing teams are eliminated. When only two teams remain, the winner of the final match is the champion.

In soccer, teams are given FIFA Ratings, which are numerical values representing each team’s relative skill level. Higher FIFA ratings indicate better previous game results, and given two teams’ FIFA ratings, it’s possible to estimate the probability that either team wins a game based on their current ratings. The FIFA Ratings from just before the two previous World Cups are available as the May 2018 Men’s FIFA Ratings and March 2019 Women’s FIFA Ratings.

Using this information, we can simulate the entire tournament by repeatedly simulating rounds until we’re left with just one team. And if we want to estimate how likely it is that any given team wins the tournament, we might simulate the tournament many times (e.g. 1000 simulations) and count how many times each team wins a simulated tournament.

### ***Implementation Details***

- First, in main, read the team data from the CSV file into your program’s memory, and add each team to the list teams.
  - The file to use will be provided as a command-line argument. You can access the name of the file, then, with sys.argv[1].
  - Recall that you can open a file with open(filename), where filename is a variable storing the name of the file.
  - Once you have a file f, you can use csv.DictReader(f) to give you a “reader”: an object in Python that you can loop over to read the file one row at a time, treating each row as a dictionary.
  - By default, all values read from the file will be strings. So be sure to first convert the team’s rating to an int (you can use the int function in Python to do this).
  - Ultimately, append each team’s dictionary to teams. The function call teams.append(x) will append x to the list teams.
  - Recall that each team should be a dictionary with a team name and a rating.

- Next, implement the simulate_tournament function. This function should accept as input a list of teams and should repeatedly simulate rounds until you’re left with one team. The function should the return the name of that team.
  - You can call the simulate_round function, which simulates a single round, accepting a list of teams as input and returning a list of all of the winners.
  - Recall that if x is a list, you can use len(x) to determine the length of the list.
  - You should not assume the number of teams in the tournament, but you may assume it will be a power of 2.

- Finally, back in the main function, run N tournament simulations, and keep track of how many times each team wins in the counts dictionary.
  - For example, if Uruguay won 2 tournaments and Portugal won 3 tournaments, then your counts dictionary should be {"Uruguay": 2, "Portugal": 3}.
  - You should use your simulate_tournament to simulate each tournament and determine the winner.
  - Recall that if counts is a dictionary, then syntax like counts[team_name] = x will associate the key stored in team_name with the value stored in x.
  - You can use the in keyword in Python to check if a dictionary has a particular key already. For example, if "Portugal" in counts: will check to see if "Portugal" already has an existing value in the counts dictionary.

# PSET 6 

The projects below besides DNA are remakes of my previous projects in the python language  

# Hello.py

Prints out a simple greeting to the user, per the below.

![Example](https://user-images.githubusercontent.com/69617120/135575206-e86fc3de-f11a-4f86-b41d-454ad0807881.PNG)

### ***Specification***

- Write, in a file called hello.py in ~/pset6/hello, a program that prompts a user for their name, and then prints hello, so-and-so, where so-and-so is their provided name, exactly as you did in Lab 1, except that your program this time should be written in Python.

# Mario.py

Recreates the structure of pyramid blocks from Super Mario Brothers using hashes with the height decided by the users input.

![pyramid](https://user-images.githubusercontent.com/69617120/135575531-11cbfadf-fca8-4097-afa2-d84dd8c27b8c.png)

### ***Specification***

- Write, in a file called mario.py in ~/pset6/mario/less/, a program that recreates the half-pyramid using hashes (#) for blocks, exactly as you did in Problem Set 1, except that your program this time should be written in Python.
- To make things more interesting, first prompt the user with get_int for the half-pyramid’s height, a positive integer between 1 and 8, inclusive.
- If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.
- Then, generate (with the help of print and one or more loops) the desired half-pyramid.
- Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.

# Cash.py

Program that calculates the minimum number of coins required to give a user change.

![Example](https://user-images.githubusercontent.com/69617120/135576302-e8d7b570-84c0-460e-b86a-cee888e1f09e.PNG)

### ***Background***

Using a greedy algorithm cash.c calculates the minimum number of coins owed as change for a cashier. Initially prompting the user for change owed, then printing the minimum number of coins with which that change can be made.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems.”

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America’s currency (and also the European Union’s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible.

### ***Specification***

- Write, in a file called cash.py in ~/pset6/cash/, a program that first asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made, exactly as you did in Problem Set 1, except that your program this time should be written in Python.
- Use get_float from the CS50 Library to get the user’s input and print to output your answer. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
  - We ask that you use get_float so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program’s input will be 9.75 and not $9.75 or 975. However, if some customer is owed $9 exactly, assume that your program’s input will be 9.00 or just 9 but, again, not $9 or 900. Of course, by nature of floating-point values, your program will likely work with inputs like 9.0 and 9.000 as well; you need not worry about checking whether the user’s input is “formatted” like money should be.
- If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
- Incidentally, so that we can automate some tests of your code, we ask that your program’s last line of output be only the minimum number of coins possible: an integer followed by a newline.
