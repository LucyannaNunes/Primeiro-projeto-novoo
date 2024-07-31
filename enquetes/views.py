from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import Perguntas, Escolha

def index(request):
    lista_ultimas_perguntas = Perguntas.objects.order_by('-data_publicado')[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {
        'ultimas_perguntas' : lista_ultimas_perguntas
    }
    return HttpResponse(template.render(contexto, request))

   


def detalhes(request,pergunta_id):
    
    try:
        Perguntas = Perguntas.objects.get(pk = pergunta_id)
    except: 
        raise Http404("A pergunta não existe ")
    return HttpResponse("Hello, world. Você está acessando a questão {pergunta_id}.")
     
def resultados(request, pergunta_id):
    pergunta = get_object_or_404( Perguntas, pk= pergunta_id)
    return render (request,"enquetes/resultados.html", {'pergunta': pergunta})

def votos(request, pergunta_id):
    Perguntas = get_object_or_404 (Perguntas, pk = pergunta_id)
    try:
        escolha_selecionada = pergunta.escolha_set.get (pk = request.POST ["escolha"])
    except (KeyError, Escolha.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "question": Pergunta,
                "error_message" : "você não seçecionou uma escolha"

            }
        )
    else:
        escolha_selecionada.votos = F("votos") + 1
        escolha_selecionada.save()
    return HttpResponse(f'Você esetá votando na questão {pergunta_id}')
