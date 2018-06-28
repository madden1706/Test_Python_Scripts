'''https://www.youtube.com/watch?v=XKu_SEDAykw'''

nums = [1, 2, 3, 9, ]
nums2 = [1, 2, 4, 4, ]
sum_wanted = 8


def sum_finder(nums, sum_wanted):
    """Finds if a list of numbers contains two that sum to a desired number"""

    for i, ni in enumerate(nums):

        for x, nx in enumerate(nums[i+1:]):

            if ni + nx == sum_wanted:
                print("Yes", ni, "and", nx, "=", sum_wanted)
            else:
                print(ni, "and", nx, "=", "No match")

#sum_finder(nums, sum_wanted)
#print("----")
#sum_finder(nums2, sum_wanted)

"""The sum_finder is slowest method.

A Binary Search Method is faster.

Faster than that is below. ONLY for sorted lists."""


def number_search(num, want):
    """Takes last and first index, if sum too big moves the last index -1. If too small
    moves the first index +1"""

    a = 0
    o = -1

    logic = num[a] + num[o]

    for x in num:
        if logic != want:

            if a == len(num) + o:
                print("No pairs") #len(num) - a,  len(num) + o)

            elif logic > want:
                # 10      8
                o = o - 1
                #print(o)
                logic = num[a] + num[o]
                #print("logic=",logic)

            elif logic < want:
                a = a + 1
                #print(a)
                logic = num[a] + num[o]
                #print("logic=", logic)

        elif logic == want:
            print("Pair found", num[a], "and", num[o])
            break


number_search(nums, sum_wanted)
print("----")
number_search(nums2, sum_wanted)












