from post_qiita import __version__
import os
from post_qiita.get_posts import get_posts, get_filenames

directory = os.path.dirname(__file__)
target_dir = os.getcwd()

def test_version():
    assert __version__ == '0.1.0'

def test_can_get_directory():
    assert get_posts(directory) == target_dir

def test_get_files_current_directory():
    assert (os.path.basename(__file__) in get_filenames(directory)) == True
