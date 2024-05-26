from django.urls import path, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from views.app import health


class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super(DefaultRouter, self).__init__()
        self.trailing_slash = "/?"

router = OptionalSlashRouter()


utils_path = [
    re_path('^', include(router.urls)),
    path("health/", health, name='health'),
]

api_paths  = [
    
]

urlpatterns = utils_path + api_paths