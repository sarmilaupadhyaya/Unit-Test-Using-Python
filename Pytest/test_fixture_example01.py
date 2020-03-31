import pytest
import numpy as np

@pytest.fixture
def example_array1():

    return np.array([1]*10)

def test_one(example_array0, example_array1):
    
    dot = np.dot(example_array0, example_array1)

    assert dot == 0





