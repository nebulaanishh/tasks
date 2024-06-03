import requests
from functools import wraps

from django.db import DatabaseError
from django.http import Http404

from recipe.builders.response_builder import ResponseBuilder
from recipe.helpers.logger import configure_logging

logger = configure_logging()


def handle_exceptions(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            return func(self, *args, **kwargs)

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

        except requests.Timeout as t:
            logger.error("Request Timed out")
            return None
        except requests.HTTPError as http_err:
            logger.error(f"HTTP error occured: {http_err}")
            return None
        except requests.RequestException as err:
            logger.error(f"An error occured: {err}")
            return None

    return wrapper
