from recipe.models import Recipe
from recipe.accessors.recipe import RecipeAccessor
from recipe.serializers.recipe import RecipeSerializer

from django.http import Http404

from rest_framework.response import Response
from rest_framework import status

class RecipeService():

    def get_all_recipes(self):
        """ """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        if not serializer:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create_new_recipe(self, data):
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get_recipe_detail(self, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        if not serializer:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update_recipe_detail(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_recipe(self, pk):
        recipe = self.get_object(pk)
        if recipe:
            recipe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)



