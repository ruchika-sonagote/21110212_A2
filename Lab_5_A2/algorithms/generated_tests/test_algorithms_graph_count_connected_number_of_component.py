# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.graph.count_connected_number_of_component as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    module_0.count_components(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 500
    module_0.count_components(int_0, int_0)


def test_case_2():
    int_0 = -1728
    set_0 = module_0.count_components(int_0, int_0)
    assert set_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = "53"
    module_0.count_components(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 97
    bytes_0 = b"=\x07iG\xcc\x03\xf6\xab\x1c\xd3lI\x9f\xe8\xc2"
    tuple_0 = (int_0, bytes_0)
    module_0.count_components(tuple_0, int_0)


def test_case_5():
    bool_0 = True
    str_0 = "N4@ _\x0c4@oEsdk"
    list_0 = [bool_0]
    tuple_0 = (str_0, list_0, list_0, bool_0)
    var_0 = module_0.count_components(tuple_0, bool_0)
    assert var_0 == 1
