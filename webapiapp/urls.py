from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns =[
    path('POST/buisnesses',create_buisness.as_view()),
    path('GET/buisnesses',get_buisness.as_view()),
    path('GET/buisnesses/<int:pk>',get_buisness_by_id.as_view()),
    path('PUT/buisnesses/<int:pk>',update_buisness.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]