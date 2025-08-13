from django.shortcuts import render
from finance.models import Category, Transaction, Budget
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from finance.forms import CategoryForm, TransactionForm, BudgetForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

@login_required
def home(request):
    total_income = Transaction.objects.filter(transaction_type="income").aggregate(total = Sum("amount"))["total"] or 0
    total_expense = Transaction.objects.filter(transaction_type="expense").aggregate(total = Sum("amount"))["total"] or 0
    balance = total_income - total_expense
    current_month = now().month
    current_year = now().year

    budgets = Budget.objects.filter(budget_month=current_month, budget_year=current_year)
    alerts = []
    for budget in budgets:
        spent = Transaction.objects.filter(
            transaction_type="expense",
            category=budget.category,
            date__year=current_year,
            date__month=current_month
        ).aggregate(total=Sum("amount"))["total"] or 0

        if spent >= budget.amount:
            alerts.append(f"Alert! You have exceeded the budget for '{budget.category.name}'.")
        elif spent >= 0.9 * budget.amount:
            alerts.append(f"Warning! You are nearing the budget limit for '{budget.category.name}'.")



    context = {
        "total_income" : total_income,
        "total_expense" : total_expense,
        "balance" : balance,
        "alerts": alerts,
    }

    return render(request, "home.html", context)

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy("category-list")



class TransactionListView(ListView):
    model = Transaction
    template_name = "transaction_list.html"
    context_object_name = "transactions"

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transaction_form.html"
    success_url = reverse_lazy("transaction-list")

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transaction_form.html"
    success_url = reverse_lazy("transaction-list")

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transaction_confirm_delete.html"
    success_url = reverse_lazy("transaction-list")
    



class BudgetListView(ListView):
    model = Budget
    template_name = "budget_list.html"
    context_object_name = "budgets"

class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = "budget_form.html"
    success_url = reverse_lazy("budget-list")

class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = "budget_form.html"
    success_url = reverse_lazy("budget-list")

class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = "budget_confirm_delete.html"
    success_url = reverse_lazy("budget-list")



