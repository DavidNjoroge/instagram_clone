from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^accounts/profile$',views.profile,name='profile'),
    url(r'^accounts/profile/update_profile',views.update_profile,name='update_profile')

]