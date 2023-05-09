# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from datetime import datetime


FILENAME = './list.json'
READ_MODE = 'r'
WRITE_MODE = 'w'
TIME_FORMAT = '%H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'
NAME_FIELD = 'name'
DATE_FIELD = 'date'
BUSY_FIELD = 'busy'
STARTTIME_FIELD = 'startTime'
TIMEWORKED_FIELD = 'timeWorkedInMinutes'
ALL_FIELDS = [
    (NAME_FIELD, ""),
    (BUSY_FIELD, False),
    (STARTTIME_FIELD, datetime.now().strftime(TIME_FORMAT)),
    (TIMEWORKED_FIELD, 0),
    (DATE_FIELD, datetime.now().strftime(DATE_FORMAT))
    ]
DEFAULT_ENCODING = 'UTF-8'
