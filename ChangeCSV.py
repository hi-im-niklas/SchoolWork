import csv;

def GetFileContent(path):
    with open(path, newline='') as csvfile:
        dialect = cvs.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        return reader

path = input("Pfad angeben:\n\n")

csvReader = GetFileContent(path)


print('Was moechten sie mit der Datei machen')
print('[0]Auslesen')
print('[1]Einen Wert hinzufuegen')
print('[2]Einen Wert loeschen')
print('[3]Ein Attribut hinzufuegen')
choiceIndex = input()











