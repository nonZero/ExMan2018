import random
import silly
from django.core.management.base import BaseCommand

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create some silly expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help="Number of expenses to create")

    def handle(self, n, *args, **kwargs):
        # Expense.objects.all().delete()
        for i in range(n):
            o = Expense()
            o.title = silly.a_thing()
            o.date = silly.datetime().date()
            o.amount = f"{random.uniform(1, 1000):.2f}"
            o.comment = "\n".join(silly.paragraph() for i in range(random.randrange(3,8)))
            o.save()
