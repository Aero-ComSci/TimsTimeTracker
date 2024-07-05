import json
import math
from datetime import datetime
open_json = open("Priorities.json")
load_priorities = json.load(open_json)
now = datetime.now()
input_id = 0
priorities_list = []
def notify_user():
    for key in load_priorities:
        print(key)
        #Change this later
        if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) == str(load_priorities[key][2]) or (now.strftime("%B") + " " + str((int(now.strftime("%d")) - 1)) + " " + now.strftime("%Y")) == str(load_priorities[key][2]):
            return "HEADS UP! {} is due PRETTY soon! Date: {}.".format(key, load_priorities[key][2])
class Priority():
    input_id += 1
    def __init__(self, name, event_type, date, priority_number):
        self.name = name
        self.event_type = event_type
        self.date = date
        self.priority_number = priority_number
    def get_priority():
        pass
    #Dunder methods
    def __len__(self):
        return len(priorities_list)
    @abstractmethod
    def __repr__(self):
        return "NAME: {} \n TYPE: {} \n DATE: {} \n PRIORITY NUMBER: {} \n ID: {} \n".format(self.name, self.event_type, self.date, self.priority_number, input_id)
class Event(Priority):
    def __init__(self):
        super().__init__(self.name, "EVENT", self.date, self.priority_number)
    def __repr__(self, reason):
        self.reason = reason
        return super().__repr__(self) + "REASON: {} \n".format(self.reason)
class Assignment(Priority):
    def __init__(self):
        super().__init__(self.name, "ASSIGNMENT", self.date, self.priority_number)
    def __repr__(self, subject):
        self.subject = subject
        return super().__repr__(self) + "SUBJECT: {} \n".format(self.subject)
class PrioritySettings(Priority):
    def __init__(self):
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