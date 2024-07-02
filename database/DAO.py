from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def nome1():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as local 
from classification c """
        cursor.execute(query)
        for row in cursor:
            result.append(row["local"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome2():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.Localization as loc1, c2.Localization as loc2, i.GeneID1, i.GeneID2, count(distinct i.`Type`) as peso
from classification c, classification c2, interactions i 
where c2.Localization <> c.Localization and i.GeneID1 = c.GeneID and i.GeneID2 = c2.GeneID 
group by c.Localization, c2.Localization
order by c.Localization, c2.Localization"""
        cursor.execute(query)
        for row in cursor:
            #row["GeneID1"], row["GeneID2"],
            result.append((row["loc1"], row["loc2"], row["peso"]))
            #Prodotto(**row)
        cursor.close()
        conn.close()
        return result
