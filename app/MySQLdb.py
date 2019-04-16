#!/usr/bin/env python
from mysql.connector import connect
from selector import selector

class MySQLRepository:
    MYSQL_URI = "db"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = None
    DATABASE_NAME = "EsportsWiki"
    DATABASE_CONFIG_FILE = "./databasedata/config_init.sql"

    def __init__(self):
        self.connector = None
        try:
            self.__connect()
        except Exception as exception:
            print(exception)

    def __connect(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD,
                                 database=self.DATABASE_NAME)

    def __verify_connection(self):
        if self.connector is None:
            self.__connect()

    def getAll(self, table_name):
        self.__verify_connection()
        tb = table_name
        all = selector.getAll(self.connector.cursor(), tb)
        return all

    def getGameByID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()
        return selector.getGameByID(cursor, id)

    def getLeaguebyID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()
        return selector.getLeagueByID(cursor, id)

    def getTeamByID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()
        return selector.getTeamByID(cursor, id)



