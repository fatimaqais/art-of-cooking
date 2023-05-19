from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostRecipe.as_view(), name='home'),
    path('view_recipe/<slug:slug>/', views.RecipeDetail.as_view(),
         name='view_recipe'),
    path('like/<slug:slug>', views.LikeRecipe.as_view(), name='like_recipe'),
    path('share_recipe/', views.ShareRecipe.as_view(), name='share_recipe'),
]
