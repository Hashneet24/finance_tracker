"""
URL configuration for finance_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finance import views
from finance.views import (CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                           TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
                           BudgetListView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView,)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name = "home"),
    path('admin/', admin.site.urls),
    path("categories/", CategoryListView.as_view(), name = "category-list"),
    path("categories/add/", CategoryCreateView.as_view(), name="category-add"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category-edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    
    path("transactions/", TransactionListView.as_view(), name = "transaction-list"),
    path("transactions/add/", TransactionCreateView.as_view(), name="transaction-add"),
    path("transactions/<int:pk>/edit/", TransactionUpdateView.as_view(), name="transaction-edit"),
    path("transactions/<int:pk>/delete/", TransactionDeleteView.as_view(), name="transaction-delete"),
    
    path("budgets/", BudgetListView.as_view(), name = "budget-list"),
    path("budgets/add/", BudgetCreateView.as_view(), name="budget-add"),
    path("budgets/<int:pk>/edit/", BudgetUpdateView.as_view(), name="budget-edit"),
    path("budgets/<int:pk>/delete/", BudgetDeleteView.as_view(), name="budget-delete"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]

