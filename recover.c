#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

// Custom data type for bytes
typedef uint8_t BYTE;

#define FILE_NAME_SIZE 8
#define BLOCK_SIZE 512

bool start_new_jpeg(BYTE buffer[]);
 
int main(int argc, char *argv[])
{
    // Error checking for exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    // Open memory card file but if unable to then print error message
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("File was unable to be located");
        return 1;
    }
    
    // Create buffer
    BYTE buffer[BLOCK_SIZE];
    
    int file_index = 0;
    bool found_first_jpeg = false;
    FILE *outfile;
    while (fread(buffer, BLOCK_SIZE, 1, infile))
    {
        if (start_new_jpeg(buffer))
        {
            if (!found_first_jpeg)
            {
                found_first_jpeg = true;
            }
            else
            {
                fclose(outfile);
            }
                
            char filename[FILE_NAME_SIZE];
            sprintf(filename, "%03i.jpg", file_index++);
            outfile = fopen(filename, "w");
            if (outfile == NULL)
            {
                return 1;
            }
            // Writes 512 bytes to outfile once we find the first jpeg
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
        }
        else if (found_first_jpeg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
        }
    }
    // Close files
    fclose(outfile);
    fclose(infile);
}
// Reads the first 4 bytes of the buffer
bool start_new_jpeg(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
}