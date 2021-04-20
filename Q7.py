"""
Searching: Given a sorted array arr[] of n elements, write a
function to search a given element x in arr[]. Do it using linear
and binary search techniques.
"""

arr = list(map(int, input("Enter the array values: ").strip()))
search_number = int(input("Enter a number to search: "))

arr.sort()


class Searching:

    def __init__(self, number, array):
        self.number = number
        self.array = array

    def linear_search(self):
        """
        Implements Linear Search Algorithm.

        :Inputs:
            - number <int>: Search Number
            - array <list>: Sorted List of Numbers

        :Returns:
            - num <int>: Search Index
        """
        for num in range(len(self.array)):
            if self.number == self.array[num]:
                return f"Number found at index {num}"
                break

    def binary_search(self, first=0, last=0):
        """
        Implements Binary Search Algorithm.

        :Inputs:
            - number <int>: Search Number
            - array <list>: Sorted List of Numbers
            - first <int>: First element in the list
            - last <int>: Last element in the list

        :Returns:
            - num <int>: Search Index
        """
        last = len(self.array) - 1

        while first <= last:

            mid = first + last // 2

            if self.number not in self.array:
                break
            elif self.array[mid] == self.number:
                return f"Number found at index {mid}"
            elif arr[mid] > self.number:
                last = mid - 1
            elif arr[mid] < self.number:
                first = mid + 1

        return "Search number is not found in the list"


search = Searching(number=search_number, array=arr)

print(search.linear_search())
print(search.binary_search())
