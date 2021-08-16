# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.com, mruizq@unah.hn, fernando.murillo@unah.hn
    @version 0.1.0
    @date 2021/08/09
"""

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
    
    def auxSelect(self,query):
        self.link.execute(query)
        fetch = self.link.consume_result()
        self.mydb.free_result()
        return fetch

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