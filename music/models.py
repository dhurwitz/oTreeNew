# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from random import randint

# </standard imports>

author = 'Dylan Hurwitz'

# The description of the app support HTML tags
doc = """
This is a music piracy game. It is testing the effect of subscription services on the music market.
"""

# Link of the source code of your app or empty
source_code = "https://github.com/oTree-org/oTree/"


# List of strings of recomended literature for this app or an empty list
bibliography = (
    (
        'Basar, T., Olsder, G. J., Clsder, G. J., Basar, T., Baser, T., & '
        'Olsder, G. J. (1995). Dynamic noncooperative game theory (Vol. 200). '
        'London: Academic press.'
    ),
    (
        'Harsanyi, J. C., & Selten, R. (1988). A general theory of '
        'equilibrium selection in games. MIT Press Books, 1.'
    )
)


# Resources for understand your app, normally a wikipedia articles
# or an empty dict (This will be sorted alphabetically)
links = {
    "Wikipedia": {
        "Game Theory": "http://en.wikipedia.org/wiki/Game_theory",
        "Nash Equilibrim": "http://en.wikipedia.org/wiki/Nash_equilibrium"
    },
    "Resources": {
        "Introduction to Game Theory [Video]":
                "https://www.youtube.com/watch?v=nM3rTU927io",
    }
}


# A list of relevant keywords for your app or an empty list. This keyword will
# be automatically linked with duckduckgo.com anonymous search
keywords = ("Game Theory", "Nash Equilibrium", "Economics")


class Constants:
    name_in_url = 'music'
    players_per_group = 3
    num_rounds = 2
    producer_budget = 200
    consumer_budget = 100
    album_production_cost = 50
    album_own_cost = 20


    # define more constants here


class Subsession(otree.models.BaseSubsession):
    pass


class Album():

    def __init__(self, player):
        self.player = player
        self.value = randint(7, 13)

    def get_value(self):
        return self.value


class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


    A1 = Album(1)
    A2 = Album(2)
    A3 = Album(3)
    A4 = Album(4)
    A5 = Album(5)
    A6 = Album(6)
    A7 = Album(7)
    A8 = Album(8)
    A9 = Album(9)
    A10 = Album(10)

    val = A1.value
    val1 = A2.value
    val2 = A3.value
    val3 = A4.value
    val4 = A5.value
    val5 = A6.value
    val6 = A7.value
    val7 = A8.value
    val8 = A9.value
    val9 = A10.value





    def get_albums(self):
        producer = self.get_player_by_role('producer')


        return producer.my_field

    def get_albums2(self):

        producer2 = self.get_player_by_role('producer2')

        return producer2.my_field

    def get_value(self):
        consumer = self.get_player_by_role('consumer')

        return consumer.totalValue

    def calc_prod_albumsBought(self):
        calcBought = 0
        producer = self.get_player_by_role('producer')
        for p in producer.get_others_in_group():
            if p.id_in_group != 2:
                calcBought += p.album1BuyCount
                calcBought += p.album2BuyCount
                calcBought += p.album3BuyCount
                calcBought += p.album4BuyCount
                calcBought += p.album5BuyCount
        return calcBought

    def calc_prod_albumsBought2(self):
        calcBought2 = 0
        producer2 = self.get_player_by_role('producer2')
        for p in producer2.get_others_in_group():
            if p.id_in_group != 1:
                calcBought2 += p.album6BuyCount
                calcBought2 += p.album7BuyCount
                calcBought2 += p.album8BuyCount
                calcBought2 += p.album9BuyCount
                calcBought2 += p.album10BuyCount
        return calcBought2

    def calc_prod_albumsPirated(self):
        calcPirated = 0
        producer = self.get_player_by_role('producer')
        for p in producer.get_others_in_group():
            if p.id_in_group != 2:
                calcPirated += p.album1PiracyCount
                calcPirated += p.album2PiracyCount
                calcPirated += p.album3PiracyCount
                calcPirated += p.album4PiracyCount
                calcPirated += p.album5PiracyCount
        return calcPirated

    def calc_prod_albumsPirated2(self):
        calcPirated2 = 0
        producer2 = self.get_player_by_role('producer2')
        for p in producer2.get_others_in_group():
            if p.id_in_group != 1:
                calcPirated2 += p.album6PiracyCount
                calcPirated2 += p.album7PiracyCount
                calcPirated2 += p.album8PiracyCount
                calcPirated2 += p.album9PiracyCount
                calcPirated2 += p.album10PiracyCount
        return calcPirated2


    def calc_prod_albumsListened(self):
        calcListens = 0
        producer = self.get_player_by_role('producer')
        for p in producer.get_others_in_group():
            if p.id_in_group != 2:
                calcListens += p.album1ListenCount
                calcListens += p.album2ListenCount
                calcListens += p.album3ListenCount
                calcListens += p.album4ListenCount
                calcListens += p.album5ListenCount
        return calcListens

    def calc_prod_albumsListened2(self):
        calcListens2 = 0
        producer2 = self.get_player_by_role('producer2')
        for p in producer2.get_others_in_group():
            if p.id_in_group != 1:
                calcListens2 += p.album6ListenCount
                calcListens2 += p.album7ListenCount
                calcListens2 += p.album8ListenCount
                calcListens2 += p.album9ListenCount
                calcListens2 += p.album10ListenCount
        return calcListens2

    def calc_prod_payoff(self):
        calcPayoff = 0
        producer = self.get_player_by_role('producer')
        for p in producer.get_others_in_group():
            if p.id_in_group != 2:
                calcPayoff += p.album1BuyCount
                calcPayoff += p.album2BuyCount
                calcPayoff += p.album3BuyCount
                calcPayoff += p.album4BuyCount
                calcPayoff += p.album5BuyCount
                calcPayoff *= Constants.album_own_cost
        return calcPayoff

    def calc_prod2_payoff(self):
        calc2Payoff = 0
        producer2 = self.get_player_by_role('producer2')
        for p in producer2.get_others_in_group():
            if p.id_in_group != 1:
                calc2Payoff += p.album6BuyCount
                calc2Payoff += p.album7BuyCount
                calc2Payoff += p.album8BuyCount
                calc2Payoff += p.album9BuyCount
                calc2Payoff += p.album10BuyCount
                calc2Payoff *= Constants.album_own_cost
        return calc2Payoff




    def set_payoffs(self):
        consumer = self.get_player_by_role('consumer')
        producer = self.get_player_by_role('producer')
        producer2 = self.get_player_by_role('producer2')


        consumer.payoff = self.get_value()
        producer.payoff = self.calc_prod_payoff()
        producer2.payoff = self.calc_prod2_payoff()




class Player(otree.models.BasePlayer):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    group = models.ForeignKey(Group, null = True)
    # </built-in>



    # example field
    my_field = models.PositiveIntegerField(
        min=0,
        max=(Constants.producer_budget/Constants.album_production_cost),
        doc="""
        Description of this field, for documentation
        """
    )

    totalValue = models.PositiveIntegerField()

    album1BuyCount = models.PositiveIntegerField()
    album2BuyCount = models.PositiveIntegerField()
    album3BuyCount = models.PositiveIntegerField()
    album4BuyCount = models.PositiveIntegerField()
    album5BuyCount = models.PositiveIntegerField()
    album6BuyCount = models.PositiveIntegerField()
    album7BuyCount = models.PositiveIntegerField()
    album8BuyCount = models.PositiveIntegerField()
    album9BuyCount = models.PositiveIntegerField()
    album10BuyCount = models.PositiveIntegerField()

    album1ListenCount = models.PositiveIntegerField()
    album2ListenCount = models.PositiveIntegerField()
    album3ListenCount = models.PositiveIntegerField()
    album4ListenCount = models.PositiveIntegerField()
    album5ListenCount = models.PositiveIntegerField()
    album6ListenCount = models.PositiveIntegerField()
    album7ListenCount = models.PositiveIntegerField()
    album8ListenCount = models.PositiveIntegerField()
    album9ListenCount = models.PositiveIntegerField()
    album10ListenCount = models.PositiveIntegerField()

    album1PiracyCount = models.PositiveIntegerField()
    album2PiracyCount = models.PositiveIntegerField()
    album3PiracyCount = models.PositiveIntegerField()
    album4PiracyCount = models.PositiveIntegerField()
    album5PiracyCount = models.PositiveIntegerField()
    album6PiracyCount = models.PositiveIntegerField()
    album7PiracyCount = models.PositiveIntegerField()
    album8PiracyCount = models.PositiveIntegerField()
    album9PiracyCount = models.PositiveIntegerField()
    album10PiracyCount = models.PositiveIntegerField()

    subPurchaseCount = models.PositiveIntegerField()

    def get_num_bought(self):
        numB = 0
        numB += self.album1BuyCount
        numB += self.album2BuyCount
        numB += self.album3BuyCount
        numB += self.album4BuyCount
        numB += self.album5BuyCount
        numB += self.album6BuyCount
        numB += self.album7BuyCount
        numB += self.album8BuyCount
        numB += self.album9BuyCount
        numB += self.album10BuyCount
        return numB

    def get_num_pirate(self):
        numP = 0
        numP += self.album1PiracyCount
        numP += self.album2PiracyCount
        numP += self.album3PiracyCount
        numP += self.album4PiracyCount
        numP += self.album5PiracyCount
        numP += self.album6PiracyCount
        numP += self.album7PiracyCount
        numP += self.album8PiracyCount
        numP += self.album9PiracyCount
        numP += self.album10PiracyCount
        return numP

    def get_num_listen(self):
        numL = 0
        numL += self.album1ListenCount
        numL += self.album2ListenCount
        numL += self.album3ListenCount
        numL += self.album4ListenCount
        numL += self.album5ListenCount
        numL += self.album6ListenCount
        numL += self.album7ListenCount
        numL += self.album8ListenCount
        numL += self.album9ListenCount
        numL += self.album10ListenCount
        return numL








    def role(self):
        # you can make this depend of self.id_in_group
        if self.id_in_group == 1:
            return 'producer'
        if self.id_in_group == 2:
            return 'producer2'
        if self.id_in_group == 3:
            return 'consumer'




