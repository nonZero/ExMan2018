from django.db.models import Sum
from django.shortcuts import render

from expenses.models import Expense


def list_expenses(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        # 'total': sum(o.amount for o in Expense.objects.all())
        'total': Expense.objects.aggregate(
            total=Sum('amount'))['total']
    })
