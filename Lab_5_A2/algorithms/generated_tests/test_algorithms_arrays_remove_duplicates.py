# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.remove_duplicates as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xba\x02\x1c\xd7_\xcf\x98\xa7\xaaF\xed\x9b\xa9\x92\xc2\xf5"
    var_0 = module_0.remove_duplicates(bytes_0)
    bool_0 = False
    module_0.remove_duplicates(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.remove_duplicates(none_type_0)


def test_case_2():
    str_0 = "bR"
    var_0 = module_0.remove_duplicates(str_0)
    bytes_0 = b"\xdf\x9byWk\x1b\xd2\xfb\xeb\x9fN=\xfc"
    var_1 = module_0.remove_duplicates(bytes_0)
    var_2 = module_0.remove_duplicates(bytes_0)
    var_3 = module_0.remove_duplicates(var_1)
    var_4 = module_0.remove_duplicates(str_0)
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, tuple_0, bytes_0]
    var_5 = module_0.remove_duplicates(bytes_0)
    var_6 = module_0.remove_duplicates(tuple_0)
    var_7 = module_0.remove_duplicates(var_0)
    var_8 = module_0.remove_duplicates(tuple_0)
    var_9 = module_0.remove_duplicates(list_0)
    var_10 = module_0.remove_duplicates(var_6)
    var_11 = module_0.remove_duplicates(list_0)
