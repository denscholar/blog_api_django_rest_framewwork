from django.urls import path
from .views import *

urlpatterns = [
    path("posts/", AllPostview.as_view(), name='posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post'),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
]
