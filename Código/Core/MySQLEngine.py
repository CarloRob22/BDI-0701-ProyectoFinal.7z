# -*- coding: utf-8 -*-

import mysql.connector
from tabulate import tabulate

class MySQLEngine:

    def __init__(self, config):
        self.connect(config)

    def connect(self,config):
        self.mydb = mysql.connector.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.database
        )

        self.link = self.mydb.cursor()

    def select(self,query):
        self.link.execute(query)
        return self.link.fetchall()

    def printAsTable(self, result, headers=[]):

        if not headers:
            print (tabulate(result))
        else:
            print (tabulate(result, headers=headers))
        
    def saveAsTable(self, fileName, result, headers=[]):

        content = ""
        if not headers:
            content = tabulate(result)
        else:
            content = tabulate(result, headers=headers)

        f = open(fileName, "w")
        f.write(content)
        f.close()

        return True

    def insert(self, query):
        self.link.execute(query)
        self.mydb.commit()

    def update(self, query):
        self.link.execute(query)
        self.mydb.commit()

    def auth():
        pass
     