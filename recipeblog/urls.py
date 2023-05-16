from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostRecipe.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='view_recipe'),
    path('like/<slug:slug>', views.LikeRecipe.as_view(), name='like_recipe'),
]
