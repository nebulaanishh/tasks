import requests
from recipe.models import Recipe

class RecipeAccessor():
    """ Methods for accessing recipe data from external api """

    API_BASE_URL = "https://dummyjson.com/"

    def get_all_recipes(self) -> list:
        full_path = self.API_BASE_URL + "recipes"
        try:
            response = requests.get(full_path)
        except TimeoutError as t:
            return {'error': "Request Timed Out"}
        if response.json().get('recipes', None):
            return response.json()['recipes']
        return None
        

    def get_recipe_by_id(self, id):
        full_path = self.API_BASE_URL + "recipes/" + id
        
        try:
            response = requests.get(full_path)
        except TimeoutError as t:
            return {'error': 'Request Timed Out'}
        
        return response.json()


    def save_recipe_to_db(self, recipe: dict) -> bool:
        """ Saves the fetched recipe to database and returns bool value """
        
        try:
            current_recipe = Recipe.objects.get_or_create(
                name =  recipe.get('name', ''),
                instructions =  " ".join(recipe.get('instructions', [])),
                cook_time_minutes = recipe.get("cookTimeMinutes", 0),
                servings = recipe.get("servings", 1),
                difficulty = recipe.get("difficulty", ""),
                cuisine = recipe.get("cuisine", ""),
                calories_per_serving = recipe.get("caloriesPerServing"),
                image = recipe.get("image", ""),
                rating =  recipe.get("rating", 0.0),
                ingredients = recipe.get('ingredients', []),
                tags = recipe.get('tags', [])
                
            )
            return True
        except Exception as e:
            print(e)
            return False    
        

    def save_recipes_bulk(self, recipes: list[dict]) -> bool:
        """ """
        for recipe in recipes:
            is_saved_to_db = self.save_recipe_to_db(recipe)
            if not is_saved_to_db:
                return False
        return True
    