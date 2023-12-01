from django.shortcuts import render,redirect
from requests import post
from lmsmainapp.forms import *
from lmsmainapp.models import *
from django.contrib.auth import logout
from lmsmainapp.serializers import *



############### login #################

# def login(request):

#     return render(request, 'User_UI/login.html')

def user_login(request):

   
	msg=''
   
	if request.method=='POST':
        
       
		username=request.POST['username']
		password=request.POST['password']
		user=login.objects.filter(username=username,password=password,role=2).count()
        
		if user > 0:
            
			user=login.objects.filter(username=username,password=password,role=2).first()
			request.session['userid'] = user.id
			print(request.session['userid'])
            
			return redirect('index')
            

		else:
			msg='Invalid!!'
            
	form=UserLoginForm
	return render(request, 'User_UI/login.html',{'form':form,'msg':msg})





def user_logut(request):
        logout(request)
        return redirect('loginu')


#################### home ###############
def index(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:
        un=request.session['userid']   
        user=login.objects.filter(id=un).values
        banners=banner.objects.all()
        
        context={
            'username':user,
            'bann':banners
        }

        return render(request, 'User_UI/index.html',context)

def about(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        return render(request, 'User_UI/about.html')



def coursereg(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        return render(request, 'User_UI/coursereg.html')


# def contact(request):
#     if 'userid' not in request.session:
#         return redirect('loginu')
#     else:

#         return render(request, 'User_UI/contact.html')

############### all exam ###################


def vexam(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:
        exm = exam.objects.all()
        context = {'exm':exm}
        return render(request, 'User_UI/viewallexam.html', context)


############### all Courses ###################


def vcourse(request,id):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        exm = course.objects.filter(exam=id)
      
        context = {
            'exm':exm
        }
        return render(request, 'User_UI/allcourse.html',context)



################### video tutorials #########################

def error404(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        return render(request, 'User_UI/404.html')


################ video class ############################

from django.shortcuts import render, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse

def vclass(request,id):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        st = video_class.objects.filter(course=id)
        form = CommentForm()
        com = videocomment.objects.all()
        un=request.session['userid']   
        user=login.objects.filter(id=un).values
        pdf=notes.objects.all()
        syl=syllabus.objects.filter(course=id)
        context = {
            'vde':st,
            'form':form,
            'com':com,
            'userid':un,
            'username':user,
            'pdf':pdf,
            'syl':syl
            }

        return render(request, 'User_UI/tutorials.html',context)








###################### comment ############################





def video(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:

        st = video_class.objects.all()
        
        context = {
            'vde':st
        }
        return render(request, 'User_UI/video.html',context)         







def coursedesc(request,id):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:
        designation = course.objects.filter(id=id)
        coun = course_registration.objects.filter(course=id).count()
        context = {
            'c':coun,
            'st': designation,
            }
        return render(request, 'User_UI/coursereg.html',context)
    



def contact(request):
    if 'userid' not in request.session:
        return redirect('loginu')
    else:
        if request.method == 'POST':
            form = enquiryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = enquiryForm()
                context = {'form': form}
                return render(request, 'User_UI/contact.html', context)
        else:
            form = enquiryForm()
        context = {'form': form}
        return render(request, 'User_UI/contact.html',context)



@csrf_exempt
def save_data_comment(request):
    if request.method == 'POST':
        commentt = request.POST['comment']
        videoo = request.POST['video']
        user = request.POST['user']
        lg=login.objects.get(id=user)
        vid=video_class.objects.get(id=(videoo))
        s = videocomment.objects.create(comment=commentt, video=vid, user=lg)
        exm = videocomment.objects.filter(video=videoo).select_related('user').values('id', 'video', 'user__username', 'datetime', 'comment')
        student_data = list(exm)
        for comment in student_data:
            comment['datetime'] = comment['datetime'].strftime('%b %d %Y %I:%M %p')
        return JsonResponse({'status':'Data Saved', 'student_data':student_data})
    else:
        return JsonResponse({'status':'Not Saved'})
