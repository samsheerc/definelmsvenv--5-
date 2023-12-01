from django.http import JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = DepartmentForm()
    dsn = Department.objects.all()
    context = {'form':form, 'dsn':dsn}
    return render(request, 'core/home.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            did = request.POST.get('dsnid')
            designation = request.POST['designation']
            print('student id',did)

            if(did == ''):
                d = Department(designation=designation)
            else:
                d = Department(id=did, designation=designation)
            d.save()

            dsn = Department.objects.values()
            student_data = list(dsn)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        d = Department.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        print('Student ID',id)
        desgn = Department.objects.get(pk=id)
        student_data = {'id':desgn.id, 'designation':desgn.designation}
        return JsonResponse(student_data)