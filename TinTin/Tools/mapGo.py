import sys
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
from tintin import TinTin
import os
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

areaName = sys.argv[1]
notelist = sys.argv[2]
results = None

results = db3k.select_one("SELECT * FROM MapInterests WHERE RoomSymbol=%s AND AreaName=%s", [notelist, areaName])
if results:
    TinTin.execute("#map run " + str(results[2]))
else:
    results = db3k.select_one("SELECT * FROM MapInterests WHERE Note=%s AND AreaName=%s", [notelist, areaName])
    TinTin.showme("#map run {{roomnote} {" + notelist + "}}")
    TinTin.execute("#map run {{roomnote} {" + notelist + "}}")

db3k.dispose()
