import time
import json
import os

from utils._logger import MyLogger

file_name = os.path.basename(__file__)
logger = MyLogger(name=file_name, level="debug").logger


def log_event(log_file: str, event_type, activity, **kwargs):
    unix_timestamp = time.time()
    time_str = (
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        + " UTC"
        + f"{time.timezone / 3600:.0f}"
    )
    event_record = {
        "unix_timestamp": unix_timestamp,
        "local_time": time_str,
        "event_type": event_type,
        "activity": activity,
        **kwargs,
    }
    logger.info(event_record)
    with open(log_file, "r+") as f:
        # Move the pointer to the end of the file before the last closing bracket
        f.seek(0, os.SEEK_END)
        f.seek(f.tell() - 1, os.SEEK_SET)
        # If the file is not empty, add a comma to separate the new record
        if f.tell() > 1:
            f.write(",\n")
        # Write the new event record
        json.dump(event_record, f)
        # Close the JSON array
        f.write("]")


def create_log_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("[]")
