import pytest


ANSWER_TO_THE_GREAT_QUESTION = 42

@pytest.skipif(reason="Blah")
def test_example():
    ''' This test serves as a representative for more meaningful tests. '''
    assert ANSWER_TO_THE_GREAT_QUESTION == 42, \
        "What's the answer to the great question?"
