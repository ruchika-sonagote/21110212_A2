# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.three_sum as module_0


def test_case_0():
    int_0 = 252
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.three_sum(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.three_sum(none_type_0)


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.three_sum(list_0)


def test_case_3():
    int_0 = -1587
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.three_sum(list_0)


def test_case_4():
    float_0 = -3715.0
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, float_0]
    var_0 = module_0.three_sum(list_0)
