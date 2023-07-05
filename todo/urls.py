from django.urls import path
from .views import (
    TodoListView,
    UserTodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
   
)
from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-index'),
    path('user/<str:username>', UserTodoListView.as_view(), name='user-todos'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('tood/new/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('about/', views.about, name='todo-about'),
]
