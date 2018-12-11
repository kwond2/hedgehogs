import csv
#import sys


### Single #: deprecated/unused
### Double #: Test Cases
### Triple #: Notes

### Takes SimFin Data and creates a CSV file "fundamentalsWuuid.csv" included with UUID files

def main():
	c_uuid = ""
	##x = 0
	##y = 0

	newunderscore = open('fundamentalsWuuid.csv','w')
	with open('underscore.csv', 'r') as readdata:
	    reader = csv.reader(readdata)
	    next(reader)  # Skip the header row.
	    for row in reader:
	    	##x+=1 			#	/// Just a quick 10 INSERT calls to check if working
	    	##if x == 10:
	    	##	break
	    	uuid_list = open("uuid_list.txt", 'r')
	    	uuidread = csv.reader(uuid_list)
	    	for item in uuidread:
	    	#	y+=1
	    		if item[2] == row[1]:   # if the ticker IDs match
	    			c_uuid = item[0]	# set c_uuid to that company UUID
	    			break
	    	newunderscore.write("{},{},{},{},{}\n".format(c_uuid, row[2], row[3], row[4], row[0]))
	    	#y = 0
	#conn.commit()
	newunderscore.close()
	readdata.close()
	uuid_list.close()



if __name__ == '__main__':

	main()