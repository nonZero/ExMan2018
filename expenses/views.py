from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from expenses.forms import ExpenseForm, NoteForm
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

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.instance.expense = o
            form.save()
            return redirect(o)
    else:
        form = NoteForm()

    return render(request, "expenses/expense_detail.html", {
        'object': o,
        'form': form,
    })


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # form.instance.expense = ...
            o = form.save()
            return redirect(o)
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })


