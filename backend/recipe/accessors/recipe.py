import requests
from recipe.models import Recipe
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from recipe.helpers.logger import configure_logging
from recipe.helpers.exception_handlers import handle_exceptions

logger = configure_logging()


class RecipeAccessor:
    """Methods for accessing recipe data from external api"""

    API_BASE_URL = "https://dummyjson.com/"

    def __init__(self):
        self.base_url = self.API_BASE_URL
        self.session = requests.Session()
        retries = Retry(
            total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    @handle_exceptions
    def get_all_recipes(self, params=None) -> list:
        full_path = self.API_BASE_URL + "recipes"
        response = self.session.get(full_path, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("recipes", None)

    @handle_exceptions
    def get_recipe_by_id(self, id):
        full_path = self.API_BASE_URL + "recipes/" + id

        response = requests.get(full_path)
        return response.json()

    @handle_exceptions
    def save_recipe_to_db(self, recipe: dict) -> bool:
        """Saves the fetched recipe to database and returns bool value"""

        logger.info("Saving recipe to database")
        if not recipe.get("name"):
            return False

        current_recipe, is_recipe_created = Recipe.objects.get_or_create(
            name=recipe.get("name", ""),
            instructions=" ".join(recipe.get("instructions", [])),
            cook_time_minutes=recipe.get("cookTimeMinutes", 0),
            servings=recipe.get("servings", 1),
            difficulty=recipe.get("difficulty", ""),
            cuisine=recipe.get("cuisine", ""),
            calories_per_serving=recipe.get("caloriesPerServing"),
            image=recipe.get("image", ""),
            rating=recipe.get("rating", 0.0),
            ingredients=recipe.get("ingredients", []),
            tags=recipe.get("tags", []),
        )
        if not is_recipe_created:
            logger.info("Recipe already exists in the database")
        else:
            logger.info("Saved one recipe to database")

        return is_recipe_created

    @handle_exceptions
    def save_recipes_bulk(self, recipes: list[dict]) -> bool:
        """ """
        logger.info("Saving recipes to databse BULK")
        for recipe in recipes:
            is_saved_to_db = self.save_recipe_to_db(recipe)
            if not is_saved_to_db:
                return False
        logger.info("Bulk save to database successful")
        return True
