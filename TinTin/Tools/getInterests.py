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

area = sys.argv[1];


cursor.execute("SELECT * FROM MapInterests WHERE AreaName='" + str(area) +"'");
results = cursor.fetchall()

TinTin.showme("<094>------- Interests in " + str(area) + " ------ ")
for row in results:
  TinTin.showme("<088>   <039>" + str(row[1]) + "<088> in room [<039>" + str(row[2]) + "<088>] marked with [<139>" + str(row[4]) + "<088>]")

TinTin.showme("<094>---------------------")
cursor.close()
db.close()

