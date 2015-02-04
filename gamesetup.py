import csv
import random
import smtplib


def import_csv(list_to_write, file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_to_write.append(row)
    list_to_write.pop(0) #removes headers from master
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
        list_to_export.insert(0,['Timestamp', 'First and Last Name', 'Email', 'ID']) #adds headers for csv export
        writer.writerows(list_to_export)
        list_to_export.pop(0) #removes headers from master


def get_target(index):
    if index == len(master)-1:
        return master[0]
    else:
        return master[index+1]


def send_email(content, receiver):
    gmail_user = 'shsassassin15@gmail.com'
    gmail_pwd = ''#password censored since GitHub is public
    FROM = 'shsassassin15@gmail.com'
    TO = [receiver] #must be a list
    SUBJECT = "Assassin Information"
    TEXT = content

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


def email_assassins():
    for i in range(0,len(master)):
        body = 'This email is intended for '+master[i][1]+'.  Your target is '+get_target(i)[1]+'.  Your unique ID is '+str(master[i][3])+'.'
        body += '''  This will be your ID for the rest of the game and will NEVER change.
Do not share your ID with anybody on the grounds of disqualification, EXCEPT when you are eliminated.
The ONLY time you will share your ID is when you are assassinated, in which case you MUST give your ID to the person who assassinated you.
'''
        send_email(body, master[i][2])

master = list()
import_csv(master, 'responses1.csv') #the latter parameter should be changed to match the name of the csv file
generate_IDs(master)
random.shuffle(master) #shuffles outer list
'''
master is a list of lists
master[n] is the Nth participant's data
master[n][0] is their timestamp
master[n][1] is their name
master[n][2] is their email
master[n][3] is their ID
master[n+1] is their target's data (except for the last participant in the list, their target is master[0])
'''
export_csv(master, 'masterlist.csv')
email_assassins()
