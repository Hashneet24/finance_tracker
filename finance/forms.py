from django import forms
from finance.models import Category, Transaction, Budget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "type"
        ]

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["category", 
                  "title", 
                  "amount", 
                  "date", 
                  "transaction_type"
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields =[
            "category",
            "amount",
            "budget_month",
            "budget_year",
        ]