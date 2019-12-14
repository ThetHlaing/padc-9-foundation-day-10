from db_connector import connect

class Database :
    _cursor,_db = connect()

    @staticmethod
    def base_find(id,table_name):
        Database._cursor.execute(f"Select * from {table_name} where id = {id}")
        result = Database._cursor.fetchone()
        return result

    @staticmethod
    def base_get(table_name):
        Database._cursor.execute(f"Select * from {table_name}")
        return Database._cursor.fetchall()