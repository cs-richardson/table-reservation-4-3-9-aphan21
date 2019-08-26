#This program checks if a person is in the reservation list in a restaurant
#You must be in the reservation list to get a table 

name = input ("Welcome! What is your name?")

reservation_name = ["Ann","Claire","Steven","Jason"]
if name == reservation_name[0]:
    print("Right this way!")
elif name == reservation_name[1]:
    print("Right this way!")
elif name == reservation_name[2]:
    print("Right this way!")
elif name == reservation_name[3]:
    print("Right this way!")
else:
    print("Sorry, we don't have a reservation under that name.")
