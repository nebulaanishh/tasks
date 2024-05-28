from .test_setup import TestRecipeSetup
from rest_framework.test import APIClient
from recipe.models import Recipe

class TestRecipe(TestRecipeSetup):

    def test_recipe_str(self):
        self.setup()
        self.assertEqual(str(self.recipe_object), "Recipe 1")

    def test_print(self):
        self.assertEqual('', '')