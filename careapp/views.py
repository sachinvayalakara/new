from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def fn_home(req):
    try:
        return render(req, 'pro.html')
    except Exception as e:
        print(e)
        return HttpResponse('hello')


def fn_wet(req):
    try:
        return render(req,'part.html')
    except Exception as e:
        print(e)
        return HttpResponse('wet error')    


def fn_shine(req):
    try:
        return render(req,'part2.html')
    except Exception as e:
        print(e)
        return HttpResponse('shine error')    


def fn_balance(req):
    try:
        return render(req,'part3.html')
    except Exception as e:
        print(e)
        return HttpResponse('balance error')    

def fn_admin(request):
    
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            print (password)
            login_obj=Login.objects.get(email=email)
            if login_obj.password == password:
                print("hiiii")
                if login_obj.role == 'admin':
                    return render(request, 'adminhome.html')
                
        return render(request, 'adminlog.html')
    except Exception as e:
        print(e)
        return HttpResponse('error occured')

def fn_createplan(req):
    try:
        if req.method == 'POST':
            plan_title = req.POST['title']
            plan_price = req.POST['price']
    
            plan_obj = Plan(plan_title=plan_title,plan_price=plan_price)
            plan_obj.save()
            
            if plan_obj.id > 0:    
                plan_serves = req.POST.getlist('services[]')
                for serv in plan_serves:
                    serv_obj = PlanServices(service_title=serv, fk_plan=plan_obj)
                    serv_obj.save()
                return HttpResponse('1')

        return render(req,'createplan.html')
    except Exception as e:
        print(e)
        return HttpResponse('balance error')    

             
def fn_viewplan(req):
    try:
        plans = Plan.objects.all()
        if 'id' in req.GET:
            plan_obj = Plan.objects.get(id=req.GET['id'])
            plan_services = PlanServices.objects.filter(fk_plan=plan_obj)
            plan_obj.serv = plan_services
            return render(req,'editplan.html', {'plan': plan_obj, 'plans': plans})
        return render(req,'viewplan.html', {'plans': plans})
    except Exception as e:
        print(e)
        return HttpResponse('balance error')

def fn_deleteService(request):
    try:
        service_id = request.POST['id']
        pservice_obj = PlanServices.objects.get(id=service_id).delete()
        
    except:
        print('error')
    return HttpResponse('ok')