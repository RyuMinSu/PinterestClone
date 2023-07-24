from django.urls import path

from articleapp.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView

app_name = "articleapp"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name="update"),
]