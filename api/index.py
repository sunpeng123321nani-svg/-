import os, sys
os.environ.setdefault("DATABASE_PATH", "/tmp/data.db")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app
