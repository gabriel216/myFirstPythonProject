from rest_framework import generics
from .models import Question
from serializers import PollSerializer
from django.shortcuts import get_object_or_404

class QuestionList(generics.ListCreateAPIView):
    query = Question.objects.all()
    serializer_class = PollSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj