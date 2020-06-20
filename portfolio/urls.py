from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path("", views.project_index, name="project_index"),
    # path("", views.project_index, name="blog_index"),
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]

