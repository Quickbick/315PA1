from apyori import apriori
import csv
import pandas as pd

def Confidence(item):
    return str(item[2][0][2])

def Alphanumeric(item):
    return str(item.items)

index = 0
temp = 0

#opens and reads file using space as delimiter
with open('./browsing-data.txt', 'r') as csvfile:
    productReader = csv.reader(csvfile, delimiter=' ')
    #counts length of longest row
    for row in productReader:
        if (index == 0):
            temp = len(row)
        elif(len(row) > temp):
            temp = len(row)
        index = index + 1

maxLength = temp
index = 0
temp = 0
new_file = ''

#recreates file as even csv
with open('./browsing-data.txt', 'r') as csvfile:
    productReader = csv.reader(csvfile, delimiter=' ')
    for row in productReader:
        new_str = ''
        index += 1

        for x in range(len(row)):
            if (row[x] != ''):
                new_str += row[x]
                new_str += ','
    
        if(len(row) < maxLength):
            diff = maxLength - len(row)
            for x in range(len(row), maxLength):
                new_str += ','

        new_file = new_file + '\n' + new_str

#writes into new file as even csv
with open('./browsing-data-csv.txt', 'w+') as f:
    f.write(new_file)

#opens csv file and sorts data
file = open('./browsing-data-csv.txt', 'r')

with open('./browsing-data-csv.txt') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')

data = pd.read_csv('./browsing-data-csv.txt', header = None)
data.head()

data.dropna()
data.head()
data.info()

records = []
rows = data.shape[0]
cols = data.shape[1]

#unsure if entire data was to be run or just sample
#to change data amount ran change this to desired max line to read
for i in range (0, 31101): 
    records.append([str(data.values[i,j]) for j in range(0, maxLength)])

productRules = apriori(records, min_support=0.0032, min_confience = 0.4, min_lift = 3, max_length = 2)
productResults = list(productRules)

outfile = open("./outfile.txt", 'w')

productResults.sort(key=Alphanumeric)
productResults.sort(reverse=True, key=Confidence)
outfile.write('Output A\n')
i = 0
for item in productResults:
    if (i == 5):
        break
    pair = item[0]
    items = [x for x in pair]
    outfile.write(items[0] + " " + items[1] + " " + str(item[2][0][2]) + '\n')
    i+=1

productRules = apriori(records, min_support=0.0032, min_confience = 0.4, min_lift = 3, max_length = 3)
productResults = list(productRules)
productResults.sort(key=Alphanumeric)
productResults.sort(reverse=True, key=Confidence)
productResults = filter(lambda x: len(x.items) > 2, productResults)

outfile.write('======================\n')
outfile.write('Output B\n')
i = 0
for item in productResults:
    if (i == 5):
        break
    pair = item[0]
    items = [x for x in pair]
    if (items[0] != 'nan' and items[1] != 'nan' and items[2] != 'nan'):
        outfile.write(items[0] + " " + items[1] + " " + items[2] + " " + str(item[2][0][2]) + '\n')
        i+=1