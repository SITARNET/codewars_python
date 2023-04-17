# 1.
# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language)
# like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater, and all of
# the items will be numbers; target will always be the sum of two different items from that array).

# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

# def two_sum(nums, t):
#     for i, x in enumerate(nums):
#         for j, y in enumerate(nums):
#             if i != j and x + y == t:
#                 return [i, j]
#
# print(two_sum([1, 2, 3], 4))

# 2.

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# Examples: (Input --> Output)

def number(lines):
    count = 1
    line = []
    for i in lines:
        line.append(str(count) + ': ' + i)
        count += 1
    return line

print(number(["a", "b", "c"]))