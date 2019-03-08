import csv

with open ('import.csv', mode='w') as csvfile:
	writeCSV = csv.writer(csvfile, delimiter=',', 
	quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for i in range(11):
		writeCSV.writerow([i,'John','Titor','PHP',f'{1999+i}',f'john.titor+{1+i}@gmail.com',f'+1 (99)999999{i}'])
