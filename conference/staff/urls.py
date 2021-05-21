from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'show_baoxiu$', show_baoxiu ),
    url(r'edit_baoxiu$', edit_baoxiu ),
    url(r'baoxiu$', baoxiu ),

]