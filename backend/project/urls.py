
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title= "Recipe App API",
        default_version = "V1",
        description = "API documentation for recipe app that fetches data from external API, processes the data and then stores it into the database.",
        contact=openapi.Contact(email='email@example.com'),
        license=openapi.License(name="Recipe app License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('recipe.urls')),

    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
