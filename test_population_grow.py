import pytest, logistic_map
import numpy as np
from math import isclose

@pytest.mark.parametrize('x, r, expected',[(0.1, 2.2,0.198),(0.2, 3.4,0.544),(0.75, 1.7,0.31875)])

def test_population_grow(x,r,expected):
    # When
    output = logistic_map.logistic_map(x,r)
    # Then
    assert isclose(output, expected)


SEED = 42
random_state = np.random.RandomState(SEED)
rand_list =  

#@pytest.mark.parametrize('x',rand_list)
def test_random_convergence(it=14,  x, r=1.5, expected=0.33):
    ouput = logistic_map.iterate_f(it,x,r)
    assert isclose(outpute, expected)

    
