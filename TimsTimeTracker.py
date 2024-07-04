import json
import math
from datetime import datetime
open_json = open("Priorities.json")
load_priorities = json.load(open_json)
now = datetime.now()
def notify_user():
    for key in load_priorities:
        print(key)
        #Change this later
        if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) == str(load_priorities[key][2]) or (now.strftime("%B") + " " + str((int(now.strftime("%d")) - 1)) + " " + now.strftime("%Y")) == str(load_priorities[key][2]):
            return "HEADS UP! {} is due PRETTY soon!".format(key)
class Priority():
    def __init__(self, name, event_type, date, priority_number):
        self.name = name
        self.event_type = event_type
        self.date = date
        self.priority_number = priority_number
class Event(Priority):
    pass
class Assignment(Priority):
    pass
program_running = True
print("Welcome to Tim's Time Tracker!")
print("Today is " + now.strftime("%A") + ", " +  now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y"))
print("It's currently {} in your time.".format(now.strftime("%I") + ":" + now.strftime("%M") + " " + now.strftime("%p")))
while program_running == True:
    notify_user()
    what_to_do = input("What do you want to do? \n [A] Set Event \n [B] Set Assignment \n [C] Change Event/Assignment \n")
    if "A" in what_to_do.upper():
        pass
    elif "B" in what_to_do.upper():
        pass    
    elif "C" in what_to_do.upper():
        pass
    else: 
        print("That's not a valid option.")
        continue