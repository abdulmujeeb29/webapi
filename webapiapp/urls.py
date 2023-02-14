from django.urls import path
from .views import *

urlpatterns =[
    path('post',buis_create.as_view()),
    path('get',buis_get.as_view()),
]