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

class Instrument():
    #Dunder method
    global instrument_list
    instrument_list = []
    def __init__(self, instruments, category, price):
        instruments = self.instruments
        category = self.category
        price = self.price
    def by_category(self):
        category_checked = True
        type_of_instrument = input("What type of instrument do you want to search for? \n [A] Woodwind \n [B] Brass \n [C] Guitar Family \n [D] Percussion \n")
        for instrument, value in default_instruments.items():
            if type_of_instrument.upper() == "A":
                if default_instrument[instrument][0] == "Woodwind":
                    instrument_list.append([instrument, value])
            elif type_of_instrument.upper() == "B":
                if default_instrument[instrument][0] == "Brass":
                    instrument_list.append([instrument, value])
            elif type_of_instrument.upper() == "C":
                if default_instrument[instrument][0] == "Guitar Family":
                    instrument_list.append([instrument, value])
            elif type_of_instrument.upper() == "D":
                if default_instrument[instrument][0] == "Percussion":
                    instrument_list.append([instrument, value])
            else:
                return "That's not an option."
        return instrument_list
    def by_price(self):
        price_checked = True
        price_of_instrument = input("What is your preferred price range for your instrument? (Type your max price, and we'll go from there): \n")
        if category_checked == False:
            for instrument, value in default_instruments.items():
                if default_instrument[instrument][2] <= price_of_instrument:
                    instrument_list.append([instrument, value])
        else:
            for instrument in instrument_list:
                if instrument[1][2] > price_of_instrument:
                    instrument_list.remove(instrument)
        return instrument_list
    #Dunder method
    def __repr__(self):
        return "{}: CATEGORY: {} AVAILABILITY: {}, PRICE {}".format(self.instruments, self.category, self.price)

class InstrumentSettings(Instrument):
    def get_instrument(self):
        super().__init__(self.name, self.category, self.price)
        for 

