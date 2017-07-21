import csv
'''
with open('BooksRead.csv', "r+", encoding="utf-8")  as inputFile:
    csvReader = csv.reader(inputFile, dialect='excel')
    for row in csvReader:
        print(row)
'''


def rCSV(filename,code):
	# ten file , code la ma nhap 
	# Vi du 'r+','a+','r'
	inputFile =open(filename,code,encoding='utf-8')
	csvReader = csv.reader(inputFile,dialect='excel')
	for row in csvReader:
		print(row)
    #inputFile.close()
def create_csv(filename):
    f = open(filename,'w')
    fieldnames = ['first_name','last_name']
    writer =csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name':'Baked','last_name':'bean'})
    f.close()
if __name__=='__main__':
    create_csv('new.csv')
rCSV('new.csv','r+')
