from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.request import Request
from rest_framework.parsers import JSONParser

from recipe.models.recipe import Recipe
from recipe.services.recipe import RecipeService
from recipe.tests.test_setup import TestRecipeSetup

class TestRecipeService(TestRecipeSetup):
    
    def setup(self):
        super().setup()
        self.factory = APIRequestFactory()
        self.service = RecipeService()
    
    def test_get_all_recipes(self):
        self.setup()
        request = self.factory.get('/recipes/')
        response = self.service.get_all_recipes()
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_new_recipe(self):
        self.setup()
        request = self.factory.post('/recipes/', self.recipe, format='json')
        response = self.service.create_new_recipe(self.recipe)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.recipe.get("name", ""))
    
    def test_get_recipe_detail(self):
        self.setup()
        request = self.factory.get(f"/recipes/{self.recipe_object.id}")
        response = self.service.get_recipe_detail(self.recipe_object.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.recipe.get('name'))

    def test_update_recipe_detail(self):
        self.setup()
        update_data = {"name" : "updated recipe"}
        factory_request = self.factory.patch(f"/recipes/{self.recipe_object.pk}/", update_data ,format='json')

        drf_request = Request(factory_request, parsers=[JSONParser()])
        response = self.service.update_recipe_detail(drf_request, self.recipe_object.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data.get("name"))

    def test_delete_recipe(self):
        self.setup()
        request = self.factory.delete(f"/recipes/{self.recipe_object.pk}/")
        response = self.service.delete_recipe(self.recipe_object.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(pk=self.recipe_object.pk)