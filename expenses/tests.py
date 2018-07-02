from django.test import TestCase

from .models import Expense


class ExpensesTests(TestCase):
    def test_expenses(self):
        n = 5

        self.assertEqual(Expense.objects.count(), 0)

        for i in range(n):
            o = Expense()
            o.title = f"Pizza #{i + 1}"
            o.date = f"2018-05-{i + 1:02}"
            o.amount = 1 + i * 4
            o.save()

        self.assertEqual(Expense.objects.count(), n)
