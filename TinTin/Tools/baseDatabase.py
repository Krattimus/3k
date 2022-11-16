import os
import mysql.connector
from mysql.connector import errorcode

class BaseDatabase(object):
    connection = None
    cursor = None

    def __init__(self):
        if self.connection is None:
            filename = os.path.expanduser('~') + '/3kdb.txt'
            file = open(filename, 'r')
            content = file.read().splitlines()
            dbConfig = {'user':'krattimus',
                'password':content[0],
                'host':'localhost',
                'database':'3kDB',
                'autocommit':'True'}

            try:
                self.connection = mysql.connector.connect(**dbConfig)
                self.cursor = self.connection.cursor()
            except Exception as error:
                print("#showme Error: Connection not established {}".format(error))

    def __execute(self, query, parameters=[]):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, parameters)
            return self.cursor
        except Exception as e:
            print("Execute error %d: %s" % (e.args[0], e.args[1]))

    def __select(self, query, parameters):
        return self.__execute(query, parameters)
   
    def execute(self, query, parameters=[]):
        return self.__execute(query, parameters).rowcount
 
    def insert(self, query, parameters=[]):
        self.__execute(query, parameters).rowcount
        self.connection.commit()
        return self.cursor.lastrowid

    def select_all(self, query, parameters=[]):
        self.cursor = self.__select(query, parameters)
        return self.cursor.fetchall()
   
    def select_one(self, query, parameters=[]):
        self.cursor = self.__select(query, parameters)
        return self.cursor.fetchone()
   
    def dispose(self):
        if self.connection:
            self.connection.close()