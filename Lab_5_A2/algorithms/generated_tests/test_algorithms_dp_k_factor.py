# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dp.k_factor as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {}
    var_0 = module_0.find_k_factor(bool_0, bool_0)
    assert var_0 == 0
    tuple_0 = (bool_0, dict_0, bool_0, dict_0)
    module_0.find_k_factor(tuple_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.find_k_factor(bool_0, bool_0)
    assert var_0 == 0
    none_type_0 = None
    var_1 = module_0.find_k_factor(bool_0, var_0)
    assert var_1 == 26
    module_0.find_k_factor(none_type_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_k_factor(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.find_k_factor(bool_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.find_k_factor(bool_0, bool_0)
    assert var_1 == 0
    var_2 = module_0.find_k_factor(bool_0, bool_0)
    assert var_2 == 0
    var_3 = module_0.find_k_factor(var_0, bool_0)
    assert var_3 == 0
    var_4 = module_0.find_k_factor(var_3, var_1)
    assert var_4 == 0
    var_5 = module_0.find_k_factor(var_1, var_2)
    assert var_5 == 0
    var_6 = module_0.find_k_factor(var_4, var_2)
    assert var_6 == 0
    var_7 = module_0.find_k_factor(var_2, bool_0)
    assert var_7 == 0
    var_8 = module_0.find_k_factor(var_1, var_7)
    assert var_8 == 0
    var_9 = module_0.find_k_factor(var_1, var_1)
    assert var_9 == 0
    var_10 = module_0.find_k_factor(bool_0, var_3)
    assert var_10 == 26
    var_11 = module_0.find_k_factor(var_10, bool_0)
    assert var_11 == 309801001842261997850579881527297
    var_12 = module_0.find_k_factor(var_10, var_10)
    assert var_12 == 0
    var_13 = module_0.find_k_factor(bool_0, var_3)
    assert var_13 == 26
    none_type_0 = None
    module_0.find_k_factor(none_type_0, var_13)
