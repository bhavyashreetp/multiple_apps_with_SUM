from django.urls import path

from app2.views import *


app_name='anything'

urlpatterns=[
    path('yash/',yash, name='yash'),
    path('kicha/',kicha, name='kicha'),



]