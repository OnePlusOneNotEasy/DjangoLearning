from django.urls import path
from .views import (
    ArticleListView
)

app_name = 'Blog'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list')
]
