import os

def write_gogle(firstname, lastname, email):
    with open("google_contacts.csv", "a") as file:
        #if empty - #initializing the file w headers
        if os.path.getsize("google_contacts.csv") == 0:
            file.write("Name, Email\n")

        file.write(firstname + " " + lastname + "," + email + "\n")
