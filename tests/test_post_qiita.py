from post_qiita import __version__
import os
from post_qiita.get_posts import get_posts, get_md_filenames, cat_file

# このテストファイルのディレクトリ
directory = os.path.dirname(__file__)
# 実行されている作業ディレクトリ
current_directory = os.getcwd()

# テスト用のmdファイル
test_md_file = "test.md"

test_text_in_mdfile = "This is test."

# test用md以外のファイル
test_py_file = "__init__.py"

def test_version():
    assert __version__ == '0.1.0'

def test_can_get_directory():
    assert get_posts(directory) == current_directory

def test_get_files_current_directory():
    assert (test_md_file in get_md_filenames(directory)) == True

def test_get_only_md_files_current_directory():
    assert (test_md_file in get_md_filenames(directory)) == True
    assert (test_py_file in get_md_filenames(directory)) == False

def test_cat_file():
    assert cat_file(current_directory + "/tests/" + test_md_file) == [test_text_in_mdfile]

def test_create_file(tmpdir):
    i = tmpdir.mkdir("tmp").join("test.txt")
    i.write("This is content")
    assert i.read() == "This is content"
    assert len(tmpdir.listdir()) == 1
