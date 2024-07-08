from abc import ABC, abstractmethod
from collections import deque
from datetime import datetime
import json
import math
open_json = open("Priorities.json")
load_priorities = json.load(open_json)
now = datetime.now()
#Used for json.dump()
exportation_dict = {}
global event_info
global month_list
global program_running
program_running = True
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
event_info = []
priorities_list = []
def notify_user():
    for key in load_priorities.keys():
        print(key)
        #Change this later
        if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) == str(load_priorities[key][2]) or (now.strftime("%B") + " " + str((int(now.strftime("%d")) - 1)) + " " + now.strftime("%Y")) == str(load_priorities[key][2]):
            return "HEADS UP! {} is due PRETTY soon! Date: {}.".format(key, load_priorities[key][2])
def setup(type_of_event):
    name_of_event = input("What is the name of your {}?".format(type_of_event))
    number_priority = input("How high is this {} on your priority list? (Scale from 1-10) > ".format(name_of_event))
    if abs(round(number_priority)) <= 10:
        month = input("What MONTH is this {} occurring in? (Type a number between 1 and 12) > ".format(name_of_event))
        if abs(math.floor(month)) <= 12:
            #Year called before day to make sure leap years are accounted for
            year = input("What YEAR is {} occurring in? (Enter a valid year) > ".format(name_of_event))
            #To ensure nobody sets their deadline for 2016 or so
            if str(year) >= str(now.strftime("%Y")):
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
    def __init__(self, name, event_type, date, priority_number, informal_day, informal_month, informal_year):
        self.name = name
        #There was no need for a single underscore since this code isn't supposed to be imported as a module and therefore doesn't need any variables to be highlighted as "non-public" or only accessible to the programmer.
        #There was no need for double underscores since no variables need to be set to private nor have a set value
        self.event_type = event_type
        self.date = date
        self.priority_number = priority_number
        self.informal_day = informal_day
        self.informal_year = informal_year
        self.informal_month = informal_month
    #Dunder methods
    def __repr__(self):
        priorities_list.append(self.name)
        return "NAME: {} \n TYPE: {} \n DATE: {} \n PRIORITY NUMBER: {}".format(self.name, self.event_type, self.date, self.priority_number)
    
class Event(Priority):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(self.name, "EVENT", self.date, self.priority_number, self.informal_day, self.informal_month, self.informal_year)
    def __repr__(self):
        return super().__repr__() + " REASON: {} \n".format(self.reason)
    
class Assignment(Priority):
    def __init__(self, subject):
        self.subject = subject
        super().__init__(self.name, "ASSIGNMENT", self.date, self.priority_number, self.informal_day, self.informal_month, self.informal_year)
    def __repr__(self):
        return super().__repr__() + " SUBJECT: {} \n".format(self.subject)
    
class PrioritySettings():
    def __init__(self, sort_by, to_delete, selection): 
        self.sort_by = sort_by 
        self.to_delete = to_delete
        self.selection = selection
    def get_priority(self):
        if self.sort_by == "A":
            self.sort_by = "Priority Number"
            most_prioritized = dict(sorted(load_priorities.items(), key=lambda x: x[2], reverse=True))
            for item in most_prioritized.keys():
                for i in range(1, 5):
                    to_return = to_return + item.upper() + ": DUE DATE: " + most_prioritized[item[1]] + ": PRIORITY NUMBER: " + str(most_prioritized[item[2]]) + "\n"
        elif self.sort_by == "B":
            self.sort_by = "Due Date"
            nearest_dates = []
            nearest_dates = deque(nearest_dates)
            for key, value in load_priorities.items():
                if (now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y")) != str(key[2]):
                    if (str(key[3]) <= nearest_dates[0][1][3]) and (str(key[4]) <= nearest_dates[0][1][4] and str(key[5]) <= nearest_dates[0][1][5]):
                        #Earlier dates are ensured to be listed first.
                        nearest_dates.appendleft([key, value])
                    else:
                        #Later dates get pushed back in favor of earlier dates.
                        nearest_dates.append([key, value])
            for item in nearest_dates:
                for i in range(1, 5):
                    to_return = to_return + item[0] + ": DUE DATE: " + item[1][1] + ": PRIORITY NUMBER: " + item[1][2] + "\n"
        else:
            print("That's not a valid option.")
            to_return = "None"
        return to_return
    def del_priority(self):
        for key in load_priorities:
            if key.upper() == self.to_delete.upper():
                del load_priorities[key]
                priorities_list.remove(key)
                return "{} deleted.".format(key)
        else:
            return "Length cannot be obtained."
        #if type(self.selection) == 'list':
        #   return "There are {} assignments and events that you currently have on your list.".format(str(abs(len(self.selection))))
    #All classes inheriting from Priority must have their own unique spin on __repr__() (Adding more text or values to return counts)
    @abstractmethod
    def __repr__(self):
        return "Sorted by: {} \n Deleted: {}".format(self.sort_by, self.to_delete)
class find_length(PrioritySettings):
    def __init__(self):
        super().__init__(self.sort_by, self.to_delete, self.selection)
        self.length = len(self.selection)
    def __len__(self):
        return self.length
    def __repr__(self):
        return "Events/Assignments total: {}".format(self.length)
print("Welcome to Tim's Time Tracker!")
print("Today is " + now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y"))
print("It's currently {} in your time.".format(now.strftime("%I") + ":" + now.strftime("%M") + " " + now.strftime("%p")))
while program_running == True:
    notify_user()
    what_to_do = input("What do you want to do? \n [A] Set Event/Deadline \n [B] Change Event/Assignment \n [C] View Assignments \n [D] Check Number of Events/Assignments \n")
    if "A" in what_to_do.upper():
        what_event = input("Do you want to set an event or a deadline? \n [A] Event \n [B] Deadline \n ")
        if "A" in what_event.upper():
            what_event = "EVENT"
        elif "B" in what_event.upper():
            what_event = "ASSIGNMENT"
        else:
            what_event = "NONE"
        setup(what_event)
        event_info[0][1] = what_event
        event_at_hand = Priority(event_info[0][0], event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6])
        if event_info[0][1] == "EVENT":
            reason_why = input("What's the reason for the event? > ")
            Event(reason_why)
        elif event_info[0][1] == "ASSIGNMENT":
            subject_at_hand = input("What subject is this assignment under? > ")
            Assignment(subject_at_hand)
        elif event_info[0][1] == "NONE":
            continue
        is_this_correct = input("Is this information correct? \n [A] Yes \n [B] No \n ")
        if "A" in is_this_correct.upper():
            exportation_dict.update({event_info[0][0] : [event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6]],})
            json.dumps(exportation_dict, skipkeys=True, allow_nan = True)
        else:
            continue
    elif "B" in what_to_do.upper():
        change_or_delete = input("What do you want to do? \n [A] Change Event/Deadline \n [B] Delete Event/Deadline > ")
        if "A" in change_or_delete.upper():
            print(load_priorities)
            to_change = input("What event/deadline do you want ot change? (ENTER EVENT/DEADLINE NAME IN ALL CAPS) > ")
            for priority, value in load_priorities.items():
                if priority.upper() == to_change.upper():
                    ask_to_change = input("What do you want to change? \n [A] Name \n [B] Event Type \n [C] Date \n [D] Priority Number \n")
                    if "A" in ask_to_change.upper():
                        new_name = input("What is the new name? > ")
                        updated_priority = Priority(new_name, value[1], value[2], value[3], value[4], value[5], value[6])
                    elif "B" in ask_to_change.upper():
                        event_or_assignment = input("What is this? \n [A] Event \n [B] Assignment \n")
                        if "A" in event_or_assignment.upper():
                            updated_priority = Priority(value[0], "Event", value[2], value[3], value[4], value[5], value[6])    
                        elif "B" in event_or_assignment.upper():
                            updated_priority = Priority(value[0], "Assignment", value[2], value[3], value[4], value[5], value[6])  
                    elif "C" in ask_to_change.upper():
                        new_month = input("What's the new month? (Enter a number from one to twelve) > ")
                        new_year = input("What's the new year? > ")
                        new_day = input("What's the new day? (Choose a number from 1 to 31) > ")
                        if (abs(new_day) <= 31 and (new_year % 4) != 0) or (abs(new_day) <= 29 and (new_year % 4) == 0 and new_month == 2):
                            for key, value in month_list.items():
                                if key == new_month:
                                    new_month = value
                            new_date = "{} {} {}".format(new_month, new_day, new_year)
                            updated_priority = Priority(value[0], value[1], new_date, value[3], new_day, new_month, new_year)
                    elif "D" in ask_to_change.upper():
                        new_priority_number = input("What is the new priority number? (Enter a number from 1-10) > ")
                        if (type(new_priority_number) == "int") and (new_priority_number <= 10):
                            updated_priority = Priority(value[0], value[1], value[2], new_priority_number, value[4], value[5], value[6]) 
                        else: 
                            print("Invalid number.")
                            continue
                    exportation_dict.update({event_info[0][0] : [event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6]],})
                    del priority
                    json.dumps(exportation_dict, skipkeys=True, allow_nan = True)
        elif "B" in change_or_delete.upper():
            for priority in load_priorities.keys():
                print(priority)
            to_erase = input("Which event/deadline do you want to delete? (Type the name of the event/deadline as it appears) > ")
            for priority in load_priorities.keys():
                if priority.upper() == to_erase.upper():
                    settings = PrioritySettings(to_erase, "None", "None")
                    settings.del_priority()
                else:
                    print("Not a valid event/deadline to erase.")
                    continue
    elif "C" in what_to_do.upper():
        by_number_or_date = input("What do you want the events/deadlines to be sorted by? \n [A] Priority Number \n [B] Date \n")
        if "A" in by_number_or_date.upper():
            settings = PrioritySettings("None", "A", "None")
            settings.get_priority()
        elif "B" in by_number_or_date.upper():
            settings = PrioritySettings("None", "B", "None")
            settings.get_priority()   
        else:
            print("That's not a valid option.")
            continue  
    elif "D" in what_to_do.upper():
        list_of_priorities = []
        for priority, value in load_priorities:
            list_of_priorities.append(priority)
        priorities = find_length("None", "None", list_of_priorities)
        priorities.__len__()
    else: 
        print("That's not a valid option.")
        #Don't select a correct option = go through entire process again
        continue
    user_done = input("Are you done adding events and deadlines? \n [A] Yes \n [B] No \n")
    if "A" in user_done.upper():
        program_running = False
    else:
        continue