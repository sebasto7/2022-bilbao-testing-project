import pytest, logistic_map
import numpy as np
from math import isclose

@pytest.mark.parametrize('x, r, expected',[(0.1, 2.2,0.198),(0.2, 3.4,0.544),(0.75, 1.7,0.31875)])

def test_population_grow(x,r,expected):
    # When
    output = logistic_map.logistic_map(x,r)
    # Then
    assert isclose(output, expected)


#SEED = 42
#random_state = np.random.RandomState(SEED)
#rand_list =

#@pytest.mark.parametrize('x',rand_list)
#def test_random_convergence(it = 100000,  x, r = 3.8, expected = 0.33):
    #ouput = logistic_map.iterate_f(it,x,r)
    #assert isclose(outpute, expected)

def test_chaos():
    X0 = 0.1
    it = 100000
    r = 3.8
    output = logistic_map.iterate_f(it,X0,r)
    assert output.all() >=0 and output.all() <=1


def test_unique():
    X0 = 0.1
    it = 100000
    r = 3.8
    l = 1000
    output = logistic_map.iterate_f(it,X0,r)
    assert len(np.unique(output[-l:])) == l
