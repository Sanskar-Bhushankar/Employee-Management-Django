from django.shortcuts import render,redirect
from .models import employee

# Create your views here.
def emp(request):
    emps=employee.objects.all()
    return render(request,'home.html',{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        print("Data incoming")

        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")
        
        #create model object with the data
        e=employee()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department

        if emp_working is None:
            e.working=False
        
        else:
            e.working=True

        #saving data
        e.save()


        return redirect("/emp/home/")
    return render(request,'add_emp.html',{})

def delete_emp(request,emp_id):
    print(emp_id)
    emp=employee.objects.get(id=emp_id)
    emp.delete()
    return redirect('/emp/home')

def update_emp(request,emp_id):
    emp=employee.objects.get(id=emp_id)
    return render(request,'update_emp.html',{
        'emp':emp,
    })

def do_update_emp(request,emp_id):
    if request.method=='POST':
         emp_name=request.POST.get("emp_name")
         emp_id_temp=request.POST.get("emp_id")
         emp_phone=request.POST.get("emp_phone")
         emp_address=request.POST.get("emp_address")
         emp_department=request.POST.get("emp_department")
         emp_working=request.POST.get("emp_working")

         e=employee.objects.get(id=emp_id)

         e.name=emp_name
         e.emp_id=emp_id_temp
         e.phone=emp_phone
         e.address=emp_address
         e.department=emp_department
         if emp_working is None:
            e.working=False
        
         else:
             e.working=True

        #saving data
         e.save()

         

    return redirect("/emp/home")

