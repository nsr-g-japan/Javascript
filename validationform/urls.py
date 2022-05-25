from django.urls import path
from .views import *
urlpatterns = [

    path('userform',userform),
    path('serverisexists',serverisexists, name='serverisexists')
]