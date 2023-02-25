from django.urls import path
from .views import *
from . import views 

urlpatterns =[
    path('POST/buisnesses',create_buisness.as_view()),
    path('GET/buisnesses',get_buisness.as_view()),
    path('GET/buisnesses/<int:pk>',get_buisness_by_id.as_view()),
    path('PUT/buisnesses/<int:pk>',update_buisness.as_view()),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
]