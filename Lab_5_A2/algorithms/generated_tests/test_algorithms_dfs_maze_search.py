# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dfs.maze_search as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2405
    set_0 = {int_0, int_0}
    tuple_0 = (set_0,)
    var_0 = module_0.find_path(tuple_0)
    assert var_0 == 0
    module_0.find_path(int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "<>,v"
    module_0.find_path(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    module_0.find_path(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2284
    int_1 = -1433
    tuple_0 = (int_0, int_1)
    tuple_1 = (tuple_0,)
    module_0.find_path(tuple_1)


def test_case_4():
    object_0 = module_1.object()
    set_0 = {object_0}
    list_0 = [set_0, set_0, set_0]
    tuple_0 = (list_0, list_0)
    var_0 = module_0.find_path(tuple_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_5():
    object_0 = module_1.object()
    set_0 = {object_0}
    list_0 = [set_0]
    str_0 = "*opIe_(BGE*SwT*Om^8u"
    tuple_0 = (list_0, str_0)
    var_0 = module_0.find_path(tuple_0)
    assert var_0 == -1
    int_0 = 1294
    module_0.find_path(int_0)


def test_case_6():
    str_0 = "9"
    var_0 = module_0.find_path(str_0)
    assert var_0 == 0
    var_1 = module_0.dfs(str_0, var_0, var_0, str_0, str_0)
    assert var_1 == "9"
    set_0 = {str_0}
    list_0 = [set_0, set_0, set_0]
    tuple_0 = (list_0, list_0)
    var_2 = module_0.find_path(tuple_0)
    assert var_2 == -1


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "9"
    var_0 = module_0.find_path(str_0)
    assert var_0 == 0
    var_1 = module_0.find_path(str_0)
    assert var_1 == 0
    var_2 = module_0.dfs(str_0, var_1, var_1, str_0, str_0)
    assert var_2 == "9"
    var_3 = module_0.dfs(str_0, var_1, var_1, var_1, var_1)
    object_0 = module_1.object()
    set_0 = {object_0}
    list_0 = [set_0, set_0, set_0]
    tuple_0 = (list_0, list_0)
    bool_0 = True
    bool_1 = False
    var_4 = module_0.dfs(tuple_0, bool_0, bool_0, bool_1, var_3)
    assert var_4 == 0
    var_5 = module_0.find_path(tuple_0)
    assert var_5 == -1
    module_0.find_path(var_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "9"
    var_0 = module_0.find_path(str_0)
    assert var_0 == 0
    str_1 = "L"
    var_1 = module_0.dfs(str_0, var_0, var_0, str_0, str_1)
    assert var_1 == "9"
    var_2 = module_0.dfs(str_0, var_0, var_0, var_0, var_0)
    var_3 = module_0.dfs(var_1, var_2, var_0, var_2, var_2)
    object_0 = module_1.object()
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    tuple_0 = (list_0, list_0)
    var_4 = module_0.find_path(tuple_0)
    assert var_4 == -1
    module_0.find_path(set_0)
