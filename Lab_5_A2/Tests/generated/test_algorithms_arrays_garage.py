# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.garage as module_0

 
@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"zK\x9d3\xf1\x8ac\x11"
    none_type_0 = None
    module_0.garage(bytes_0, none_type_0)


def test_case_1():
    bytes_0 = b"2\x0c\x06=.u"
    var_0 = module_0.garage(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    tuple_0 = (bool_0,)
    module_0.garage(list_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.garage(list_0, list_0)
    module_0.garage(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"?dZ9\xb6\xe6mt^\x84\xb6,\xa5\x00"
    var_0 = module_0.garage(bytes_0, bytes_0)
    module_0.garage(bytes_0, var_0)
