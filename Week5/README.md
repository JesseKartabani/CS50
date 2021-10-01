# CS50 Week 5

https://cs50.harvard.edu/x/2021/weeks/5/

# Inheritance

Simulates the inheritance of blood types for each member of a family.

This project included distribution code, work completed by me can be found under implementation details.

![Capt67ure](https://user-images.githubusercontent.com/69617120/135559294-38d28038-0b71-4e72-9cfc-d972bfb5ba94.PNG)

### ***Background***

A person’s blood type is determined by two alleles (i.e., different forms of a gene). The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different). Each of a child’s parents randomly passes one of their two blood type alleles to their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

For example, if one parent has blood type AO and the other parent has blood type BB, then the child’s possible blood types would be AB and OB, depending on which allele is received from each parent. Similarly, if one parent has blood type AO and the other OB, then the child’s possible blood types would be AO, OB, AB, and OO.

### ***Implementation Details***

Complete the implementation of inheritance.c, such that it creates a family of a specified generation size and assigns blood type alleles to each family member. The oldest generation will have alleles assigned randomly to them.

- The create_family function takes an integer (generations) as input and should allocate (as via malloc) one person for each member of the family of that number of generations, returning a pointer to the person in the youngest generation.
  - For example, create_family(3) should return a pointer to a person with two parents, where each parent also has two parents.
  - Each person should have alleles assigned to them. The oldest generation should have alleles randomly chosen (as by calling the random_allele function), and younger generations should inherit one allele (chosen at random) from each parent.
  - Each person should have parents assigned to them. The oldest generation should have both parents set to NULL, and younger generations should have parents be an array of two pointers, each pointing to a different parent.

 create_family Function.

- First, you should allocate memory for a new person. Recall that you can use malloc to allocate memory, and sizeof(person) to get the number of bytes to allocate.
- Next, we’ve included a condition to check if generations > 1.
  - If generations > 1, then there are more generations that still need to be allocated. Your function should set both parents by recursively calling create_family. (How many generations should be passed as input to each parent?) The function should then set both alleles by randomly choosing one allele from each parent.
  - Otherwise (if generations == 1), then there will be no parent data for this person. Both parents should be set to NULL, and each allele should be generated randomly.
- Finally, your function should return a pointer for the person that was allocated.

The free_family function should accept as input a pointer to a person, free memory for that person, and then recursively free memory for all of their ancestors.

- Since this is a recursive function, you should first handle the base case. If the input to the function is NULL, then there’s nothing to free, so your function can return immediately.
- Otherwise, you should recursively free both of the person’s parents before freeing the child.

# Speller

Command line program that spell-checks .txt files using a hash table, per the below.

![Capturelala](https://user-images.githubusercontent.com/69617120/135560945-dbe03c71-84ab-4d4f-8925-57245eeb4a26.PNG)

This project included distribution code. Work completed by me consists of load, hash, size, check, and upload. Implemented as efficiently as possible using a hash table in such a way that TIME IN load, TIME IN check, TIME IN size, and TIME IN unload are all minimized. Minimized in this context meaning fastest run time possible measured in milliseconds, with storgae space being the second priority.



