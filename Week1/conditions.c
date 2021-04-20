#include <cs50.h>
#include <stdio.h>

int main (void)
{
      // Prompt user for x
      int x = get_int("x: ");

      // Prompt user for y
      int y = get_int("y: ");

      // Compare x and y
      if  (x < y)
   {
      printf("x is less than y");
   }
      else if (x > y)
   {
      printf("x is not less than y");
   }
      else
   {
      printf("x is equal to y");
   }
}