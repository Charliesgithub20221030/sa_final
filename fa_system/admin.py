from django.contrib import admin
from fa_system.models import  Investor, Report, Purchase, Sales, Utility, Salary



class InvestorAdmin(admin.ModelAdmin):

    list_display=['investor','number_of_invest']
class ReportAdmin(admin.ModelAdmin):
    list_display=['reportid','analyst','topic','month','path']

class PurchaseAdmin(admin.ModelAdmin):
    list_display=['purchaseid','itemid','itemname','branch','month','price','quantity']

class SalesAdmin(admin.ModelAdmin):
    list_display=['salesid','date','branch','itemid','itemname','price','quantity']

class UtilityAdmin(admin.ModelAdmin):
    list_display=['billid','branch','month','rent','electric']
class SalaryAdmin(admin.ModelAdmin):
    list_display=['salaryid','branch','month','total']
        

# class UserAdmin(UserAdmin):
#     list_display=['username','email','password','authority']


# class InvestorAdmin(admin.ModelAdmin):
#     play_list=['investorId','account','name','phone','numberOfInvest']
# class BranchAdmin(admin.ModelAdmin):
#     play_list=['branchId','account','shopkeeper','branch','address']
# class FinancialDepAdmin(admin.ModelAdmin):
#     play_list=['account','manager','address']
# class AnalystAdmin(admin.ModelAdmin):
#     play_list=['analystId','account','name']
# class BillAdmin(admin.ModelAdmin):
#     play_list=['billId','itemId','branchId','month','itemName','price','quantity']
# class ReceiptAdmin(admin.ModelAdmin):
#     play_list=['receiptId','branchId','month','rent','fee']
# class SalaryAdmin(admin.ModelAdmin):
#     play_list=['paySheetId','branchId','month','totalSalary']
# class SalesAdmin(admin.ModelAdmin):
#     play_list=['orderId','date','branchId','itemId','itemName','price','quantity']
# class ReportAdmin(admin.ModelAdmin):
#     play_list=['reportId','analystId','topic','folder']


admin.site.register(Investor, InvestorAdmin)#
admin.site.register(Report, ReportAdmin)   
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sales,SalesAdmin)
admin.site.register(Utility,UtilityAdmin)  
admin.site.register(Salary, SalaryAdmin)

 
