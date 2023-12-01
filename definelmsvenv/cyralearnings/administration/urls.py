from django.urls import path
from . import views
from lmsmainapp.views import*


urlpatterns = [

path('login/', views.admin_login, name='login'),
path('logout/', views.admin_logout, name='logout'),

path('home/', views.home_page,name="home"),

path('administartion/', views.home, name='administration'),
path('save/', views.save_data, name='save'),
path('delete/', views.delete_data, name='delete'),
path('edit/', views.edit_data, name='edit'),

##############exam#########################
path('exam/', views.home_exam, name='add-examex'),
path('saveex/', views.save_data_exam, name='saveex'),
path('deleteex/', views.delete_data_exam, name='deleteex'),
path('editex/', views.edit_data_exam, name='editex'),

##############course#########################
path('addcourse/', views.add_course, name='addcourse'),
path('editcourse/<id>', views.editcourse, name='editcourse'),
path('course/', views.add_course,name='cr'),
path('deletec/', views.delete_data_course, name='deletecr'),


##############subject#########################

path('subjects/', views.add_subject,name='sub'),
path('deletes/', views.delete_data_subject, name='deletesb'),
path('editc/<id>', views.editsubject, name='editsub'),



##############topic#########################
path('topic/', views.add_topic, name='topicc'),
path('deletet/', views.delete_data_topic, name='deletetp'),
path('editt/<id>', views.edittopic, name='edittp'),



##############subtopic#########################
path('topicsb/', views.add_subtopic, name='topicsub'),
path('deletesb/', views.delete_data_subtopic, name='deletesub'),
path('editt/<id>', views.editsubtopic, name='editstp'),



##############questionbank#########################
path('questionbankadd/', views.add_question, name='qbadd'),
path('questionbankdelete/', views.delete_data_question, name='deleteqb'),
path('editqs/<id>', views.editqs, name='editqs'),

##############exammaster########################
path('exammaster/', views.addexmaster, name='homeem'),
path('deleteem/', views.delete_data_exmaster, name='deleteem'),
path('editexmm/<id>', views.editem,name='editst'),

############options#################
path('op/', views.addoptions, name='op'),
path('deleteop/', views.delete_data_addoptions, name='deleteop'),
path('editop/<id>', views.editop,name='editop'),



############videoclass#################
path('video/', views.addvideo, name='vdo'),
path('deletevdo/', views.deletevideo, name='deletevdo'),
path('editvd/<id>', views.editvideo,name='editvd'),


######banner############################
path('addbanner/', views.addbanner,name="addbanner"),
path('deleteba/', views.delete_data_banner, name='deleteba'),


#############add course subject allocation################

path('addcsallo/', views.addcsallo,name="addcsallo"),
path('deletecs/', views.delete_data_csallo, name='deletecs'),
path('editcs/<id>', views.editcallo, name='editcs'),

################add course subject topic allocation############

path('addtcallo/', views.addtcallo,name="addtcallo"),
path('deletetc/', views.delete_data_tcallo, name='deletetc'),
path('edittc/<id>', views.edittcallo, name='edittc'),

#add Examamster question allocation

path('addeqallo/', views.addeqallo,name="addeqallo"),
path('deleteeq/', views.delete_data_eqallo, name='deleteeq'),
path('editeq/<id>', views.editqallo, name='editq'),

###########notes############

path('addnotes/', views.addnotes,name="addnote"),
path('deletenotes/', views.delete_data_notes, name='deleteno'),
path('editnotes/<id>', views.editnote, name='editnotes'),



#########add syllabus#################


path('addsyllabus/', views.addsyllabus,name="addsyllabus"),
path('deletesy/', views.delete_data_syllabus, name='deletesy'),
path('editsyl/<id>', views.editsyl, name='editsyl'),


####Enquiry

path('enquiry/', views.enquiry_,name='enquiry'),
path('deleteten/', views.delete_data_enquiry, name='deleteten'),




#add testimonial

path('addtestimonial/', views.addtestimonial,name="addtestimonial"),
path('deletetst/', views.delete_data_testimonial, name='deletetst'),
path('edittst/<id>', views.edittesti, name='edittesti'),



]