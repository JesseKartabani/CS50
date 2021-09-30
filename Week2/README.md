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
