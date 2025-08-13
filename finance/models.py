from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return f"{self.name} ({self.type})"
       

class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(max_length=10 , choices=[
        ("income", "Income"), 
        ("expense", "Expense")
        ]
    ) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.transaction_type})"
    
class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget_month = models.IntegerField()
    budget_year = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} Budget - {self.amount} ({self.budget_month}/{self.budget_year})"
