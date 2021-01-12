from pytest import mark


ANSWER_TO_THE_GREAT_QUESTION = 42


def test_example():
    ''' This test serves as a representative for more meaningful tests. '''
    assert ANSWER_TO_THE_GREAT_QUESTION == 42, \
        "What's the answer to the great question?"

@mark.skip(reason="Why should tests pass anyway?")
def test_another_example():
    assert False, "It don't works!"
