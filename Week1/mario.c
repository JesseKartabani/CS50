#include <cs50.h>
#include <stdio.h>

void print(char c, int height);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: "); // Prompts the user for input
    }
    while (height < 1 || height > 8); // Error checking user input

    for (int i = 0; i < height; i++) // Looping until height is equal to the users input
    {
        print(' ', height - 1 - i); // Prints out the pyramid
        print('#', i + 1);
        print(' ', 2);
        print('#', i + 1);

        printf("\n");
    }
}

void print(char c, int height)
{
    for (int i = 0; i < height; i++)
    {
        printf("%c", c);
    }
}
