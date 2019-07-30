from .models import Question
from rest_framework import serializers 

class PollSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Question 
        fields = ('question_text', 'pub_date')