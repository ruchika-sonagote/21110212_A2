# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.backtrack.generate_abbreviations as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ""
    var_0 = module_0.generate_abbreviations(str_0)
    var_1 = module_0.generate_abbreviations(str_0)
    var_2 = module_0.generate_abbreviations(str_0)
    var_3 = module_0.generate_abbreviations(var_1)
    dict_0 = {str_0: str_0, str_0: var_1}
    module_0.generate_abbreviations(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    module_0.generate_abbreviations(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ""
    var_0 = module_0.generate_abbreviations(str_0)
    var_1 = module_0.generate_abbreviations(var_0)
    var_2 = module_0.generate_abbreviations(str_0)
    var_3 = module_0.generate_abbreviations(str_0)
    var_4 = module_0.generate_abbreviations(var_3)
    var_5 = module_0.generate_abbreviations(var_1)
    var_6 = module_0.generate_abbreviations(var_0)
    var_7 = module_0.generate_abbreviations(var_2)
    var_8 = module_0.generate_abbreviations(var_0)
    var_9 = module_0.generate_abbreviations(var_7)
    var_10 = module_0.generate_abbreviations(var_4)
    none_type_0 = None
    var_11 = module_0.generate_abbreviations(var_8)
    var_12 = module_0.generate_abbreviations(str_0)
    var_13 = module_0.generate_abbreviations(var_6)
    var_14 = module_0.generate_abbreviations(var_5)
    var_15 = module_0.generate_abbreviations(var_14)
    var_16 = module_0.generate_abbreviations(var_1)
    var_17 = module_0.generate_abbreviations(var_6)
    module_0.generate_abbreviations(none_type_0)
