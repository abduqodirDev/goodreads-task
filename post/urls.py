from django.urls import path
from .views import main_page, create_post, update_post, delete_post, detail_post


urlpatterns = [
    path('', main_page, name='home'),
    path('create-post/', create_post, name='create-post'),
    path('update-post/<int:id>/', update_post, name='update-post'),
    path('delete-post/<int:id>/', delete_post, name='delete-post'),
    path('detail-post/<int:id>/', detail_post, name='detail-post'),
]
