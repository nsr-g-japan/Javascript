from django.urls import path
from .views import *
urlpatterns = [

    path('userform',userform),
    path('validateno', validateno),
    path('serverisexists',serverisexists, name='serverisexists')
]