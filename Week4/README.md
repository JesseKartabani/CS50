# CS50 Week 4

https://cs50.harvard.edu/x/2021/weeks/4/

# Volume.c

Modifies the volume of a WAV file by taking three command-line arguments. First the name of the original audio file followed by the desired name of the new audio file that should be generated, and finally the factor by which the volume of the original audio file should be scaled. 

![9Capture](https://user-images.githubusercontent.com/69617120/135434393-b8526a76-8cc9-4194-a957-bc7d457f02fa.PNG)

### ***Background***

WAV files are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

### ***Implementation Details***

- The program accepts three command-line arguments: input represents the name of the original audio file, output represents the name of the new audio file that should be generated, and factor is the amount by which the volume of the original audio file should be scaled.
  - For example, if factor is 2.0, then your program should double the volume of the audio file in input and save the newly generated audio file in output.

- The program should first read the header from the input file and write the header to the output file. Recall that this header is always exactly 44 bytes long.

- The program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Program should multiply each sample by the factor and write the new sample to the output file.
  - You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this lab.
 
- If the program uses malloc, it must not leak any memory.

# Filter.c

Command line program that applies filters (greyscale, sepia, reflection and blur) to BMPs, per the below. 

![Captu99re](https://user-images.githubusercontent.com/69617120/135555981-9a58e280-8c22-4ff5-8f40-adddf04fcc90.PNG)

### ***Background***

***Grayscale***

One common filter is the “grayscale” filter, where we take an image and want to convert it to black-and-white. How does that work?

If the red, green, and blue values are all set to 0x00 (hexadecimal for 0), then the pixel is black. And if all values are set to 0xff (hexadecimal for 255), then the pixel is white. So long as the red, green, and blue values are all equal, the result will be varying shades of gray along the black-white spectrum, with higher values meaning lighter shades (closer to white) and lower values meaning darker shades (closer to black).

So to convert a pixel to grayscale, we just need to make sure the red, green, and blue values are all the same value. But how do we know what value to make them? Well, it’s probably reasonable to expect that if the original red, green, and blue values were all pretty high, then the new value should also be pretty high. And if the original values were all low, then the new value should also be low.

In fact, to ensure each pixel of the new image still has the same general brightness or darkness as the old image, we can take the average of the red, green, and blue values to determine what shade of grey to make the new pixel.

If you apply that to each pixel in the image, the result will be an image converted to grayscale.

***Sepia***

An image can be converted to sepia by taking each pixel, and computing new red, green, and blue values based on the original values of the three.

There are a number of algorithms for converting an image to sepia, but for this problem, i'll use the following algorithm. For each pixel, the sepia color values should be calculated based on the original color values per the below.

![C11apture](https://user-images.githubusercontent.com/69617120/135556336-d596bad0-4e8a-4006-8be9-5a54a42579f9.PNG)

Of course, the result of each of these formulas may not be an integer, but each value could be rounded to the nearest integer. It’s also possible that the result of the formula is a number greater than 255, the maximum value for an 8-bit color value. In that case, the red, green, and blue values should be capped at 255. As a result, we can guarantee that the resulting red, green, and blue values will be whole numbers between 0 and 255, inclusive.

***Reflection***

Some filters might also move pixels around. Reflecting an image, for example, is a filter where the resulting image is what you would get by placing the original image in front of a mirror. So any pixels on the left side of the image should end up on the right, and vice versa.

Note that all of the original pixels of the original image will still be present in the reflected image, it’s just that those pixels may have rearranged to be in a different place in the image.

***Blur***

There are a number of ways to create the effect of blurring or softening an image. For this problem, we’ll use the “box blur,” which works by taking each pixel and, for each color value, giving it a new value by averaging the color values of neighboring pixels.

### ***Specification***

- The function grayscale should take an image and turn it into a black-and-white version of the same image.
- The function sepia should take an image and turn it into a sepia version of the same image.
- The reflect function should take an image and reflect it horizontally.
- Finally, the blur function should take an image and turn it into a box-blurred version of the same image.
