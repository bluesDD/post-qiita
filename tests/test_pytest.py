import pytest
import pathlib

def increment(x):
    return x + 1

def throw_valueerror():
    print(pathlib.Path)
    raise ValueError("This is test")

def open_file(file):
    with open(file) as f:
        return f.read()

class TestCase:
    def test_increment(self):
        assert increment(1) == 2, "足し算が違ってる"

    def test_increment_exception(self):
        with pytest.raises(ValueError) as error_info:
            throw_valueerror()
        assert str(error_info.value) == "This is test"

    def test_open_file(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "heelo.txt"
        p.write_text("hello")
        assert p.read_text() == "hello"

