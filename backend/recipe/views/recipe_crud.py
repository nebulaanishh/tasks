from rest_framework.views import APIView

from recipe.accessors.recipe import RecipeAccessor
from recipe.services.recipe import RecipeService

class RecipeList(APIView):
    """ List all recipes or create new recipe """
    service = RecipeService()


    def get(self, request, format=None):
        response = self.service.get_all_recipes()
        return response
    
    
    def post(self, request, format=None):
        response = self.service.create_new_recipe(request.data)
        return response


class RecipeDetail(APIView):
    """ Retrieve, update or delete a recipe instance """

    service = RecipeService()

    def get(self, request, pk, format=None):
        response = self.service.get_recipe_detail(pk)
        return response
    

    def put(self, request, pk, format=None):
        response = self.service.update_recipe_detail(request, pk)
        return response
    
    def delete(self, request, pk, format=None):
        response = self.service.delete_recipe(pk)
        return response