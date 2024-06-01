from django.test import TestCase
from recipe.models import Recipe
from rest_framework.test import APIClient


class TestRecipeSetup(TestCase):
    def setup(self):
        self.recipe = {
            "name": "Recipe 1",
            "instructions": "Instructions for recipe",
            "cook_time_minutes": 2,
            "servings": 3,
            "difficulty": "Easy",
            "cuisine": "Italian",
            "calories_per_serving": 400,
            "image": "https://images.pexels.com/photos/1066176/pexels-photo-1066176.jpeg?cs=srgb&dl=pexels-minan1398-1066176.jpg&fm=jpg",
            "rating": 4.5,
            "ingredients": ["tomato", "potato"],
            "tags": ["italian"],
        }

        self.recipe_object = Recipe.objects.create(
            name="Recipe 1",
            instructions="Instructions for recipe",
            cook_time_minutes=2,
            servings=3,
            difficulty="Easy",
            cuisine="Italian",
            calories_per_serving=400,
            image="https://images.pexels.com/photos/1066176/pexels-photo-1066176.jpeg?cs=srgb&dl=pexels-minan1398-1066176.jpg&fm=jpg",
            rating=4.5,
            ingredients=["tomato", "potato"],
            tags=["italian"],
        )
