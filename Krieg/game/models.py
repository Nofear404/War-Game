from django.db import models
from queue import Queue
import random


# Karte Klasse
class Karte:
    def __init__(self, zahl, farbe):
        self.zahl = zahl
        self.farbe = farbe


# Kartendeck Klasse
class Kartendeck:
    def __init__(self):
        self.karten_dict = {
            "Pik 2": 1,
            "Pik 3": 2,
            "Pik 4": 3,
            "Pik 5": 4,
            "Pik 6": 5,
            "Pik 7": 6,
            "Pik 8": 7,
            "Pik 9": 8,
            "Pik 10": 9,
            "Pik Bube": 10,
            "Pik Dame": 11,
            "Pik König": 12,
            "Pik Ass": 13,
            "Herz 2": 1,
            "Herz 3": 2,
            "Herz 4": 3,
            "Herz 5": 4,
            "Herz 6": 5,
            "Herz 7": 6,
            "Herz 8": 7,
            "Herz 9": 8,
            "Herz 10": 9,
            "Herz Bube": 10,
            "Herz Dame": 11,
            "Herz König": 12,
            "Herz Ass": 13,
            "Karo 2": 1,
            "Karo 3": 2,
            "Karo 4": 3,
            "Karo 5": 4,
            "Karo 6": 5,
            "Karo 7": 6,
            "Karo 8": 7,
            "Karo 9": 8,
            "Karo 10": 9,
            "Karo Bube": 10,
            "Karo Dame": 11,
            "Karo König": 12,
            "Karo Ass": 13,
            "Kreuz 2": 1,
            "Kreuz 3": 2,
            "Kreuz 4": 3,
            "Kreuz 5": 4,
            "Kreuz 6": 5,
            "Kreuz 7": 6,
            "Kreuz 8": 7,
            "Kreuz 9": 8,
            "Kreuz 10": 9,
            "Kreuz Bube": 10,
            "Kreuz Dame": 11,
            "Kreuz König": 12,
            "Kreuz Ass": 13,
        }

    def getKartendeck(self):
        return self.karten_dict


class Spieler:
    def __init__(self, name):
        self.name = name
        self.spielerqueue = []
        self.cards_won = []


class Game:
    def __init__(self, player_1, player_2):
        self.s_name1 = Spieler(player_1)
        self.s_name2 = Spieler(player_2)

    def karten_mischen(self):

        # benutze das Dictionary aus Klasse Kartendeck
        self.kartendeck = Kartendeck().karten_dict

        # in Liste umwandeln umzu mischen
        items = list(self.kartendeck.keys())

        # mischen
        random.shuffle(items)

        return items

    def gamestart(self):
        # jeder Spieler bekommt 26 Karten in Form von einer Queue
        # Karten müssen gemischt sein
        deck = self.karten_mischen()
        self.s_name1.spielerqueue = deck[:26]
        self.s_name2.spielerqueue = deck[26:]
    

    def kriegregeln(self, spieler1, spieler2):
        while (len(spieler1.spielerqueue) >= 0 and len(spieler2.spielerqueue)):
            if (self.kartendeck[spieler1.spielerqueue[0]] > self.kartendeck[spieler2.spielerqueue[0]]):

                #hinzufügen ins neue deck von Spieler 1 und aus aktuell deck pop()
                spieler1.cards_won.append(spieler1.spielerqueue.pop(0))
                spieler1.cards_won.append(spieler2.spielerqueue.pop(0))

            elif(self.kartendeck[spieler1.spielerqueue[0]] < self.kartendeck[spieler2.spielerqueue[0]]):

                #hinzufügen ins neue deck von Spieler 1 und aus aktuell deck pop()
                spieler2.cards_won.append(spieler1.spielerqueue.pop(0))
                spieler2.cards_won.append(spieler2.spielerqueue.pop(0))

            else:
                # Dict für 6 Karten 
                temp = [] 
                
                while (self.kartendeck[spieler1.spielerqueue[0]] == self.kartendeck[spieler2.spielerqueue[0]]):
     

                    #Counter einbauen 
                    for i in range(0, 3):
                        temp.append(spieler1.spielerqueue.pop(0))
                        temp.append(spieler2.spielerqueue.pop(0))
                    
                    
                


            
        
        


test = Game("Dan", "Selman")
test.gamestart()
print(test.s_name1.spielerqueue)
print(test.s_name2.spielerqueue)
