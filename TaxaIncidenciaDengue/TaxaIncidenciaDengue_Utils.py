from pymongo import MongoClient
import csv

client = MongoClient()
db = client.TaxasIncidenciasDengue

def connectDb():
    client = MongoClient()
    db = client.TaxasIncidenciasDengue
    return db;

def updateDb():
    csvfile = open('C:/Users/luisdeolpy/Documents/GitHub/OpenDataBR/TaxaIncidenciaDengue/series_historicas_dengue.csv')
    spamreader = csv.reader (csvfile, delimiter = ';')
    headers = next(spamreader, None)
    incidencias = db.IncidenciasPorUF
    title = ""
    for row in spamreader:
        desc = row[0]
        incidencias.insert_one({
            "Description": desc,
            "1990": row[1],
            "1991": row[2],
            "1992": row[3],
            "1993": row[4],
            "1994": row[5],
            "1995": row[6],
            "1996": row[7],
            "1997": row[8],
            "1998": row[9],
            "1999": row[10],
            "2000": row[11],
            "2001": row[12],
            "2002": row[13],
            "2003": row[14],
            "2004": row[15],
            "2005": row[16],
            "2006": row[17],
            "2007": row[18],
            "2008": row[19]
        })
def updateDb_Br():
    csvfile = open('C:/Users/luisdeolpy/Documents/GitHub/OpenDataBR/TaxaIncidenciaDengue/series_historicas_dengue_Brasil.csv')
    spamreader = csv.reader (csvfile, delimiter = ';')
    headers = next(spamreader, None)
    incidencias = db.IncidenciasBrasil
    title = ""
    for row in spamreader:
        desc = row[0]
        incidencias.insert_one({
            "Description": desc,
            "1990": row[1],
            "1991": row[2],
            "1992": row[3],
            "1993": row[4],
            "1994": row[5],
            "1995": row[6],
            "1996": row[7],
            "1997": row[8],
            "1998": row[9],
            "1999": row[10],
            "2000": row[11],
            "2001": row[12],
            "2002": row[13],
            "2003": row[14],
            "2004": row[15],
            "2005": row[16],
            "2006": row[17],
            "2007": row[18],
            "2008": row[19]
        })