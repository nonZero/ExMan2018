import random
import silly
from django.core.management.base import BaseCommand
from django.db import transaction

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create some silly expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help="Number of expenses to create")

    def handle(self, n, *args, **kwargs):
        Expense.objects.all().delete()
        for i in range(n):
            with transaction.atomic():
                o = Expense()
                o.title = silly.a_thing()
                o.date = silly.datetime().date()
                o.amount = f"{random.uniform(1, 1000):.2f}"
                o.comment = "\n".join(
                    silly.paragraph() for i in range(random.randrange(0, 3)))
                o.save()

                for j in range(random.randrange(5)):
                    o.notes.create(
                        content="\n".join(silly.paragraph() for i in
                                          range(random.randrange(1, 4)))
                    )
