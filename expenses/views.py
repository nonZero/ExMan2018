from django.db.models import Sum
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        # 'total': sum(o.amount for o in Expense.objects.all())
        'total': Expense.objects.aggregate(
            total=Sum('amount'))['total']
    })


def expense_detail(request, pk):
    # try:
    #     o = Expense.objects.get(pk=pk)
    # except Expense.DoesNotExist:
    #     raise Http404("unknown expense")
    #
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })
