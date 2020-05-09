import mysql.connector
from mysql.connector import errorcode

def connector(my_host,my_user,my_pass,my_db):
    try:
        cnx = mysql.connector.connect(user=my_user,database=my_db,password=my_pass,host=my_host)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()