import csv
import os

def GetFileContentInformation(path):
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvreader = csv.reader(csvfile)
        if csv.Sniffer().has_header(csvfile.read(1024)):
            header = []
            header = next(csvreader)