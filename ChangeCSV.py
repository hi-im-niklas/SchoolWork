import csv;

def GetFileContent(path):
    with open(path, newline='') as csvfile:
        dialect = cvs.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        return reader

path = input("Pfad angeben:\n\n")

csvReader = GetFileContent(path)

print('done')








