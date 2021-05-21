from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'add_conference$', add_conference),
    url(r'show_conferences$', show_conferences),
    url(r'delete_conference', delete_conference),
    url(r'add_user$', add_user),
    url(r'show_users$', show_users),
    url(r'delete_user$', delete_user),
    url(r'update_conference$', update_conference),
    url(r'select_conference$', select_conference),
    url(r'select_conferenceByid$', select_conferenceByid),
    url(r'update_user$', update_user),
    url(r'select_user$', select_user),
    url(r'show_forms$', show_forms),
    url(r'delete_form', delete_form),
    url(r'show_meeting', show_meeting),
    url(r'editPassword', editPassword),
]
