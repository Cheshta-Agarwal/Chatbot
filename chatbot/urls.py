from django.urls import path
from . import views # import views from same directory

urlpatterns = [
    # path('', views.index, name='index'),  # Handles /chat/
    path('', views.index_redirect),
    path('api/', views.chatbot_api),
    path('greet/', views.greet, name = 'greet'),
    path('greet/<str:name>/', views.greet, name = 'greet'),
]
