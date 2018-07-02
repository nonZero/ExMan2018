from django.contrib import admin

from . import models


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date',
        'amount',
        'is_expensive',
    )
    search_fields = (
        'id',
        'title',
        'date',
        'amount',
    )
    date_hierarchy = 'date'



admin.site.register(models.Expense, ExpenseAdmin)
