from recipe.models import Recipe
from recipe.accessors.recipe import RecipeAccessor
from recipe.serializers.recipe import RecipeSerializer
from recipe.helpers.logger import configure_logging

from django.http import Http404
from django.db import DatabaseError

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

logger = configure_logging()


class RecipeService:

    def get_all_recipes(self):
        logger.info("FETCHING all recipes from database.")
        try:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            logger.info(f"FETCHED {len(recipes)} recipes from database")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def create_new_recipe(self, data):
        logger.info("CREATING new recipe")
        try:
            serializer = RecipeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                logger.info("CREATED Recipe successfully.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.info("CREATE a new recipe FAILED. Validation errors occured")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            logger.error(f"FAILED to FETCH Recipe with given id: {id}")
            raise Http404

    def get_recipe_detail(self, pk):
        logger.info("FETCHING recipe detail by id")
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe)
            logger.info(f"FETCHED details for recipe with id {pk}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update_recipe_detail(self, request, pk):
        logger.info(f"UPDATING recipe with id: {pk}..")
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"UPDATE recipe with id: {pk} successfully")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"UPDATE recipe with id: {pk} Failed: Validation Errors")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete_recipe(self, pk):
        logger.info(f"DELETING recipe with id: {pk}")
        try:
            recipe = self.get_object(pk)
            recipe.delete()
            logger.info(f"DELETED Recipe with id: {pk}successfully.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
