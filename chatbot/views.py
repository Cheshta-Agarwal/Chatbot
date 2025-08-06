from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the homepage of my chatbot!")

def home_redirect(request):
    return redirect('/chat/')

def index(request):
    return HttpResponse("Chatbot is working!")

def index_redirect(request):
    return redirect('/chat/api/')

def greet(request, name = 'Cheshta'):
    return HttpResponse(f'Hi, {name}!')

def api_response(request):
    data = {"message": "Hello, world!"}
    return JsonResponse(data)

def my_page(request):
    return render(request, 'my_template.html', {'message': 'Hello, world!'})

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def chatbot_api(request):
    """
    Simple chatbot API that returns a response based on the input message.
    """
    user_message = request.data.get('message', '').lower()

    if user_message == 'hi':
        response_message = "Hello!"
    elif user_message == 'bye':
        response_message = "Goodbye!"
    else:
        response_message = "I don't understand."

    return Response({'response': response_message})