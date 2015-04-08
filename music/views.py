# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import HttpResponse




def vars_for_all_templates(self):
    return {
            'producer_budget': Constants.producer_budget,
            'consumer_budget': Constants.consumer_budget,
            'album_production_cost': Constants.album_production_cost,
            'album_own_cost': Constants.album_own_cost,
            'role': self.player.role()
    }




class MyPage(Page):

    form_model = models.Player
    form_fields = ['my_field']

    def is_displayed(self):

        return self.player.role() == ('producer') or self.player.role() == ('producer2')

    def vars_for_template(self):
        return {
            'my_variable_here': 1,
        }



    #timeout_seconds = 30




class MyPageWait(WaitPage):

    def body_text(self):
        return "Waiting for other participants to contribute."



class ConsumerPhase(Page):

    form_model = models.Player
    form_fields = ['totalValue', 'album1BuyCount', 'album2BuyCount', 'album3BuyCount', 'album4BuyCount', 'album5BuyCount', 'album6BuyCount', 'album7BuyCount', 'album8BuyCount', 'album9BuyCount', 'album10BuyCount',
                   'album1ListenCount', 'album2ListenCount', 'album3ListenCount', 'album4ListenCount', 'album5ListenCount', 'album6ListenCount', 'album7ListenCount', 'album8ListenCount', 'album9ListenCount', 'album10ListenCount',
                   'album1PiracyCount', 'album2PiracyCount', 'album3PiracyCount', 'album4PiracyCount', 'album5PiracyCount', 'album6PiracyCount', 'album7PiracyCount', 'album8PiracyCount', 'album9PiracyCount', 'album10PiracyCount',
                   'subPurchaseCount'
    ]






    def is_displayed(self):
        return self.player.role() == 'consumer'


    def vars_for_template(self):
        return {
            'album1': self.group.val,
            'album2': self.group.val1,
            'album3': self.group.val2,
            'album4': self.group.val3,
            'album5': self.group.val4,
            'album6': self.group.val5,
            'album7': self.group.val6,
            'album8': self.group.val7,
            'album9': self.group.val8,
            'album10': self.group.val9,
            'testNum': self.group.get_albums(),
            'testNum2': self.group.get_albums2(),

        }

    #timeout_seconds = 120


class ConsumerPhaseWait(WaitPage):

    def body_text(self):
        return "Waiting for other participants to contribute."


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()



class ConsumerResults(Page):

    def is_displayed(self):
        return self.player.role() == 'consumer'

    def vars_for_template(self):
        return {
            'testVal': self.player.get_value(),
            'numBought': self.player.get_num_bought(),
            'numPirate': self.player.get_num_pirate(),
            'numListen': self.player.get_num_listen(),
            'subPurchaseCount': self.player.subPurchaseCount,

        }

    #timeout_seconds = 30

    pass

class ProducerResults(Page):

    def is_displayed(self):
        return self.player.role() == ('producer')

    def vars_for_template(self):
        return {
            'numBought': self.group.calc_prod_albumsBought(),
            'numPirate': self.group.calc_prod_albumsPirated(),
            'numListen': self.group.calc_prod_albumsListened(),


        }

    #timeout_seconds = 30

    pass

class ProducerResults2(Page):

    def is_displayed(self):
        return self.player.role() == ('producer2')

    def vars_for_template(self):
        return {
            'numBought2': self.group.calc_prod_albumsBought2(),
            'numPirate2': self.group.calc_prod_albumsPirated2(),
            'numListen2': self.group.calc_prod_albumsListened2(),


        }

    #timeout_seconds = 30

    pass


page_sequence =[

        MyPage,
        MyPageWait,
        ConsumerPhase,
        ConsumerPhaseWait,
        ResultsWaitPage,
        ConsumerResults,
        ProducerResults,
        ProducerResults2,
    ]
