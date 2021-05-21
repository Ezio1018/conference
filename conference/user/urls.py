from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'login$', login_user ),
    url(r'register$', register ),
    url(r'detect$', detect ),

]