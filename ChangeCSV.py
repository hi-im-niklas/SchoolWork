import csv
import os

def GetFileContent(path):
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        return reader

def ShowContent(csvReader):
    for row in csvReader:
        print(row + '\n')

path = input("Pfad angeben:\n\n")

csvReader = GetFileContent(path)


print('Was moechten sie mit der Datei machen')
print('[0]Auslesen')
print('[1]Einen Wert hinzufuegen')
print('[2]Einen Wert loeschen')
choiceIndex = input()

#nicht sicher ob das klappt aber eigentlich sollte es die Console Clearen
clear = lambda: os.system('cls')
clear()

if(choiceIndex == 0):
    ShowContent(csvReader)
elif(choiceIndex == 1):
    print(1)

elif(choiceIndex == 2):
    print(2)
elif(choiceIndex == 3):
    print(3)

input()







