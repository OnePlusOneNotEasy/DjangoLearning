from django.urls import path
from .views import fruit_detail_view, fruit_create_view, fruit_delete_view, fruit_list_view

app_name = 'fruit'
urlpatterns = [
    path('create/', fruit_create_view, name='fruits-create'),
    path('<int:my_id>/', fruit_detail_view, name='fruits-detail'),
    path('delete/<int:my_id>/', fruit_delete_view, name='fruits-delete'),
    path('list/', fruit_list_view, name='fruits-list'),
]
