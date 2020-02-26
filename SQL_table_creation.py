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

TABLES = {}
TABLES['manhattan_PLUTO'] = ("""
     CREATE TABLE manhattan_PLUTO (
      lot_id INT NOT NULL AUTO_INCREMENT,
      block varchar(22) NOT NULL,
      lot varchar(22),
      cd varchar(50),
      zipcode varchar(50),
      address varchar(50),
      zonedist1 varchar(50),
      schooldist varchar(50),
      splitzone varchar(50),
      bldgclass varchar(50),
      landuse varchar(50),
      ownername varchar(50),
      lotarea int(22),
      lottype int(22),
      numfloors int(22),
      unitsres int(22),
      yearbuilt int(22),
      yearalter1 int(22),
      yearalter2 int(22),
      histdist varchar(50),
      landmark varchar(50),
      builtfar decimal(10,8),
      residfar decimal(10,8),
      lat decimal(10,8),
      lng decimal(10,8),
      PRIMARY KEY (lot_id)
    ) ENGINE=InnoDB""")

TABLES['manhattan_sales'] = ("""
     CREATE TABLE manhattan_sales (
      sale_id INT NOT NULL AUTO_INCREMENT,
      neighborhood varchar(50),
      block varchar(22) NOT NULL,
      lot varchar(22),
      address varchar(50),
      sale_price int,
      sale_date varchar(50),
      apt_number varchar(22),
      unit_type varchar(22),
      year varchar(22),
      PRIMARY KEY (sale_id)
    ) ENGINE=InnoDB""")



#table creation function accepts a list and exectutes each element
def table_creation(table_list):
    for table_name in table_list:
        table_description = table_list[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

table_creation(TABLES)
