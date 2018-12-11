import csv
import sys
import psycopg2

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


#CREATE TABLE new_table AS TABLE existing_table;

	cur.execute("ALTER TABLE company_info DROP COLUMN ticker_id;")
	conn.commit()
	cur.execute("ALTER TABLE company_info ADD COLUMN company_name text;")
	conn.commit()


# Direcly use psycopg2 cursor object copy_from function to directly copy data into tables.
	with open('fundamentalsWuuid.csv', 'r') as f:
		cur.copy_from(f, 'fundamentals', sep=',')
	conn.commit()



if __name__ == '__main__':

	main()