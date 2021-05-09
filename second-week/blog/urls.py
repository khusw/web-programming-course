from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.get_poem, name='get_poem'),
    path(r'post_list', views.post_list, name='post_list'),
]