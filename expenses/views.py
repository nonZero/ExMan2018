from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, \
    CreateView, UpdateView, DeleteView

from expenses.forms import NoteForm
from expenses.models import Expense


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense

    def total(self):
        return Expense.objects.aggregate(total=Sum('amount'))['total']


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


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = "__all__"

    def form_valid(self, form):
        resp = super().form_valid(form)
        msg = f"Expense #{form.instance.id} created successfully."
        messages.success(self.request, msg)
        return resp


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = "__all__"

    def form_valid(self, form):
        resp = super().form_valid(form)
        msg = f"Expense #{form.instance.id} updated successfully."
        messages.success(self.request, msg)
        return resp


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy("expenses:list")

    def delete(self, request, *args, **kwargs):
        o = self.get_object()
        msg = f"Expense #{o.id} deleted."
        resp = super().delete(request, *args, **kwargs)
        messages.success(request, msg)
        return resp
