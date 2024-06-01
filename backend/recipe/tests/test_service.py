from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.request import Request
from rest_framework.parsers import JSONParser

from recipe.models.recipe import Recipe
from recipe.services.recipe import RecipeService
from recipe.tests.test_setup import TestRecipeSetup
from recipe.builders.response_builder import ResponseBuilder

response_builder = ResponseBuilder()


class TestRecipeService(TestRecipeSetup):

    def setup(self):
        super().setup()
        self.factory = APIRequestFactory()
        self.service = RecipeService()

    def test_get_all_recipes_success(self):
        self.setup()
        response = self.service.get_all_recipes()
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status-code"], 1)
        self.assertEqual(
            response.data.get("data")[0].get("name", ""), self.recipe.get("name")
        )
        self.assertEqual(len(response.data["data"]), 1)

    def test_create_new_recipe(self):
        self.setup()
        response = self.service.create_new_recipe(self.recipe)
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["status-code"], 1)
        self.assertEqual(response.data.get("data").get("name"), self.recipe.get("name"))

    def test_create_new_recipe_validation_error(self):
        self.setup()
        self.recipe.pop("instructions")
        response = self.service.create_new_recipe(self.recipe)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["status-code"], -1)

    def test_get_recipe_detail(self):
        self.setup()
        response = self.service.get_recipe_detail(self.recipe_object.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status-code"], 1)
        self.assertEqual(response.data["data"]["name"], self.recipe.get("name"))

    def test_get_recipe_detail_404(self):
        self.setup()
        response = self.service.get_recipe_detail(11)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["status-code"], -1)

    def test_update_recipe_detail(self):
        self.setup()
        update_data = {"name": "updated recipe"}
        factory_request = self.factory.put(
            f"/recipes/{self.recipe_object.pk}/", update_data, format="json"
        )

        drf_request = Request(factory_request, parsers=[JSONParser()])
        response = self.service.update_recipe_detail(drf_request, self.recipe_object.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status-code"], 1)
        self.assertEqual(response.data["data"]["name"], update_data.get("name"))

    def test_delete_recipe(self):
        self.setup()
        request = self.factory.delete(f"/recipes/{self.recipe_object.pk}/")
        response = self.service.delete_recipe(self.recipe_object.pk)
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["status-code"], 1)
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(pk=self.recipe_object.pk)
