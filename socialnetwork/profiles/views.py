from django.shortcuts import render
# from django.http import HttpResponse
from profiles.models import Profile


# Create your views here.
def index(request):
    # return HttpResponse('Bem-vindo ao Social Network')
    #
    # response = HttpResponse()
    # response.write("<h1>Bem-vindo ao Connectedin!</h1>")
    # response.write("<p>A sua rede social.</p>")

    return render(request, 'index.html')


def show(request, profile_id):

    # print 'ID do perfil recebido: %s' % profile_id

    # profile = Profile()

    # if profile_id == '1':
    #     profile = Profile('Kleber Carvalho', 'kleber.carvalho@gmail.com', '1111111', 'IBM')
    # ''
    # if profile_id == '2':
    #     profile = Profile('Arthur Carvalho', 'arthur.carvalho@gmail.com', '2222222', 'Microsoft')
    #
    # if profile_id == '3':
    #     profile = Profile('Marcia Carvalho', 'marcia.carvalho@gmail.com', '3333333', 'Red Hat')

    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', { "profile" : profile})