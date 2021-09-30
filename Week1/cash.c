#include <cs50.h>
#include <stdio.h>
#include <math.h> // Used for rounding function only

int main(void)
{
    float dollars; // Declare dollars
    do
    {
        dollars = get_float("Change owed: "); // Prompt user to input the total change owed and store it in the variable dollars 
    }

    while (dollars < 0); // Error checking user input 

    int cents = round(dollars * 100); // Calculates total cents by multiplying dollars by 100 then rounding off
    int coins = 0; // Declare coins 

    while (cents >= 25) // Increments coins by 1 so long as cents is greater than or equal to 25
    {
        cents -= 25; // Subtract 25 from cents
        coins++; // Increment coins by 1
    }
    while (cents >= 10) // Once cents is less than 25 increment coins by 1
    {
        cents -= 10; // Subtract 10 from cents
        coins++; // Increment coins by 1
    }
    while (cents >= 5) // Once cents is less than 10 increment coins by 1
    {
        cents -= 5; // Subtract 5 from cents
        coins++; // Increment coins by 1
    }
    while (cents >= 1) // If there is 1 cent left over increment coins by 1
    {
        cents -= 1; // Subtract 1 from cents
        coins++; // Increment coins by 1
    }
    printf("%i\n", coins); // Print total number of coins 
}
