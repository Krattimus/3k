import os
import sys
from tintin import TinTin
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

area = sys.argv[1]

results = db3k.select_all("SELECT * FROM MapInterests WHERE AreaName=%s", [area]);

TinTin.showme("<094>------- Interests in " + str(area) + " ------ ")
for row in results:
  TinTin.showme("<088>   <039>" + str(row[1]) + "<088> in room [<039>" + str(row[2]) + "<088>] marked with [<139>" + str(row[4]) + "<088>]")

TinTin.showme("<094>---------------------")

db3k.dispose()
