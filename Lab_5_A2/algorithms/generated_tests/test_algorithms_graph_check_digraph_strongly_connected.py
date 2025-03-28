# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.graph.check_digraph_strongly_connected as module_0


def test_case_0():
    bool_0 = True
    graph_0 = module_0.Graph(bool_0)
    var_0 = graph_0.is_strongly_connected()
    assert var_0 is True
    assert len(graph_0.graph) == 1


def test_case_1():
    int_0 = 58
    graph_0 = module_0.Graph(int_0)
    var_0 = graph_0.dfs()
    assert var_0 is False
    assert len(graph_0.graph) == 1
    var_1 = graph_0.add_edge(var_0, var_0)
    var_2 = graph_0.is_strongly_connected()
    assert var_2 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    graph_0 = module_0.Graph(none_type_0)
    graph_0.is_strongly_connected()


def test_case_3():
    bool_0 = True
    graph_0 = module_0.Graph(bool_0)
    var_0 = graph_0.is_strongly_connected()
    assert var_0 is True
    assert len(graph_0.graph) == 1
    var_1 = graph_0.add_edge(graph_0, bool_0)


def test_case_4():
    bool_0 = True
    graph_0 = module_0.Graph(bool_0)
    var_0 = graph_0.add_edge(bool_0, graph_0)
    var_1 = graph_0.is_strongly_connected()
    assert var_1 is True
    assert len(graph_0.graph) == 2


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    graph_0 = module_0.Graph(bool_0)
    var_0 = graph_0.is_strongly_connected()
    assert var_0 is True
    assert len(graph_0.graph) == 1
    var_1 = graph_0.is_strongly_connected()
    assert var_1 is True
    bool_1 = False
    int_0 = 4518
    graph_1 = module_0.Graph(int_0)
    var_2 = graph_1.add_edge(bool_1, bool_0)
    graph_2 = module_0.Graph(var_1)
    assert graph_2.vertex_count is True
    var_3 = graph_1.is_strongly_connected()
    assert var_3 is False
    assert len(graph_1.graph) == 2
    var_2.dfs()
