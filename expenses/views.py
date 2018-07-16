from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

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
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            funny = form.cleaned_data.pop('funny')
            o = Expense.objects.create(**form.cleaned_data)
            return redirect(o)
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
