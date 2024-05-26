from django.contrib import admin
from recipe.models.recipe import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
