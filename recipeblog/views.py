from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, View, CreateView, UpdateView
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class PostRecipe(ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Get method for fetching comments and post details and returning
        variables.
        """
        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "view_recipe.html",
            {
                "recipe": post,
                "comments": comment,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method for comment form setting recipe object and returning
        variables.
        """

        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "view_recipe.html",
            {
                "recipe": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class LikeRecipe(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('view_recipe', args=[slug]))


class ShareRecipe(CreateView):

    model = Recipe
    form_class = RecipeForm
    template_name = 'share_recipe.html'


class UserRecipes(ListView):

    model = Recipe
    template_name = 'user_recipes.html'

    def get(self, request):

        queryset = Recipe.objects.filter(
            author=request.user.id).order_by('-created_on')
        queryset_dict = {
            'your_recipes': queryset,
        }

        return render(
            request,
            self.template_name,
            queryset_dict,
        )


class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'


class DeleteRecipe(View):

    def get(self, request, pk, *args, **kwargs):

        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()

        return redirect(reverse('user_recipes'))


class SavedRecipe(ListView):

    model = Recipe
    template_name = 'saved_recipe.html'

    def get(self, request):

        author = request.user
        queryset = Recipe.objects.filter(status=1).filter(likes=author)
        queryset_dict = {
            'saved_recipes': queryset,
        }

        return render(
            request,
            self.template_name,
            queryset_dict,
        )
