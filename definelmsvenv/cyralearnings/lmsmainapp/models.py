from email.policy import default
from logging.config import IDENTIFIER
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields import CharField, TextField

class login(models.Model):
    id       = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role     = models.IntegerField(null=True)
    deviceId = models.CharField( max_length=100,null=True,default="")

    class Meta:
        db_table = 'login'

    def __str__(self):
        return self.username

class registration(models.Model):
    
    name       = models.CharField(max_length=50,default="",null=True)
    address    = models.CharField(max_length=500,default="",null=True)
    mobile     = models.CharField(max_length=10,default="",null=True)
    email      = models.EmailField(max_length=254,default="",null=True)
    username   = models.CharField(max_length=50,primary_key=True)
    image      = models.ImageField(upload_to='register',null=True,default="")

    class Meta:
        db_table='registration'

    def __str__(self):
        return self.name

class exam(models.Model):
    id          = models.AutoField(primary_key=True)
    exam_name   = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    remarks     = models.CharField(max_length=500)

    class Meta:
        db_table = 'exam'

    def __str__(self):
        return self.exam_name

class course(models.Model):
    id          = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=20,default="")
    description = models.CharField(max_length=1000,default="")
    amount      = models.IntegerField(default=0)
    duration    = models.CharField(max_length=10,default="")
    exam        = models.ForeignKey(exam,on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='course')
    isdemanded  =models.BooleanField(default=False,blank=True)
    user        = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='course'

    def __str__(self):
        return self.course_name

class subject(models.Model):
    id           = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50,default="")
    description  = models.CharField(max_length=2000,default="")
    image        = models.ImageField(max_length=150,default="")
    user         = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='subject'

    def __str__(self):
        return self.subject_name
    

class course_subject_allocation(models.Model):
    id        = models.AutoField(primary_key=True)
    course    = models.ForeignKey(course,on_delete=models.CASCADE,related_name='subjects')
    subject   = models.ForeignKey(subject,on_delete=models.CASCADE)

    class Meta:
        db_table='course_subject_allocation'



class topic(models.Model):
    id           = models.AutoField(primary_key=True)
    topic_name   = models.CharField(max_length=100,default="")
    description  = models.CharField(max_length=2000,default="")
    subject      = models.ForeignKey(subject,on_delete=models.CASCADE)
    user         = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='topic'

    def __str__(self):
        return self.topic_name

class topic_course_allocation(models.Model):
    id          = models.AutoField(primary_key=True)
    course      = models.ForeignKey(course,on_delete=models.CASCADE)
    subject     = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic       = models.ForeignKey(topic,on_delete=models.CASCADE)
    class Meta:
        db_table='topic_course_allocation'


# subtopic details
class Subtopics(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    topic       = models.ForeignKey(topic, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'Subtopics'

    def __str__(self):
        return self.name


# class course_info(models.Model):
#     id          = models.AutoField(primary_key=True)
#     course      = models.CharField(max_length=100)
#     subject     = models.CharField(max_length=100)
#     topic       = models.CharField(max_length=100)
#     course_type = models.BooleanField(default=True)
#     description = models.CharField(max_length=2000,default="")
#     image       = models.ImageField(upload_to='course_info',null=True)
#     user        = models.ForeignKey(login,on_delete=models.CASCADE)

#     class Meta:
#         db_table='course_info'


class course_registration(models.Model):
    id            = models.AutoField(primary_key=True)
    course        = models.ForeignKey(course,on_delete=models.CASCADE)
    register      = models.ForeignKey(registration,on_delete=models.CASCADE)
    date          = models.DateField(auto_now_add=True)
    membership    = models.BooleanField(default=True)
    paid_reg_date = models.DateField(auto_now_add=True) 
    end_reg_date  = models.DateField()
    user          = models.ForeignKey(login,on_delete=models.CASCADE)
    is_paid       = models.BooleanField(default=False)

    class Meta:
        db_table='course_registration'



class notification(models.Model):
    id          = models.AutoField(primary_key=True)
    course      = models.ForeignKey(course,on_delete=models.CASCADE)
    message     = models.CharField(max_length=1000,default="")
    expiry_date = models.DateField()
    date        = models.DateField(auto_now_add=True)
    remarks     = models.CharField(max_length=50,default="")

    class Meta:
        db_table='notification'


class payment(models.Model):
    id              = models.AutoField(primary_key=True)
    invoice         = models.IntegerField()
    course          = models.CharField(max_length=50)
    date            = models.DateField()
    registration    = models.ForeignKey(registration,on_delete=models.CASCADE)
    amount          = models.IntegerField(default=0)
    tax             = models.IntegerField()
    payment_details = models.CharField(max_length=500)
    user            = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='payment'


class question_bank(models.Model):
    id              = models.AutoField(primary_key=True)
    question        = models.CharField(max_length=5000,default="",null=False)
    subject         = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic           = models.ForeignKey(topic,on_delete=models.CASCADE)
    subtopic        = models.ForeignKey(Subtopics, on_delete=models.CASCADE)
    no_of_options   = models.IntegerField(default=0,null=False)
    tags            = models.CharField(max_length=1000)
    is_explanation  = models.BooleanField(default=False)
    is_image        = models.BooleanField(default=False)
    explanation     = models.CharField(max_length=1000,default="")
    difficulty_level= models.CharField(max_length=50,default="")
    created_date    = models.DateField(auto_now_add=True)
    last_updated_date= models.DateField(auto_now=True)
    user            = models.ForeignKey(login,on_delete=models.CASCADE)
    status          = models.BooleanField(default=False)
    remark          = models.CharField(max_length=50,blank=True)
    is_reported     = models.BooleanField(default=False)
    report_reason   = models.CharField(max_length=1000,default="")
    correct_answer  = models.CharField(max_length=1,null=False)
    

    class Meta:
        db_table='question_bank'

    def __str__(self):
        return self.question

class question_bank_options(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,related_name='options',on_delete=models.CASCADE)
    choice           = models.CharField(max_length=1500,null=False)
    identifier       = models.CharField(max_length=1,null=False)

    class Meta:
        db_table='question_bank_options'


class exam_master(models.Model):
    id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length=250,default="")
    exam             = models.ForeignKey(exam,on_delete=models.CASCADE)
    course           = models.ForeignKey(course,on_delete=models.CASCADE)
    no_of_questions  = models.IntegerField(default=0)
    total_time       = models.IntegerField(default=0)
    no_of_attempt    = models.IntegerField(default=0)
    datetime         = models.DateTimeField(auto_now_add=True)
    exam_start_date  = models.DateField()
    exam_end_date    = models.DateField()
    image            = models.ImageField(upload_to='exammaster',default="")
    exam_description = models.CharField(max_length=500,default="")
    correct_mark     = models.FloatField(default=0)
    incorrect_mark   = models.FloatField(default=0)
    is_draft         = models.BooleanField(default=False)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table = 'exam_master'

    def __str__(self):
        return self.name

class exam_question_allocation(models.Model):
    id               = models.AutoField(primary_key=True)
    exam_master      = models.ForeignKey(exam_master,on_delete=models.CASCADE)
    question         = models.ForeignKey(question_bank,related_name='qid',on_delete=models.CASCADE)

    class Meta:
        db_table = 'exam_question_allocation'

class contribution(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,on_delete=models.CASCADE)
    subject          = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic            = models.ForeignKey(topic,on_delete=models.CASCADE)
    explanation      = models.CharField(max_length=500,default="",null=False)
    is_approved      = models.BooleanField(default=False,null=False)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='contribution'


class question_reporting(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,on_delete=models.CASCADE)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)
    reported_date    = models.DateField(auto_now_add=True)
    reporting_reason = models.CharField(max_length=500,default="")
    remarks          = models.CharField(max_length=250,default="")
    is_solved        = models.BooleanField(default=True)

    class Meta:
        db_table = 'question_reporting'



class video_class(models.Model):
    id               = models.AutoField(primary_key=True)
    course           = models.ForeignKey(course,on_delete=models.CASCADE)
    class_name       = models.CharField(max_length=250,default="")
    image            = models.ImageField(upload_to='videoclass')
    duration         = models.CharField(max_length=10,default="")
    price            = models.IntegerField(default=0)
    is_paid          = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    videolink        = models.CharField(max_length=500,default="")
    user             = models.ForeignKey(login,on_delete=models.CASCADE)
    class Meta:
        db_table='video_class'

    def __str__(self):
        return self.class_name



class videocomment(models.Model):
    id               = models.AutoField(primary_key=True)
    video            = models.ForeignKey(video_class,on_delete=models.CASCADE)
    user             = models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    datetime         = models.DateTimeField(auto_now_add=True)
    comment          = models.CharField(max_length=5000,default="")
    class Meta:
        db_table='videocomment'


class banner(models.Model):
    id               = models.AutoField(primary_key=True)
    banner           = models.ImageField(upload_to='banner')
    class Meta:
        db_table='banner'



class examresult(models.Model):
    id               = models.AutoField(primary_key=True)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)
    exam             = models.ForeignKey(exam,on_delete=models.CASCADE,default=54)
    course           = models.ForeignKey(course,on_delete=models.CASCADE,default=59)
    exam_master      = models.ForeignKey(exam_master,on_delete=models.CASCADE)
    datetime         = models.DateTimeField(auto_now_add=True)
    no_of_questions  = models.IntegerField(default=0)
    total_correct    = models.IntegerField(default=0)
    total_wrong      = models.IntegerField(default=0)
    total_skipped    = models.IntegerField(default=0)
    flagged_correct  = models.IntegerField(default=0)
    flagged_attempt  = models.IntegerField(default=0)
    switched_wrong_correct    = models.IntegerField(default=0)
    switched_correct_wrong    = models.IntegerField(default=0)
    final_score    = models.FloatField(default=0)
   

   


    class Meta:
        db_table='examresult'


class result_details(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,on_delete=models.CASCADE)
    examresult       = models.ForeignKey(examresult,related_name="attent",on_delete=models.CASCADE)
    attempted_time   = models.TimeField()
    is_flagged       = models.BooleanField(default=False)
    user_answer      = models.CharField(max_length=1,null=False)
    correct_answer   = models.CharField(max_length=1,null=True)
    switched_wrong_correct    = models.IntegerField(default=0)
    switched_correct_wrong    = models.IntegerField(default=0)
    options_switched = models.IntegerField(default=0)

    class Meta:
        db_table='result_details'



class notes(models.Model):
    id          = models.AutoField(primary_key=True)
    notename    = models.CharField(max_length=100,default="")
    pdf_file    = models.FileField(upload_to='pdf',default="")
    subject     = models.ForeignKey(subject,on_delete=models.CASCADE)
    video       = models.ForeignKey(video_class,on_delete=models.CASCADE)
    isactive    = models.BooleanField(default=False)
    user        = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='notes'

    

class syllabus(models.Model):
    id               = models.AutoField(primary_key=True)
    course           = models.ForeignKey(course,on_delete=models.CASCADE)
    syllabus         = models.TextField()
    isactive         = models.BooleanField(default=False)
    user        = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='syllabus'





class testimonial(models.Model):
    id               = models.AutoField(primary_key=True)
    datetime         = models.DateTimeField(auto_now_add=True)
    name             = models.CharField(max_length=100)
    profession       = models.CharField(max_length=100)
    photo            = models.ImageField(upload_to='testimonial')
    description      = models.CharField(max_length=2000)
    
    class Meta:
        db_table='testimonial'

class enquiry(models.Model):
    id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length=100)
    email            = models.EmailField(max_length=300)
    phone            = models.CharField(max_length=10)
    message          = models.CharField(max_length=2000)

    class Meta:
        db_table='enquiry'