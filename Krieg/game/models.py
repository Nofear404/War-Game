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
    def __init__(self, player_1: str, player_2: str):
        self.s_name1 = Spieler(player_1)
        self.s_name2 = Spieler(player_2)

    def karten_mischen(self, deck_keys):

        # in Liste umwandeln umzu mischen
        items = list(deck_keys)

        # mischen
        random.shuffle(items)

        return items

    def new_deck(self, old_deck: list, won_cards: list):
        old_deck.extend(won_cards) # Selman - besser extend als append 
        won_cards.clear()  
        return self.karten_mischen(old_deck)

    def kriegregeln(self, spieler1: Spieler, spieler2: Spieler):

        # Dict für Unentschieden 
        temp = []

        #While Schleife für ein Spiel
        while len(spieler1.spielerqueue) + len(spieler1.cards_won) > 0 and len(spieler2.spielerqueue) + len(spieler2.cards_won) > 0:

            #While Schleife für eine Runde
            while len(spieler1.spielerqueue) > 0 and len(spieler2.spielerqueue) > 0:

                #Check ob Spieler 1 die Schlacht gewinntt
                if Kartendeck().karten_dict[spieler1.spielerqueue[0]] > Kartendeck().karten_dict[spieler2.spielerqueue[0]]:
                    spieler1.cards_won.append(spieler1.spielerqueue.pop(0))
                    spieler1.cards_won.append(spieler2.spielerqueue.pop(0))
                    spieler1.cards_won.extend(temp)  
                    temp.clear()  
                #Check ob Spieler 2 die Schlacht gewinnt
                elif Kartendeck().karten_dict[spieler1.spielerqueue[0]] < Kartendeck().karten_dict[spieler2.spielerqueue[0]]:
                    spieler2.cards_won.append(spieler1.spielerqueue.pop(0))
                    spieler2.cards_won.append(spieler2.spielerqueue.pop(0))
                    spieler2.cards_won.extend(temp)  
                    temp.clear()  

                #Gleichstand
                else:
                    # einfach 3 Karten in Temp und in die nächste Iteration der Runde
                    if len(spieler1.spielerqueue) >= 3 and len(spieler2.spielerqueue) >= 3:
                        for i in range(3):
                            temp.append(spieler1.spielerqueue.pop(0))
                            temp.append(spieler2.spielerqueue.pop(0))
                    else:
                        #solange was in der Queue vorhanden ist in Temp rein
                        while spieler1.spielerqueue:
                            temp.append(spieler1.spielerqueue.pop(0))
                        while spieler2.spielerqueue:
                            temp.append(spieler2.spielerqueue.pop(0))
                        
                        #neuer Stapel machen
                        spieler1.spielerqueue = self.new_deck(spieler1.spielerqueue, spieler1.cards_won)  
                        spieler2.spielerqueue = self.new_deck(spieler2.spielerqueue, spieler2.cards_won)  
                        temp.clear()  

                if len(spieler1.spielerqueue) == 0:
                    spieler1.spielerqueue = self.new_deck(spieler1.spielerqueue, spieler1.cards_won)  
                
                if len(spieler2.spielerqueue) == 0:
                    spieler2.spielerqueue = self.new_deck(spieler2.spielerqueue, spieler2.cards_won)  

        if len(spieler1.spielerqueue) + len(spieler1.cards_won) > 0:
            print(f"{spieler1.name} hat gewonnen")
            return f"{spieler1.name} gewonnen!"
        else:
            print(f"{spieler2.name} hat gewonnen")
            return f"{spieler2.name} hat gewonnen!"

    def gamestart(self):
        self.deck = self.karten_mischen(Kartendeck().karten_dict.keys())
        self.s_name1.spielerqueue = self.deck[:26]
        self.s_name2.spielerqueue = self.deck[26:]
        self.kriegregeln(self.s_name1, self.s_name2)


test = Game("Dan", "Selman")
test.gamestart()
