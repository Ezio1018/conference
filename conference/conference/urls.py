from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import api_test.urls

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^api/', include(api_test.urls)),
#     url(r'^$', TemplateView.as_view(template_name="index.html")),
# ]
import form.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/', include(form.urls)),
    url(r'^api/', include(api_test.urls)),
    url(r'^api/', include('user.urls')),
    url(r'^hq/', include('staff.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]



    
