import pytest
from random import randint
from exercise_code import sort_mass


@pytest.mark.repeat(100)
def test_random():
    my_list = []
    my_list.append(randint(-1000,1000))
    x = sort_mass(my_list.copy())
    my_list.sort()
    assert x == my_list

@pytest.mark.repeat(100)
def test_max():
    my_list = []
    my_list.append(randint(100000000000000000, 1000000000000000000))
    x = sort_mass(my_list.copy())
    my_list.sort()
    assert x == my_list
