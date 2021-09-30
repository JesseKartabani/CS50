# CS50 Week 4

https://cs50.harvard.edu/x/2021/weeks/4/

# Volume.c

Modifies the volume of a WAV file by taking three command-line arguments. First the name of the original audio file followed by the desired name of the new audio file that should be generated, and finally the factor by which the volume of the original audio file should be scaled. 

### ***Background***

WAV files are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

### ***Implementation Details***

- The program accepts three command-line arguments: input represents the name of the original audio file, output represents the name of the new audio file that should be generated, and factor is the amount by which the volume of the original audio file should be scaled.
  - For example, if factor is 2.0, then your program should double the volume of the audio file in input and save the newly generated audio file in output.
- program should first read the header from the input file and write the header to the output file. Recall that this header is always exactly 44 bytes long.
  - Note that volume.c already defines a variable for you called HEADER_SIZE, equal to the number of bytes in the header.
- program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Program should multiply each sample by the factor and write the new sample to the output file.
  - You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this lab.
- If the program uses malloc, it must not leak any memory.
