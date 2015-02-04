#This should be run every 5 minutes to check if any kills have been reported in the last five minutes.  If so, update the master list and send an email and tweet.
import csv
import webbrowser
import time
import os
import smtplib


def import_csv(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)
    list_to_write.pop(0) #removes headers


def export_csv(list_to_export, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        list_to_export.insert(0,['Timestamp', 'First and Last Name', 'Email', 'ID']) #adds headers for csv export
        writer.writerows(list_to_export)
        list_to_export.pop(0) #removes headers


def get_target(index):
    if index == len(master)-1:
        return 0
    else:
        return index+1

    
def verify(index):
    assassin_ID = kills[index][1]
    target_ID = kills[index][2]
    for j in range(0,len(master)):
        if assassin_ID == master[j][3] and target_ID == master[get_target(j)][3]:
            return j
    return -1    


def email_next_target(index):
    gmail_user = 'shsassassin15@gmail.com'
    gmail_pwd = ''#password censored since GitHub is public
    FROM = 'shsassassin15@gmail.com'
    TO = [master[index][2]] #must be a list
    SUBJECT = "Your Next Assassin Target"
    TEXT = 'This email is intended for '+master[index][1]+'.  Congratulations on eliminating '+eliminated[1]+'.  Your next target is '+master[get_target(index)][1]+'.  Good luck.'

    # Prepare actual message
    message = '''\From: %s\nTo: %s\nSubject: %s\n\n%s
    ''' % (FROM, ', '.join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')
    
master = list()
kills = list()
webbrowser.open('http://docs.google.com/spreadsheets/d/FILE_ID/export?format=csv') #replace FILE_ID with the ID of the spreadsheet
time.sleep(5) #number of seconds to wait for file to download
import_csv(master, 'masterlist.csv')
import_csv(kills, 'D:\Downloads\Kill Responses - Form Responses 1.csv') #change drive letter
'''
master is a list of lists
master[n] is the Nth participant's data
master[n][0] is their timestamp
master[n][1] is their name
master[n][2] is their email
master[n][3] is their ID
master[n+1] is their target's data (except for the last participant in the list, their target is master[0])

kills is a list of lists
kills[n] is the Nth kill reported
kills[n][0] is the kills' timestamp
kills[n][1] is the ID of the assassin
kills[n][2] is the ID of the target
'''
for i in range(0,len(kills)):
    killer_index = verify(i)
    if killer_index > -1:
        eliminated = master.pop(get_target(killer_index))
        if killer_index == len(master): #if the killer was the last person in master then everyone moves up a spot when their target was popped, hence...
            killer_index -= 1           #... the killer's index must be reduced by 1
        email_next_target(killer_index)
        #email_elimination_message(get_target(killer_index))
        #tweet(killer_index)
os.remove('D:\Downloads\Kill Responses - Form Responses 1.csv') #change drive letter
