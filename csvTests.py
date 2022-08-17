import csv
import os

def csvHandler(path):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile)
        header = []
        header = next(csvreader) #returned die erste Zeile und springt zur nächsten
        datacore = []
        for row in csvreader:
            datacore.append(row)
    print("header:", header)
    print("daten:", datacore)
    return "it worked"

pfad = input("Bitte gib Dateipfad an:")      
print(csvHandler(pfad))
print("ENDE")       