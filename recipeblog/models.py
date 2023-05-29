from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.urls import reverse
from django.utils.text import slugify

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

    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=200, unique=True, null=False)
    featured_image = CloudinaryField('Main Image', default='placeholder')
    excerpt = models.TextField(max_length=150)
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
        return '{} {} {}'.format(self.title, self.category, self.author)

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.category}-{str(self.author)}")
        super(Recipe, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user_recipes')


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
