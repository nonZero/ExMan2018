from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from expenses.forms import ExpenseForm, NoteForm
from expenses.models import Expense


@login_required
def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        # 'total': sum(o.amount for o in Expense.objects.all())
        'total': Expense.objects.aggregate(
            total=Sum('amount'))['total']
    })


@login_required
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


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # form.instance.expense = ...
            o = form.save()
            msg = f"Expense #{o.id} created successfully."
            messages.success(request, msg)
            return redirect(o)
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })


@login_required
def expense_update(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=o)
        if form.is_valid():
            o = form.save()
            msg = f"Expense #{o.id} updated successfully."
            messages.success(request, msg)
            return redirect(o)
    else:
        form = ExpenseForm(instance=o)

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
