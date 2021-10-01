from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Superhero

def home(request):
    """
    Home page of the Superheroes app

    :param request: HTTP request
    :return: HTTP Response with displayable text
    """
    return HttpResponse("<h1>Welcome to the superhero app</h1>")

def hero(request, hero_name):
    """
    Display name and secret identity

    :param request: HTTP request
    :param hero_name: name of hero (str)
    :return: HTTP Response with displayable text
    """
    s = get_object_or_404(Superhero, name=hero_name)

    return HttpResponse(
        "{} is really {} WOW!".format(s.secret_identity, s.name)
    )

