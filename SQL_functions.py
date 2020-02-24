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
               (block, lot, cd, zipcode, address, zonedist1, schooldist, splitzone, bldgclass, landuse, ownertype, ownername, lotarea
               lottype, numfloors, unitsres, yearbuilt, yearalter1, yearalter2, histdist, landmark, builtfar, residfar, how_many, lat, lng)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")

    cursor.executemany(add_row, tuples)
    cnx.commit()


def insert_sale(tuples):

    add_row = ("""INSERT INTO manhattan_sales
               (block, lot, neighborhood, building_class_category, building_class, address, apt_number, res_units, comm_units, land_sq_feet, gross_sq_feet, year_built, sale_date, sale_price)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")

    cursor.executemany(add_row, tuples)
    cnx.commit()
