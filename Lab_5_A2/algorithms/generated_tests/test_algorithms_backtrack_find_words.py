# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.backtrack.find_words as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\n    Pancake_sort\n    Sorting a given array\n    mutation of selection sort\n\n    reference: https://www.geeksforgeeks.org/pancake-sorting/\n    \n    Overall time complexity : O(N^2)\n    "
    var_0 = module_0.find_words(str_0, str_0)
    none_type_0 = None
    module_0.find_words(none_type_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.find_words(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\nSearch in Rotated Sorted Array\nSuppose an array sorted in ascending order is rotated at some pivot unknown\nto you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).\n\nYou are given a target value to search. If found in the array return its index,\notherwise return -1.\n\nYour algorithm's runtime complexity must be in the order of O(log n).\n---------------------------------------------------------------------------------\nExplanation algorithm:\n\nIn classic binary search, we compare val with the midpoint to figure out if\nval belongs on the low or the high side. The complication here is that the\narray is rotated and may have an inflection point. Consider, for example:\n\nArray1: [10, 15, 20, 0, 5]\nArray2: [50, 5, 20, 30, 40]\n\nNote that both arrays have a midpoint of 20, but 5 appears on the left side of\none and on the right side of the other. Therefore, comparing val with the\nmidpoint is insufficient.\n\nHowever, if we look a bit deeper, we can see that one half of the array must be\nordered normally(increasing order). We can therefore look at the normally ordered\nhalf to determine whether we should search the low or hight side.\n\nFor example, if we are searching for 5 in Array1, we can look at the left element (10)\nand middle element (20). Since 10 < 20, the left half must be ordered normally. And, since 5\nis not between those, we know that we must search the right half\n\nIn array2, we can see that since 50 > 20, the right half must be ordered normally. We turn to\nthe middle 20, and right 40 element to check if 5 would fall between them. The value 5 would not\nTherefore, we search the left half.\n\nThere are 2 possible solution: iterative and recursion.\nRecursion helps you understand better the above algorithm explanation\n"
    var_0 = module_0.find_words(str_0, str_0)
    list_0 = [var_0, var_0, var_0]
    str_1 = "pdzn7>g"
    var_1 = module_0.find_words(list_0, list_0)
    var_2 = module_0.find_words(str_0, str_0)
    str_2 = "+{h@"
    tuple_0 = (str_0, list_0, str_1, str_2)
    module_0.find_words(list_0, tuple_0)
