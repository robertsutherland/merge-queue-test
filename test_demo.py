from pytest import mark


ANSWER_TO_THE_GREAT_QUESTION = 42

@mark.skip(reason="Blah")
def test_example():
    ''' This test serves as a representative for more meaningful tests. '''
    assert ANSWER_TO_THE_GREAT_QUESTION == 422, \
        "What's the answer to the great question?"
