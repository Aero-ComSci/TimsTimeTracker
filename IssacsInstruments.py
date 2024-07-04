import math
#Dictionary for default instruments in this program
#These prices aren't exactly accurate since instrument prices vary by size, brand, and quality
default_instruments = {
    "Flute" : ["Woodwind", "IN STOCK", 600.00],
    "Piano" : ["Percussion", "IN STOCK", 1700.00],
    "Alto Saxophone" : ["Woodwind", "IN STOCK", 1170.00],
    "Tenor Saxophone" : ["Woodwind", "IN STOCK", 850.00],
    "Tambourine" : ["Percussion", "IN STOCK", 15.00],
    "Snare Drum" : ["Percussion", "IN STOCK", 93.00],
    "Clarinet" : ["Woodwind", "IN STOCK", 800.00],
    "Oboe" : ["Woodwind", "IN STOCK", 470.00],
    "Trombone" : ["Brass", "IN STOCK", 1577.00],
    "Guitar (Acoustic)" : ["Guitar Family", "IN STOCK", 298.00],
    "Guitar (Electric)" : ["Guitar Family", "IN STOCK", 250.00],
    "Bass Guitar" : ["Guitar Family", "IN STOCK", 220.00],
    "Cello" : ["Bowed String", "IN STOCK", 460.00],
    "Violin" : ["Bowed String", "IN STOCK", 100.00],
    "Viola" : ["Bowed String", "IN STOCK", 360.00],
    "Double Bass" : ["Bowed String", "IN STOCK", 1800.00],
    "Piccolo" : ["Woodwind", "IN STOCK", 500.00],
    "Bongo Drums" : ["Percussion", "IN STOCK", 360.00],
    "Triangle" : ["Percussion", "IN STOCK", 25.00],
    "Trumpet" : ["Brass", "IN STOCK", 869.70],
    "French Horn" : ["Brass", "IN STOCK", 569.00],
    "Tuba" : ["Brass", "IN STOCK", 1680.00],
    "Drum Set" : ["Percussion", "IN STOCK", 400.00],
    "Bassoon" : ["Woodwind", "IN STOCK", 1485.00],
}
class User:
    def __init__(self, role="User"):
        role = self.role
    def __repr__(self):
        return "You are a {}.".format(self.role)
class Admin(User):
    def enter_admin_passcode(self):
        admin_passcode = "C^rr0ts"
        attempts = 1
        while attempts <= 3:
            enter_passcode = input("Enter the Admin passcode in order to do this:  > ")
            if enter_passcode == admin_passcode:
                super().__init__("Admin")
                return True
                continue
            else:
                attempts += 1
        return "Sorry, you used all your password attempts."
class Instrument():
    #Dunder method
    global instrument_list
    instrument_list = []
    def __init__(self, instruments, category, price):
        instruments = self.instruments
        category = self.category
        price = self.price
    def by_category(self):
        global category_checked
        category_checked = True
        type_of_instrument = input("What type of instrument do you want to search for? \n [A] Woodwind \n [B] Brass \n [C] Guitar Family \n [D] Percussion \n [E] Other \n")
        if price_checked == False:
            for instrument, value in default_instruments.items():
                if type_of_instrument.upper() == "A":
                    if default_instruments[instrument][0] == "Woodwind":
                        instrument_list.append([instrument, value])
                elif type_of_instrument.upper() == "B":
                    if default_instruments[instrument][0] == "Brass":
                        instrument_list.append([instrument, value])
                elif type_of_instrument.upper() == "C":
                    if default_instruments[instrument][0] == "Guitar Family":
                        instrument_list.append([instrument, value])
                elif type_of_instrument.upper() == "D":
                    if default_instruments[instrument][0] == "Percussion":
                        instrument_list.append([instrument, value])
                elif type_of_instrument.upper() == "E":
                    if default_instruments[instrument][0] == "Other":
                        instrument_list.append([instrument, value])
                else:
                    return "That's not an option."
        else:
            for instrument in instrument_list:
                if type_of_instrument.upper() != "A" and instrument[1][0] == "Woodwind":
                    instrument_list.remove(instrument)
                elif type_of_instrument.upper() != "B" and instrument[1][0] == "Brass":
                    instrument_list.remove(instrument)
                elif type_of_instrument.upper() == "C" and instrument[1][0] == "Guitar Family":
                    instrument_list.remove(instrument)
                elif type_of_instrument.upper() == "D" and instrument[1][0] == "Percussion":
                    instrument_list.remove(instrument)
                else:
                    return "That's not an option."
                
        return instrument_list
    def by_price(self):
        global price_checked
        price_checked = True
        price_of_instrument = input("What is your preferred price range for your instrument? (Type your max price, and we'll go from there): \n")
        if category_checked == False:
            for instrument, value in default_instruments.items():
                if default_instruments[instrument][2] <= price_of_instrument:
                    instrument_list.append([instrument, value])
        else:
            for instrument in instrument_list:
                if instrument[1][2] > price_of_instrument:
                    instrument_list.remove(instrument)
        return instrument_list
    #Dunder method
    def __repr__(self):
        return "{}: CATEGORY: {} AVAILABILITY: {}, PRICE {}".format(self.instruments, self.category, self.price)

class InstrumentSettings(Instrument, Admin):
    def get_instrument(self):
        instrument_of_choice = super().__init__(self.name, self.category, self.price)
        return instrument_of_choice
    def set_instrument(self):
        check_role = Admin()
        check_role.enter_admin_passcode()
        if check_role.enter_admin_passcode == True:
            instrument_name  = input("What is the name of the instrument? > ")
            instrument_category = input("What category is this instrument classified under? \n [A] Woodwind \n [B] Brass \n [C] Guitar Family \n [D] Percussion \n [E] Other \n")
            if "A" == instrument_category.upper():
                instrument_category = "Woodwind"
            elif "B" == instrument_category.upper():
                instrument_category = "Brass"
            elif "C" == instrument_category.upper():
                instrument_category = "Guitar Family"
            elif "D" == instrument_category.upper():
                instrument_category = "Percussion"
            elif "E" == instrument_category.upper():
                instrument_category = "Other"
            instrument_price = input("What's the price of this instrument? > ")
            super().__init__(instrument_name, instrument_category, instrument_price)
            correct_or_not = input("Is this correct? \n [Y] Yes \n [N] No \n")
            if correct_or_not.upper() == "Y":
                default_instruments.update({instrument_name : [instrument_category, "IN STOCK", instrument_price]})
            elif correct_or_not.upper() == "N":
                InstrumentSettings.set_instrument()
        else: 
            return "Sorry, you don't have access to this feature."
    def del_instrument(self):
        check_role = Admin()
        check_role.enter_admin_passcode()
        if check_role.enter_admin_passcode == True:
            print(default_instruments)
            instrument_to_delete = input("What instrument do you want to delete? TYPE THE NAME OF THE INSTRUMENT: > ")
            for key, value in default_instruments.items():
                if instrument_to_delete.upper() == key.upper():
                    super().__init__(key, default_instruments[0], default_instruments[2])
                    sure_or_not = input("Are you sure you want to delete this instrument? \n [Y] Yes \n [N] No \n")
                    if sure_or_not.upper() == "Y":
                        del default_instruments[key]
                    elif sure_or_not.upper() == "N":
                        InstrumentSettings.del_instrument()
        else: 
            return "Sorry, you don't have access to this feature."
    def change_instrument():
        check_role = Admin()
        check_role.enter_admin_passcode()
        if check_role.enter_admin_passcode == True:
            print(default_instruments)
            instrument_to_change = input("What instrument do you want to change? TYPE THE NAME OF THE INSTRUMENT: > ")
            what_to_change = input("What do you want to change about the instrument? \n [A] Instrument Name \n [B] Instrument Category \n [C] Availability \n [D] Pricing \n")
            if what_to_change.upper() == "A":
                name_to_change = input("What name do you want to change this instrument to? > ")
                for instrument in default_instruments.keys():
                    if instrument.upper() == instrument_to_change.upper():        
                        instrument = instrument_to_change
            elif what_to_change.upper() == "B":
                category_to_change = input("What category do you want to change this instrument to? \n [A] Woodwind \n [B] Brass \n [C] Guitar Family \n [D] Percussion \n [E] Other \n")
                if category_to_change.upper() == "A":
                    category_to_change = "Woodwind"
                elif category_to_change.upper() == "B":
                    category_to_change = "Brass"
                elif category_to_change.upper() == "C":
                    category_to_change = "Guitar Family"
                elif category_to_change.upper() == "D":
                    category_to_change = "Percussion"
                elif category_to_change.upper() == "E":
                    category_to_change = "Other"
                for instrument in default_instruments.keys():
                    if instrument.upper == instrument_to_change.upper():
                        default_instruments[instrument][0] = category_to_change
            elif what_to_change.upper() == "C":
                in_or_out = input("Is the instrument in or out of stock? \n [A] IN \n [B] OUT \n")
                if "A" in in_or_out.upper():
                    for instrument in default_instruments.keys():
                        if instrument.upper() == instrument_to_change.upper():
                            default_instruments[instrument][1] = "IN STOCK"
                elif "B" in in_or_out.upper():
                    for instrument in default_instruments.keys():
                        if instrument.upper() == instrument_to_change.upper():
                            default_instruments[instrument][1] = "OUT OF STOCK"
            elif what_to_change.upper() == "D":
                change_price = input("What's the new price of this instrument? > ")
                for instrument in default_instruments.keys():
                    if instrument.upper() == instrument_to_change.upper():
                        default_instruments[instrument][2] = change_price
        else:
            return "Sorry, you don't have access to this feature."


                



