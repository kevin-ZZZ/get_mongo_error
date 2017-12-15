#!/usr/bin/env python
import os
import sys
from gme.views import connectMongod,getAverageKeySet
from threading import Thread

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GME.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    db = connectMongod()

    t1 = Thread(target=getAverageKeySet(db))
    t1.start()
    t1.join()

