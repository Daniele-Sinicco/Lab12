from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_country_dao():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct Country FROM go_retailers"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_retailers_dao(country):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT Retailer_code, Retailer_name FROM go_retailers WHERE Country = %s"""
        cursor.execute(query, (country,))
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"]))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_peso_dao(n1, n2, year):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection error")
            return
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select COUNT(DISTINCT g1.Product_number) AS prodotti_comuni
                    from go_daily_sales g1, go_daily_sales g2
                    where g1.Retailer_code = %s and 
                    g2.Retailer_code= %s and 
                    g1.Product_number = g2.Product_number and
                    year(g1.`Date`)=year(g2.`Date`) and 
                    year(g1.`Date`)=%s"""
        cursor.execute(query, (n1, n2, year))
        for row in cursor:
            result.append(row["prodotti_comuni"])
        cursor.close()
        cnx.close()
        return result