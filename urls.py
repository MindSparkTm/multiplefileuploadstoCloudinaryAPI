from django.conf.urls import url, include
from . import views
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()



urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^photo/$', views.upload.as_view(), name='upload'),
    url(r'^video/$', views.videoupload.as_view(), name='videoupload'),

)