from dataclasses import fields
from rest_framework import serializers
from lmsmainapp.models import *

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'
        
class CustomUserTokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

class logincheckSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields='__all__'

class examSerializer(serializers.ModelSerializer):
    class Meta:
        model=exam
        fields='__all__'

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields='__all__'

class topicSerializer(serializers.ModelSerializer):
    class Meta:
        model=topic
        fields='__all__'

class subtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subtopics
        fields='__all__'

class exam_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model=exam_master
        fields='__all__'

class examQuestionallocationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=exam_question_allocation
        fields='__all__'

class question_bankSerializer(serializers.ModelSerializer):
    class Meta:
        model=question_bank
        fields = '__all__'
        
        

class question_bankSerializer1(serializers.ModelSerializer):
    subject=serializers.StringRelatedField()
    # question=serializers.StringRelatedField()
    class Meta:
        model=question_bank
        fields = ['subject']


class question_bank_optionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=question_bank_options
        fields='__all__'

#mcq+++++++++++++++++++++++++++++++++++++++

class optSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_bank_options
        fields = ['identifier','choice']

class qustnSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    class Meta:
        model = question_bank
        fields = ['id','question', 'correct_answer','options']

class examQuestionallocationSerializer1(serializers.ModelSerializer):
     class Meta:
         model=exam_question_allocation
         fields=['question']
##############################################

class questionOptionsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = question_bank_options
        fields = ['id','choice','identifier']
        depth  = 1

class questionSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    #options = questionOptionsSerializer(many=True,read_only=True)
    class Meta: 
        model = question_bank
        fields = ['id','question','no_of_options','options']
        depth  = 1
        
               
class examdetailsSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    question1 = questionSerializer(many=True,read_only=True)
    class Meta: 
        model = exam_question_allocation
        fields = ['id','question','question1','options']
        depth  = 1




class VideoclassSerializer(serializers.ModelSerializer):
    class Meta:
        model=video_class
        fields='__all__'






class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=videocomment
        fields='__all__'



class CommentSerializer2(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=videocomment
        fields=['id','video','user','datetime','comment']



class courseSubjectallocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=course_subject_allocation
        fields='__all__'

class topicCourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=topic
        fields='__all__'



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=banner
        fields='__all__'


class DetailsresultSerializer(serializers.ModelSerializer):
    class Meta:
        model=result_details
        fields = ['id','question','attempted_time','is_flagged','user_answer','correct_answer','options_switched','switched_wrong_correct','switched_correct_wrong']

class ExamrsltSerializer(serializers.ModelSerializer):
    attent = DetailsresultSerializer(many=True)
    class Meta:
        model=examresult
        fields = ['id','user','exam','course','exam_master','datetime','no_of_questions','total_correct','total_wrong','total_skipped','flagged_correct','flagged_attempt','final_score','attent']
    def create(self, validated_data):
        exam_data = validated_data.pop('attent')
        results = examresult.objects.create(**validated_data)
        for exam_data in exam_data:
            result_details.objects.create(examresult=results, **exam_data)
        return results

class subexamserializer(serializers.ModelSerializer):
    class Meta:
        model=examresult
        fields=['user']


class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model=syllabus
        fields='__all__'



class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=notes
        fields='__all__'




class pexam_masterSerializer(serializers.ModelSerializer):
    exam=serializers.StringRelatedField()
    course=serializers.StringRelatedField()
    class Meta:
        model=exam_master
        fields=['exam','course']



class ppexam_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model=exam_master
        fields=['course','no_of_questions']


class pcourseSubjectallocationSerializer(serializers.ModelSerializer):
    subject=serializers.StringRelatedField()
    class Meta:
        model=course_subject_allocation
        fields=['subject']
        


class perfomanceserializer(serializers.ModelSerializer):
    exam=serializers.StringRelatedField()
    course=serializers.StringRelatedField()
    class Meta:
        model=examresult
        fields=['exam','course']



class pcourseSubjectallocationSerializer(serializers.ModelSerializer):
    subject=serializers.StringRelatedField()
    class Meta:
        model=course_subject_allocation
        fields=['subject']

class pcourseSerializer(serializers.ModelSerializer):
    subjects=pcourseSubjectallocationSerializer(many=True, read_only=True)
    exam=serializers.StringRelatedField()
    class Meta:
        model=course
        fields=['course_name','exam','subjects']



 
class pExmresultSerializer(serializers.ModelSerializer):
    exam=serializers.StringRelatedField()
    class Meta:
        model=examresult
        fields = ['user','total_correct','no_of_questions','exam']
 
class ExmresultSerializer(serializers.ModelSerializer):

    # exam=serializers.StringRelatedField()

    perfomance = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_perfomance(self, obj):
        
        my_variable = self.context.get('perfomance')
        # Perform your calculations here to get the value of the extra variable
        return my_variable
    
    exams = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_exams(self, obj):
        
        my_variable = self.context.get('exams')
        # Perform your calculations here to get the value of the extra variable
        return my_variable
    

    no_of_questions = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_no_of_questions(self, obj):
        
        my_variable = self.context.get('no_of_questions')
        # Perform your calculations here to get the value of the extra variable
        return my_variable
    

    total_correct = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_total_correct(self, obj):
        
        my_variable = self.context.get('total_correct')
        # Perform your calculations here to get the value of the extra variable
        return my_variable
    

    exam = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_exam(self, obj):
        
        my_variable = self.context.get('exam')
        # Perform your calculations here to get the value of the extra variable
        return my_variable


    class Meta:
        model=examresult
        fields = ['user','exams','no_of_questions','total_correct','perfomance','exam']




class rsltserializer(serializers.ModelSerializer):

    subjects = serializers.SerializerMethodField()

    # Define the method to calculate the value of the extra variable
    def get_subjects(self, obj):
        
        my_subjects = self.context.get('my_subjects')
        # Perform your calculations here to get the value of the extra variable
        return my_subjects


    course=serializers.StringRelatedField()
    exam=serializers.StringRelatedField()
    class Meta:
        model=examresult
        fields=['user','course','exam','subjects']



class rsltdtl(serializers.ModelSerializer):
    question=serializers.StringRelatedField()
    class Meta:
        model=result_details
        fields=['question']
        
class rsltdtl1(serializers.ModelSerializer):
    # question=serializers.StringRelatedField()
    class Meta:
        model=result_details
        fields='__all__'




class testimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=testimonial
        fields='__all__'



class enquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=enquiry
        fields='__all__'


class courseregSerializer(serializers.ModelSerializer):
    class Meta:
        model=course_registration
        fields='__all__'
    