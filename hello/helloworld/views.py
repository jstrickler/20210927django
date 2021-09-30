from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello DJANGO world at long last")

def halloween(request):
    return HttpResponse("Halloween is coming!")

