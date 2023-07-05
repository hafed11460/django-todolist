from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import TodoItem

page_count = 1

def home(request):
    context = {
        'objects': TodoItem.objects.all()
    }
    return render(request, 'todo/index.html', context)


class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    ordering = ['-pk']
    paginate_by = page_count


class UserTodoListView(ListView):
    model = TodoItem
    template_name = 'todo/user_todos.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    paginate_by = page_count

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TodoItem.objects.filter(author=user).order_by('-pk')


class TodoDetailView(DetailView):
    model = TodoItem


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoItem
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TodoItem
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TodoItem
    success_url = '/'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})
