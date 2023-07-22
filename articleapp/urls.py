from django.urls import path

from articleapp.views import ArticleCreateView, ArticleListView

app_name = "articleapp"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('list/', ArticleListView.as_view(), name='list'),
]