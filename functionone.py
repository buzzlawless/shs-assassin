import csv
import random


def import_csv(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)
    list_to_write.pop(0) #removes headers
    for i in range(0,len(list_to_write)-2): #removes duplicates
        if list_to_write[i][1] == list_to_write[i+1][1]:
            list_to_write.pop(i)


def generate_IDs(list_to_id):
    ids = random.sample(range(len(list_to_id)), len(list_to_id)) #generates a list of unique random numbers from 0 to the number of participants
    for i in range(0,len(list_to_id)):
        list_to_id[i].append(ids[i])


def export_csv(list_to_export, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_to_export)

master = list()  
import_csv(master, 'responses1.csv') #the latter parameter should be changed to match the name of the csv file
generate_IDs(master)
'''
master is a list of lists
master[n] is the Nth participant's data
master[n][0] is their timestamp
master[n][1] is their name
master[n][2] is their email
master[n][3] is their ID
'''
export_csv(master, 'masterlist.csv')
