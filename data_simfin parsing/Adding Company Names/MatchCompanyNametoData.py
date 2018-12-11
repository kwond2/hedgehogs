import csv
#import sys


def main():
	c_name = ""


	companycsv = open('company_info.csv','r')
	c_info_with_names_itr = open('company_info_with_names.csv','w')
	with open('constituents.csv', 'r') as companylist:
	    companylist_itr = csv.reader(companylist)
	    companycsv_itr = csv.reader(companycsv)
	    next(companylist_itr)  # Skip the header row/// Symbol -- Name -- Sector
	    for row in companycsv_itr:
	    	for item in companylist_itr:
	    	#	y+=1
	    		if item[0] == row[1]:   # if the ticker IDs match
	    			c_name = item[1]	# set c_uuid to that company UUID
	    			break
	    	c_info_with_names_itr.write("{},{},{}\n".format(row[0], row[1], c_name))


	companycsv.close()
	c_info_with_names_itr.close()
	companylist.close()



if __name__ == '__main__':

	main()