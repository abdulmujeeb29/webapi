from django.urls import path
from .views import *

urlpatterns =[
    path('buisness',create_buisness),
    path('buisnesses',get_buisness),
    path('buisnesses/<int:pk>',get_buisness_by_id),
    #path('PUT/buisnesses/<int:pk>',update_buisness.as_view()),
]