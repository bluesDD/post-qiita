import os

def get_posts(directory):
    default_path = os.getcwd()
    return default_path

def get_md_filenames(directory):
    files = []
    for item in os.listdir(directory):
        base, ext = os.path.splitext(item)
        if ext == ".md":
          files.append(item)
    return files

def cat_file(file_path):
    with open(file_path) as f:
      return [line.strip() for line in f.readlines()]    
  
if __name__ == "__main__":
  get_posts("hoge")
