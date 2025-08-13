from django.contrib import admin
from finance.models import Category, Transaction, Budget

admin.site.register(
    [
        Category, 
        Transaction, 
        Budget
    ]
)