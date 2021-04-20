"""
Input a text file (containing 1 or more paragraphs of English
text) from the user, parse this file to display the frequency of
occurrence of each word in this text file. Find the 3 most frequent
words as well.
"""


def key_func(k):
    return frequencies[k]


punctuations = [".", ",", "'", "(", ")", "/", "\""]
frequencies = {}

# Read the text file
txt_file = open(file="sample_file.txt", mode="r")

# Split the text files into words
words = [x.lower().split(" ") for x in txt_file.readlines()]

# Convert list of list to normal list
words = [items for x in words for items in x]

# Add frequencies in a Dictionary
for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

# Counting Top 3 Frequent Words
top_3 = sorted(frequencies, key=key_func, reverse=True)[:3]

for top in top_3:
    print(f"{top}: {frequencies[top]}")