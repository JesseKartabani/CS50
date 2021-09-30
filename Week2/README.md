# CS50 Week 2

https://cs50.harvard.edu/x/2021/weeks/2/

## Scrabble.c

Determines which of two Scrabble words is worth more. 

In the game of Scrabble, players create words to score points, and the number of points is the sum of the point values of each letter in the word.

![Scrabble Table](https://user-images.githubusercontent.com/69617120/135396818-cbbddaa6-7b34-4cce-be6c-d928bc481a0a.PNG)

For example, if we wanted to score the word Code, we would note that in general Scrabble rules, the C is worth 3 points, the o is worth 1 point, the d is worth 2 points, and the e is worth 1 point. Summing these, we get that Code is worth 3 + 1 + 2 + 1 = 7 points.


## Readability.c

Computes the approximate grade level needed to comprehend any inputed text, using the Coleman-Liau index test. The formula is:

![Formula](https://user-images.githubusercontent.com/69617120/135398061-00d78ce1-fc16-421f-80c4-3422837c1255.PNG)

Here, ***L*** is the average number of letters per 100 words in the text, and ***S*** is the average number of sentences per 100 words in the text. For example:

![Example](https://user-images.githubusercontent.com/69617120/135398547-eba9a887-3b5b-4d41-81e6-cee3539a4650.PNG)

The text the user inputted has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words. And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words. Plugged into the Coleman-Liau formula, and rounded to the nearest whole number, we get an answer of 3: so this passage is at a third grade reading level.

If we abstract away the details all that's happening is that as the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level.

## Caesar.c

Encrypts messages using Caesar's cipher, per the below

![Example](https://user-images.githubusercontent.com/69617120/135401660-6ff1cd83-d336-4ffa-9712-773e94ab2ee6.PNG)

### Background

Supposedly, Caesar (yes, that Caesar) used to “encrypt” (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, …, and, wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP. Upon receiving such messages from Caesar, recipients would have to “decrypt” them by shifting letters in the opposite direction by the same number of places.

The secrecy of this “cryptosystem” relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you’re perhaps the first in the world to do it, pretty secure!

Unencrypted text is generally called plaintext. Encrypted text is generally called ciphertext. And the secret used is called a key.

To be clear, then, here’s how encrypting HELLO with a key of 1 yields IFMMP:

![Ca4pture](https://user-images.githubusercontent.com/69617120/135401899-a3ebd751-9e65-4b84-9701-88dfaad05a5c.PNG)


