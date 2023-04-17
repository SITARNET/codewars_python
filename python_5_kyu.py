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

# def number(lines):
#     count = 1
#     line = []
#     for i in lines:
#         line.append(str(count) + ': ' + i)
#         count += 1
#     return line
#
# print(number(["a", "b", "c"]))

# 3. Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.

# def unique_in_order(sequence):
#     res = []
#     prev = None
#     for i in sequence[0:]:
#         if i != prev:
#             res.append(i)
#             prev = i
#     return res
#
# print(unique_in_order('AAAABBBCCDAABBB'))

# 4. You are given an array(list) strarr of strings and an integer k. Your task is to return
# the first longest string consisting of k consecutive strings taken in the array.

def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
    return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))