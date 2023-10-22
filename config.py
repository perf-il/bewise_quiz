import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

