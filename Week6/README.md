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

# Readability.py

Computes the approximate grade level needed to comprehend any inputed text, using the Coleman-Liau index test. The formula is:

![Formula](https://user-images.githubusercontent.com/69617120/135398061-00d78ce1-fc16-421f-80c4-3422837c1255.PNG)

### ***Background***

Here, ***L*** is the average number of letters per 100 words in the text, and ***S*** is the average number of sentences per 100 words in the text. For example:

![Example](https://user-images.githubusercontent.com/69617120/135398547-eba9a887-3b5b-4d41-81e6-cee3539a4650.PNG)

The text the user inputted has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words. And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words. Plugged into the Coleman-Liau formula, and rounded to the nearest whole number, we get an answer of 3: so this passage is at a third grade reading level.

If we abstract away the details all that's happening is that as the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level.

### ***Specification***

- Write, in a file called readability.py in ~/pset6/readability/, a program that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula, exactly as you did in Problem Set 2, except that your program this time should be written in Python.
  - Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
- Use get_string from the CS50 Library to get the user’s input, and print to output your answer.
- Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
- Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
- If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, your program should output "Before Grade 1".

# DNA

Command line program that identifies a person based on their DNA, per the below.

![Example](https://user-images.githubusercontent.com/69617120/135580170-3ce3fcea-25a9-4a35-8e57-c6c35ca2e5af.PNG)

### ***Background***

DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?

Well, DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has billions of these nucleotides arranged in sequence. Some portions of this sequence (i.e. genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.

![DNA Strings](https://user-images.githubusercontent.com/69617120/135580550-a84dcebc-9bf9-4fc6-9a89-f498ee06ed43.PNG)

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, The FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

![Capasture](https://user-images.githubusercontent.com/69617120/135580828-d7e6629e-26ee-4210-90e0-8aa10e9b93b6.PNG)

The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.

### ***Specification***

In a file called dna.py in ~/pset6/dna/, implement a program that identifies to whom a sequence of DNA belongs.

- The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
  - If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with print). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file, and that the second argument is the filename of a valid text file.
- Your program should open the CSV file and read its contents into memory.
  - You may assume that the first row of the CSV file will be the column names. The first column will be the word name and the remaining columns will be the STR sequences themselves.
- Your program should open the DNA sequence and read its contents into memory.
- For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify.
- If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
  - You may assume that the STR counts will not match more than one individual.
  - If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print "No match".
