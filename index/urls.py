from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('send_email/', views.sendEmail, name='send'),

    path('create_post/', views.createpost, name='create_post'),
    path('update_post/<str:pk>/', views.Updatepost, name='update_post'),
    path('delete_post/<str:pk>/', views.deletepost, name='delete_post')


]

