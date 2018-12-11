
filepath = 'openlist.csv'  
fp = open(filepath)
#replace .csv indicator spaces with underscores..

line = fp.readline()
cnt = 0
while line:
	cnt +=1
	line = line.strip()
	print('{} {}'.format(cnt, line.replace(" ", "_")))#, end = " ")
	#print("text,")
	line = fp.readline()


fp.close()

