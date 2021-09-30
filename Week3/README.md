# CS50 Week 3

https://cs50.harvard.edu/x/2021/weeks/3/

# Plurality.c

Command line simulation of a plurality election. This problem set included distrubution code as a starting point, the functions I completed can be found under specifications.

### Background

Perhaps the simplest way to hold an election, though, is via a method commonly known as the “plurality vote” (also known as “first-past-the-post” or “winner take all”). In the plurality vote, every voter gets to vote for one candidate. At the end of the election, whichever candidate has the greatest number of votes is declared the winner of the election.

### Specification

- Complete the vote function. 
  - vote takes a single argument, a string called name, representing the name of the candidate who was voted for. 
  - If name matches one of the names of the candidates in the election, then update that candidate’s vote total to account for the new vote. The vote function in this case should return true to indicate a successful ballot. 
  - If name does not match the name of any of the candidates in the election, no vote totals should change, and the vote function should return false to indicate an invalid ballot. 
  - You may assume that no two candidates will have the same name. 
- Complete the print_winner function. 
  - The function should print out the name of the candidate who received the most votes in the election, and then print a newline. 
  - It is possible that the election could end in a tie if multiple candidates each have the maximum number of votes. In that case, you should output the names of each of the winning candidates, each on a separate line. 
