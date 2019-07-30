from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls/$', QuestionList.as_view(), name='polls')
]
