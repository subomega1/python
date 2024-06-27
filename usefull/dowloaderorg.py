import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler






sourcepath= "C:/Users/sfar/Downloads"
with os.scandir(sourcepath) as entries :
  for entry in entries:
    print(entry.name)