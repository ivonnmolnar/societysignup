import os

def write_gogle(firstname, lastname, email):
    with open("google_contacts.csv", "a") as file:
        #if empty - #initializing the file w headers
        if os.path.getsize("google_contacts.csv") == 0:
            file.write("Name, Email\n")

        file.write(firstname + " " + lastname + "," + email + "\n")

def write_info(firstname, lastname, email, id, subject, year):
    with open("contacts.csv", "a") as file:
        #if empty - #initializing the file w headers
        if os.path.getsize("contacts.csv") == 0:
            file.write("Name, Email, Student ID, Subject, Year\n")

        file.write(firstname + " " + lastname + "," + email + "," + id + "," + subject + "," + year + "\n")
