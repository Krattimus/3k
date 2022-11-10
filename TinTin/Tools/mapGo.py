import sys
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
from tintin import TinTin
import os


filename = os.path.expanduser('~') + '/3kdb.txt'
file = open(filename, 'r')
content = file.read().splitlines()


dbConfig = {'user':'krattimus',
            'password':content[0],
            'host':'localhost',
            'database':'3kDB',
            'autocommit':'True'}

try:
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print ("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print ("Database does not exist")
    else:
        print (err)

areaName = sys.argv[1];
notelist = sys.argv[2];

if len(notelist) == 1:
    cursor.execute("SELECT * FROM MapInterests WHERE RoomSymbol='" + str(notelist) +"' AND AreaName='" + str(areaName) +"'")
else:
    cursor.execute("SELECT * FROM MapInterests WHERE Note='" + str(notelist) +"' AND AreaName='" + str(areaName) +"'")

results = cursor.fetchone()

if results:
    TinTin.execute("#map run " + str(results[2]))
else:
    TinTin.showme("#map run {{roomnote} {" + notelist + "}}")
    TinTin.execute("#map run {{roomnote} {" + notelist + "}}")


cursor.close()
db.close()

  

