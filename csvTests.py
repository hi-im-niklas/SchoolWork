import csv
from lib2to3.pgen2.token import NEWLINE
import os

def csvHandler(path, newzeile):
    with open(path, "r", newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = []
        header = next(csvreader) #returned die erste Zeile und springt zur nächsten
        datacore = []
        for row in csvreader:
            datacore.append(row)
    print("header:", header)
    print("daten:", datacore)
    if newzeile:
        with open(path, "a", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            teile = newzeile.split(' ')
            neueAttribute = ['\n']
            for teil in teile:
                print(teil)
                neueAttribute.append(teil)
            print(neueAttribute)
            csvwriter.writerow(neueAttribute)
        
    return "it worked"

pfad = input("Bitte gib Dateipfad an:")    
daten = input("gib neue Daten für Name, Alter und CoolJaNein an:")  
print(csvHandler(pfad, daten))


print("ENDE")       