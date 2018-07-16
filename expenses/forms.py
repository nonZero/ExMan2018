from django import forms

from expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    funny = forms.BooleanField(required=False)

    class Meta:
        model = Expense
        fields = "__all__"
