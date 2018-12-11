import csv
import sys
import psycopg2
# Order to run
# Raw FinSim CSV --> parsefin.py --> .py --> AddUUIDtoEODData.py

def connection():
    print('[LOG] Trying to connect')
    try:
        conn = psycopg2.connect("host=206.189.181.163 port=5432 user=rcos password=hedgehogs_rcos dbname=rcos")
        cur = conn.cursor()
        print('[LOG] Connected!')
        return conn, cur
    except:
        print("[ERROR] Unable to connect. Quitting...")


def main():
	(conn, cur) = connection()


	#~~~~~~~~~~Add some more code to drop/delete some unecessary schema.
	#\/\/\/\/\/\/ Original table had incorrect columns + datatypes.



	cur.execute("CREATE TABLE eod (c_id UUID, ticker text, day date, open float, high float, low float, close float, volume float)")
	conn.commit()
#	cur.execute("DROP TABLE eod CASCADE")
#	conn.commit()
#	cur.execute("ALTER TABLE eod DROP COLUMN primary_key;")  #clear all columns in "eod"
#	cur.execute("ALTER TABLE eod DROP COLUMN symbol;")
#	cur.execute("ALTER TABLE eod DROP COLUMN date;")
#	cur.execute("ALTER TABLE eod DROP COLUMN open;")
#	cur.execute("ALTER TABLE eod DROP COLUMN high;")
#	cur.execute("ALTER TABLE eod DROP COLUMN low;")
#	cur.execute("ALTER TABLE eod DROP COLUMN close;")
#	cur.execute("ALTER TABLE eod DROP COLUMN volume;")
#	conn.commit()
#add columns
#	cur.execute("ALTER TABLE eod ADD COLUMN c_id UUID;")
#	cur.execute("ALTER TABLE eod ADD COLUMN ticker text;")
#	cur.execute("ALTER TABLE eod ADD COLUMN day date;")
#	cur.execute("ALTER TABLE eod ADD COLUMN open float;")	
#	cur.execute("ALTER TABLE eod ADD COLUMN high float;")	
#	cur.execute("ALTER TABLE eod ADD COLUMN low float;")	
#	cur.execute("ALTER TABLE eod ADD COLUMN close float;")	
#	cur.execute("ALTER TABLE eod ADD COLUMN volume float;")	
#	conn.commit()


# Direcly use psycopg2 cursor object copy_from function to directly copy data into tables.
	with open('eod_with_uuid.csv', 'r') as f:
		cur.copy_from(f, 'eod', sep=',')
	conn.commit()

#Eod data is formatted as:
# 0 UUID
# 1 TickerName
# 2 Day
# 3 Open
# 4 High
# 5 Low
# 6 Close
# 7 Volume


if __name__ == '__main__':

	main()



#Aside//
# Helpful psql code to check Datatypes
#SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'company_info' AND COLUMN_NAME = 'ticker_id'