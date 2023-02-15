from django.urls import path
from .views import *

urlpatterns =[
    path('POST/buisnesses',create_buisness.as_view()),
    path('GET/buisnesses',get_buisness.as_view()),
    path('GET/buisnesses/<int:pk>',get_buisness_by_id.as_view()),
]