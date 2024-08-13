from abc import ABC, abstractmethod
from contextlib import suppress
from collections import deque
from datetime import datetime
import json
import math
global now
global program_running
global event_info
global return_text
now = datetime.now()
#Used for json.dump()
open_json = open("Priorities.json")
load_priorities = json.load(open_json)
exportation_dict = {}
program_running = True
priorities_list = []
event_info = []
def setup(type_of_event):
    return_text = "Text Here"
    name_of_event = " "
    if type_of_event == "EVENT" or type_of_event == "ASSIGNMENT":
        name_of_event = input("What is the name of your {}? > ".format(type_of_event))
        number_priority = input("How high is this {} on your priority list? (Scale from 1-10) > ".format(name_of_event))
        if number_priority.isnumeric() and type(int(round(float(number_priority)))) == int and abs(round(float(number_priority))) <= 10 and abs(round(float(number_priority))) >= 1:
            number_priority = str(abs(round(float(number_priority))))
            if return_text != " ":
                month = input("What MONTH is this {} occurring in? (Type a number between 1 and 12) > ".format(name_of_event))
                if month.isnumeric() and type(int(month)) == int and abs(int(round(float(month)))) <= 12 and abs(int(round(float(month)))) >= 1:
                    month = str(abs(int(round(float(month)))))
                    #Year called before day to make sure leap years are accounted for
                    if return_text != " ":
                        year = input("What YEAR is {} occurring in? (Enter a valid year) > ".format(name_of_event))
                        #To ensure nobody sets their deadline for 2016 or so
                        if year.isnumeric() and (type(int(abs(round(float(year)))) == int)) and (int(round(float(year))) >= int(now.strftime("%Y"))) and int(abs(round(float(year)))) >= 0:
                            year = str(abs(round(float(year))))
                            if return_text != " ":
                                day = input("What DAY is this {} occurring in? (Type a number between 1 and 31) > ".format(name_of_event))
                                if day.isnumeric():
                                    if (((abs(int(round(float(day)))) <= 31) and (abs(int(round(float(year))) % 4) != 0) and (type(int(round(float(day))))) == int)) or (((abs(int(round(float(day)))) <= 29 and abs(int(round(float(year)))) % 4 == 0 and int(round(float(month))) == 2 and type(int(round(float(day)))) == int))) or (((abs(int(round(float(day)))) <= 31 and int(round(float(year))) % 4 == 0 and int(round(float(month))) != 2 and type(int(round(float(day)))) == int))) and int(round(float(day))) >= 1:
                                        day = str(abs(round(float(day))))
                                        if (int(now.strftime("%Y")) <= int(year)):
                                            if ((int(now.strftime("%m"))) <= int(month) and (int(now.strftime("%Y")) == int(year))) or (int(now.strftime("%Y")) < int(year)):
                                                if (int(now.strftime("%d"))) <= int(day) and (int(now.strftime("%Y")) == int(year)) or (int(now.strftime("%Y")) < int(year)):
                                                    string_date = "{} {} {}".format(str(month), str(day), str(year))
                                                    event_info.append([name_of_event.upper(), type_of_event.upper(), string_date.upper(), str(number_priority), str(month), str(day), str(year),])
                                                    return event_info
                                                else:
                                                    print("Invalid Date.")
                                                    return " "
                                            else:
                                                print("Invalid Date.")
                                                return " "
                                        else:
                                            print("Invalid Date.")
                                            return " "
                                    else:
                                        print("That's not a valid day given the total date you put in.")
                                        return " "
                                else:
                                    print("That's not a valid day given the total date you put in.")
                                    return " "
                        else:
                            print("That's not a valid year.")
                            return_text = " "
                            return return_text
                else:
                    print("That's not a valid month.")
                    return_text = " "
                    return return_text
        else:
            print("That's not a valid number on the priority scale.")
            return_text = " "
            return return_text
    else:
        print("Invalid.")
        return_text = " "
        return return_text
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
    def add_info(self):
        event_info.append(self.name)
        event_info.append(self.event_type)
        event_info.append(self.date)
        event_info.append(self.priority_number)
        event_info.append(self.informal_day)
        event_info.append(self.informal_year)
        event_info.append(self.informal_month)
        return event_info
    #Dunder methods
    def __repr__(self):
        priorities_list.append(self.name)
        return "NAME: {}\nTYPE: {}\nDATE: {}\nPRIORITY NUMBER: {}".format(self.name, self.event_type, self.date, self.priority_number)
    
class Event(Priority):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(event_info[0][0], "EVENT", event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6])

    def __repr__(self):
        event_info[0].insert(7, self.reason)
        return super().__repr__() + "\nREASON: {} \n".format(self.reason)
    
class Assignment(Priority):
    def __init__(self, subject):
        self.subject = subject
        super().__init__(event_info[0][0], "ASSIGNMENT", event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6])
    def __repr__(self):
        event_info[0].insert(7, self.subject)
        return super().__repr__() + "\nSUBJECT: {} \n".format(self.subject)
    
class PrioritySettings():
    def __init__(self, sort_by, to_delete, selection): 
        self.sort_by = sort_by 
        self.to_delete = to_delete
        self.selection = selection
    def get_priority(self):
        if self.sort_by == "A":
            self.sort_by = "Priority Number"
            to_return = ""
            count = 0
            most_prioritized = []
            most_prioritized = deque(most_prioritized)
            for key, value in load_priorities.items():
                if (len(most_prioritized) == 0):
                    most_prioritized.append([key, value])
                else:
                    if (int(value[2]) > int(most_prioritized[0][1][2])):
                        most_prioritized.appendleft([key, value])
                    elif (int(value[2]) <= int(most_prioritized[0][1][2])):
                        if len(most_prioritized) == 1:
                            most_prioritized.append([key, value])
                        else:
                            if (int(value[2]) < int(most_prioritized[1][1][2])) or (int(value[2]) == int(most_prioritized[1][1][2])):
                                if (int(value[2]) < int(most_prioritized[-1][1][2])) or (int(value[2]) == int(most_prioritized[-1][1][2])):
                                    most_prioritized.append([key, value])
                            else:
                                most_prioritized.insert(1, [key, value])
                    else:
                        most_prioritized.append([key, value])
            most_prioritized = dict(most_prioritized)
            for item in most_prioritized.keys():
                if count <= 4:
                    to_return = to_return + item.upper() + ": DUE DATE: " + most_prioritized[item][1] + ": PRIORITY NUMBER: " + str(most_prioritized[item][2]) + "\n"
                    count += 1
        elif self.sort_by == "B":
            self.sort_by = "Due Date"
            count = 0
            to_return = ""
            nearest_dates = []
            nearest_dates = deque(nearest_dates)
            for key, value in load_priorities.items():
                if (now.strftime("%m") + " " + now.strftime("%d") + " " + now.strftime("%Y")) != str(value[2]):
                    if (len(nearest_dates) == 0):
                        nearest_dates.append([key, value])
                    else:
                        if len(nearest_dates) == 1:
                            nearest_dates.append([key, value])
                        elif (int(value[3]) <= int(nearest_dates[0][1][3])) and (int(value[4]) <= int(nearest_dates[0][1][5]) and int(value[5]) <= int(nearest_dates[0][1][4])):
                            #Earlier dates are ensured to be listed first.
                            nearest_dates.appendleft([key, value])
                        elif (str(value[5]) >= nearest_dates[0][1][4]):
                            if int(value[3]) >= int(nearest_dates[0][1][3]):
                                if int(value[4]) >= int(nearest_dates[0][1][5]):
                                    if (int(value[4]) <= int(nearest_dates[1][1][5])):
                                        if int(value[3]) <= int(nearest_dates[1][1][3]):
                                            if int(value[4]) <= int(nearest_dates[1][1][4]):
                                                nearest_dates.insert(1, [key, value])
                                        else:
                                            nearest_dates.append([key, value])
                                    else:
                                        nearest_dates.append([key, value])
                                else:
                                    nearest_dates.append([key, value])
                            else:
                                nearest_dates.append([key, value])
                        elif (int(value[4]) == int(nearest_dates[-1][1][5]) and int(value[3]) <= int(nearest_dates[-1][1][3]) and int(value[5]) <= int(nearest_dates[-1][1][4])):
                            nearest_dates.insert(1, [key, value])
                        else:
                            #Later dates get pushed back in favor of earlier dates.
                            nearest_dates.append([key, value])
            nearest_dates = dict(nearest_dates)
            for item in nearest_dates.keys():
                if count <= 5:
                    to_return = to_return + item.upper() + ": DUE DATE: " + nearest_dates[item][1] + ": PRIORITY NUMBER: " + str(nearest_dates[item][2]) + "\n"
                    count += 1
        else:
            print("That's not a valid option.")
        return to_return
    def del_priority(self):
        for key in load_priorities.keys():
            if key.upper() == self.to_delete.upper():
                with open("Priorities.json", "w") as output_json:
                    del load_priorities[key]
                    json.dump(load_priorities, output_json)
                return "Event/Assignment deleted."
        #if type(self.selection) == 'list':
        #   return "There are {} assignments and events that you currently have on your list.".format(str(abs(len(self.selection))))
    #All classes inheriting from Priority must have their own unique spin on __repr__() (Adding more text or values to return counts)
    @abstractmethod
    def __repr__(self):
        return "Sorted by: {} \n Deleted: {}".format(self.sort_by, self.to_delete)
class find_length(PrioritySettings):
    def __init__(self, sort_by, to_delete, selection):
        super().__init__(sort_by, to_delete, selection)
        self.length = len(selection)
    def __repr__(self):
        return "Events/Assignments total: {}".format(self.length)
print("Welcome to Tim's Time Tracker!")
print("Today is " + now.strftime("%B") + " " + now.strftime("%d") + " " + now.strftime("%Y"))
print("It's currently {} in your time.".format(now.strftime("%I") + ":" + now.strftime("%M") + " " + now.strftime("%p")))
while program_running == True:
    exportation_dict.clear()
    event_info = []
    what_to_do = input("What do you want to do? \n [A] Set Event/Deadline \n [B] Change Event/Assignment \n [C] View Assignments \n [D] Check Number of Events/Assignments \n [E] Quit \n")
    if "A" in what_to_do.upper():
        what_event = input("Do you want to set an event or a deadline? \n [A] Event \n [B] Deadline \n ")
        if "A" in what_event.upper():
            what_event = "EVENT"
        elif "B" in what_event.upper():
            what_event = "ASSIGNMENT"
        else:
            print("Invalid option.")
            continue
        if setup(what_event) != " ":
            event_at_hand = Priority(event_info[0][0], event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6])
            if event_info[0][1] == "EVENT":
                reason_why = input("What's the reason for the event? > ")
                print(Event(reason_why))
            elif event_info[0][1] == "ASSIGNMENT":
                subject_at_hand = input("What subject is this assignment under? > ")
                print(Assignment(subject_at_hand))
            is_this_correct = input("Is this information correct? \n [A] Yes \n [B] No \n ")
            if "A" in is_this_correct.upper():
                exportation_dict.update({event_info[0][0] : [event_info[0][1], event_info[0][2], event_info[0][3], event_info[0][4], event_info[0][5], event_info[0][6], event_info[0][7]],},)
                with open("Priorities.json", "w") as output_json:
                    load_priorities.update(exportation_dict)
                    json.dump(load_priorities, output_json)
                    output_json.close()
                print("Event Added! Please rerun the application to see your changes.\n")
                program_running = False
        else:
            continue
    elif "B" in what_to_do.upper():
        exportation_dict.clear()
        change_or_delete = input("What do you want to do? \n [A] Change Event/Deadline \n [B] Delete Event/Deadline > ")
        if "A" in change_or_delete.upper():
            for priority, value in load_priorities.items():
                print("\nNAME: {} TYPE: {} REASON/SUBJECT: {}\n".format(priority, value[0], value[6]))
            to_change = input("What event/deadline do you want to change? (ENTER EVENT/DEADLINE NAME IN ALL CAPS) > ")
            with suppress(RuntimeError):
                for priority, value in load_priorities.items():
                    if priority.upper() == to_change.upper():
                        ask_to_change = input("What do you want to change? \n [A] Name \n [B] Event Type \n [C] Date \n [D] Priority Number \n [E] Reason \n")
                        if "A" in ask_to_change.upper():
                            new_name = input("What is the new name? > ")
                            updated_priority = Priority(new_name, value[0], value[1], value[2], value[3], value[4], value[5])
                            updated_priority.add_info()
                        elif "B" in ask_to_change.upper():
                            event_or_assignment = input("What is this? \n [A] Event \n [B] Assignment \n")
                            if "A" in event_or_assignment.upper():
                                updated_priority = Priority(priority, "EVENT", value[1], value[2], value[3], value[4], value[5])   
                                updated_priority.add_info()
                            elif "B" in event_or_assignment.upper():
                                updated_priority = Priority(priority, "ASSIGNMENT", value[1], value[2], value[3], value[4], value[5]) 
                                updated_priority.add_info()
                            else:
                                continue
                        elif "C" in ask_to_change.upper():
                            new_month = input("What's the new month? (Enter a number from one to twelve) > ")
                            if new_month.isnumeric() and type(int(round(float(new_month)))) == int and abs(round(float((int(new_month))))) <= 12:
                                new_month = str(math.floor(int(new_month)))
                                new_year = input("What's the new year? > ")
                                if new_year.isnumeric() and (type(int(abs(round(float(new_year)))) == int)) and (int(round(float(new_year))) >= int(now.strftime("%Y"))) and int(abs(round(float(new_year)))) >= 0:
                                    new_year = str(abs(round(float(new_year))))
                                    new_day = input("What's the new day? (Choose a number from 1 to 31) > ")
                                    if new_day.isnumeric():
                                        if (((abs(int(round(float(new_day)))) <= 31) and (abs(int(round(float(new_year))) % 4) != 0) and (type(int(round(float(new_day))))) == int)) or (((abs(int(round(float(new_day)))) <= 29 and abs(int(round(float(new_year)))) % 4 == 0 and int(round(float(new_month))) == 2 and type(int(round(float(new_day)))) == int))) or (((abs(int(round(float(new_day)))) <= 31 and int(round(float(new_year))) % 4 == 0 and int(round(float(new_month))) != 2 and type(int(round(float(new_day)))) == int))) and int(round(float(new_day))) >= 1:
                                            new_day = str(abs(round(float(new_day))))                                
                                            if (int(now.strftime("%Y")) <= int(new_year)):
                                                if ((int(now.strftime("%m"))) <= int(new_month) and (int(now.strftime("%Y")) == int(new_year))) or (int(now.strftime("%Y")) < int(new_year)):
                                                    if (int(now.strftime("%d"))) <= int(new_day) and (int(now.strftime("%Y")) == int(new_year)) or (int(now.strftime("%Y")) < int(new_year)):
                                                        new_date = "{} {} {}".format(str(new_month), str(new_day), str(new_year))
                                                        updated_priority = Priority(priority, value[0], new_date.upper(), value[2], str(new_month), str(new_day), str(new_year))
                                                        updated_priority.add_info()
                                                    else:
                                                        print("Invalid Date.")
                                                        continue
                                                else:
                                                    print("Invalid Date.")
                                                    continue
                                            else:
                                                print("Invalid Date.")
                                                continue
                                        else:
                                            print("Invalid Date.")
                                            continue      
                                    else:
                                        print("Invalid day.") 
                                        continue
                                else:
                                    print("Invalid year.")
                                    continue
                            else:
                                print("Invalid Month.")
                                continue
                        elif "D" in ask_to_change.upper():
                            new_priority_number = input("What is the new priority number? (Enter a number from 1-10) > ")
                            if new_priority_number.isnumeric():
                                if int(round(float(new_priority_number))) <= 10:
                                    new_priority_number = int(round(float(new_priority_number)))
                                    updated_priority = Priority(priority, value[0], value[1], str(new_priority_number), value[3], value[4], value[5]) 
                                    updated_priority.add_info()
                            else:
                                continue
                        elif "E" in ask_to_change.upper():
                            new_subres = input("What is the new subject/reason? > ")
                            updated_priority = Priority(priority, value[0], value[1], value[2], value[3], value[4], value[5]) 
                            updated_priority.add_info()
                        else: 
                            print("Invalid character.")
                            continue
                        if "E" not in ask_to_change.upper():
                            exportation_dict.update({event_info[0] : [event_info[1], event_info[2], event_info[3], event_info[4], event_info[5], event_info[6], value[6]]})
                            program_running = False
                        else:
                            exportation_dict.update({event_info[0] : [event_info[1], event_info[2], event_info[3], event_info[4], event_info[5], event_info[6], new_subres]})
                            program_running = False
                        del load_priorities[priority]
                        with open("Priorities.json", "w") as output_json:
                            load_priorities.update(exportation_dict)
                            json.dump(load_priorities, output_json)
                            output_json.close()
                        event_info.clear()
                        print("\nIf you want to view the list sooner, go to Priorities.json.")
                        print("Please rerun the application to see your changes.\n")
        elif "B" in change_or_delete.upper():
            for priority, value in load_priorities.items():
                print("\nNAME: {} TYPE: {} REASON/SUBJECT: {}\n".format(priority, value[0], value[6]))
            priority_keys_length = len(load_priorities)
            for priority in load_priorities.keys():
                print(priority)
            to_erase = input("Which event/deadline do you want to delete? (Type the name of the event/deadline as it appears) > ")
            already_deleted_item = False
            for priority in list(load_priorities.keys()):
                if priority.upper() == to_erase.upper() and already_deleted_item == False:
                    settings = PrioritySettings("None", to_erase, "None")
                    print(settings.del_priority())
    elif "C" in what_to_do.upper():
        by_number_or_date = input("What do you want the events/deadlines to be sorted by? \n [A] Priority Number \n [B] Date \n")
        if "A" in by_number_or_date.upper():
            settings = PrioritySettings("A", "None", "None")
            print(settings.get_priority())
        elif "B" in by_number_or_date.upper():
            settings = PrioritySettings("B", "None", "None")
            print(settings.get_priority())  
        else:
            print("That's not a valid option.")
            continue 
    elif "D" in what_to_do.upper():
        list_of_priorities = []
        for priority, value in load_priorities.items():
            list_of_priorities.append(priority)
        priorities = find_length("None", "None", list_of_priorities)
        print(priorities)
    elif "E" in what_to_do.upper():
        open_json.close()
        program_running = False
    else:
        print("That's not a valid option.")
        continue
    if what_to_do.upper() != "E" and program_running != False:
        user_done = input("Are you done adding events and deadlines? \n [A] Yes \n [B] No \n")
        if "A" in user_done.upper():
            open_json.close()
            program_running = False
        else:
            continue
    else:
        continue