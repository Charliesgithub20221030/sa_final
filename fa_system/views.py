from django.shortcuts import render
# from fa_system.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# page
def index(request):
    return render(request,"index.html")

def login(request):
	return render(request,"login.html")

def login_action(request):
    msg={'message':''}
    # 確認方法正確
    if request.method =="POST":
        id=request.POST.get('username')
        pwd=request.POST.get('password')
        # 確認帳號存在
        if User.objects.filter(account=id).exists():
            if User.objects.filter(password=pwd).exists():
                request.session['user']=id
                response =HttpResponseRedirect('/index/')
                return response
            else:
                msg['message']='Password error!'
        else:
            msg['message']='Account doesn\'t exist! Please contact your system administrator...'
    else:
        msg['message']="invalid method! use POST instead of GET or others"
    return render(request,"login.html",msg)

def product(request):
	return render(request,"product.html")
def about(request):
	return render(request,"about.html")
def statusReport(request):
	return render(request,"statusReport.html")
def branchReport(request):
	return render(request,"branchReport.html")
def salesReport(request):
	return render(request,"salesReport.html")
def financialReport(request):
	return render(request,"financialReport.html")
def analyzeData(request):
	return render(request,"analyzeData.html")

@login_required
def upload(request):
	return render(request,"upload.html")
def analyzeData(request):
	return render(request,"analysisData.html")
def analysisReport(request):
	return render(request,"analysisReport.html")


# actions
# uploading data
def upload_aciton(request):
    pass
def upload_report(request):
    pass
def view_data(requst):
    pass
def view_graph(request):
    pass
def search_data(request):
    pass