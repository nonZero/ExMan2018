from django import forms


class ExpenseForm(forms.Form):
    date = forms.DateField()
    title = forms.CharField(max_length=400)
    amount = forms.DecimalField(max_digits=9, decimal_places=2)
    comment = forms.CharField(required=False, widget=forms.Textarea())
    funny = forms.BooleanField(required=False)
