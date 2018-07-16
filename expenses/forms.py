from django import forms

from expenses.models import Expense, Note


class ExpenseForm(forms.ModelForm):
    funny = forms.BooleanField(required=False)

    class Meta:
        model = Expense
        fields = "__all__"


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'content',
        )
