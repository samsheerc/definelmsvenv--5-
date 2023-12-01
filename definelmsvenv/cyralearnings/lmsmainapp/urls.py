from django.urls import path
from lmsmainapp import views as api_views
from rest_framework.authtoken import views
from lmsmainapp import views

from rest_framework.routers import DefaultRouter




urlpatterns = [
    
    path('checkuser/', api_views.Loginview.as_view(), name="loginapi"),
    # path('checkuser/', api_views.CheckuserView.as_view(), name="checkuser"),
    

    path('loginapi/', api_views.loginView.as_view(), name="login1"),
    path('loginapi/<id>', api_views.loginView.as_view(), name="login_put_dlt"),

    path('registration/', api_views.registrationView.as_view(), name="registration"),
    path('registration/<username>', api_views.registrationView.as_view(), name="registration_put_dlt"),

    path('exam/', api_views.examView.as_view(), name="exam"),
    path('exam/<id>', api_views.examView.as_view(), name="exam_put_dlt"),

    path('courseall/', api_views.courseView.as_view(), name="course"),
    path('course/<id>', api_views.courseView.as_view(), name="course_put_dlt"),
    path('course/', api_views.Courseview.as_view(), name="course"),
    path('demandedcourse/', api_views.isdemanded.as_view(), name="demandedcourse"),
    
 
    path('subject/', api_views.subjectView.as_view(), name="subject"),
    path('subject/<id>', api_views.subjectView.as_view(), name="subject_put_dlt"),
   

    path('topic/', api_views.topicView.as_view(), name="topic"),
    path('topic/<id>', api_views.topicView.as_view(), name="topic_put_dlt"),
    path('topicfilter/<id>', api_views.ParticularTopic.as_view(), name="particular_topic"),

    path('subtopic/', api_views.subtopicView.as_view(), name="subtopic"),
    path('subtopic/<id>', api_views.subtopicView.as_view(), name="subtopic_put_dlt"),
    
    path('exammaster/', api_views.exammasterView.as_view(), name="exam_master"),
    path('exammaster/<id>', api_views.exammasterView.as_view(), name="exam_master_put_dlt"),
    path('masterview/<id>', api_views.masterView.as_view(), name="master_view"),
    path('masterview/', api_views.masterView.as_view(), name="master_view"),

    path('eqallocation/', api_views.examQuestionAllocationView.as_view(), name="exam_question_allocation"),
    path('eqallocation/<id>', api_views.examQuestionAllocationView.as_view(), name="exam_question_allocation_put_dlt"),

    path('questionbank/', api_views.question_bankView.as_view(), name="question_bank"),
    path('questionbank/<id>', api_views.question_bankView.as_view(), name="question_bank_put_dlt"),
    path('questionview/', api_views.questionView.as_view(), name="question_bank"),

    path('questionoption/', api_views.questionbankoptionsview.as_view(), name="question"),
    path('questionoption/<id>', api_views.questionbankoptionsview.as_view(), name="exam_put_dlt"),
    
    
    path('mcq/', api_views.mcqView.as_view(), name="mcq"),
    path('mcq/<id>', api_views.GetQuestions.as_view(), name="mcq"),


    path('videoapi/', api_views.VideoClassView.as_view(), name="vdoapi"),
    path('videoapi/<id>', api_views.VideoClassView.as_view(), name="vdoapi"),


    path('commentpost/', api_views.commentview.as_view(), name="commentclear"),
    path('commentget/', api_views.commentget.as_view(), name="comment"),
    path('comment/<id>', api_views.commentview.as_view(), name="commentedit"),


    path('csallocation/', api_views.courseSubjectAllocationView.as_view(), name="course_subject_allocation"),
    path('csallocation/<id>', api_views.courseSubjectAllocationView.as_view(), name="course_subject_put_dlt"),
    
  
    path('tcallocation/', api_views.topicCourseAllocationView.as_view(), name="topic_question_allocation"),
    path('tcallocation/<id>', api_views.topicCourseAllocationView.as_view(), name="topic_question_allocation_put_delete"),


    path('banner/', api_views.bannerView.as_view(), name="banner"),
    path('banner/<id>', api_views.bannerView.as_view(), name="banner_put_dlt"),

    path('examresult/', api_views.GetResultView.as_view(), name="result"),
    path('examresult/<id>', api_views.GetResultView.as_view(), name="result_dlt"),

    path('syllabus/', api_views.SyllabusView.as_view(), name="syllabus"),
    path('syllabus/<id>', api_views.SyllabusView.as_view(), name="syllabus_put_dlt"),



    path('notes/', api_views.notesView.as_view(), name="notes"),
    path('notes/<id>', api_views.notesView.as_view(), name="notes_put_dlt"),




    path('perfomance/<id>', api_views.perfomanceview.as_view(), name="perfomance"),


    path('subperfomance/<id>', api_views.subperfomanceview.as_view(), name="subperfomance"),



    path('testimonial/', api_views.testimonialView.as_view(), name="testimonial"),
    path('enquiry/', api_views.enquiryView.as_view(), name="enquiry"),


    path('getcoursereg/', api_views.GetcrsregView.as_view(), name="course_reg"),
    path('coursereg/', api_views.courseregpostView.as_view(), name="courseregpostView"),
    
    path('Checksub/', api_views.Checksub.as_view(), name="Checksub"),
    
]