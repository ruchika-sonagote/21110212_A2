# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.graph.find_path as module_0


def test_case_0():
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    var_0 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_0 = {bytes_0: bytes_0}
    var_1 = module_0.find_shortest_path(dict_0, bytes_0, dict_0)
    var_2 = module_0.find_path(var_0, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    bytes_0 = b"/\xc82x9\xf3G"
    dict_0 = {
        bytes_0: bytes_0,
        none_type_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_0 = module_0.find_all_path(dict_0, none_type_0, dict_0)
    module_0.find_path(none_type_0, dict_0, bytes_0)


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.find_all_path(dict_0, bool_0, bool_0)


def test_case_3():
    none_type_0 = None
    bytes_0 = b"/\xc82x9\xf3G"
    dict_0 = {
        bytes_0: bytes_0,
        none_type_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_0 = module_0.find_all_path(dict_0, none_type_0, dict_0)


def test_case_4():
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    var_0 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_0 = {bytes_0: bytes_0}
    var_1 = module_0.find_shortest_path(dict_0, bytes_0, dict_0)


def test_case_5():
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.find_shortest_path(dict_0, bytes_0, dict_0)


def test_case_6():
    none_type_0 = None
    var_0 = module_0.find_all_path(none_type_0, none_type_0, none_type_0)
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    dict_0 = {
        bytes_0: bytes_0,
        none_type_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_1 = module_0.find_path(dict_0, dict_0, dict_0)
    var_2 = module_0.find_all_path(dict_0, none_type_0, dict_0)
    var_3 = module_0.find_all_path(none_type_0, var_2, var_2)
    var_4 = module_0.find_path(var_0, dict_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "2:a^{3'"
    var_0 = module_0.find_path(str_0, str_0, str_0)
    module_0.find_path(str_0, str_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    var_0 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_0 = {bytes_0: bytes_0, bytes_0: var_0}
    var_1 = module_0.find_shortest_path(dict_0, bytes_0, dict_0)
    none_type_0 = None
    var_2 = module_0.find_all_path(bytes_0, none_type_0, var_1)
    int_0 = -508
    var_3 = module_0.find_path(var_1, dict_0, dict_0)
    var_4 = module_0.find_path(var_3, var_3, int_0)
    module_0.find_shortest_path(var_1, bytes_0, dict_0, var_3)


def test_case_9():
    none_type_0 = None
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    dict_0 = {
        bytes_0: bytes_0,
        none_type_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_0 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_1 = {bytes_0: bytes_0}
    var_1 = module_0.find_shortest_path(dict_1, dict_1, dict_1)
    var_2 = module_0.find_path(var_0, var_0, var_0)
    str_0 = ":hC2rJ`D\\P-4r-\x0b_`VHG"
    var_3 = module_0.find_path(dict_0, bytes_0, str_0, var_2)


@pytest.mark.xfail(strict=True)
def test_case_10():
    none_type_0 = None
    var_0 = module_0.find_all_path(none_type_0, none_type_0, none_type_0)
    bytes_0 = b""
    dict_0 = {
        bytes_0: bytes_0,
        none_type_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_1 = module_0.find_shortest_path(dict_0, bytes_0, bytes_0)
    var_2 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_1 = {bytes_0: bytes_0}
    var_3 = module_0.find_shortest_path(dict_1, bytes_0, dict_1)
    var_4 = module_0.find_all_path(var_2, dict_1, bytes_0)
    var_5 = module_0.find_path(var_2, var_2, var_2)
    var_6 = module_0.find_all_path(dict_0, none_type_0, var_4)
    str_0 = "NT=vW0#x"
    str_1 = ":hC2rJ`D\\P-4r-\x0b_`VHG"
    var_7 = module_0.find_path(dict_0, bytes_0, str_1, var_5)
    module_0.find_path(str_0, var_4, var_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b"\xe1K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    var_0 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_0 = {bytes_0: bytes_0, bytes_0: var_0}
    var_1 = module_0.find_path(dict_0, bytes_0, var_0)
    none_type_0 = None
    module_0.find_all_path(bytes_0, none_type_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = "!"
    dict_0 = {str_0: str_0, str_0: str_0}
    none_type_0 = None
    var_0 = module_0.find_all_path(dict_0, str_0, none_type_0)
    none_type_1 = None
    var_1 = module_0.find_all_path(none_type_1, none_type_1, none_type_1)
    bytes_0 = b"\xe1*K\x95)\xfd\xa0\xc2;\xc0s\xbc\x8a\xe2\xa7\xef"
    dict_1 = {
        bytes_0: bytes_0,
        none_type_1: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_2 = module_0.find_shortest_path(dict_1, bytes_0, bytes_0)
    var_3 = module_0.find_shortest_path(bytes_0, bytes_0, bytes_0)
    dict_2 = {bytes_0: bytes_0}
    var_4 = module_0.find_shortest_path(dict_2, bytes_0, dict_2)
    var_5 = module_0.find_path(var_3, dict_2, dict_2, var_3)
    var_6 = module_0.find_shortest_path(var_4, var_4, var_4)
    var_7 = module_0.find_all_path(var_3, dict_2, bytes_0)
    var_8 = module_0.find_path(var_3, var_3, var_3)
    var_9 = module_0.find_all_path(dict_1, none_type_1, var_7)
    list_0 = [dict_1, str_0]
    module_0.find_path(none_type_0, dict_2, list_0)


def test_case_13():
    none_type_0 = None
    none_type_1 = None
    var_0 = module_0.find_all_path(none_type_1, none_type_1, none_type_1)
    bytes_0 = b"\x9cF\xf4\t*:\x89U\xb9\x12\xfc\xb3\xce\xf1"
    dict_0 = {bytes_0: bytes_0, none_type_1: var_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_1 = module_0.find_shortest_path(none_type_0, none_type_0, none_type_0)
    var_2 = module_0.find_all_path(dict_0, none_type_1, var_1)
    var_3 = module_0.find_shortest_path(dict_0, none_type_0, var_1)
    float_0 = -934.7433735150169
    var_4 = module_0.find_path(var_2, float_0, float_0)


def test_case_14():
    none_type_0 = None
    var_0 = module_0.find_all_path(none_type_0, none_type_0, none_type_0)
    bytes_0 = b"\x9cF\xf4\t*:\x89U\xb9\x12\xfc\xb3\xce\xf1"
    dict_0 = {bytes_0: bytes_0, none_type_0: var_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_1 = module_0.find_shortest_path(none_type_0, none_type_0, none_type_0)
    var_2 = module_0.find_shortest_path(dict_0, none_type_0, var_1)
