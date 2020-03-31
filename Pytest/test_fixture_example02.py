import pytest
import numpy as np

@pytest.fixture
def example_array2():

    return np.array([2]*10)

def test_one(example_array0, example_array2):

    dot = np.dot(example_array0, example_array2)
    
    assert dot == 0



