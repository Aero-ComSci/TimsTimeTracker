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
    def __init__(self, name, category, price):
        name = self.name
        category = self.category
        price = self.price
