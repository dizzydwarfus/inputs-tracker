# read json events into dataframe
# Built-in imports
import json
from pathlib import Path
import sys
import os
import sqlite3

sys.path.append(os.path.abspath(os.path.join("..", "..", "..")))
sys.path.append(os.path.abspath(os.path.join("..", "..")))
sys.path.append(os.path.abspath(os.path.join("..")))
sys.path.append(os.path.abspath(os.path.join(".")))

# Third-party imports
import pandas as pd

# Internal imports
from input_tracker.utils import MyLogger

file_name = Path(__file__).name
logger = MyLogger(name=__file__, level="debug").logger

print(file_name)
