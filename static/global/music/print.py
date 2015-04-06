# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import HttpResponse



def test(request):
        if request.method == 'POST':
            if 'pieFact' in request.POST:
                pieFact = request.POST['pieFact']
                print pieFact
                # doSomething with pieFact here...
                # if everything is OK
                return HttpResponse('success')
        # nothing went well
            return HttpResponse('FAIL!!!!!')

