# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.compression.elias as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.elias_delta(bool_0)
    assert var_0 == "0"


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
    module_0.elias_generic(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    module_0.binary(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "U.VdD+~#{xFbg"
    module_0.unary(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 3357.0
    list_0 = [float_0, float_0, float_0]
    tuple_0 = (list_0, list_0)
    module_0.elias_gamma(tuple_0)
