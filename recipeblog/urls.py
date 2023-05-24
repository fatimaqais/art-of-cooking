from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostRecipe.as_view(), name='home'),
    path('view_recipe/<slug:slug>/', views.RecipeDetail.as_view(),
         name='view_recipe'),
    path('like/<slug:slug>', views.LikeRecipe.as_view(), name='like_recipe'),
    path('share_recipe/', views.ShareRecipe.as_view(), name='share_recipe'),
    path('user_recipe/', views.UserRecipes.as_view(), name='user_recipes'),
    path('edit_recipe/<slug:slug>', views.EditRecipe.as_view(),
         name='edit_recipe'),
    path('delete_recipe/<int:pk>', views.DeleteRecipe.as_view(),
         name='delete_recipe')
]
