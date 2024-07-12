from django.shortcuts import render
from django.http import HttpResponse


#rota da página inicial

def index(request):
    return render(request, 'homepage/index.html')

#rota da página de login

def logIndex(request):
    return render(request, 'login/logIndex.html')

#rota da página de cadastro

def cadIndex(request):
    return render(request, 'cadastro/cadIndex.html')

#rota da página inicial (usuários)

def startIndex(request):
    return HttpResponse('<h1>Essa será a página principal dos Usuários<h1>')

#rota da página de tutoriais

def helpIndex(request):
    return HttpResponse('<h1>Essa será a página com os tutoriais<h1>')

#rota da página dos "créditos finais"

def classIndex(request):
    return HttpResponse('<h1>Essa será a página de apresentação da turma<h1>')