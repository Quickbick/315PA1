from array import array
from constant import SUPPORT
import constant.py

class Product:
    name: str
    count: int

def aPriori(infile):
    productStore = []
    instream = open(infile, 'r')
    line = instream.readline()
    while (line != 0):
        items = line.split
        for item in items:
            for product in productStore:
                if (item == product):
                    product.count += 1
                    break
                else:
                    productTemp = Product()
                    productTemp.name = item
                    productTemp.count = 1
                    productStore.append(productTemp)
    frequentProducts = []
    for product in productStore:
        if (product.count >= SUPPORT):
            frequentProducts.append(product.name)
    for product in frequentProducts:
        print(product)