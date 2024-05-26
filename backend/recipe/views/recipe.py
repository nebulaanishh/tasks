from recipe.accessors.recipe import RecipeAccessor
from recipe.services.recipe import RecipeService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RecipeFetchView(APIView):

    def get(self, request, format=None):
        """ Gets all recipes from external API"""
        accessor = RecipeAccessor()
        service = RecipeService()

        recipes = accessor.get_all_recipes()
        is_saved_to_db = accessor.save_recipes_bulk(recipes)
        if is_saved_to_db:
            return Response(recipes, status=status.HTTP_201_CREATED)
        return Response([], status.HTTP_204_NO_CONTENT)

