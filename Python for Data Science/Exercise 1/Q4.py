"""
Given an array which may contain duplicates, print all elements
and their frequencies.
"""

frequencies = {}

element_list = ["A", "B", "A", 1, 2, 3, 3, 5, 5, "C", "E", "C", 1]

for element in element_list:
    frequencies[element] = frequencies.get(element, 0) + 1

print(frequencies)
