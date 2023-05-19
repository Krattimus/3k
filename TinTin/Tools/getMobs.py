import os
import sys
from tintin import TinTin
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

results = db3k.select_all("SELECT * FROM MapMobs WHERE MapMobID<5200 ORDER BY MapMobID DESC LIMIT 3000")

for result in results:
  TinTin.execute(".addMobToMobsList {"+ str(result[3])+"} {"+str(result[2])+"} {"+str(result[4])+"} {"+str(result[5])+"} {"+str(result[1])+"}")