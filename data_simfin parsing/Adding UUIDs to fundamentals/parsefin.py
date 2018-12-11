import sys
import csv
# takes simfin data and creates a better .csv
csv.field_size_limit(sys.maxsize)
f = open("simfin.csv")
writeout = open("underscore.csv", 'w')
csv_f = csv.reader(f)
indicator = set()


for row in csv_f:

    indicator.add(row[2])
    row[2] = row[2].replace(" ", "_")

    writeout.write("{},{},{},{},{}\n".format(row[0], row[1], row[2], row[3], row[4]))

#for item in indicator: //testing
#	print(item)


f.close()
writeout.close()