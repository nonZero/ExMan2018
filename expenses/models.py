from django.db import models

# ORM: Object Relational Mapping


class Expense(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=400)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.amount})"
        # return f"[#{self.id}] ${self.amount}@{self.date} ({self.title})"

    def is_expensive(self):
        return self.amount >= 100