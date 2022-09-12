from django.urls import path
from .views import CourseView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView
app_name = 'course'
urlpatterns = [
    path('', CourseView.as_view(template_name='base.html'), name='course-home'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('list/', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/delete', CourseDeleteView.as_view(), name='course-delete'),
    path('<int:id>/update', CourseUpdateView.as_view(), name='course-update'),
]
