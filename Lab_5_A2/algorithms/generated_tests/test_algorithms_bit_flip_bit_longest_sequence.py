# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import algorithms.bit.flip_bit_longest_sequence as module_0


def test_case_0():
    int_0 = 1703
    var_0 = module_0.flip_bit_longest_seq(int_0)
    assert var_0 == 4


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.flip_bit_longest_seq(tuple_0)
    assert var_0 == 1
    var_1 = module_0.flip_bit_longest_seq(tuple_0)
    assert var_1 == 1
    var_2 = module_0.flip_bit_longest_seq(var_0)
    assert var_2 == 2
