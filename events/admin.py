from django.contrib import admin

from models import *


class EventAdmin(admin.ModelAdmin):
    readonly_fields = [
        'outcome',
        'current_buy_price',
        'current_sell_price',
        'last_transaction_date',
        'Q_for',
        'Q_against',
    ]


class BetAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Bet, BetAdmin)
admin.site.register(Transaction, TransactionAdmin)