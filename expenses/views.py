from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from expenses.forms import ExpenseForm
from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        # 'total': sum(o.amount for o in Expense.objects.all())
        'total': Expense.objects.aggregate(
            total=Sum('amount'))['total']
    })


def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


def expense_create(request):
    form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
