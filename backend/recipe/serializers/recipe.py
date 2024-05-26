from rest_framework import serializers
from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'instructions', 'cook_time_minutes', 'servings', 'difficulty', 'cuisine', 'calories_per_serving', 'image', 'rating', 'ingredients', 'tags']   

