from django.conf.urls import url

from website.views import *

app_name = 'website'


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^services/', ServicesView.as_view(), name='services'),
    url(r'^support/', SupportView.as_view(), name='support'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^success/', SuccessView.as_view(), name='success'),
]