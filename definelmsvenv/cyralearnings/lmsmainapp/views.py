from copy import Error
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse, response,JsonResponse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from collections import namedtuple
from PIL import Image
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.conf import settings
import jwt

class Loginview(APIView):
    def post(self,request):
        def get_tokens_for_login(user):
            refresh = RefreshToken.for_user(user)
            
            return {
            'status':"success",
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            }
        username=request.data.get("phone")
        use=login.objects.filter(username=username).first()
        serializer=loginSerializer(use,many=False)
       
        try:
            log=login.objects.filter(username=username,role=2)
            if(log):
                
                user=User.objects.get_or_create(username="user")[0]
                token=get_tokens_for_login(user)
                
                token['data'] = serializer.data
                return Response(token,status=status.HTTP_200_OK)
            else:
                raise ValueError
        except:
            return Response({"status":"fail"},status=status.HTTP_401_UNAUTHORIZED)



class WebLogin(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        data = login.objects.filter(username = username, password = password, role='Admin')
        if not data.exists():
            return Response(Error)
        login_data = login.objects.filter(username = username).first()
        serializer = loginSerializer(login_data, many=False)
        return Response(serializer.data)

class loginView(APIView):
 
    def get(self,request,username=None):
        if username is not None:
            user = login.objects.filter(username = username).first()
            serializer = loginSerializer(user, many=False)
            return Response(serializer.data)

        user = login.objects.all()
        serializer = loginSerializer(user,many=True)
        return Response(serializer.data)

    def post(self,req):
        serializer = loginSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
       
    def delete(self,req,id):
        login.objects.filter(id=id).delete()
        return Response({"msg":1})

    def put(self,req,id): 
        user   = login.objects.filter(id=id).first()
        
        serializer = loginSerializer(user,data=req.data,partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class CheckuserView(APIView):
    def post(self,req):
        username = req.data['phone']
        user = login.objects.filter(username = username,role=2).first()
        if user is None:
            return Response({"msg":"fail"})
        else:
            serializer=loginSerializer(user,many=False)
            return Response({"msg":"success","data":serializer.data})


# SERIALIZER FOR REGISTRATION OPERATIONS:

class registrationView(APIView):

    def get(self,request,username=None):
        if username is not None:
            register   = registration.objects.get(username=username)
            serializer = registrationSerializer(register)
            return Response(serializer.data)

        register       = registration.objects.all()
        serializer     = registrationSerializer(register,many=True)
        return Response(serializer.data)

    def post(self,req):
        def get_tokens_for_login(user):
            refresh = RefreshToken.for_user(user)
            
            return {
            'status':"success",
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            }
        Login={'username':req.data['mobile'],'password':req.data['mobile'],'deviceId':req.data['deviceId'],'role':2}
        serializer = registrationSerializer(data=req.data)
        logserial=loginSerializer(data=Login)
        if serializer.is_valid():
            serializer.save()

            if logserial.is_valid():
                logserial.save()
                user=User.objects.get_or_create(username="user")[0]
                token=get_tokens_for_login(user)
                token['data'] = serializer.data
            return Response(token)
        else:
            return Response({"status":"fail","error":serializer.errors})
    
    def delete(self,req,username):
        registration.objects.filter(username=username).delete()
        return Response({"msg":1})

    def put(self,req,username): 
        register   = registration.objects.filter(username=username).first()
        
        serializer = registrationSerializer(register,data=req.data,partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



from rest_framework.decorators import permission_classes, authentication_classes
import jwt
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class examView(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self,request,id=None):
        if id is not None:
            exam1      = exam.objects.get(id=id)
            serializer = examSerializer(exam1)
            return Response(serializer.data) 
        exam1      = exam.objects.all()       
        serializer = examSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = examSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        exam.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        exam1      = exam.objects.filter(id=id).first()
        serializer = examSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  



class courseView(APIView):



    def get(self,request,id=None):
        if id is not None:
            exam1      = course.objects.get(id=id)
            serializer = courseSerializer(exam1)
            return Response(serializer.data) 
        exam1      = course.objects.all()       
        serializer = courseSerializer(exam1,many=True)
        return Response(serializer.data)

    # def get(self, request,id):

    #     mcq        = course.objects.filter(exam=id)
    #     serializer = courseSerializer(mcq, many=True)
    #     return Response(serializer.data)

    #parser_classes = (MultiPartParser, FormParser, )
    def post(self,req, *args, **kwarg):
        print(req.data)
        serializer = courseSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        course.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        courses = course.objects.filter(id=id).first()
        serializer = courseSerializer(courses,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  

#SERIALIZERS FOR SUBJECT OPERATION

class subjectView(APIView):


    def get(self,request,id=None):
        if id is not None:
            subjects = subject.objects.get(id=id)
            serializer = subjectSerializer(subjects)
            return Response(serializer.data) 
        subjects = subject.objects.all()       
        serializer = subjectSerializer(subjects,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = subjectSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        subject.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        subjects = subject.objects.filter(id=id).first()
        serializer = subjectSerializer(subjects,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


#SERIALIZERS FOR TOPIC OPERATION

# get particular topic assosiated with particular subjects
class ParticularTopic(APIView):
    def get(self, request,id):
        topics = topic.objects.filter(subject = id)
        serializer = topicSerializer(topics, many=True)
        return Response(serializer.data)

class topicView(APIView):

    def get(self,request,id=None):
        if id is not None:
            topics     = topic.objects.get(id=id)
            serializer = topicSerializer(topics)
            return Response(serializer.data) 
        topics     = topic.objects.all()       
        serializer = topicSerializer(topics,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = topicSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        topic.objects.get(id=id).delete()
        return Response({"msg":1})   


    def put(self,req,id):
        topics = topic.objects.filter(id=id).first()
        serializer = topicSerializer(topics,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#subtopic

class subtopicView(APIView):

    def get(self,request,id=None):
        if id is not None:
            subtopics     = Subtopics.objects.get(id=id)
            serializer = subtopicSerializer(subtopics)
            return Response(serializer.data) 
        subtopics     = Subtopics.objects.all()       
        serializer = subtopicSerializer(subtopics,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = subtopicSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        Subtopics.objects.get(id=id).delete()
        return Response({"msg":1})   


    def put(self,req,id):
        subtopics = Subtopics.objects.filter(id=id).first()
        serializer = subtopicSerializer(subtopics,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#SERIALIZER FOR QUESTION BANK

class question_bankView(APIView):

    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank.objects.get(id=id)
            serializer     = question_bankSerializer(question1)
            return Response(serializer.data) 
        question1      = question_bank.objects.all()       
        serializer     = question_bankSerializer(question1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = question_bankSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        question_bank.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        question1      = question_bank.objects.filter(id=id).first()
        serializer     = question_bankSerializer(question1,data=req.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


class questionView(APIView):  #TO GET QUESTION BY CERTAIN TOPIC ID

    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank.objects.filter(topic=id)
            serializer     = question_bankSerializer(question1,many=True)
            return Response(serializer.data) 


#FOR EXAM MASTER

class exammasterView(APIView):

    def get(self,request,id=None):
        if id is not None:
            master1      = exam_master.objects.get(id=id)
            serializer     = exam_masterSerializer(master1)
            return Response(serializer.data) 
        master1        = exam_master.objects.all()       
        serializer     = exam_masterSerializer(master1,many=True)
        return Response(serializer.data)

    def post(self,req):
        serializer  = exam_masterSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  

    def put(self,request,id):
        exammaster1 =  exam_master.objects.get(id=id)
        serializer  =  exam_master(exammaster1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self,request,id):
        exam_master.objects.get(id=id).delete()
        return Response("successfully deleted")


# API to list the available tests...

class masterView(APIView):

    def get(self, request,id):

        mcq        = exam_master.objects.filter(course=id)
        serializer = exam_masterSerializer(mcq, many=True)
        return Response(serializer.data)

    # def post(self,request):
    #     sub_id=request.data['subject']
    #     tpc_id=request.data['topic']
    #     date  =request.data['date']

    #     print(request)
    #     master1      = exam_master.objects.filter(exam_criteria__subject=sub_id,exam_criteria__topic=tpc_id , exam_start_date__lte=date, exam_end_date__gte=date)
    #     serializer   = exam_masterSerializer(master1,many=True)
    #     return Response(serializer.data)  


class Courseview(APIView):

    def post(self,request):
        exm=request.data['exam']
        course1=course.objects.filter(exam=exm)
        serializer=courseSerializer(course1,many=True)
        return Response(serializer.data)



class isdemanded(APIView):

    def get(self, request):

        mcq        = course.objects.filter(isdemanded=1)
        serializer = courseSerializer(mcq, many=True)
        return Response(serializer.data)



class examQuestionAllocationView(APIView):

    def get(self,request,id=None):
        if id is not None:
            exam1      = exam_question_allocation.objects.get(id=id)
            serializer = examQuestionallocationSerializer(exam1)
            return Response(serializer.data) 
        exam1      = exam_question_allocation.objects.all()       
        serializer = examQuestionallocationSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = examQuestionallocationSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        exam_question_allocation.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        exam1      = exam_question_allocation.objects.filter(id=id).first()
        serializer = examQuestionallocationSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 


class questionbankoptionsview(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank_options.objects.get(id=id)
            serializer     = question_bank_optionsSerializer(question1)
            return Response(serializer.data) 
        question1      = question_bank_options.objects.all()       
        serializer     = question_bank_optionsSerializer(question1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = question_bank_optionsSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        question_bank_options.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        question1      = question_bank_options.objects.filter(id=id).first()
        serializer     = question_bank_optionsSerializer(question1,data=req.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class mcqView(APIView):

    def get(self,request,id=None):
        if id is not None:
            mcq        = question_bank.objects.get(id=id)
            serializer = qustnSerializer(mcq)
            return Response(serializer.data) 
        mcq        = question_bank.objects.all()       
        serializer = qustnSerializer(mcq,many=True)
        return Response(serializer.data)

class Particularmcq(APIView):

    def get(self, request,id):
        mcq        = exam_question_allocation.objects.filter(id=id)
        serializer = examQuestionallocationSerializer(mcq, many=True)
        return Response(serializer.data)

class GetQuestions(APIView):
    def get(self, request,id):
        
        exam_questions = []
        
        for exam_question in exam_question_allocation.objects.filter(exam_master=id):
            serializer = examQuestionallocationSerializer(exam_question)
            print(serializer.data.get('question', None))
            questions = question_bank.objects.filter(id=serializer.data.get('question', None))
            serializer = questionSerializer(questions, many=True)
            exam_questions.append(serializer.data[0])
        return Response(exam_questions)


# # @login_required(login_url='login')
# def home_page(request):
#     total_course   = course.objects.count()
#     total_subject  = subject.objects.count()
#     total_exam     = exam.objects.count()
#     total_question = question_bank.objects.count()
#     context={
#         'course'  :total_course,
#         'subject' :total_subject,
#         'exam'    :total_exam,
#         'question':total_question
#     }
#     return render(request, 'home.html',context)

# def add_designation(request):
#     forms = AddDesignationForm()
#     if request.method == 'POST':
#         forms = AddDesignationForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('designation')
#     designation = Designation.objects.all()
#     context = {'forms': forms, 'designation': designation}
#     return render(request, 'administration/designation.html', context)




###############################################
#     forms = Addexam()
#     if request.method == 'POST':
#         forms = Addexam(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('add-exam')
#     exam1 = exam.objects.all()
#     context = {'form': forms, 'exam': exam1}
#     return render(request, 'exam/exam.html', context)



#video class api

class VideoClassView(APIView):

    def post(self,request):
        crs=request.data['course']
        video1=video_class.objects.filter(course=crs)
        serializer=VideoclassSerializer(video1,many=True)
        return Response(serializer.data)

    # def get(self,request,id=None):
    #     if id is not None:
    #         subjects = video_class.objects.get(id=id)
    #         serializer = VideoclassSerializer(subjects)
    #         return Response(serializer.data) 
    #     subjects = video_class.objects.all()       
    #     serializer = VideoclassSerializer(subjects,many=True)
    #     return Response(serializer.data)


    # def post(self,req):
    #     serializer = VideoclassSerializer(data=req.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)  


    def delete(self,req,id):
        video_class.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        subjects = video_class.objects.filter(id=id).first()
        serializer = VideoclassSerializer(subjects,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#comment clear api

class commentget(APIView):
    def post(self,request):
        crs=request.data['video']
        video1=videocomment.objects.filter(video=crs)
        noc=videocomment.objects.filter(video=crs).count()
        serializer=CommentSerializer2(video1,many=True)
        return Response(serializer.data)




class commentview(APIView):
    def get(self,request,id=None):
        if id is not None:
            subjects = videocomment.objects.get(id=id)
            serializer = CommentSerializer2(subjects)
            return Response(serializer.data) 
        subjects = videocomment.objects.all()       
        serializer = CommentSerializer2(subjects,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = CommentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        videocomment.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        subjects = videocomment.objects.filter(id=id).first()
        serializer = CommentSerializer(subjects,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

from django.shortcuts import render
from rest_framework import viewsets



class Examview(viewsets.ModelViewSet):
    serializer_class = examSerializer
    queryset = exam.objects.all()



#course subject allocation api

class courseSubjectAllocationView(APIView):

    def get(self,request,id=None):

        if id is not None:
            exam1      = course_subject_allocation.objects.get(id=id)
            serializer = courseSubjectallocationSerializer(exam1)
            return Response(serializer.data) 
        exam1      = course_subject_allocation.objects.all()       
        serializer = courseSubjectallocationSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):

        serializer = courseSubjectallocationSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):

        course_subject_allocation.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):

        exam1      = course_subject_allocation.objects.filter(id=id).first()
        serializer = courseSubjectallocationSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



    #TOPIC COURSE ALLOCATION

class topicCourseAllocationView(APIView):

    def get(self,request,id=None):
        if id is not None:
            exam1      = topic_course_allocation.objects.get(id=id)
            serializer = topicCourseAllocationSerializer(exam1)
            return Response(serializer.data) 
        exam1      = topic_course_allocation.objects.all()       
        serializer = topicCourseAllocationSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = topicCourseAllocationSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        topic_course_allocation.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        exam1      = topic_course_allocation.objects.filter(id=id).first()
        serializer = topicCourseAllocationSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)





class bannerView(APIView):

    def get(self,request,id=None):

        if id is not None:
            banners = banner.objects.get(id=id)
            serializer = BannerSerializer(banners)
            return Response(serializer.data) 
        banners = banner.objects.all()       
        serializer = BannerSerializer(banners,many=True)
        return Response(serializer.data)

    #parser_classes = (MultiPartParser, FormParser, )
    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = BannerSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):

        banner.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):

        courses = banner.objects.filter(id=id).first()
        serializer = BannerSerializer(courses,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)





class GetResultView(APIView):

   


    def post(self,req):
        
        serializer = ExamrsltSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404)
    


    def delete(self,req,id):

        examresult.objects.get(id=id).delete()
        return Response({"msg":1}) 


   





class SyllabusView(APIView):

    def get(self,request,id=None):

        if id is not None:
            subjects = syllabus.objects.get(id=id)
            serializer = SyllabusSerializer(subjects)
            return Response(serializer.data) 
        subjects = syllabus.objects.all()       
        serializer = SyllabusSerializer(subjects,many=True)
        return Response(serializer.data)


    def post(self,request):
        crs=request.data['course']
        video1=syllabus.objects.filter(course=crs)
        serializer=SyllabusSerializer(video1,many=True)
        return Response(serializer.data)  


    def delete(self,req,id):

        syllabus.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        
        subjects = syllabus.objects.filter(id=id).first()
        serializer = SyllabusSerializer(subjects,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class notesView(APIView):

    def get(self,request,id=None):

        if id is not None:
            subjects = notes.objects.get(id=id)
            serializer = NotesSerializer(subjects)
            return Response(serializer.data) 
        subjects = notes.objects.all()       
        serializer = NotesSerializer(subjects,many=True)
        return Response(serializer.data)
    

    def post(self,request):

        crs=request.data['video']
        master1      = notes.objects.filter(video=crs)
        serializer   = NotesSerializer(master1,many=True)
        return Response(serializer.data)

    def delete(self,req,id):

        notes.objects.get(id=id).delete()
        return Response({"msg":1})


      
class testimonialView(APIView):

    def get(self, request):
        
        data = testimonial.objects.all()
        serializer = testimonialSerializer(data, many=True)
        return Response(serializer.data)
    

class enquiryView(APIView):

    def get(self, request):
        
        data = enquiry.objects.all()
        serializer = enquirySerializer(data, many=True)
        return Response(serializer.data)
    

    def post(self,req):
        
        serializer = enquirySerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404)





class perfomanceview(APIView):

    def get(self, request,id):
        perfom=[]
        data = examresult.objects.filter(user=id)
        noexm=examresult.objects.filter(user=id).count()
        serializer1 = pExmresultSerializer(data, many=True)
        for i in range(0,noexm):
            tc=serializer1.data[i]['total_correct']
            tq=serializer1.data[i]['no_of_questions']
            exm=serializer1.data[i]['exam']
            print(exm)
            perfo=(tc/tq)*100
            serializer = ExmresultSerializer(data, many=True,context={'perfomance': perfo,'exams':noexm,'no_of_questions':tq,'total_correct':tc,'exam':exm})   
            perfom.append(serializer.data[0])
        
        
        return Response(perfom)
        


# class subperfomanceview(APIView):

#     def get(self, request,id):
#         exam_questions = []

#         for exam_question in examresult.objects.filter(user=id):
#             serializer = ExamrsltSerializer(exam_question)
#             print(serializer.data.get('course', None))
#             questions = course_subject_allocation.objects.filter(course=serializer.data.get('course', None))
#             serializer1 = pcourseSubjectallocationSerializer(questions, many=True)
#             exam_questions.append(serializer1.data[0])
            


#         mcq        = examresult.objects.filter(user=id)
#         serializer = rsltserializer(mcq, many=True)
        
        
#         serializer = rsltserializer(mcq, many=True,context={'my_subjects': exam_questions})
#         return Response (serializer.data)
from django.db.models import Count
import random
from django.db.models import F

class subperfomanceview(APIView):

    def get(self, request,id):
        exam_questions = []

        for exam_question in examresult.objects.filter(user=id):
            serializer = ExamrsltSerializer(exam_question)
            print(serializer.data.get('course', None))
            crs = course_subject_allocation.objects.filter(course=serializer.data.get('course', None))
            serializer1 = pcourseSubjectallocationSerializer(crs, many=True)
            exam_questions.append(serializer1.data[0])
            ep=result_details.objects.filter(examresult=serializer.data.get('id',None))
            serializer2= rsltdtl1(ep, many=True)
            for item in serializer2.data:
                print("#################")
                print(item.get('question', None))
            for qs in question_bank.objects.filter(id=item.get('question',None)):
                serializer4=question_bankSerializer1(qs)
                print("##################")
                sub= serializer4.data.get('subject',None)  
                l1=[]
                l1.append(serializer4.data)
                print(sub) 
                for ite in serializer1.data:
                    print("#################")
                    print(ite.get('subject', None))
                    ls=[]
                    ls.append(ite)
                    if l1==ls:
                        
                        print("same")
                        
                    else:
                        print("not same")
                        
                        
                        
                
                   
                



            mcq        = examresult.objects.filter(user=id)
            # serializer = rsltserializer(mcq,many=True)
            
            
            serializer3 = rsltserializer(mcq, many=True,context={'my_subjects': exam_questions})
            return Response(serializer3.data)
        
            


    #     # exam_questions = result_details.objects.filter(examresult=id)
    #     # serializer = rsltdtl(exam_questions, many=True)
    #     # return Response (serializer.data)


    # def post(self, request):
        
    #     crs=request.data['user']
    # # Step 1: Retrieve all the exams attempted by the user.
    #     exams_attempted = examresult.objects.filter(user=crs).select_related('exam_master__course', 'exam_master').prefetch_related('attent__question')

    #     # Step 2: For each exam, calculate the percentage of correct answers.
    #     exam_percentage = {}
    #     for exam in exams_attempted:
    #         total_questions = exam.no_of_questions
    #         correct_answers = result_details.objects.filter(examresult_id=exam.id, correct_answer=F('user_answer')).count()
    #         percentage = round(correct_answers / total_questions * 100, 2)
    #         exam_percentage[exam.exam_master.course.course_name + " " + exam.exam_master.name] = percentage

    #     # Step 3: For each subject in the course, calculate the percentage of correct answers.
    #     courses = {}
    #     for exam in exams_attempted:
    #         course_name = exam.exam_master.course.course_name
    #         exam_name = exam.exam_master.name

    #         if course_name not in courses:
    #             courses[course_name] = {
    #                 'Exam': exam_name,
    #                 'Subjects': {}
    #             }

    #         for subject in exam.exam_master.course.subjects.all():
    #             subject_id = subject.id
    #             subject_name = subject.subject

    #             if subject_id not in courses[course_name]['Subjects']:
    #                 courses[course_name]['Subjects'][subject_id] = {
    #                     'id': subject_id,
    #                     'Name': subject_name,
    #                     'Confidence level': 0,
    #                     'color': '#'+str(hex(random.randint(0, 0xFFFFFF)))[2:].zfill(6)
    #                 }

    #             total_questions = question_bank.objects.filter(subject=subject_id, status=True).count()
    #             correct_answers = result_details.objects.filter(examresult_id=exam.id, question__subject_id=subject_id, correct_answer=F('user_answer')).count()
    #             if total_questions == 0:
    #                 percentage = 0
    #             else:
    #                 percentage = round(correct_answers / total_questions * 100, 2)
    #                 courses[course_name]['Subjects'][subject_id]['Confidence level'] += percentage

    #                 for course in courses:
    #                     for subject in courses[course]['Subjects']:
    #                         courses[course]['Subjects'][subject]['Confidence level'] /= len(exams_attempted)

    #                 # Step 4: Return the result in the desired format.
    #                 result = []
    #                 for course in courses:
    #                     course_result = {
    #                         'course': course,
    #                         'Exam': courses[course]['Exam'],
    #                         'Subjects': list(courses[course]['Subjects'].values())
    #                     }
    #                     result.append(course_result)

    #                 return Response(result, safe=False)

            
class courseregpostView(APIView):

    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = courseregSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


class GetcrsregView(APIView):
    def post(self,request):
        crs=request.data['user']
        video1=course_registration.objects.filter(user=crs)
        serializer=courseregSerializer(video1,many=True)
        return Response(serializer.data)
    


class Checksub(APIView):
    def post(self,request):
        usr=request.data['user']
        crs=request.data['course']
        itemcount=course_registration.objects.filter(user=usr,course=crs).count()
        if itemcount>0:
            return Response({"msg":"True"})
        else:
            return Response({"msg":"False"})
        
        
        
        
        
        
        
