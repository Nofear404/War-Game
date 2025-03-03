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
        for i in won_cards:
            old_deck.append(i)
        old_deck = self.karten_mischen(self.deck)
        won_cards = []

    def kriegregeln(self, spieler1: Spieler, spieler2: Spieler):
        # Dict für 6 Karten
        temp = []
        counter = 0
        while (len(spieler1.spielerqueue) and len(spieler2.spielerqueue)) or (
            len(spieler1.cards_won) and len(spieler2.cards_won)
        ):
            counter += 1
            print(counter)
            try:
                spieler1.spielerqueue.remove([])
                spieler2.spielerqueue.remove([])
            except ValueError:
                pass

            while (
                Kartendeck().karten_dict[spieler1.spielerqueue[0]]
                == Kartendeck().karten_dict[spieler2.spielerqueue[0]]
            ):
                if len(spieler1.spielerqueue) >= 3 and len(spieler2.spielerqueue) >= 3:
                    # Counter einbauen
                    for i in range(0, 3):
                        temp.append(spieler1.spielerqueue.pop(0))
                        temp.append(spieler2.spielerqueue.pop(0))

                else:
                    temp.append(spieler1.spielerqueue.pop(0))
                    temp.append(spieler2.spielerqueue.pop(0))
                    self.new_deck(spieler1.spielerqueue, spieler1.cards_won)
                    self.new_deck(spieler2.spielerqueue, spieler2.cards_won)

            if (
                Kartendeck().karten_dict[spieler1.spielerqueue[0]]
                > Kartendeck().karten_dict[spieler2.spielerqueue[0]]
            ):

                # hinzufügen ins neue deck von Spieler 1 und aus aktuell deck pop()
                spieler1.cards_won.append(spieler1.spielerqueue.pop(0))
                spieler1.cards_won.append(spieler2.spielerqueue.pop(0))
                spieler1.cards_won.append(temp)

            else:

                # hinzufügen ins neue deck von Spieler 1 und aus aktuell deck pop()
                spieler2.cards_won.append(spieler1.spielerqueue.pop(0))
                spieler2.cards_won.append(spieler2.spielerqueue.pop(0))
                spieler2.cards_won.append(temp)

            if len(spieler1.spielerqueue) == 0:
                spieler1.spielerqueue = spieler1.cards_won
                random.shuffle(spieler1.spielerqueue)
                spieler1.cards_won = []

            if len(spieler2.spielerqueue) == 0:
                spieler2.spielerqueue = spieler2.cards_won
                random.shuffle(spieler2.spielerqueue)
                spieler2.cards_won = []

            temp = []
        if (len(spieler1.spielerqueue) + len(spieler1.cards_won)) != 0:
            print(f"{spieler1.name} hat gewonnen")
            return f"{spieler1.name} gewonnen!"
        else:
            print(f"{spieler2.name} hat gewonnen")
            return f"{spieler2.name} hat gewonnen!"

    def gamestart(self):
        # jeder Spieler bekommt 26 Karten in Form von einer Queue
        # Karten müssen gemischt sein
        self.deck = self.karten_mischen(Kartendeck().karten_dict.keys())
        self.s_name1.spielerqueue = self.deck[:26]
        self.s_name2.spielerqueue = self.deck[26:]
        self.kriegregeln(self.s_name1, self.s_name2)


test = Game("Dan", "Selman")
test.gamestart()
