import os

def get_posts(directory):
    default_path = os.getcwd()
    return default_path


def get_filenames(directory):
    return os.listdir(directory)

def cat_file(file_path):
    with open(file_path) as f:
      return [line.strip() for line in f.readlines()]    
  
if __name__ == "__main__":
  get_posts("hoge")
