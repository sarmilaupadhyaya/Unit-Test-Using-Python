import math
import pytest

@pytest.fixture(scope='module', params=[2,4,5])
def square(request):

    yield request.param ** 2


def test_area(square):

    assert (square * math.pi) > 0
