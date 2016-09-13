from pymongo import MongoClient
import csv

client = MongoClient()
db = client.FUNTTEL

def connectDb():
    client = MongoClient()
    db = client.FUNTTEL
    return db;

def updateDB():
    row_list = []
    csvfile = open('C:/Users/luisdeolpy/Documents/Python Scripts/OpenDataBR/FUNTTEL/indicadores-funttel.csv')
    spamreader = csv.reader (csvfile, delimiter = ';')
    headers = next(spamreader, None)
    nothing = next(spamreader, None)
    title = ""
    for row in spamreader:
        full_title = row[0] + '-' + row[1]
        title = row[0].replace(' ', '').replace('-','').split('(')[0]
        desc = row[1].replace(' ', '').replace('-','').split('(')[0]
        db[title+desc].insert_one({
            "Description": desc,
            "2012": row[2],
            "2013": row[3],
            "2014": row[4]
        })
        row_list.append(row)


