from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):

    CATEGORIES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Appetizer", "Appetizer"),
        ("Salad", "Salad"),
        ("Baked-goods", "Baked-goods"),
        ("Dessert", "Dessert"),
        ("Soup", "Soup"),
        ("Vegetarian", "Vegetarian")
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('Main Image', default='placeholder')
    image_1 = CloudinaryField('Image 2', blank=True)
    image_2 = CloudinaryField('Image 3', blank=True)
    excerpt = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posted_recipes')
    category = models.CharField(max_length=100, choices=CATEGORIES)
    servings = models.PositiveIntegerField()
    ingredients = models.TextField()
    direction = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
