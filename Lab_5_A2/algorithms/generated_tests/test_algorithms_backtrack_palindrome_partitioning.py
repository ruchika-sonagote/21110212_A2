# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.backtrack.palindrome_partitioning as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xab"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.palindromic_substrings_iter(dict_0)
    module_0.palindromic_substrings(var_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.palindromic_substrings(dict_0)


def test_case_2():
    str_0 = "~{qg."
    list_0 = [str_0, str_0, str_0]
    list_1 = [list_0]
    var_0 = module_0.palindromic_substrings(list_1)
    bool_0 = False
    var_1 = module_0.palindromic_substrings_iter(bool_0)
    var_2 = module_0.palindromic_substrings_iter(bool_0)


def test_case_3():
    none_type_0 = None
    var_0 = module_0.palindromic_substrings(none_type_0)
    complex_0 = 1941.055134 + 4126j
    var_1 = module_0.palindromic_substrings_iter(complex_0)
    var_2 = module_0.palindromic_substrings_iter(var_1)
    bytes_0 = b"Y\xae\xe8b\x16{\xec\x9b\x86\x88\xd5"
    var_3 = module_0.palindromic_substrings_iter(var_1)
    var_4 = module_0.palindromic_substrings(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "C\x0b\nK%fnr\t(RIr%"
    var_0 = module_0.palindromic_substrings(str_0)
    var_1 = module_0.palindromic_substrings_iter(var_0)
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "C\x0b\nK%fnr\t(RIr%"
    var_0 = module_0.palindromic_substrings_iter(str_0)
    module_1.object(*var_0)
