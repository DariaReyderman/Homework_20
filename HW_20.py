# Exercise 1
"""
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


def brackets(bracket: str) -> bool:
    """
    Gets a string and determine if the input is valid.
    :param bracket: '(', ')', '{', '}', '[', ']'.
    :return: True, False
    """
    open_bracket_list: list[str] = []
    for b in bracket:
        if b in ["{", "[", "("]:
            open_bracket_list.append(b)
            continue
        if b in ["}", "]", ")"]:
            if len(open_bracket_list) == 0:
                return False
            last = open_bracket_list[-1]
            if b == "}" and last == "{" or b == "]" and last == "[" or b == ")" and last == "(":
                open_bracket_list.pop()
            else:
                return False

    if len(open_bracket_list) > 0:
        return False
    else:
        return True


print(brackets("{{[[]]}}"))

# Exercise 2
"""
Run on the list from the first item (i = 0).
Until we reach the end of the list (while i < len(list)):
  check the items after the current one (j = i + 1)
  check all items till the end of the list (while j < len(list)):
    if we find duplication (j = i) -> remove it (pop j)
    else -> continue to the next one (j += 1)
  after checking all the items, go to the next one (i += 1)
  
"""


def remove_duplicates(list1: list[int]) -> list[int]:
    """
    Gets the list of numbers with duplicates and returns a list without duplicates
    without using set, count and reference lists.
    :param list1: list[int]
    :return: list[int]
    """
    i = 0
    while i < len(list1):
        j = i + 1
        while j < len(list1):
            if list1[j] == list1[i]:
                list1.pop(j)
            else:
                j += 1
        i += 1
    return list1


print(remove_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6]))

# Exercise 3
"""
Compare items from both lists and add the smaller one to the result list. 
    if list1_item <= list2_item -> list3.append(list1_item)
    list1_item += 1
    else (list2_item < list1_item) -> list3.append(list2_item)
    list2_item += 1
If one of the lists is over, add the remaining items from the second one to the result list
"""


def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Gets two sorted lists and unites them to the third sorted list with duplications.
    :param list1: list[int]
    :param list2: list[int]
    :return: list[int]
    """
    result: list[int] = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


print(merge_two_lists([1, 2, 4], [1, 3, 4]))
