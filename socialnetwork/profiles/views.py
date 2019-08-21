from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Bem-vindo ao Social Network')
    return render(request, 'index.html')