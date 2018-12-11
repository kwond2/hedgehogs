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


#~~~~~~~~~~~~~~~~~~~ take data from table "end_of_day_data_table" into separate file to access//need to modify code that 
#~~~~~~~~~~~~~~~~~~~ webscrapes the data so we don't have to keep updating eod this way--temporary fix
	row_count = 0
	cur.execute("SELECT * FROM end_of_day_data_table")
	f = open("eod_without_uuid.csv", 'w')
	for row in cur:
		f.write(str(row[1]))
		f.write(',')
		f.write(str(row[2]))
		f.write(',')
		f.write(str(row[3]))
		f.write(',')
		f.write(str(row[4]))
		f.write(',')
		f.write(str(row[5]))
		f.write(',')
		f.write(str(row[6]))
		f.write(',')
		f.write(str(row[7]))
		f.write("\n")
	f.close()
#~~~~~~~~~~~~~~~~~~~



	c_uuid = ""
	x = 0
	y = 0

	eoddatawithuuid = open('eod_with_uuid.csv','w')
	with open('eod_without_uuid.csv', 'r') as readdata:
	    reader = csv.reader(readdata)
	    for row in reader:
	    	x+=1 			#	/// Just a quick 10 INSERT calls to check if working
	    	#if x == 10:
	    	#	break
	    	uuid_list = open("uuid_list.txt", 'r')
	    	uuidread = csv.reader(uuid_list)
	    	for item in uuidread:
	    	#	y+=1
	    		if item[1] == row[0]:   # if the ticker matches
	    			c_uuid = item[0]	# set c_uuid to that company UUID
	    			break
	    	eoddatawithuuid.write("{},{},{},{},{},{},{},{}\n".format(c_uuid, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))	
	eoddatawithuuid.close()
	readdata.close()
	uuid_list.close()



if __name__ == '__main__':

	main()
