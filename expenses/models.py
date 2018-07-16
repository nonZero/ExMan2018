from django.db import models

# ORM: Object Relational Mapping
from django.urls import reverse


class Expense(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=400)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.amount})"
        # return f"[#{self.id}] ${self.amount}@{self.date} ({self.title})"

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))

    def is_expensive(self):
        return self.amount >= 100

    is_expensive.boolean = True
    is_expensive.short_description = "$$$$"
    is_expensive.admin_order_field = "amount"


class Note(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE,
                                related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = (
            '-created_at',
        )
