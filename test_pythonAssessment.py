from pythonAssessment import (
    count_specific_word,
    identify_most_common_word,
)
def test_count_specific_word():
    text = "Apple pie apple pie Apple"
    assert count_specific_word(text, "apple") == 3


def test_identify_most_common_word():
    text = "pie apple pie pie machine"
    assert identify_most_common_word(text) == "pie"
    