# -*- coding: utf-8 -*-
import factory
import pytz

from django.utils.timezone import datetime

from .models import Event, RelatedEvent, Bet, Transaction


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    estimated_end_date = datetime.now(tz=pytz.UTC)
    title = u'Długi tytuł testowego wydarzenia'
    short_title = u'Tytuł wydarzenia'
    title_fb_yes = u'Tytuł na tak'
    title_fb_no = u'Tytuł na nie'
    description = u'Opis wydarzenia testowego.'
    is_front = True
    is_featured = True
    outcome = Event.EVENT_OUTCOME_CHOICES.IN_PROGRESS


class ShortEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    estimated_end_date = datetime.now(tz=pytz.UTC)


class RefugeesEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    estimated_end_date = datetime.now(tz=pytz.UTC)
    title = u'Odbędzie się w Polsce referendum w '\
        u'sprawie przyjmowania uchodźców.'
    short_title = u'.'
    title_fb_yes = u'.'
    title_fb_no = u'.'
    description = u'Do dnia 30 czerwca 2016 r. zostanie zebrane i złożone w '\
        u'sejmie minimum 500 tys. podpisów pod wnioskiem o referendum ws. '\
        u'przyjmowania uchodźców.'


class CruzEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    estimated_end_date = datetime.now(tz=pytz.UTC)
    title = u'Ted Cruz wygrywa prawybory GOP w Wisconsin.'
    short_title = u'.'
    title_fb_yes = u'.'
    title_fb_no = u'.'
    description = u'Ted Cruz zdobywa największe poparcie w prawyborach '\
        u'partii republikańskiej w Wisconsin 5 kwietnia 2016 r.'


class RelatedEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RelatedEvent


class BetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bet

    has = 1
    bought = 1
    outcome = Bet.BET_OUTCOME_CHOICES.YES


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction
