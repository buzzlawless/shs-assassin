import csv
import random


def importCSV(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)

input_data = list()  
importCSV(input_data, 'responses1.csv')
input_data.pop(1)
input_data.pop(1)
ids = random.sample(range(len(input_data)-1), len(input_data)-1)
print(ids)
for i in range(1,len(input_data)):
    input_data[i].append(ids[i-1])
    print(input_data[i])
