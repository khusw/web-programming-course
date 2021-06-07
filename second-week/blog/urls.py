from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]

'''
    장고를 통해서 특정 url 에 접근할때
    urls.py 를 쓰는데 
    그 중에서도 동일 카테고리에서 특정한 한 대상에 접근하고자 하는 경우
    post/<int:pk>/ 이런식으로 접근해야 한다
'''