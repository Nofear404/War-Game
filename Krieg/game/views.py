from django.http import HttpResponse
from django.template import loader
from .models import Game


def gaming(request):
    game = Game("Selman", "Dan").gamestart()

    return HttpResponse(game)
