import csv
import random


def inputCSV(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)
    list_to_write.pop(0)    

def generateIDs(list_to_id):
    ids = random.sample(range(len(list_to_id)), len(list_to_id))
    for i in range(0,len(list_to_id)):
        list_to_id[i].append(ids[i])

master = list()  
inputCSV(master, 'responses1.csv')
generateIDs(master)

for element in master:
    print(element)
