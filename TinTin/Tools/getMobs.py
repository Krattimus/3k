import os
import sys
from tintin import TinTin
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

area = sys.argv[1]

results = db3k.select_all("SELECT DISTINCT MobName,Rating FROM MapMobs Where AreaName LIKE %s", [area]);

for row in results:
  rooms = db3k.select_all("SELECT DISTINCT RoomID FROM MapMobs Where MobName LIKE %s AND AreaName LIKE %s", [row[0], area]);
  display = ""
  for room in rooms:
    if display == "":
      display += str(room[0])
    else:
      display += "," + str(room[0])
  TinTin.showme("<088>   <039>" + str(row[0]) + "<088> (<139>" + str(row[1]) + "<088>) found in rooms [<139>" + display + "<088>]")
  

db3k.dispose()
