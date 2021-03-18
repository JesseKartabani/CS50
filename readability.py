from cs50 import get_string

# Get text from user
s = get_string("Text: ").strip()

# Declaring variables
num_words, num_letters, num_sentences = 0, 0, 0

# Loops over every word in the text
for i in range(len(s)):
    # Finds the number of words in the text
    if (i == 0 and s[i] != " ") or (i != len(s) - 1 and s[i] == " " and s[i + 1] != " "):
        num_words += 1
    # Finds the number of letters in the text
    if s[i].isalpha():
        num_letters += 1
    # Finds the number of sentences in the text
    if s[i] == "." or s[i] == "?" or s[i] == "!":
        num_sentences += 1

# L is the average number of letters per 100 words in the text
L = num_letters / num_words * 100
# S is the average number of sentences per 100 words in the text
S = num_sentences / num_words * 100
# Coleman-Liau index
index = round(0.0588 * L - 0.296 * S - 15.8)
# Prints out the texts Grade 
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print ("Grade 16+")
else:
    print(f"Grade {index}")