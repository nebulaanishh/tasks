from recipe.models import Recipe
from recipe.accessors.recipe import RecipeAccessor
from recipe.serializers.recipe import RecipeSerializer
from recipe.helpers.logger import configure_logging
from recipe.builders.response_builder import ResponseBuilder

from django.http import Http404
from django.db import DatabaseError

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


logger = configure_logging()


class RecipeService:

    def get_all_recipes(self):
        response_builder = ResponseBuilder()
        logger.info("FETCHING all recipes from database.")
        try:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            logger.info(f"FETCHED {len(recipes)} recipes from database")
            return (
                response_builder.result_object(serializer.data)
                .success()
                .ok_200()
                .get_response()
            )
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return (
                response_builder.result_object(
                    {"error": f"Database error occured: {e}"}
                )
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )
        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            return (
                response_builder.result_object({"error": f"Exception Occured: {e}"})
                .fail()
                .bad_request_400()
                .get_response()
            )

    def create_new_recipe(self, data):
        logger.info("CREATING new recipe")
        response_builder = ResponseBuilder()
        try:
            serializer = RecipeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                logger.info("CREATED Recipe successfully.")
                return (
                    response_builder.result_object(serializer.data)
                    .success()
                    .accepted_202()
                    .get_response()
                )
            logger.error("Validation Error in Create Recipe")
            return (
                response_builder.result_object({"error": f"{serializer.errors}"})
                .fail()
                .bad_request_400()
                .get_response()
            )

        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return (
                response_builder.result_object({"error": f"Database Error: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )

        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            return (
                response_builder.result_object({"error": f"Exception Occured: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            logger.error(f"FAILED to FETCH Recipe with given id: {id}")
            raise Http404

    def get_recipe_detail(self, pk):
        logger.info("FETCHING recipe detail by id")
        response_builder = ResponseBuilder()
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe)
            logger.info(f"FETCHED details for recipe with id {pk}")
            return (
                response_builder.result_object(serializer.data)
                .success()
                .ok_200()
                .get_response()
            )
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return (
                response_builder.result_object({"error": f"Database Error: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )
        except Http404 as e:
            logger.error("Object not found")
            return (
                response_builder.result_object({"error": "Resource not found"})
                .fail()
                .not_found_404()
                .get_response()
            )
        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            return (
                response_builder.result_object({"error": f"Exception Occured: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )

    def update_recipe_detail(self, request, pk):
        logger.info(f"UPDATING recipe with id: {pk}..")
        response_builder = ResponseBuilder()
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"UPDATE recipe with id: {pk} successfully")
                return (
                    response_builder.result_object(serializer.data)
                    .success()
                    .ok_200()
                    .get_response()
                )
            logger.error(f"UPDATE recipe with id: {pk} Failed: Validation Errors")
            return (
                response_builder.result_object({"error": serializer.errors})
                .fail()
                .bad_request_400()
                .get_response()
            )
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return (
                response_builder.result_object({"error": f"Database Error: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )
        except Http404 as e:
            logger.error("Object not found")
            return (
                response_builder.result_object({"error": "Resource not found"})
                .fail()
                .not_found_404()
                .get_response()
            )
        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            return (
                response_builder.result_object({"error": f"Exception Occured: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )

    def delete_recipe(self, pk):
        logger.info(f"DELETING recipe with id: {pk}")
        response_builder = ResponseBuilder()
        try:
            recipe = self.get_object(pk)
            recipe.delete()
            logger.info(f"DELETED Recipe with id: {pk} successfully.")
            return (
                response_builder.message("Deleted Successfully")
                .success()
                .accepted_202()
                .get_response()
            )
        except DatabaseError as e:
            logger.error("HTTP 500 Internal Server Error")
            return (
                response_builder.result_object({"error": f"Database Error: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )
        except Http404 as e:
            logger.error("Object not found")
            return (
                response_builder.result_object({"error": "Resource not found"})
                .fail()
                .not_found_404()
                .get_response()
            )

        except Exception as e:
            logger.error(f"Exception Occured: {e}")
            return (
                response_builder.result_object({"error": f"Exception Occured: {e}"})
                .fail()
                .internal_error_500()
                .get_response()
            )
