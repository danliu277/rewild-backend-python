from django.conf.urls import url, include
from .import views
from rest_framework import routers

router = routers.DefualtRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    url('', include(router.urls))
]