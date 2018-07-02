import random
from django.shortcuts import render


def list_expenses(request):
    return render(request, "expenses/expense_list.html", {
        'foo': random.randint(1, 3),
        'bar': 'kuku<b>kuku</b>',
        'colors': ['red', 'green', 'blue'],
    })
