from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^accounts/profile$',views.profile,name='profile'),
    url(r'^accounts/profile/update_profile',views.update_profile,name='update_profile'),
    url(r'^post/(\d+)/$',views.post,name='post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)