import csv
import os

def GetFileContentInformation(path):
    with open(path, "r", newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvreader = csv.reader(csvfile, dialect=dialect)
        datacore = []
        if csv.Sniffer().has_header(csvfile.read(1024)):
            header = []
            header = next(csvreader)
            for row in csvreader:
                datacore.append(row)
            return datacore, header
        else:
            for row in csvreader:
                datacore.append(row)
            return datacore
    
def ManipulateFileContents(path):
    
    
          
pfad = input("Geben Sie den Dateipfad an:")            

print('Was moechten sie mit der Datei machen')
print('[0]Auslesen')
print('[1]Einen Wert hinzufuegen')
print('[2]Einen Wert loeschen')
choiceIndex = input()

if choiceIndex == 0:
    GetFileContentInformation(pfad)