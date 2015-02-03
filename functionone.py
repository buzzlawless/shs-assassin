import csv
import random


def importCSV(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)

input_data = list()  
importCSV(input_data, 'responses1.csv')
input_data.pop(0)
input_data.pop(0)
input_data.pop(0)
ids = random.sample(range(len(input_data)), len(input_data))
for i in range(0,len(input_data)):
    input_data[i].append(ids[i])
    print(input_data[i])
