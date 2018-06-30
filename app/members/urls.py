from django.urls import path

from . import views

app_name = 'members'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/follow/', views.follow_toggle, name='follow'),
    path('<int:user_pk>/unfollow/', views.unfollow_toggle, name='unfollow'),
    path('<int:user_pk>/block/', views.block_toggle, name='block'),
]
