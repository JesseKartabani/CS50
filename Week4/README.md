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

***Sepia***

An image can be converted to sepia by taking each pixel, and computing new red, green, and blue values based on the original values of the three.

There are a number of algorithms for converting an image to sepia, but for this problem, i'll use the following algorithm. For each pixel, the sepia color values should be calculated based on the original color values per the below.

![C11apture](https://user-images.githubusercontent.com/69617120/135556336-d596bad0-4e8a-4006-8be9-5a54a42579f9.PNG)

Of course, the result of each of these formulas may not be an integer, but each value could be rounded to the nearest integer. It’s also possible that the result of the formula is a number greater than 255, the maximum value for an 8-bit color value. In that case, the red, green, and blue values should be capped at 255. As a result, we can guarantee that the resulting red, green, and blue values will be whole numbers between 0 and 255, inclusive.

***Reflection***

Reflecting an image for example, it's a filter where the resulting image is what you would get by placing the original image in front of a mirror. So any pixels on the left side of the image should end up on the right, and vice versa.

Note that all of the original pixels of the original image will still be present in the reflected image, it’s just that those pixels may have rearranged to be in a different place in the image.

***Blur***

There are a number of ways to create the effect of blurring or softening an image. For this problem, we’ll use the “box blur,” which works by taking each pixel and, for each color value, giving it a new value by averaging the color values of neighboring pixels.

### ***Specification***

- The function grayscale should take an image and turn it into a black-and-white version of the same image.
- The function sepia should take an image and turn it into a sepia version of the same image.
- The reflect function should take an image and reflect it horizontally.
- Finally, the blur function should take an image and turn it into a box-blurred version of the same image.

# ***Recover.c***

Command line program that recovers deleted JPEGs from a forensic image, per the below. 

![C11a1pture](https://user-images.githubusercontent.com/69617120/135557589-39f00a5a-79d8-4f39-adb0-ea8b1d86ec47.PNG)

### ***Background*** 

Even though JPEGs are more complicated than BMPs, JPEGs have “signatures,” patterns of bytes that can distinguish them from other file formats. Specifically, the first three bytes of JPEGs are 

![Ca32pture](https://user-images.githubusercontent.com/69617120/135557904-4c7caa9d-08bd-4439-92bd-78ec3c89ba56.PNG)

from first byte to third byte, left to right. The fourth byte, meanwhile, is either 0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef. Put another way, the fourth byte’s first four bits are 1110. 

Odds are, if you find this pattern of four bytes on media known to store photos (e.g., my memory card), they demarcate the start of a JPEG. To be fair, you might encounter these patterns on some disk purely by chance, so data recovery isn’t an exact science. 

Fortunately, digital cameras tend to store photographs contiguously on memory cards, whereby each photo is stored immediately after the previously taken photo. Accordingly, the start of a JPEG usually demarks the end of another. However, digital cameras often initialize cards with a FAT file system whose “block size” is 512 bytes (B). The implication is that these cameras only write to those cards in units of 512 B. A photo that’s 1 MB (i.e., 1,048,576 B) thus takes up 1048576 ÷ 512 = 2048 “blocks” on a memory card. But so does a photo that’s, say, one byte smaller (i.e., 1,048,575 B)! The wasted space on disk is called “slack space.” Forensic investigators often look at slack space for remnants of suspicious data. 

The implication of all these details is that you, the investigator, can probably write a program that iterates over a copy of my memory card, looking for JPEGs’ signatures. Each time you find a signature, you can open a new file for writing and start filling that file with bytes from my memory card, closing that file only once you encounter another signature. Moreover, rather than read my memory card’s bytes one at a time, you can read 512 of them at a time into a buffer for efficiency’s sake. Thanks to FAT, you can trust that JPEGs’ signatures will be “block-aligned.” That is, you need only look for those signatures in a block’s first four bytes. 

Realize, of course, that JPEGs can span contiguous blocks. Otherwise, no JPEG could be larger than 512 B. But the last byte of a JPEG might not fall at the very end of a block. Recall the possibility of slack space. But not to worry. Because this memory card was brand-new when I started snapping photos, odds are it’d been “zeroed” (i.e., filled with 0s) by the manufacturer, in which case any slack space will be filled with 0s. It’s okay if those trailing 0s end up in the JPEGs you recover; they should still be viewable. 

I’ve gone ahead and created a “forensic image” of the card, storing its contents, byte after byte, in a file called card.raw. So that you don’t waste time iterating over millions of 0s unnecessarily, I’ve only imaged the first few megabytes of the memory card. But you should ultimately find that the image contains 50 JPEGs. 
