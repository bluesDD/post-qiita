from dotenv import load_dotenv
from os.path import join, dirname
import os

load_dotenv(verbose=True)

dotenv_file = ".env"
dotenv_path = join(dirname(__file__), dotenv_file)
load_dotenv(dotenv_path)

qiita_token = os.environ.get("QIITA_ACCESS_TOKEN")
