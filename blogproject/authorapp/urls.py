
app_name = 'authorapp'
from django.urls import path
from . import views


urlpatterns = [
    # Add your URL patterns here
    path('',views.author_list, name='author_list'),
    path('create',views.add_author, name='create'),
    path('upadate/<int:id>',views.update_author, name='update'),
    path('delete/<int:id>',views.delete_author, name='delete'),
]

