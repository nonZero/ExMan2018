from django.contrib import admin

from . import models


class NoteInline(admin.TabularInline):
    model = models.Note
    extra = 0


class ExpenseAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]
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
admin.site.register(models.Note)
