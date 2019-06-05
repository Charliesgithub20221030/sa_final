
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Investor(models.Model):

    investor=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=True,primary_key=True)
    number_of_invest=models.PositiveIntegerField()
    def __str__(self):
        return self.investor

class Report(models.Model):
    reportid=models.CharField(max_length=30, primary_key=True)
    analyst=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic=models.CharField(max_length=100,)
    path=models.CharField(max_length=300)
    month=models.PositiveIntegerField()
    def __str__(self):
        return self.analyst

class Purchase(models.Model):
    purchaseid=models.CharField(max_length=30, primary_key=True)
    itemid=models.CharField(max_length=300)    
    itemname=models.CharField(max_length=50)
    branch=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    month=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.purchaseid

class Sales(models.Model):
    salesid=models.CharField(max_length=30, primary_key=True)
    date=models.DateField(auto_now=True)
    branch=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=True)
    itemid=models.CharField(max_length=30)
    itemname=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return self.salesid

class Utility(models.Model):
    billid=models.CharField(max_length=30, primary_key=True)
    branch=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=True)
    month=models.PositiveIntegerField()
    rent=models.PositiveIntegerField()
    electric=models.PositiveIntegerField()
    def __str__(self):
        return self.billid


class Salary(models.Model):
    salaryid=models.CharField(max_length=30, primary_key=True)
    branch=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    month=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    def __str__(self):
        return self.salaryid



# ## -----------------old line------------
# class User(AbstractUser):
#     # account=models.CharField()
#     authority = models.IntegerField()
    

# # class Users(models.Model):
# #     account = models.OneToOneField( User,primary_key=True,on_delete=models.CASCADE)
# #     password = models.CharField( max_length=50)
# #     authority = models.IntegerField()
# #     # Investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
# #     # Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
# #     # Analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.account
    
# class Investor(models.Model):
#     investId = models.CharField( max_length=10,primary_key=True)
#     # account = models.CharField( max_length=50)
#     account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     name = models.CharField( max_length=15)
#     phone = models.CharField( max_length=15)
#     numberOfInvest = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name
# class Branch(models.Model):
#     branchId = models.CharField( max_length=10,primary_key=True)
#     # account = models.CharField( max_length=50)
#     account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
#     shopkeeper = models.CharField( max_length=15)
#     branch = models.CharField( max_length=50)
#     address = models.CharField( max_length=50)

#     def __str__(self):
#         return branch

# class FinancialDep(models.Model):
#     # User = models.ForeignKey(User, on_delete=models.CASCADE)
#     # account = models.CharField( max_length=50,primary_key=True)
#     account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
#     manager = models.CharField( max_length=15)
#     address = models.CharField( max_length=50)
#     def __str__(self):
#         return self.manager

# class Analyst(models.Model):

#     analystId = models.CharField( max_length=10,primary_key=True)
#     # account = models.CharField( max_length=50)
#     account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     name = models.CharField( max_length=15)
#     def __str__(self):
#         return self.name

# class Bill(models.Model):
#     billId = models.CharField( max_length=10,primary_key=True)
#     itemId = models.CharField( max_length=10)
#     # branchId = models.CharField( max_length=10)
#     month = models.PositiveIntegerField()
#     itemName = models.CharField( max_length=15)
#     price = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField()
#     branchId = models.ForeignKey(Branch, on_delete=models.CASCADE)

#     def __str__(self):
#         return itemName

# class Receipt(models.Model):
#     receiptId = models.CharField(max_length=10,primary_key=True)
#     # branchId = models.CharField( max_length=10)
#     month = models.PositiveIntegerField()
#     rent = models.PositiveIntegerField()
#     fee = models.PositiveIntegerField()
#     branchId = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.receiptId

# class Salary(models.Model):
#     paySheetId = models.CharField( max_length=10,primary_key=True)
#     # branchId = models.CharField( max_length=10)
#     month = models.PositiveIntegerField()
#     totalSalary = models.PositiveIntegerField()
#     branchId = models.ForeignKey(Branch, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.paySheetId

# class Sales(models.Model):
#     orderId = models.CharField( max_length=10,primary_key=True)
#     date = models.DateField( auto_now=False, auto_now_add=False)
#     # branchId = models.CharField( max_length=10)
#     itemId = models.CharField( max_length=10)
#     price = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField()
#     branchId = models.ForeignKey(Branch, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.orderId

# class Report(models.Model):
#     reportId = models.CharField( max_length=10,primary_key=True)
#     # analystId = models.CharField( max_length=10)
#     topic = models.CharField( max_length=15)
#     folder = models.CharField( max_length=50)
#     analystId = models.ForeignKey(Analyst, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.receiptId