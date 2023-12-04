from django.shortcuts import render
from grievance.forms import userregforms,complaintregforms
from grievance.models import employees_ModelTable,complaint_ModelTable

# Create your views here.
def home(request):
    return render(request,'Home.html')
def admin(request):
    return render(request,'Admin.html')
def About(request):
    return render(request,'about.html')
def emlogin(request):
    return render(request,'emlogin.html')
def logout(request):
    return render(request,'logout.html')
def rly(request):
    return render(request,'reply.html')
def emphome(request):
    return render(request,'employees.html')
def adminlog(request):
    N=request.POST['name']
    P=request.POST['p']
    print(N,P)
    if(N=='admin' and P=='1234'):
        return render(request,'Adminhome.html')
    else:
        return render(request,'about.html')
def emlog(request):
    N=request.POST['name']
    P=request.POST['p']
    a=employees_ModelTable.objects.all().filter(Name=N,Mobilno=P).values()
    if not a:
        return render(request,'emlogin.html')  
    else:
        N=a[0]['Name']
        ID=a[0]['id']
        print(N,ID)
        request.session['Name']=N
        request.session['id']=ID
    return render(request,'employees.html',{'Name':N,'id':ID})
def empy(request):
    a=userregforms(request.POST)
    if(a.is_valid()):
        a.save()
        return render(request,'employeview.html',{'myform':a})
    else:
        return render(request,'regsiter.html',{'myform':a})
def employeeview(request):
    a=employees_ModelTable.objects.all()
    if not a:
        return render(request,'Adminhome.html')
    else:
        return render(request,'employeview.html',{'data':a})
def Adminhome(request):
    return render(request,'Adminhome.html')
def editiuser(request):
    uid=request.GET['userid']
    print('userid',uid)
    e=employees_ModelTable.objects.all().filter(id=uid)
    return render(request,'employeview.html',{'data':e})
def deleteuser(request):
    uid=request.GET['userid']
    print('userid',uid)
    d=employees_ModelTable.objects.get(id=uid)
    d.delete()
    d=employees_ModelTable.objects.all()
    return render(request,'employeview.html',{'data':d})
def EDIT(request):
    uid=request.GET['userid']
    print('userid',uid) 
    e=employees_ModelTable.objects.all().filter(id=uid)
    return render(request,'Editi.html',{'data':e})
def customerupdate (request):
    id=request.POST['id']
    Name=request.POST['Name']
    Mobilno=request.POST['Mobilno']
    Email=request.POST['Email']
    employees_ModelTable.objects.filter(id=id).update(Name=Name,Mobilno=Mobilno,Email=Email)
    e=employees_ModelTable.objects.all()
    return render(request,'employeview.html',{'data':e})
def complaint(request):
    n=request.session['Name']
    ID=request.session['id'] 
    return render(request,'grivncereg.html',{'empid':ID,'name':n})
def complaintview(request):
    a=complaint_ModelTable.objects.all()
    if not a:
        return render(request,'Adminhome.html')
    else:
        return render(request,'grivance.html',{'data':a})
def mycompaint(request):
    n=request.session['Name']
    ID=request.session['id'] 
    print(n)
    print(ID)
    b=complaint_ModelTable.objects.all().filter(id=ID).values()
    return render(request,'complaint.html',{'data':b})
def REPLY(request):
    uid=request.GET['userid']
    print('userid',uid) 
    return render(request,'reply.html',{'id':uid})
def replay2(request):
    ID=request.session['id']
    e=request.GET['id']
    c=request.GET['replay']
    complaint_ModelTable.objects.all().filter(id=e).update(reply=c)
    return render(request,'grivance.html',{'empid':ID,})
def complaint1(request):
    n=request.session['Name']
    ID=request.session['id']
    N=request.POST['Name']
    e=request.POST['empid']
    c=request.POST['complaint']
    mdl=complaint_ModelTable()
    mdl.empid=e
    mdl.Name=N
    mdl.complaint=c
    mdl.save()
    return render(request,'complaint.html',{'empid':ID,'name':n})
 

