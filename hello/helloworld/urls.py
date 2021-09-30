from django.urls import path
from . import views

app_name = 'helloworld'

# associate HOST/  ==> views.home
#           HOST/spooky  ==> views.halloween
urlpatterns = [
    path('', views.home, name='home'),
    path('spooky', views.halloween, name='spooky'),
]
