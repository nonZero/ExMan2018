from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, TemplateView, ListView, \
    CreateView, UpdateView, DeleteView

from expenses.forms import ExpenseForm, NoteForm
from expenses.models import Expense


class MyView(LoginRequiredMixin, TemplateView):
    template_name = "my_template.html"
    title = "The best VIEW ever!!!!!"
    foo = "adslkfjhadlkfjhadlkfjhas"

    def bar(self):
        return 10 * 20

    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        d['baz'] = 8734 * 8736 + 343
        return d


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense

    def total(self):
        return Expense.objects.aggregate(total=Sum('amount'))['total']


# @login_required
# def expense_list(request):
#     return render(request, "expenses/expense_list.html", {
#         'object_list': Expense.objects.all(),
#         # 'total': sum(o.amount for o in Expense.objects.all())
#         'total': Expense.objects.aggregate(
#             total=Sum('amount'))['total']
#     })


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense

    def get(self, request, *args, **kwargs):
        self.form = NoteForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, pk):
        self.object = self.get_object()
        self.form = NoteForm(request.POST)
        if self.form.is_valid():
            self.form.instance.expense = self.object
            self.form.save()
            return redirect(self.object)

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# @login_required
# def expense_detail(request, pk):
#     o = get_object_or_404(Expense, pk=pk)
#
#     if request.method == "POST":
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.instance.expense = o
#             form.save()
#             return redirect(o)
#     else:
#         form = NoteForm()
#
#     return render(request, "expenses/expense_detail.html", {
#         'object': o,
#         'form': form,
#     })

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = "__all__"

    def form_valid(self, form):
        resp = super().form_valid(form)
        msg = f"Expense #{form.instance.id} created successfully."
        messages.success(self.request, msg)
        return resp



# @login_required
# def expense_create(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             # form.instance.expense = ...
#             o = form.save()
#             msg = f"Expense #{o.id} created successfully."
#             messages.success(request, msg)
#             return redirect(o)
#     else:
#         form = ExpenseForm()
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = "__all__"

    def form_valid(self, form):
        resp =  super().form_valid(form)
        msg = f"Expense #{form.instance.id} updated successfully."
        messages.success(self.request, msg)
        return resp

# @login_required
# def expense_update(request, pk):
#     o = get_object_or_404(Expense, pk=pk)
#
#     if request.method == "POST":
#         form = ExpenseForm(request.POST, instance=o)
#         if form.is_valid():
#             o = form.save()
#             msg = f"Expense #{o.id} updated successfully."
#             messages.success(request, msg)
#             return redirect(o)
#     else:
#         form = ExpenseForm(instance=o)
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy("expenses:list")

    def delete(self, request, *args, **kwargs):
        o = self.get_object()
        msg = f"Expense #{o.id} deleted."
        resp = super().delete(request, *args, **kwargs)
        messages.success(request, msg)
        return resp


# @login_required
# def expense_delete(request, pk):
#     o = get_object_or_404(Expense, pk=pk)
#
#     if request.method == "POST":
#         msg = f"Expense #{o.id} deleted."
#         o.delete()
#         messages.success(request, msg)
#         return redirect("expenses:list")
#
#     return render(request, "expenses/expense_confirm_delete.html", {
#         'object': o,
#     })
