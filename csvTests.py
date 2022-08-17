import csv
from lib2to3.pgen2.token import NEWLINE
import os

def csvHandler(path, newzeile):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, newline='')
        header = []
        header = next(csvreader) #returned die erste Zeile und springt zur nächsten
        datacore = []
        for row in csvreader:
            datacore.append(row)
    print("header:", header)
    print("daten:", datacore)
    if newzeile != False or newzeile != '':
        csvwriter = csv.writer(csvfile)
        teile = newzeile.split(' ')
        neueAttribute = []
        for teil in teile:
            neueAttribute.append(teil)
        csvwriter.writerow(neueAttribute)
        
    return "it worked"

pfad = input("Bitte gib Dateipfad an:")    
daten = input("gib neue Daten für Name, Alter und CoolJaNein an:")  
print(csvHandler(pfad, daten))


print("ENDE")       