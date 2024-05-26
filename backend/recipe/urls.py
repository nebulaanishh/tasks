from django.urls import path, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from recipe.views.app import health
from recipe.views.recipe import RecipeFetchView
from recipe.views.recipe_crud import RecipeList, RecipeDetail

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
    path('external/recipes/', RecipeFetchView.as_view(), name='recipe-fetch'),

    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path("recipes/<int:pk>/", RecipeDetail.as_view(), name='recipe-detail'),
]

urlpatterns = utils_path + api_paths