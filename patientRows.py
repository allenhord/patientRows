import csv

def headingToInt(arg):
        switcher = {
        "Accession #": 1,
        "Patient Last Name": 3,
        "Patient First Name": 4,
        "Patient Birth Date": 5,
        "Patient Gender": 6,
        "Race": 7,
        "Ethnicity": 8,
        "Patient State": 12,
        "Patient Zip Code": 13,
        "Collected Date": 14,
        "Source": 16,
        }
        return switcher.get(arg)

def raceSwitch(arg):
        switcher = {
        "Black": "B",
        "Black/African American": "B",
        "White": "W",
        "Hispanic": "H",
        "Asian": "A",
        }
        return switcher.get(arg)

def nameCombine(last, first):
        fullname = (last + ", " + first)
        return fullname

assNumbers = []
with open(r'assNumbers.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        line_count = 0
        for row in csv_reader:
                row = str(row)
                row = row.strip('[]\'')
                assNumbers.append(row)
                line_count+=1
csv_file.close()

#clear outputfile
with open(r'output.csv', mode='w', newline='') as csv_new:
        csv_new.truncate()
        csv_new.close()

columnDict = {}
with open(r'input.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
                for i in range(len(row)):
                        columnDict[headingToInt(row[i])] = i
        
                break
	for row in csv_reader:
		for i in assNumbers:
                        if row[columnDict[1]] == i: #check for matching accession numbers
                                rowlist = []
                                j=0
                                while j < 15:
                                        rowlist.append("")
                                        j+=1
                                
                                k = 0
                                while k < 15:
                                        try:
                                                rowlist.insert(k,((row[columnDict[(k+1)]])))
                                        except:
                                                print("Skipping empty cell")
                                        k+=1
                                        
                                #race handling, USA default country, remove "-" from zip codes
                                rowlist[6] = raceSwitch(rowlist[6])
                                if raceSwitch(rowlist[6]) == "Hispanic":
                                        rowlist[7] = raceSwitch(rowlist[6])
                                rowlist.pop(7)
                                rowlist[8] = "USA"
                                rowlist[11] = rowlist[11].strip('-')
                                rowlist[12] = rowlist[12][:-6]
                                
                                with open(r'output.csv', mode='a', newline='') as csv_new:
                                        csv_writer = csv.writer(csv_new)
                                        csv_writer.writerow(rowlist)
csv_file.close()
print("Complete!")
input("Press Enter to continue...")
