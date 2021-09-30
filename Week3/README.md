# CS50 Week 3

https://cs50.harvard.edu/x/2021/weeks/3/

# Plurality.c

Command line simulation of a plurality election, per the below.

![6Capture](https://user-images.githubusercontent.com/69617120/135426010-faf4925e-7784-409d-b68f-68641470e03d.PNG)

This problem set included distrubution code as a starting point. The functions I completed can be found under specification.

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

# Runoff.c

Command line simulation of a runoff election, per the below.

![Captu8re](https://user-images.githubusercontent.com/69617120/135426398-e4a380b3-cae0-4b13-93d8-46a86f59510e.PNG)

This problem set included distrubution code as a starting point. The functions I completed can be found under specification.

### Background

In an instant runoff election, voters can rank as many candidates as they wish. If any candidate has a majority (more than 50%) of the first preference votes, that candidate is declared the winner of the election.

If no candidate has more than 50% of the vote, then an “instant runoff” occurrs. The candidate who received the fewest number of votes is eliminated from the election, and anyone who originally chose that candidate as their first preference now has their second preference considered. Why do it this way? Effectively, this simulates what would have happened if the least popular candidate had not been in the election to begin with.

The process repeats: if no candidate has a majority of the votes, the last place candidate is eliminated, and anyone who voted for them will instead vote for their next preference (who hasn’t themselves already been eliminated). Once a candidate has a majority, that candidate is declared the winner.

### Specification

- Complete the vote function. 
  - The function takes arguments voter, rank, and name. If name is a match for the name of a valid candidate, then you should update the global preferences array to indicate that the voter voter has that candidate as their rank preference (where 0 is the first preference, 1 is the second preference, etc.). 
  - If the preference is successfully recorded, the function should return true; the function should return false otherwise (if, for instance, name is not the name of one of the candidates). 
  - You may assume that no two candidates will have the same name. 

- Complete the tabulate function. 
  - The function should update the number of votes each candidate has at this stage in the runoff. 
  - Recall that at each stage in the runoff, every voter effectively votes for their top-preferred candidate who has not already been eliminated. 

- Complete the print_winner function. 
  - If any candidate has more than half of the vote, their name should be printed to stdout and the function should return true. 
  - If nobody has won the election yet, the function should return false. 

- Complete the find_min function. 
  - The function should return the minimum vote total for any candidate who is still in the election. 

- Complete the is_tie function. 
  - The function takes an argument min, which will be the minimum number of votes that anyone in the election currently has. 
  - The function should return true if every candidate remaining in the election has the same number of votes and should return false otherwise. 

- Complete the eliminate function. 
  - The function takes an argument min, which will be the minimum number of votes that anyone in the election currently has. 
  - The function should eliminate the candidate (or candidates) who have min number of votes. 
