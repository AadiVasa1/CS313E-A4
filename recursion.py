"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On mOn my/our honor, Aadi Vasa and Raghuvendra Chowdhry, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: adv982
UT EID 2: rbc993
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start>=len(nums):
        return False
    return group_sum(start+1, nums, target-nums[start]) or group_sum(start+1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start>=len(nums):
        return False
    if nums[start]==6:
        return group_sum_6(start+1, nums, target-nums[start])
    attempt1 = group_sum_6(start+1, nums, target-nums[start])
    attempt2 = group_sum_6(start+1, nums, target)
    return attempt1 or attempt2


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start>=len(nums):
        return False
    attempt1 = group_no_adj(start+2, nums, target-nums[start])
    attempt2 = group_no_adj(start+1, nums, target)
    return attempt1 or attempt2



def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start>=len(nums):
        return False
    if nums[start] % 5 == 0:
        if (start+1) < len(nums) and  nums[start+1] == 1:
            return group_sum_5(start+2, nums, target-nums[start])
        return group_sum_5(start+1, nums, target-nums[start])
    attempt1 = group_sum_5(start+1, nums, target-nums[start])
    attempt2 = group_sum_5(start+1, nums, target)
    return attempt1 or attempt2


def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if target==0:
        return True
    if start>=len(nums):
        return False
    clump_len = 1
    i = start + 1
    while i < len(nums) and nums[i] == nums[start]:
        clump_len += 1
        i += 1
    if clump_len > 1:
        attempt1 = group_sum_clump(start+clump_len, nums, target-(nums[start]*clump_len))
        attempt2 = group_sum_clump(start+clump_len, nums, target)
        return attempt1 or attempt2
    attempt1 = group_sum_clump(start+1, nums, target-nums[start])
    attempt2 = group_sum_clump(start+1, nums, target)
    return attempt1 or attempt2


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_array_helper(nums)



def split_array_helper(nums, sum_1=0, sum_2=0):
    """
    split array helper, returns true if nums can be evenly split into two equal sums,
    false otherwise
    """
    if len(nums)==0 and sum_1==sum_2:
        return True
    if len(nums)==0:
        return False
    add = nums.pop()
    attempt1 = split_array_helper(nums.copy(),sum_1+add,sum_2)
    attempt2 = split_array_helper(nums.copy(),sum_1,sum_2+add)
    return attempt1 or attempt2

def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_odd_10_helper(nums)


def split_odd_10_helper(nums, sum_1 = 0, sum_2 = 0):
    """
    recursive helper function for above split_odd_10"""
    if len(nums)==0 and ((sum_1 % 10 == 0 and sum_2 % 2 == 1)
                         or (sum_2 % 10 == 0 and sum_1 % 2 == 1)):
        return True
    if len(nums)==0:
        return False
    add = nums.pop()
    attempt1 = split_odd_10_helper(nums.copy(),sum_1+add,sum_2)
    attempt2 = split_odd_10_helper(nums.copy(),sum_1,sum_2+add)
    return attempt1 or attempt2

def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_53_helper(nums)

def split_53_helper(nums, sum_1=0, sum_2=0, iterations = 0):
    """
    recursive helper function for above split_53_helper"""
    if len(nums)==0 and sum_1==sum_2:
        return True
    if len(nums)==0:
        return False
    add = nums.pop()
    if add % 5 == 0:
        return split_53_helper(nums.copy(),sum_1+add,sum_2,iterations+1)
    if add % 3 == 0:
        return split_53_helper(nums.copy(), sum_1, sum_2+add,iterations+1)
    attempt1 = split_53_helper(nums.copy(),sum_1+add,sum_2,iterations+1)
    attempt2 = split_53_helper(nums.copy(),sum_1,sum_2+add,iterations+1)
    return attempt1 or attempt2
