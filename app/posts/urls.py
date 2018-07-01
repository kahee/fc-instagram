from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # config.urls
    #  path('posts/', include(이 urlpatterns))
    path('', views.post_list, name='post-list'),
    path('tags/<str:tag>/', views.search_post_result, name='search-post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('create/', views.post_create, name='post-create'),
    path('<int:pk>/post/like/', views.post_like, name='post-like'),
    path('<int:pk>/comment/create/', views.comment_create, name='comment-create'),
    path('<int:pk>/re_comment/create/', views.re_comment_create, name='re-comment-create'),

]
