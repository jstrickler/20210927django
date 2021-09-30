from django.http import HttpResponse

def goodbye(request):
    return HttpResponse("Goodbye from my app")
