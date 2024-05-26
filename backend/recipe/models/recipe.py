from .base import *


class Recipe(BaseModel):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    cook_time_minutes = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=20)
    calories_per_serving = models.IntegerField()
    image = models.URLField(max_length=200)
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    ingredients = models.JSONField()
    tags = models.JSONField()


    def __str__(self) -> str:
        return self.name


