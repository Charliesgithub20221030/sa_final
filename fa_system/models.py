from django.db import models


class User(models.Model):
    """Model definition for User."""

    account = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    authentication = models.IntegerField()
    def __str__(self):
        return self.account
    
class Investor(models.Model):

    investId = models.CharField( max_length=10)
    account = models.CharField( max_length=50)
    name = models.CharField( max_length=15)
    phone = models.CharField( max_length=15)
    numberOfInvest = models.PositiveIntegerField()

    def __str__(self):
        return self.

class FinancialDep(models.Model):

    account = models.CharField( max_length=50)
    manager = models.CharField( max_length=15)
    address = models.CharField( max_length=50)
    def __str__(self):
        return self.manager

class Analyst(models.Model):

    analystId = models.CharField( max_length=10)
    account = models.CharField( max_length=50)
    name = models.CharField( max_length=15)
    def __str__(self):
        return self.name

class Bill(models.Model):
    billId = models.CharField( max_length=10)
    itemId = models.CharField( max_length=10)
    branchId = models.CharField( max_length=10)
    month = models.PositiveIntegerField()
    itemName = models.CharField( max_length=15)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return itemName

class Receipt(models.Model):
    receiptId = models.CharField(max_length=10)
    branchId = models.CharField( max_length=10)
    month = models.PositiveIntegerField()
    rent = models.PositiveIntegerField()
    fee = models.PositiveIntegerField()
    
    def __str__(self):
        return self.receiptId

class Salary(models.Model):
    paySheetId = models.CharField( max_length=10)
    branchId = models.CharField( max_length=10)
    month = models.PositiveIntegerField()
    totalSalary = models.PositiveIntegerField()

    def __str__(self):
        return self.paySheetId

class Sales(models.Model):
    orderId = models.CharField(, max_length=10)
    date = models.DateField(, auto_now=False, auto_now_add=False)
    branchId = models.CharField(, max_length=10)
    itemId = models.CharField(, max_length=10)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.orderId

class Report(models.Model):
    reportId = models.CharField(, max_length=10)
    analystId = models.CharField(, max_length=10)
    topic = models.CharField(, max_length=15)
    folder = models.CharField(, max_length=50)

    def __str__(self):
        return self.receiptId