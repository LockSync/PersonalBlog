from abc import ABC

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# handle the traffic of home page
def home(request):
    # take out the data form the database
    context = {
        'posts': Post.objects.all()
    }
    # pass the data to templates
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'

    #
    context_object_name = 'posts'
    ordering = ['-date_posted']

    # 2 posts in one page
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # 2 posts in one page
    paginate_by = 5

    # Only gets the posts from a certain user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


# Create post
# before the user create a post, the user has to login first
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = {'title', 'content'}

    def form_valid(self, form):
        # set the instance to the current login user
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update post
# with UserPassesTestMixin others can not update the post by the url
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check if the user is the user trying to update the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# delete the post
# login before trying to delete
# check if the current post has the current login user
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
