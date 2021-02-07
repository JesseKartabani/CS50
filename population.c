#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n, y, b, d, end;
    
    do
    
    {
        n = get_int("Start size: ");
    } 
    while (n < 9);

    // TODO: Prompt for end size
 
    do
    {
        end = get_int("End size: ");
    } 
    while (end < n);

    // TODO: Calculate number of years until we reach threshold
    for (y = 0; n < end; y++)
    {
        b = n / 3;
        d = n / 4;
        n = n + b - d;  
    }
    
    // TODO: Print number of years
    printf("Years: %i\n", y);
}