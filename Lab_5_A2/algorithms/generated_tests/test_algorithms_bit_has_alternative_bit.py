# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import algorithms.bit.has_alternative_bit as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.has_alternative_bit(object_0)


def test_case_1():
    bool_0 = False
    var_0 = module_1.has_alternative_bit(bool_0)
    var_1 = module_1.has_alternative_bit_fast(bool_0)
    assert var_1 is True


def test_case_2():
    bool_0 = False
    var_0 = module_1.has_alternative_bit_fast(bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_1.has_alternative_bit_fast(bool_0)
    assert var_0 is True
    var_1 = module_1.has_alternative_bit_fast(var_0)
    assert var_1 is True
    bytes_0 = b"f\xe3\xf6\x0b\xf4\xbf\x9f\x820"
    module_1.has_alternative_bit_fast(bytes_0)


def test_case_4():
    int_0 = 2
    var_0 = module_1.has_alternative_bit(int_0)
    assert var_0 is True


def test_case_5():
    int_0 = -6
    var_0 = module_1.has_alternative_bit(int_0)
    assert var_0 is False
