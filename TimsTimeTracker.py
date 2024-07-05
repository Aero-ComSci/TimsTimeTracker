import json
import math
from abc import ABC, abstractmethod
from collections import deque
from datetime import datetime
open_json = open("Priorities.json")
load_priorities = json.load(open_json)
now = datetime.now()
#Used for json.dump()
exportation_dict = {
    
}
input_id = 0
global event_info
event_info = []
priorities_list = []
def notify_user():
    for key in load_priorities.keys():
        print(key)
        #Change this later
        if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) == str(load_priorities[key][2]) or (now.strftime("%B") + " " + str((int(now.strftime("%d")) - 1)) + " " + now.strftime("%Y")) == str(load_priorities[key][2]):
            return "HEADS UP! {} is due PRETTY soon! Date: {}.".format(key, load_priorities[key][2])
def setup(type_of_event):
    month_list = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }
    name_of_event = input("What is the name of your {}?".format(type_of_event))
    number_priority = input("How high is this {} on your priority list? (Scale from 1-10) > ".format(name_of_event))
    if abs(round(number_priority)) <= 10:
        month = input("What MONTH is this {} occurring in? (Type a number between 1 and 12) > ".format(name_of_event))
        if abs(math.floor(month)) <= 12:
            #Year called before day to make sure leap years are accounted for
            year = input("What YEAR is {} occurring in? (Enter a valid year) > ".format(name_of_event))
            #To ensure nobody sets their deadline for 2016 or so
            if (year) >= str(now.strftime("%Y")):
                day = input("What DAY is this {} occurring in? (Type a number between 1 and 31) > ".format(name_of_event))
                if (abs(day) <= 31 and (year % 4) != 0) or (abs(day) <= 29 and (year % 4) == 0 and month == 2):
                    for key, value in month_list.items():
                        if key == month:
                            month = value
                    string_date = "{} {} {}".format(month, day, year)
                    event_info.append([name_of_event.upper(), number_priority, month, year, day, string_date.upper()])
                    
    else:
        print("That's not a valid number on the priority scale.")
class Priority(ABC):
    input_id += 1
    def __init__(self, name, event_type, date, priority_number, informal_day, informal_month, informal_year):
        self.name = name
        self.event_type = event_type
        self.date = date
        self.priority_number = priority_number
        self.informal_day = informal_day
        self.informal_year = informal_year
        self.informal_month = informal_month
    #Dunder methods
    def __repr__(self):
        priorities_list.append(self.name)
        return "NAME: {} \n TYPE: {} \n DATE: {} \n PRIORITY NUMBER: {} \n ID: {} \n".format(self.name, self.event_type, self.date, self.priority_number, input_id)
    
class Event(Priority):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(self.name, "EVENT", self.date, self.priority_number, self.informal_day, self.informal_month, self.informal_year)
    def __repr__(self):
        return super().__repr__() + "REASON: {} \n".format(self.reason)
    
class Assignment(Priority):
    def __init__(self, subject):
        self.subject = subject
        super().__init__(self.name, "ASSIGNMENT", self.date, self.priority_number, self.informal_day, self.informal_month, self.informal_year)
    def __repr__(self):
        return super().__repr__() + "SUBJECT: {} \n".format(self.subject)
    
class PrioritySettings():
    def __init__(self, sort_by, to_delete): 
        self.sort_by = sort_by 
        self.to_delete = to_delete
        #super().__init__(self.name, self.event_type, self.date, self.priority_number, self.informal_day, self.informal_month, self.informal_year)
    def get_priority(self):
        if self.sort_by == "A":
            most_prioritized = dict(sorted(load_priorities.items(), key=lambda x: x[2], reverse=True))
            for item in most_prioritized.keys():
                for i in range(1, 5):
                    to_return = to_return + item.upper() + ": DUE DATE: " + most_prioritized[item[1]] + ": PRIORITY NUMBER: " + str(most_prioritized[item[2]]) + "\n"
        elif self.sort_by == "B":
            nearest_dates = []
            nearest_dates = deque(nearest_dates)
            for key, value in load_priorities.items():
                if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) != str(key[2]):
                    if str(key[3]) <= nearest_dates[0][1][3] and str(key[4]) <= nearest_dates[0][1][4] and str(key[5]) <= nearest_dates[0][1][5]:
                        #Earlier dates are ensured to be listed first.
                        nearest_dates.appendleft([key, value])
                    else:
                        #Later dates get pushed back in favor of earlier dates.
                        nearest_dates.append([key, value])
            for item in nearest_dates:
                for i in range(1, 5):
                    to_return = to_return + item[0] + ": DUE DATE: " + item[1][1] + ": PRIORITY NUMBER: " + item[1][2] + "\n"
        return to_return
    def del_priority(self):
        for key in load_priorities:
            if key.upper() == self.to_delete:
                del load_priorities[key]
                priorities_list.remove(key)
                return "{} deleted.".format(key)
    def __len__(self):
        return "There are {} assignments and events that you currently have on your list.".format(len(priorities_list))
program_running = True
print("Welcome to Tim's Time Tracker!")
print("Today is " + now.strftime("%A") + ", " +  now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y"))
print("It's currently {} in your time.".format(now.strftime("%I") + ":" + now.strftime("%M") + " " + now.strftime("%p")))
while program_running == True:
    notify_user()
    what_to_do = input("What do you want to do? \n [A] Set Event/Deadline \n [B] Change Event/Assignment \n")
    if "A" in what_to_do.upper():
        what_event = input("Do you want to set an event or a deadline? \n [A] Event \n [B] Deadline \n [C] View Assignments \n [D] Check Number of Events/Assignments")
        if "A" in what_event.upper():
            what_event = "EVENT"
        elif "B" in what_event.upper():
            what_event = "ASSIGNMENT"
        setup(what_event)
        event_info[0][1] = what_event
        event_at_hand = Priority(event_info[0][0], event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6])
        if event_info[0][1] == "EVENT":
            reason_why = input("What's the reason for the event? > ")
            Event(reason_why)
        elif event_info[0][1] == "ASSIGNMENT":
            subject_at_hand = input("What subject is this assignment under? > ")
            Assignment(subject_at_hand)
        is_this_correct = input("Is this information correct? \n [A] Yes \n [B] No \n ")
        if "A" in is_this_correct.upper():
            exportation_dict.update({event_info[0][0] : [event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6]],})
            json.dumps(exportation_dict, skipkeys=True, allow_nan = True)
        elif "B" in is_this_correct.upper():
            continue
    elif "B" in what_to_do.upper():
        change_or_delete = input("What do you want to do? \n [A] Change Event/Deadline \n [B] Delete Event/Deadline > ")
        if "A" in change_or_delete.upper():
            pass
        elif "B" in change_or_delete.upper():
            print(load_priorities)
            to_erase = input("Which event/deadline do you want to delete? (Type the name of the event/deadline as it appears) > ")
            settings = PrioritySettings(to_erase)
            settings.del_priority()
    elif "C" in what_to_do.upper():
        by_number_or_date = input("What do you want the events/deadlines to be sorted by? \n [A] Priority Number \n [B] Date \n")
        if "A" in by_number_or_date.upper():
            settings = PrioritySettings("A")
            settings.get_priority()
        elif "B" in by_number_or_date.upper():
            settings = PrioritySettings("B")
            settings.get_priority()          
    elif "D" in what_to_do.upper():
        pass
    else: 
        print("That's not a valid option.")
        continue