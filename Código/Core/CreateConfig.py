# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.com, mruizq@unah.hn, fernando.murillo@unah.hn
    @version 0.1.0
    @date 2021/08/09
"""
import configparser

def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("mysql")
    config.set("mysql","host",value="localhost")
    config.set("mysql","port",value="port")
    config.set("mysql","user",value="user")
    config.set("mysql","password",value="password")
    config.set("mysql","database",value="database")
    
if __name__ == '__main__':
    path='config.ini'
    create_config(path)
