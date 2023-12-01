from django import forms

from .models import *






class examForm(forms.ModelForm):

    class Meta:
        model = exam
        fields = ('exam_name','description','remarks')
        widgets = {
            'exam_name':forms.TextInput(attrs={'class':'form-control', 'id':'examnameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'remarks':forms.TextInput(attrs={'class':'form-control', 'id':'remarksid'}),
        }

class courseform1(forms.ModelForm):
    
    class Meta:
        model = course
        fields = ('course_name','description','amount','duration','exam','isdemanded','image')
        widgets = {
            'course_name':forms.TextInput(attrs={'class':'form-control', 'id':'course_nameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'amount':forms.NumberInput(attrs={'class':'form-control', 'id':'amountid'}),
            'duration':forms.TextInput(attrs={'class':'form-control', 'id':'durationid'}),
            'exam':forms.Select(attrs={'class':'form-control', 'id':'examid'}),
            'isdemanded':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'isdemandedid'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
          
        }
        

class subjectform(forms.ModelForm):

    class Meta:
        model = subject
        fields = ('subject_name','description','image')
        widgets = {
            'subject_name':forms.TextInput(attrs={'class':'form-control', 'id':'subject_nameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
          
        }



class topicform(forms.ModelForm):

    class Meta:
        model = topic
        fields = ('topic_name','description','subject')
        widgets = {
            'topic_name':forms.TextInput(attrs={'class':'form-control', 'id':'topic_nameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'subject':forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            
        }

class subtopicform(forms.ModelForm):

    class Meta:
        model = Subtopics
        fields = ('name','description','topic')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'topic':forms.Select(attrs={'class':'form-control', 'id':'topicid'})
        }



class question_bankform(forms.ModelForm):

    class Meta:
        model = question_bank
        fields = ('question','subject','topic','subtopic','no_of_options','tags','is_explanation','is_image','explanation','difficulty_level','status','remark','is_reported','correct_answer','report_reason')
        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control', 'id':'questionid'}),
            'subject':forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            'topic':forms.Select(attrs={'class':'form-control', 'id':'topicid'}),
            'subtopic':forms.Select(attrs={'class':'form-control', 'id':'subtopicid'}),
            'no_of_options':forms.NumberInput(attrs={'class':'form-control', 'id':'no_of_optionsid'}),
            'tags':forms.TextInput(attrs={'class':'form-control', 'id':'tagsid'}),
            'is_explanation':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_explanationid'}),
            'is_image':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_imageid'}),
            'explanation':forms.TextInput(attrs={'class':'form-control', 'id':'explanationid'}),
            'difficulty_level':forms.TextInput(attrs={'class':'form-control', 'id':'difficulty_levelid'}),
            'status':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'statusid'}),
            'remark':forms.TextInput(attrs={'class':'form-control', 'id':'remarkid'}),
            'is_reported':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_reportedid'}),
            'report_reason':forms.TextInput(attrs={'class':'form-control', 'id':'report_reasonid'}),
            'correct_answer':forms.TextInput(attrs={'class':'form-control', 'id':'correct_answerid'}),
           
            
        }


class exammasterForm(forms.ModelForm):
    class Meta:
        model = exam_master
        fields =('name','exam','course','no_of_questions','total_time','no_of_attempt','exam_start_date','exam_end_date','exam_description','is_draft','image')
        widgets = {
            'name'       : forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'exam'       : forms.Select(attrs={'class':'form-control', 'id':'examid'}),
            'course'     : forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
            'no_of_questions': forms.NumberInput(attrs={'class':'form-control', 'id':'noqid'}),
            'total_time' : forms.TextInput(attrs={'class':'form-control', 'id':'ttimeid'}),
            'no_of_attempt': forms.NumberInput(attrs={'class':'form-control', 'id':'attemptid'}),
            'exam_start_date': forms.SelectDateWidget(attrs={'class':'form-control', 'id':'sdateid'}),
            'exam_end_date': forms.SelectDateWidget(attrs={'class':'form-control', 'id':'edateid'}),
            'exam_description': forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'is_draft'   : forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'userid'}),
            'image'      : forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
        }


class optionsForm(forms.ModelForm):
    class Meta:
        model = question_bank_options
        fields = ('question','choice','identifier',)
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control', 'id':'examnameid'}),
            'choice': forms.TextInput(attrs={'class': 'form-control','id':'descriptionid'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control', 'id':'remarksid'}),
        }



class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password')
        widgets = {
             'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
             'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }


class videoform(forms.ModelForm):
    class Meta:
        model = video_class
        fields =('course','class_name','image','duration','price','is_paid','is_active','videolink')
        widgets = {
            'course'     : forms.Select(attrs={'class':'form-control','id':'courseid'}),
            'class_name': forms.TextInput(attrs={'class':'form-control','id':'class_nameid'}),
            'image' : forms.FileInput(attrs={'class':'form-control','id':'imageid'}),
            'duration': forms.TextInput(attrs={'class':'form-control','id':'durationid'}),
            'price': forms.NumberInput(attrs={'class':'form-control','id':'priceid'}),
            'is_paid': forms.NullBooleanSelect(attrs={'class':'form-control','id':'is_paidid'}),
            'is_active': forms.NullBooleanSelect(attrs={'class':'form-control','id':'is_activeid'}),
            'videolink'   : forms.TextInput(attrs={'class':'form-control','id':'videolinkid'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = videocomment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'id':'commentid','rows':'4'}),
           

        }



class bannerForm(forms.ModelForm):
    class Meta:
        model = banner
        fields = ('banner',)
        widgets = {
            
            'banner'      : forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
        }



class CourseSubjectAlloForm(forms.ModelForm):
    class Meta:
        model  = course_subject_allocation
        fields = '__all__'
        widgets = {
            'course'      :forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
            'subject'      :forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
        }


class topicCourseAlloForm(forms.ModelForm):
    class Meta:
        model  = topic_course_allocation
        fields = '__all__'
        widgets = {
            'course'      :forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
            'subject'      :forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            'topic'      :forms.Select(attrs={'class':'form-control', 'id':'topicid'}),
        }


class emQuestionAlloForm(forms.ModelForm):
    class Meta:
        model  = exam_question_allocation
        fields = '__all__'
        widgets = {
            'exam_master'      :forms.Select(attrs={'class':'form-control', 'id':'exammasterid'}),
            'question'      :forms.Select(attrs={'class':'form-control', 'id':'questionid'}),
        }







class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'name','placeholder': 'Enter Your Username','onclick':'resetBtn()'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id':'pass','placeholder': 'Enter Your Password','onclick':'resetBtn()','minlength':'8'}))
    class Meta:
        model = login
        fields = ('username','password')



    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label =""
        self.fields['password'].label=""
       



class notesform(forms.ModelForm):
    class Meta:
        model = notes
        fields = ('notename','pdf_file','subject','video','isactive')
        widgets = {
            'subject'     : forms.Select(attrs={'class':'form-control','id':'subjectid'}),
            'notename'    : forms.TextInput(attrs={'class':'form-control','id':'notenameid'}),
            'pdf_file'    : forms.FileInput(attrs={'class':'form-control','id':'pdfid'}),
            'video'       : forms.Select(attrs={'class':'form-control','id':'videoid'}),
            'isactive'    : forms.NullBooleanSelect(attrs={'class':'form-control','id':'is_activeid'}),
            }


class syllabusform(forms.ModelForm):
    class Meta:
        model = syllabus
        fields = ('course','syllabus','isactive')
        widgets = {
            'course'     : forms.Select(attrs={'class':'form-control','id':'courseid'}),
            'syllabus'    : forms.TextInput(attrs={'class':'form-control','id':'syllabusid'}),
            'isactive'    : forms.NullBooleanSelect(attrs={'class':'form-control','id':'is_activeid'}),
            }




class testimonialform(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = ('name','profession','photo','description')
        widgets = {
            'name'     : forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'profession'    : forms.TextInput(attrs={'class':'form-control','id':'professionid'}),
            'photo'    : forms.FileInput(attrs={'class':'form-control','id':'photoid'}),
            'description'    : forms.TextInput(attrs={'class':'form-control','id':'descriptionid'}),
                }


class enquiryForm(forms.ModelForm):
    class Meta:
        model = enquiry
        fields = ('name','email','phone','message')
        widgets = {
            'name'     : forms.TextInput(attrs={'class':'form-control','id':'name','placeholder': 'Your Name'}),
            'email'    : forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder': 'Your Email'}),
            'phone'    : forms.TextInput(attrs={'pattern':'[1-9]{1}[0-9]{9}','class':'form-control','id':'phone','placeholder': 'Your Phone'}),
            'message'  : forms.Textarea(attrs={'style': 'height: 10em;','class':'form-control','id':'message','placeholder': 'message'}),
        }
        labels = {
        "name":  "",
        "email": "",
        "phone": "",
        "message":"",
        }
