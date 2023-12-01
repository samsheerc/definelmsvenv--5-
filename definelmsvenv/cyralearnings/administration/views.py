from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from lmsmainapp.forms import *
from lmsmainapp.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



#######login############################


def admin_login(request):

   
	msg=''
   
	if request.method=='POST':
        
       
		username=request.POST['username']
		password=request.POST['password']
		user=login.objects.filter(username=username,password=password,role=0).count()
        
		if user > 0:
            
			user=login.objects.filter(username=username,password=password,role=0).first()
			request.session['username'] = user.id
			print(request.session['username'])

			return redirect('home')
            

		else:
			msg='Invalid!!'
            
	form=loginform
	return render(request, 'administration/login/login.html',{'forms':form,'msg':msg})




def admin_logout(request):
        logout(request)
        return redirect('login')


############### home ##############################



def home_page(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        un=request.session['username']   
        user=login.objects.filter(id=un).values
        total_course   = course.objects.count()
        total_subject  = subject.objects.count()
        total_exam     = exam.objects.count()
        total_question = question_bank.objects.count()
        context={
            'course'  :total_course,
            'subject' :total_subject,
            'exam'    :total_exam,
            'question':total_question,
            'username':user
        }
        return render(request, 'administration/home/home.html',context)




####################designation######################
def home(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
    
        form = designationForm()
        dsn = designation.objects.all()
        
        context = {'form':form, 'dsn':dsn}
        return render(request, 'administration/core/home.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = designationForm(request.POST)
        if form.is_valid():
            cid = request.POST.get('dsnid')
            designation1 = request.POST['designation']
            print('student id',cid)

            if(cid == ''):
                d = designation(designation=designation1)
            else:
                d = designation(id=cid, designation=designation1)
            d.save()

            dsn = designation.objects.values()
            student_data = list(dsn)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        d = designation.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        print('Student ID',id)
        desgn = designation.objects.get(pk=id)
        student_data = {'id':desgn.id, 'designation':desgn.designation}
        return JsonResponse(student_data)

################################## add exam #################################

def home_exam(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        form = examForm()
        exm = exam.objects.all()
        context = {'form':form, 'exm':exm}
        return render(request, 'administration/exam/exam.html', context)


@csrf_exempt
def save_data_exam(request):
    if request.method == 'POST':
        form = examForm(request.POST)
        if form.is_valid():
            eid = request.POST.get('exmid')
            exam_name = request.POST['exam_name']
            description = request.POST['description']
            remarks = request.POST['remarks']
            print('student id',eid)

            if(eid == ''):
                s = exam(exam_name=exam_name, description=description, remarks=remarks)
            else:
                s = exam(id=eid, exam_name=exam_name, description=description, remarks=remarks)
            s.save()

            exm = exam.objects.values()
            student_data = list(exm)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = exam.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        print('Student ID',id)
        student = exam.objects.get(pk=id)
        student_data = {'id':student.id, 'exam_name':student.exam_name, 'description':student.description, 'remarks':student.remarks}
        return JsonResponse(student_data)


        
################################## add course #################################


def add_course(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
            if request.method == 'POST':
                form = courseform1(request.POST, request.FILES)
                userid=request.session.get('username')
                if form.is_valid():
                    obj=form.save(commit=False)
                    form=courseform1()
                    designation = login.objects.get(id=userid)
                    obj.user=designation
                    obj.save()
                details=course.objects.all()
                exams=exam.objects.all()
                context = {'form': form, 'st': details,'ex':exams}
                return render(request, 'administration/course/course.html',context)
                    
            else:
                form = courseform1()
            details=course.objects.all()
            exams=exam.objects.all()
            context = {'form': form, 'st': details,'ex':exams}
            return render(request, 'administration/course/course.html', context)




# def home_course(request):
#     if 'username' not in request.session:
#         return redirect('login')
#     else:
#         form = courseform1()
#         exm = course.objects.all()
#         context = {'form':form, 'st':exm}
#         return render(request, 'administration/course/course.html', context)


# @csrf_exempt
# def save_data_course(request):
#     if request.method == 'POST':
#         form = courseform1(request.POST)
#         if form.is_valid():
#             eid = request.POST.get('exmid')
#             course_name = request.POST['course_name']
#             description = request.POST['description']
#             amount = request.POST['amount']
#             duration = request.POST.get('duration')
#             exams = request.POST['exam']
#             image = request.POST['image']
#             isdemanded = request.POST['isdemanded']
#             print('student id',eid)

#             if(eid == ''):
#                 s = course(course_name=course_name, description=description, amount=amount,duration=duration, exams=exams, image=image,isdemanded=isdemanded)
#             else:
#                 s = course(id=eid,course_name=course_name, description=description, amount=amount,duration=duration, exams=exams, image=image,isdemanded=isdemanded)
#             s.save()

#             exm = course.objects.values()
#             student_data = list(exm)
#             return JsonResponse({'status':'Data Saved', 'student_data':student_data})
#         else:
#             return JsonResponse({'status':'Not Saved'})    


@csrf_exempt
def delete_data_course(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = course.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})  
    
      
def editcourse(request,id):
    crs =course.objects.get(id=id)
    form=courseform1(instance=crs)
    if request.method == 'POST':
        form = courseform1(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addcourse') 
    context = {'forms': form}
    return render(request,'administration/course/editcourse.html',context)

########################## add subject ########################



def add_subject(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subjectform(request.POST, request.FILES)
            userid=request.session.get('username')
            if form.is_valid():
                obj=form.save(commit=False)
                form = subjectform()
                designation = login.objects.get(id=userid)
                obj.user=designation
                obj.save()
            details=subject.objects.all()
            context = {'form': form, 'st': details}
            return render(request, 'administration/subject/subject.html',context)
                    
                
        else:
            form = subjectform()
        details=subject.objects.all()
        context = {'form': form, 'st': details}
        return render(request, 'administration/subject/subject.html', context)
        # return render(request, 'User_UI/index.html',context)


@csrf_exempt
def delete_data_subject(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = subject.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 

  
@csrf_exempt
def editsubject(request,id):
    sub =subject.objects.get(id=id)
    form=subjectform(instance=sub)
    if request.method == 'POST':
        form = subjectform(request.POST, request.FILES, instance=sub)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('sub') 
    context = {'forms': form}
    return render(request,'administration/subject/editsub.html',context)
######################add topic ###########################




def add_topic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = topicform(request.POST, request.FILES)
            userid=request.session.get('username')
            if form.is_valid():
                obj=form.save(commit=False)
                form = topicform()
                designation = login.objects.get(id=userid)
                obj.user=designation
                obj.save()
            details=topic.objects.all()
            context = {'form': form, 'st': details}
            return render(request, 'administration/topic/topic.html',context)
                
                
        else:
            form = topicform()
        details=topic.objects.all()
        context = {'form': form, 'st': details}
        return render(request, 'administration/topic/topic.html', context)  

@csrf_exempt
def delete_data_topic(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = topic.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


def edittopic(request,id):
    top =topic.objects.get(id=id)
    form=topicform(instance=top)
    if request.method == 'POST':
        form = topicform(request.POST, request.FILES, instance=top)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('topicc') 
    context = {'forms': form}
    return render(request,'administration/topic/edittopic.html',context)

######################add subtopic ###########################




def add_subtopic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subtopicform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = subtopicform()
                designation = Subtopics.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/subtopic/subtopic.html',context)
                
        else:
            form = subtopicform()
        designation = Subtopics.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/subtopic/subtopic.html', context)  

@csrf_exempt
def delete_data_subtopic(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = Subtopics.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def editsubtopic(request,id):
    st =Subtopics.objects.get(id=id)
    form=subtopicform(instance=st)
    if request.method == 'POST':
        form = subtopicform(request.POST, request.FILES, instance=st)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('topicsub') 
    context = {'forms': form}
    return render(request,'administration/subtopic/editst.html',context)

        
######################add question ###########################




def add_question(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = question_bankform(request.POST, request.FILES)
            userid=request.session.get('username')
            if form.is_valid():
                obj=form.save(commit=False)
                form = question_bankform()
                designation = login.objects.get(id=userid)
                obj.user=designation
                obj.save()
            details=question_bank.objects.all()
            context = {'form': form, 'st': details}
            return render(request, 'administration/questionbank/questionbank.html',context)
                    
        else:
            form = question_bankform()
        details=question_bank.objects.all()
        context = {'form': form, 'st': details}
        return render(request, 'administration/questionbank/questionbank.html', context)  

@csrf_exempt
def delete_data_question(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = question_bank.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    



def editqs(request,id):
    qs =question_bank.objects.get(id=id)
    form=question_bankform(instance=qs)
    if request.method == 'POST':
        form = question_bankform(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('qbadd') 
    context = {'forms': form}
    return render(request,'administration/questionbank/editqb.html',context)
################# add exam master ###########################

def addexmaster(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = exammasterForm(request.POST, request.FILES)
            userid=request.session.get('username')
            if form.is_valid():
                obj=form.save(commit=False)
                form = exammasterForm()
                designation = login.objects.get(id=userid)
                obj.user=designation
                obj.save()
                designation=exam_master.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/exam_master/exammaster.html',context)
        else:
            form = exammasterForm()
        designation=exam_master.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/exam_master/exammaster.html', context)


@csrf_exempt
def delete_data_exmaster(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s  = exam_master.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def editem(request,id):
    crs =exam_master.objects.get(id=id)
    form=exammasterForm(instance=crs)
    if request.method == 'POST':
        form = exammasterForm(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('homeem') 
    context = {'forms': form}
    return render(request,'administration/exam_master/editem.html',context)

##################### QUESTIONBANK OPTIONS ##################



def addoptions(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = optionsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = optionsForm()
                designation = question_bank_options.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/qsoptions/options.html',context)
                
        else:
            form = optionsForm()
        designation = question_bank_options.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/qsoptions/options.html',context)





@csrf_exempt
def delete_data_addoptions(request):
    if request.method == 'POST':
        id = request.POST.get('oid')
        d = question_bank_options.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 


@csrf_exempt
def editop(request,id):
    crs =question_bank_options.objects.get(id=id)
    form=optionsForm(instance=crs)
    if request.method == 'POST':
        form = optionsForm(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('op') 
    context = {'forms': form}
    return render(request,'administration/qsoptions/editoption.html',context)



################# add video_class ###########################


def addvideo(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = videoform(request.POST, request.FILES)
            userid=request.session.get('username')
            if form.is_valid():
                obj=form.save(commit=False)
                form = videoform()
                designation = login.objects.get(id=userid)
                obj.user=designation
                obj.save()
                videooo=video_class.objects.all()
                context = {'form': form, 'st': videooo}
                return render(request, 'administration/videoclass/videoclass.html',context)
        else:
            form = videoform()
        videooo=video_class.objects.all()
        context = {'form': form, 'st': videooo}
        return render(request, 'administration/videoclass/videoclass.html', context)


@csrf_exempt
def deletevideo(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s  = video_class.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


def editvideo(request,id):
    crs =video_class.objects.get(id=id)
    form=videoform(instance=crs)
    if request.method == 'POST':
        form = videoform(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('vdo') 
    context = {'forms': form}
    return render(request,'administration/videoclass/editvideo.html',context)


##################add banner##################

from django.utils import timezone

def addbanner(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        
        if request.method == 'POST':
            
            form = bannerForm(request.POST, request.FILES)
            userid = request.session.get('username')
            print
            if form.is_valid():
                obj=form.save(commit=False)
                form = bannerForm()
                uid=login.objects.get(id=userid)
                print("##########################")
                print(timezone.now())
                print("##########################")
                obj.user=uid
                obj.save()
                designation = banner.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/banner/banner.html',context)
        else:
            form = bannerForm()
        designation=banner.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/banner/banner.html',context)

@csrf_exempt
def delete_data_banner(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = banner.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})  





###############add course subject allocation


def addcsallo(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = CourseSubjectAlloForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = CourseSubjectAlloForm()
                designation = course_subject_allocation.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/csallo/csallo.html', context)
        else:
            form = CourseSubjectAlloForm()
        designation=course_subject_allocation.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/csallo/csallo.html', context)


@csrf_exempt
def delete_data_csallo(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        d = course_subject_allocation.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def editcallo(request,id):
    csa =course_subject_allocation.objects.get(id=id)
    form=CourseSubjectAlloForm(instance=csa)
    if request.method == 'POST':
        form = CourseSubjectAlloForm(request.POST, request.FILES, instance=csa)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addcsallo') 
    context = {'forms': form}
    return render(request,'administration/csallo/editcsallo.html',context)

#add course subject topic allocation


def addtcallo(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = topicCourseAlloForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = topicCourseAlloForm()
                designation = topic_course_allocation.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/tcallo/tcallo.html', context)
        else:
            form = topicCourseAlloForm()
        designation=topic_course_allocation.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/tcallo/tcallo.html', context)


@csrf_exempt
def delete_data_tcallo(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        d = topic_course_allocation.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
    
def edittcallo(request,id):
    tc =topic_course_allocation.objects.get(id=id)
    form=topicCourseAlloForm(instance=tc)
    if request.method == 'POST':
        form = topicCourseAlloForm(request.POST, request.FILES, instance=tc)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addtcallo') 
    context = {'forms': form}
    return render(request,'administration/tcallo/edittcallo.html',context)


############## add exam_master question allocation

def addeqallo(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = emQuestionAlloForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = emQuestionAlloForm()
                designation = exam_question_allocation.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/eqallo/eqallo.html', context)
        else:
            form = emQuestionAlloForm()
        designation=exam_question_allocation.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/eqallo/eqallo.html', context)


@csrf_exempt
def delete_data_eqallo(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        d = exam_question_allocation.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
    
def editqallo(request,id):
    crs =exam_question_allocation.objects.get(id=id)
    form=emQuestionAlloForm(instance=crs)
    if request.method == 'POST':
        form = emQuestionAlloForm(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addeqallo') 
    context = {'forms': form}
    return render(request,'administration/eqallo/editeqallo.html',context)

####### add notes ###################

def addnotes(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        
        if request.method == 'POST':
            
            form = notesform(request.POST, request.FILES)
            userid = request.session.get('username')
            print
            if form.is_valid():
                obj=form.save(commit=False)
                uid=login.objects.get(id=userid)
                obj.user=uid
                obj.save()
                form = notesform()
                designation = notes.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/notes/notes.html', context)
                
        else:
            form = notesform()
        designation=notes.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/notes/notes.html', context)

@csrf_exempt
def delete_data_notes(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        d = notes.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def editnote(request,id):
    crs =notes.objects.get(id=id)
    form=notesform(instance=crs)
    if request.method == 'POST':
        form = notesform(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addnote') 
    context = {'forms': form}
    return render(request,'administration/notes/editnote.html',context)

#add syllabus 



def addsyllabus(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        
        if request.method == 'POST':
            
            form = syllabusform(request.POST, request.FILES)
            userid = request.session.get('username')
            print
            if form.is_valid():
                obj=form.save(commit=False)
                form = syllabusform()
                uid=login.objects.get(id=userid)
                obj.user=uid
                obj.save()
                designation = syllabus.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/syllabus/syllabus.html', context)
        else:
            form = syllabusform()
        designation=syllabus.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/syllabus/syllabus.html', context)

@csrf_exempt
def delete_data_syllabus(request):
    if request.method == 'POST':
        id = request.POST.get('bid')
        d = syllabus.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def editsyl(request,id):
    crs =syllabus.objects.get(id=id)
    form=syllabusform(instance=crs)
    if request.method == 'POST':
        form = syllabusform(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addsyllabus') 
    context = {'forms': form}
    return render(request,'administration/syllabus/editsy.html',context)


################### Enquiry ########################

def enquiry_(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
           
                details=enquiry.objects.all()
                context = { 'st': details}
                return render(request, 'administration/enquiry/enquiry.html',context)





@csrf_exempt
def delete_data_enquiry(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = enquiry.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


#Testimonial

def addtestimonial(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = testimonialform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = testimonialform()
                designation = testimonial.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'administration/testimonial/testimonial.html', context)
        else:
            form = testimonialform()
        designation=testimonial.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'administration/testimonial/testimonial.html', context)

@csrf_exempt
def delete_data_testimonial(request):
    if request.method == 'POST':
        id = request.POST.get('emid')
        d = testimonial.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def edittesti(request,id):
    crs =testimonial.objects.get(id=id)
    form=testimonialform(instance=crs)
    if request.method == 'POST':
        form = testimonialform(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('addtestimonial') 
    context = {'forms': form}
    return render(request,'administration/testimonial/edittesti.html',context)