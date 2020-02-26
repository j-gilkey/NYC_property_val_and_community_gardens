import mysql.connector
import config
from mysql.connector import errorcode

#set database name
DB_NAME = 'nyc_PLUTO_etc'

#create connection
cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)

#start cursor
cursor = cnx.cursor()

def insert_PLUTO_lot(tuples):

    add_row = ("""INSERT INTO manhattan_PLUTO
               (block, lot, cd, zipcode, address, zonedist1, schooldist, splitzone, bldgclass, landuse, ownername, lotarea,
               lottype, numfloors, unitsres, yearbuilt, yearalter1, yearalter2, histdist, landmark, builtfar, residfar, lat, lng)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")

    cursor.execute(add_row, tuples)
    cnx.commit()

def get_PLUTO():
    get_data = ('(SELECT *  FROM manhattan_PLUTO)')
    cursor.execute(get_data)
    return cursor.fetchall()


def insert_sale(tuples):

    add_row = ("""INSERT INTO manhattan_sales
               (neighborhood, block, lot, address, sale_price, sale_date, apt_number, unit_type, year)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""")

    cursor.executemany(add_row, tuples)
    cnx.commit()
