from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('new', views.new_post, name='new_post'),
    path('<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete', views.delete_post, name='delete_post'),
]