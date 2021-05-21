from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'show_conference$', show_conference, ),
    url(r'yy_conference', yy_conference),
    url(r'show_name', show_name),
    url(r'draw_forms', draw_forms),
    url(r'cancel_book', cancel_book),
    url(r'sgin_in', sgin_in),
    url(r'update_forms', update_forms),
    url(r'participant', participant),
    url(r'delete_form', delete_form),
    
]

