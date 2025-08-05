from django.urls import path
from . import views # import views from same directory

urlpatterns = [
    path('api/', views.chatbot_api),
    # path('', views.index_redirect),
    # path('', views.index),  # temporary view
    path('greet/', views.greet, name = 'greet'),
    path('greet/<str:name>/', views.greet, name = 'greet'),
]
