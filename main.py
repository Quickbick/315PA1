import constant
from apyori import apriori
import csv
import pandas as pd

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

        new_file = new_file + '\n' + new_str + '\n'

#writes into new file as even csv
with open('./browsing-data-csv.txt', 'w+') as f:
    f.write(new_file)

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

for i in range (0, 1000):
    records.append([str(data.values[i,j]) for j in range(0,30)])

productRules = apriori(records, min_support=0.0032, min_confience = 0.4, min_lift = 3, min_length = 2)
productResults = list(productRules)

for item in productResults:

    pair = item[0]
    items = [x for x in pair]
    print(items[0] + "->" + items[1])
    print(" Confidence: " + str(item[2][0][2]))