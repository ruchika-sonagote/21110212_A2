# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.missing_ranges as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 69
    set_0 = {int_0}
    none_type_0 = None
    module_0.missing_ranges(set_0, none_type_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    bool_0 = False
    var_0 = module_0.missing_ranges(str_0, bool_0, bool_0)
    none_type_0 = None
    module_0.missing_ranges(str_0, none_type_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.missing_ranges(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3680
    list_0 = [int_0, int_0]
    bool_0 = False
    tuple_0 = (int_0, list_0, bool_0, int_0)
    module_0.missing_ranges(tuple_0, bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "ce9Jz;0F"
    bool_0 = True
    module_0.missing_ranges(str_0, str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    tuple_0 = ()
    set_0 = {tuple_0}
    module_0.missing_ranges(set_0, tuple_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    tuple_0 = (bool_0,)
    var_0 = module_0.missing_ranges(tuple_0, bool_0, bool_0)
    none_type_0 = None
    module_0.missing_ranges(var_0, none_type_0, var_0)
