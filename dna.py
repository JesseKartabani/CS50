import csv
from sys import argv, exit


def max_substring(s, sub):  # Maxium number of times a substring is repeated
    ans = [0] * len(s)
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) - 1:
                ans[i] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)        


def dna_match(r, actual):  # Checks for a DNA match
    for line in r:
        person = line[0]
        values = [int(val) for val in line[1:]]
        if values == actual:
            print(person)
            return
    print("No match")      # Tells the user if theres no match


def main():
    if len(argv) != 3:  # Making sure the user gives the correct input
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Uses the above functions to find if the DNA is a match to anyone in the csv file
    csv_path = argv[1]
    with open(csv_path) as csv_file: 
        r = csv.reader(csv_file)
        
        all_sequences = next(r)[1:]
        
        txt_path = argv[2]
        with open(txt_path) as txt_file:
            s = txt_file.read()
            actual = [max_substring(s, seq) for seq in all_sequences]
            
        dna_match(r, actual)


if __name__ == "__main__":  # Calls main
    main()