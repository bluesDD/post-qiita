import pytest
import pathlib

def increment(x):
    return x + 1

def throw_valueerror():
    print(pathlib.Path)
    raise ValueError("This is test")

class TestCase:
    def test_increment(self):
        assert increment(1) == 2, "足し算が違ってる"

    def test_increment_exception(self):
        with pytest.raises(ValueError) as error_info:
            throw_valueerror()
        assert str(error_info.value) == "This is test"
