"""A contact list is a place where you can store a specific contact with other
associated information such as a phone number, email address, birthday, etc.
Write a program that first takes in word pairs that consist of a name and a
phone number (both strings), separated by a comma. That list is followed by a
name, and your program should output the phone number associated with that
name. Assume the search name is always in the list.

Ex: If the input is:

Joe,123-5432 Linda,983-4123 Frank,867-5309
Frank

the output is:

867-5309"""

contact = str(input())
contactList = contact.split(" ")
cont = contactList[0].split(",")
act = contactList[1].split(",")
list = contactList[2].split(",")
contactLIST = [cont + act + list]
name = str(input())


for i in range(len(contactLIST)):
    if (contactLIST[i] == name):
        print(contactLIST[i+1])
