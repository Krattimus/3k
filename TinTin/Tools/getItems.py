import os
import sys
from tintin import TinTin
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

results = db3k.select_all("SELECT * FROM MapItems WHERE MapItemID<154 ORDER BY MapItemID DESC LIMIT 1000")

for result in results:
  TinTin.execute(".addItemToItemsList {"+ str(result[2])+"} {"+str(result[5])+"} {"+str(result[4])+"} {"+str(result[3])+"}")
  
db3k.dispose()
